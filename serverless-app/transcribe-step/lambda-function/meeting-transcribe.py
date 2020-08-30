import json
import urllib.parse
import boto3
import datetime

s3 = boto3.client('s3')
transcribe = boto3.client('transcribe')

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    try:
        transcribe.start_transcription_job(
            TranscriptionJobName= 'meeting_' + datetime.datetime.now().strftime("%Y%m%d%H%M%S"),
            LanguageCode='ja-JP',
            Media={
                'MediaFileUri': 'https://s3.ap-northeast-1.amazonaws.com/' + bucket + '/' + key
            },
            OutputBucketName='transcribed-jsons-ogi'
        )
        return
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e
