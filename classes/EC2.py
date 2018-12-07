import boto3
import VPC
import InternetGateway

class EC2:

    def __init__(self):
        self.__connector =  boto3.client('ec2')
        self.__resource = boto3.resource('ec2')

    def createVpc (self,args):
        cidrblock = args.get('CidrBlock')
        ipv6block = args.get('AmazonProvidedIpv6CidrBlock') if args.get('AmazonProvidedIpv6CidrBlock') != None else False
        dryrun = args.get('DryRun') if args.get('DryRun') != None else False
        tenancy = args.get('InstanceTenancy') if args.get('InstanceTenancy') != None else 'default'

        newVpc = self.__connector.create_vpc(CidrBlock=cidrblock,
                                             AmazonProvidedIpv6CidrBlock=ipv6block,
                                             DryRun=dryrun,
                                             InstanceTenancy=tenancy)

        _vpc = self.__resource.Vpc(newVpc['Vpc']['VpcId'])

        return VPC.VPC(_vpc)

    def getVpc (self, id):
        return VPC.VPC (self.__resource.Vpc(id))

    #returns a JSON describing all the VPC's in this region
    def getAllVpc (self):
        #describe VPC
        allVPC = self.__connector.describe_vpcs ()
        return allVPC

    def createInternetGateway(self):
        _igw = self.__connector.create_internet_gateway()
        return InternetGateway.InternetGateway (self.__resource.InternetGateway(_igw['InternetGateway']['InternetGatewayId']))

    def getInternetGateway (self,id):
        return InternetGateway.InternetGateway (self.__resource.InternetGateway(id))
