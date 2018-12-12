import boto3

class InternetGateway:

    def __init__(self, igw):
        self.__igw = igw

    def getId (self):
        return self.__igw.id

    def tag (self,tags):
        self.__igw.create_tags(Tags=[tags])
