import json
import urllib.parse
import boto3
import datetime

s3 = boto3.client('s3')
output_s3 = boto3.resource('s3')

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    try:
        output_bucket = 'meeting-minutes-ogi'
        output_key = 'minutes_' + datetime.datetime.now().strftime("%Y%m%d%H%M%S") + '.txt'
        obj = output_s3.Object(output_bucket, output_key)
        response = s3.get_object(Bucket=bucket, Key=key)
        body = json.load(response['Body'])
        file_contents = body['results']['transcripts'][0]['transcript']
        obj.put(ACL='public-read', Body=file_contents)
        boto3.resource('s3').Object(bucket, key).delete()
        return
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e
