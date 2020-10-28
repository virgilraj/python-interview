import logging
import argparse
import time
import boto3
import json
_ATHENA_CONNECTION_ = None
__BUCKET__ = None

''' 
Get the athena connection
'''
def get_athena_connection(): 
    # Create the connection if not already there 
    global _ATHENA_CONNECTION_
    
    if (_ATHENA_CONNECTION_ == None): 
        # TODO dont hard code this
        _ATHENA_CONNECTION_ = boto3.client('athena', 'us-east-1')
        
    return _ATHENA_CONNECTION_    


def get_bucket():
    global __BUCKET__
    if(__BUCKET__ == None):
        with open('config.json') as f:
            data = json.load(f)
            __BUCKET__ = data['bucket']
    return __BUCKET__


'''
Reads SQL statements from a file 
'''
def read_statements(file):

    commands = []
    
    with open(file, 'r') as fp: 

        curcmd = ''        
        
        for line in fp.readlines(): 
            #strip out comments
            i = line.find('--')
            if i > -1:
                line = line[:i]
            
            sl = line.split(';')
            curcmd += sl[0]
           
            if len(sl) > 1: 
 
                commands.append(curcmd.strip())
                
                i = 1
                while i < len(sl) -2: 
                    commands.append(sl[i].strip())
                    ++i
            
                curcmd = sl[i]
            
    return commands

'''
Method which executes an Athena script
'''
def execute_script(file):
    
    print('Executing SQL script: ' + file)
    statements = read_statements(file)
    
    for statement in statements:
        
        results = execute_statement(statement)
        
        if len(results['Rows']) == 0: 
            print('Empty results returned')
        else:
            print('SQL Results: ')   
            
            for row in results['Rows']:
                
                line = ''
                first = True
                
                for data in row['Data']: 
                    
                    if 'VarCharValue' not in data:
                        continue
                        
                    if first == True: 
                        first = False
                    else: 
                        line += '|'
                    
                    line += data['VarCharValue']
                
                print(line)

''' 
Executes a single SQL statement
'''
def execute_statement(statement): 
 
    client = get_athena_connection()
    bkt = get_bucket()
    statement = statement.replace('[[bucket]]', bkt)

    print('Executing SQL: \'' + statement + '\'')
    result = client.start_query_execution(QueryString=statement, ResultConfiguration={'OutputLocation':'s3://my-vehicle/temp' })
    id = result['QueryExecutionId']
    
    while True: 
        result = client.get_query_execution(QueryExecutionId=id)
        state = result['QueryExecution']['Status']['State']
    
        if state == 'SUCCEEDED': 
            print('SQL statement SUCCEEDED')
            result = client.get_query_results(QueryExecutionId=id)
            return result['ResultSet']
            
        elif state == 'FAILED':
            print('SQL statement FAILED', logging.ERROR)
            print(result['QueryExecution']['Status']['StateChangeReason'],logging.ERROR)
            raise Exception('SQL Statement Failed')
        
        elif state == 'CANCELLED':
            print('SQL statement CANCELLED')
            break
        else: 
            time.sleep(.5)

''' 
Main that executes athena scripts 
'''
if __name__ == "__main__":

    print('athenaexec')
    
    argparser = argparse.ArgumentParser(description='Executes athena scripts')
    argparser.add_argument('files', metavar='file', nargs='+', help='athena script files')
    args = argparser.parse_args()

    for f in args.files: 
        
        scriptcontents = open(f, 'r').read()
        
        if scriptcontents.find('@EXCLUDEATHENA') == -1: 
            execute_script(f)
        else: 
            print('Skipping ' + f + ' contains @EXCLUDEATHENA')
     