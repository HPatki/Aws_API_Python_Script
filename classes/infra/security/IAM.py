import boto3

class IAM:

    def __init__(self):
        self.__client = boto3.client('iam')
        self.__resource = boto3.resource('iam')


    def listAllPolicies (self):
        return self.__client.list_policies(Scope='All', OnlyAttached=False)

    def listLocalPolicies (self):
        return self.__client.list_policies(Scope='Local', OnlyAttached=False)

    def createGroup (self):
        pass
