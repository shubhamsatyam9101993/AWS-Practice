import boto3
iam=boto3.client('iam')
paginator=iam.get_paginator('list_users')
for i in paginator.paginate():
    for j in i['Users']:
        print(j['UserName']