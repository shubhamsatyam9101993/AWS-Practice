import boto3


def f1(iam):
    l1 = []
    paginator = iam.get_paginator('list_users')
    for i in paginator.paginate():
        for j in i['Users']:
            l1.append(j['UserName'])
            print(l1)


def create_user(iam):
    response = iam.create_user(UserName='another_user')
    return response


if __name__ == '__main__':
    iam = boto3.client('iam')
    f1(iam)
    response = create_user(iam)
    print(response)
# -------push token is : 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
