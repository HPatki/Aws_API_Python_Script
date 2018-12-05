import boto3

#VPC API is available through the EC2 service
connector = boto3.client('ec2')

#create a VPC
#VPC limit is 5 per region
newVpc = connector.create_vpc(CidrBlock='10.10.0.0/16',AmazonProvidedIpv6CidrBlock=False,DryRun=False,InstanceTenancy='default')
newVpcId = newVpc['Vpc']['VpcId']
#tag the newVPC
#connector.Tag(newVpcId,'Name','value')

#create Internet Gateway for the Public subnet. This will be given to the router
newIgw = connector.create_internet_gateway ()
newIgwId = newIgw['InternetGateway']['InternetGatewayId']
connector.attach_internet_gateway(newIgwId,newVpcId,DryRun=False)
#tag the new Internet Gateway
#connector.Tag(newIgwId,'Name','value')

#create Routes
newRouteTable = connector.create_route_table (DryRun=False,VpcId=newVpcId)
newRouteTableId = newRouteTable['RouteTable']['RouteTableId']
#create new Routes
newRoute = connector.create_route(RouteTableId=newRouteTableId, GatewayId= newIgwId,
                                  DestinationCidrBlock='0.0.0.0/0')
newRoute1 = connector.create_route(RouteTableId=newRouteTableId,DestinationCidrBlock='10.10.0.0/0')

#create subnet for the VPC
newSubnet = connector.create_subnet (AvailabilityZone='ap-south-1a',CidrBlock="10.10.1.0/24",VpcId=newVpcId)


#connect and check how many instances are running
instances = connector.describe_instances()
print ('----- instances ------')
print (instances)
vpcs = connector.describe_vpcs()
print ('----- vpcs -----------')
print (vpcs)

#list out users
client = boto3.client('iam')
users = client.list_users()
print ('----- users ----------')
print(users)
