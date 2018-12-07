import boto3

class RouteTable:

    def __init__(self, rt):
        self.__rt = rt

    def tag(self,tag):
        self.__rt.create_tags(Tags=[tag])

    def createRoute(self,destCidrBlock, destIpv6CidrBlock, dryRun, target):
        DestinationIpv6CidrBlock = destIpv6CidrBlock
        DryRun = dryRun

        #any be only one of these
        if target.get('EgressOnlyInternetGatewayId'):
            self.__rt.create_route( DestinationCidrBlock = destCidrBlock,
                                    .get('DestinationCidrBlock') if target.get('DestinationCidrBlock')
        GatewayId = args.get('DestinationCidrBlock']
        NatInstanceId = args.get('DestinationCidrBlock']
        NatGatewayId = args.get('DestinationCidrBlock']
        TransitGatewayId = args.get('DestinationCidrBlock']
        NetworkInterfaceId = args.get('DestinationCidrBlock']
        VpcPeeringConnectionId = args.get('DestinationCidrBlock']

        self.__rt.create_route()
