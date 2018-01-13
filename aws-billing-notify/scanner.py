import os
import zipfile
import json
import uuid
import sys
import boto3
from pprint import pprint
from datetime import datetime, timezone, timedelta
from boto3.session import Session
import datetime
import requests

obj = json.loads(os.environ['AWS_3'])
session = boto3.Session(
  aws_access_key_id=obj['ACCOUNT'],
  aws_secret_access_key=obj['SECRET'],
  region_name='us-east-1',
)
#ec2 = session.resource('cloudwatch', region_name='ap-northeast-1')

response = session.client('cloudwatch', region_name='us-east-1')

#a = response.list_metrics()
#print(json.dumps(a,indent=1))

result= response.get_metric_statistics(
    Namespace='AWS/Billing',
    MetricName='EstimatedCharges',
    Dimensions=[
        {
            'Name': 'Currency',
            'Value': 'USD'
        }
    ],
    StartTime=datetime.datetime.today() - datetime.timedelta(days=1),
    EndTime=datetime.datetime.today(),
    Period=86400,
    Statistics=['Maximum'])
billing = int(result['Datapoints'][0]['Maximum'])
text = 'AWS 研究用アカウントの、今月のお支払金額の予想値は{}ドルですよ。うふふ。'.format(billing)

requests.post("http://192.168.14.31:8091/google-home-notifier", data={'text': text})
