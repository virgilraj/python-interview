import json
import argparse
import boto3
import time
from os import path, listdir, getcwd
from botocore.exceptions import ClientError

_GLUE_CONNECTION_ = None
__BUCKET__ = None
'''
Utility function to get the glue Connection
'''
def get_glue_connection(): 
    # Create the connection if not already there 
    global _GLUE_CONNECTION_
    
    if (_GLUE_CONNECTION_ == None): 
        _GLUE_CONNECTION_ = boto3.client('glue','us-east-1')
        
    return _GLUE_CONNECTION_ 

def get_bucket():
    global __BUCKET__
    if(__BUCKET__ == None):
        with open('config.json') as f:
            data = json.load(f)
            __BUCKET__ = data['bucket']
    return __BUCKET__

''' 
Reads a deployment descriptor from a python source file
file, file to read deployment descriptor from
return deployment descriptor
'''            
def read_deployment_descriptor_from_py_file(file):
    
    descriptorjson = ''
    

    injson = False

    for line in file:

        if '@EXCLUDEGLUE' in line:
            print('File has @EXCLUDEGLUE skipping.')
            return None

        if 'BEGINJOBDEF' in line:
            injson = True
        elif injson == True:
            if 'ENDJOBDEF' in line:
                break
            else:
                descriptorjson += line
    
    if descriptorjson != '':
        return json.loads(descriptorjson)
    else: 
        return None


'''
deploys a local file as a glue job
'''
def deploy_local_glue_job(file, seript_loc):
    (jobname, ext) = path.splitext(path.basename(file))

    print('Processing file: ' + file)

    if ext == '.py':

        localfilename = file

        with open(localfilename) as fp:
            descriptor = read_deployment_descriptor_from_py_file(fp)

        if descriptor is None:
            print("No deployment descriptor found in " + file + " skipping")
            return
        descriptor['ScriptLocation'] = seript_loc
    else:
        raise Exception("Don't know how to deploy: " + file)
    
    print(descriptor)

    #pylist = build_py_files_list(localfilename)
    deploy_glue_job(jobname, descriptor)

'''
deploys a glue job based on the descriptor
'''
def deploy_glue_job(jobname, descriptor, enable_metrics=False, maxretries=None):

    if "Args" in descriptor:
        args = descriptor['Args']
    else:
        args = None
    
    if 'Connections' in descriptor:
        connections = descriptor['Connections']
    else:
        connections = None

    if 'DPU' in descriptor:
        dpus = descriptor['DPU']
    else:
        dpus = 5
    
    if 'MaxConcurrentRuns' in descriptor:
        max_concurrent = int(descriptor['MaxConcurrentRuns'])
    else:
        max_concurrent = 1

    if maxretries is not None:
        max_retries = maxretries
    else:
        if 'MaxRetries' in descriptor:
            max_retries = int(descriptor['MaxRetries'])
        else:
            max_retries = 1

    if 'ScriptLocation' not in descriptor:
        raise Exception('ScriptLocation not specified in descriptor')

    s3path = descriptor['ScriptLocation']

    job = get_glue_job(jobname)
    print(job)
    if job is None:
        print('Creating glue job: ' + jobname + ' script location: ' + s3path)
        create_glue_job(jobname, s3path, args, connections, int(dpus), max_concurrent,
                                 max_retries, enable_metrics)
    else:
        print('Updating glue job: ' + jobname + ' script location: ' + s3path)
        update_glue_job(jobname, s3path, args, connections, int(dpus), max_concurrent,
                                 max_retries, enable_metrics)

def upload_scriptfile_to_s3(file):
    filename = ''.join(path.splitext(path.basename(file)))
    s3 = boto3.resource('s3')
    BUCKET = get_bucket()

    fin = open(file, "rt")
    data = fin.read()
    data = data.replace('[[bucket]]', BUCKET)
    fin.close()

    s3.Object(BUCKET, 'src/'+filename).put(Body=data)
    return 's3://'+ BUCKET +'/src/'+filename

def create_glue_job(jobname, scriptlocation, args=None, connections = None, dpus=5, 
                    max_concurrent=1, max_retries=1, enable_metrics=False):
    conn = get_glue_connection()
    BUCKET = get_bucket()
    loguri = 's3://'+ BUCKET +'/log/' + jobname
    glueversion = '2.0'
    pythonversion='3'
    argscopy = {}
    if args is not None:
        for a in args: 
            argscopy[a] = args[a]

    response = conn.create_job(
            Name=jobname,
            Description='Glue Job',
            LogUri=loguri,
            Role='AWSGlueServiceRole',
            DefaultArguments=argscopy,
            ExecutionProperty={
                'MaxConcurrentRuns': 2
            },
            Command={
                'Name': 'glueetl',
                'ScriptLocation': scriptlocation,
                'PythonVersion': pythonversion
            },
            MaxRetries=1,
            Timeout=120,
            GlueVersion=glueversion,
            NumberOfWorkers=int(dpus),
            WorkerType='G.1X'
        )
    print("Glue job created successfully")



def update_glue_job(jobname, scriptlocation, args=None, connections = None, dpus=5, 
                    max_concurrent=1, max_retries=1, enable_metrics=False):
    conn = get_glue_connection()
    BUCKET = get_bucket()
    loguri = 's3://'+ BUCKET +'/log/' + jobname
    glueversion = '2.0'
    pythonversion='3'
    argscopy = {}
    if args is not None:
        for a in args: 
            argscopy[a] = args[a]
        
    response = conn.update_job(
        JobName=jobname,
        JobUpdate={
            'Description': 'Glue Job',
            'LogUri': loguri,
            'Role': 'AWSGlueServiceRole',
            'ExecutionProperty': {
                'MaxConcurrentRuns': 2
            },
            'Command': {
                'Name': 'glueetl',
                'ScriptLocation': scriptlocation,
                'PythonVersion': pythonversion
            },
            'DefaultArguments': argscopy,
            'MaxRetries': 1,
            'Timeout': 120,
            'WorkerType': 'G.1X',
            'NumberOfWorkers': dpus,
            'GlueVersion': glueversion
        }
    )

    print("Glue job updated created successfully")
     

'''
Gets a glue job definition
jobname, name of the job to get
return job definition or None
'''
def get_glue_job(jobname):
    
    conn = get_glue_connection()
    while True:
        try:
            return conn.get_job(JobName=jobname)
        except ClientError as e:
            if e.response['Error']['Code'] == 'ThrottlingException':
                time.sleep(.5)
            elif e.response['Error']['Code'] == 'EntityNotFoundException':
                return None
            else:
                raise e

if __name__ == "__main__":
    argparser = argparse.ArgumentParser(description='Put Glue Jobs to AWS')
    argparser.add_argument('files', metavar='file', nargs='+', help='glue script files')
    args = argparser.parse_args()
    for file in args.files:
        print(file)
        if path.isfile(file) == False:
                print('Not a file: ' + file + ' skipping')
        else:
            (jobname, ext) = path.splitext(path.basename(file))
            #print(''.join(path.splitext(path.basename(file))))
            if ext == '.py' or ext == '.json':
                seript_loc = upload_scriptfile_to_s3(file)
                deploy_local_glue_job(file,seript_loc)

    