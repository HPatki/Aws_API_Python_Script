import boto3

class VPC:

    def __init__(self, vpc):
        self.__vpc = vpc

    def tag (self, tags):
        self.__vpc.create_tags(Tags=[tags])

    def attachIGW (self,igw,runType=False):
        self.__vpc.attach_internet_gateway (DryRun=runType,InternetGatewayId=igw.getId())

    def detachIGW (self,igw):
        self.__vpc.detach_internet_gateway (InternetGatewayId=igw.getId())