import boto3
from classes.infra.network  import RouteTable

class VPC:

    def __init__(self, vpc):
        self.__vpc = vpc

    def tag (self, tags):
        self.__vpc.create_tags(Tags=[tags])

    def attachIGW (self,igw,dryRun=False):
        self.__vpc.attach_internet_gateway (DryRun=dryRun,InternetGatewayId=igw.getId())

    def detachIGW (self,igw):
        self.__vpc.detach_internet_gateway (InternetGatewayId=igw.getId())
		
    def createRouteTable(self,dryRun=False):
        return RouteTable.RouteTable(self.__vpc.create_route_table (dryRun))