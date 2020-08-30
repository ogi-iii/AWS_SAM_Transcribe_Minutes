# AWS SAM Transcribe Minutes
AWS Serverless Application Model for transcribe meeting minutes voice

# Quick Start Guide
Bellow commands should be executed on [AWS Cloud9](https://docs.aws.amazon.com/console/cloud9/).

```
aws s3 mb s3://sam-template-transcribe-ogi
aws s3 mb s3://sam-template-refile-ogi

cd ./serverless-app/transcribe-step
aws cloudformation package --template-file ./template.yaml --s3-bucket sam-template-transcribe-ogi --output-template-file packaged-template.yaml
aws cloudformation deploy --template-file ./packaged-template.yaml --stack-name sam-meeting-transcribe --capabilities CAPABILITY_IAM

cd ../refile-step
aws cloudformation package --template-file ./template.yaml --s3-bucket sam-template-refile-ogi --output-template-file packaged-template.yaml
aws cloudformation deploy --template-file ./packaged-template.yaml --stack-name sam-meeting-refile --capabilities CAPABILITY_IAM
```