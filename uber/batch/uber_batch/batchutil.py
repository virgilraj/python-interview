
import boto3
import os
import io
import gzip
import pandas as pd
from botocore.config import Config
import json
import shutil
from tempfile import TemporaryFile

_S3_CONNECTION_ = None
__BUCKET__ = None

def get_s3_connection(): 
    # Create the connection if not already there 
    global _S3_CONNECTION_
    
    if (_S3_CONNECTION_ == None): 

        _S3_CONNECTION_ = boto3.client('s3')
        
    return _S3_CONNECTION_


def list_keys(bucket, prefix):
    conn = get_s3_connection()
    keys = []
    paginator = conn.get_paginator('list_objects_v2')    

    for page in paginator.paginate(Bucket=bucket, Prefix=prefix):
        
        if page['KeyCount'] == 0: 
           break
        
        for obj in page['Contents']: 
            
            keys.append(obj['Key'])
    return keys

def get_landing_files(bkt, prefix):
    return list_keys(bkt,prefix)

def delete_from_temp(filename):
    try:
        if(os.path.isfile(filename)):
            os.remove(filename)
            print("Removed the temp file" + filename)
    except Exception as e:
        print("Error in remove file temp file")
        print(e)
    else:
        return False

def save_to_temp(bkt, filename):
    try:
        conn = get_s3_connection()
        file = filename.split('/')
        print(file)
        conn.download_file(bkt, filename, 'temp/'+file[len(file)-1])
        print('File Saved in temp location')
        
    except Exception as e:
        print("Error in writing filt to temp location")
        print(e)
        return False
    else:
        return True, 'temp/'+file[len(file)-1]

def write_out_to_s3_parquet(s3ky, bucket):
    conn = get_s3_connection()
    path = 'out' 
    files = os.listdir(path)
    files_txt = [i for i in files if i.endswith('.parquet')]
    for file in files_txt:
        try:
            response = conn.upload_file('out/'+file, bucket,s3ky+'/'+file)
        except Exception as e:
            print(e)
            return False
        return True

def remove_out_file():
    #os.rmdir('out')
    shutil.rmtree('out', ignore_errors=True)
    os.mkdir('out')
    shutil.rmtree('temp', ignore_errors=True)
    os.mkdir('temp')
    print('Removed all temp & out files')

def get_bucket():
    global __BUCKET__
    if(__BUCKET__ == None):
        with open('../../config.json') as f:
            data = json.load(f)
            __BUCKET__ = data['bucket']
    return __BUCKET__
    