import boto3

class RouteTable:

    def __init__(self, rt):
        self.__rt = rt

    def tag(self,tag):
        self.__rt.create_tags(Tags=[tag])

    def createRouteTarget_Egress(self,destCidrBlock, target, destIpv6CidrBlock=None, dryRun=False):
        route = None
        if destIpv6CidrBlock != None:
            route = self.__rt.create_route(DestinationCidrBlock=destCidrBlock,
                                   DestinationIpv6CidrBlock=destIpv6CidrBlock,
                                   DryRun=dryRun,EgressOnlyInternetGatewayId=target)
        else:
            route = self.__rt.create_route(DestinationCidrBlock=destCidrBlock,
                                   DryRun=dryRun, EgressOnlyInternetGatewayId=target)

        return route

    def createRouteTarget_Gateway(self, destCidrBlock, target, destIpv6CidrBlock=None, dryRun=False):
        route = None
        if destIpv6CidrBlock != None:
            route = self.__rt.create_route(DestinationCidrBlock=destCidrBlock,
                                            DestinationIpv6CidrBlock=destIpv6CidrBlock,
                                            DryRun=dryRun, GatewayId=target)
        else:
            route = self.__rt.create_route(DestinationCidrBlock=destCidrBlock,
                                               DryRun=dryRun, GatewayId=target)

        return route

    def createRouteTarget_NatInstance(self, destCidrBlock, target, destIpv6CidrBlock=None, dryRun=False):
        route = None
        if destIpv6CidrBlock != None:
            route = self.__rt.create_route(DestinationCidrBlock=destCidrBlock,
                                           DestinationIpv6CidrBlock=destIpv6CidrBlock,
                                           DryRun=dryRun, InstanceId=target)
        else:
            route = self.__rt.create_route(DestinationCidrBlock=destCidrBlock,
                                           DryRun=dryRun, InstanceId=target)


        return route

    def createRouteTarget_NatGateway(self, destCidrBlock, target, destIpv6CidrBlock=None, dryRun=False):
        route = None
        if destIpv6CidrBlock != None:
            route = self.__rt.create_route(DestinationCidrBlock=destCidrBlock,
                                           DestinationIpv6CidrBlock=destIpv6CidrBlock,
                                           DryRun=dryRun, NatGatewayId=target)
        else:
            route = self.__rt.create_route(DestinationCidrBlock=destCidrBlock,
                                           DryRun=dryRun, NatGatewayId=target)

    def createRouteTarget_TransitGateway(self, destCidrBlock, target, destIpv6CidrBlock=None, dryRun=False):
        route = None
        if destIpv6CidrBlock != None:
            route = self.__rt.create_route(DestinationCidrBlock=destCidrBlock,
                                           DestinationIpv6CidrBlock=destIpv6CidrBlock,
                                           DryRun=dryRun, TransitGatewayId=target)
        else:
            route = self.__rt.create_route(DestinationCidrBlock=destCidrBlock,
                                           DryRun=dryRun, TransitGatewayId=target)

    def createRouteTarget_NetworkInterface(self, destCidrBlock, target, destIpv6CidrBlock=None, dryRun=False):
        route = None
        if destIpv6CidrBlock != None:
            route = self.__rt.create_route(DestinationCidrBlock=destCidrBlock,
                                           DestinationIpv6CidrBlock=destIpv6CidrBlock,
                                           DryRun=dryRun, NetworkInterfaceId=target)
        else:
            route = self.__rt.create_route(DestinationCidrBlock=destCidrBlock,
                                           DryRun=dryRun, NetworkInterfaceId=target)

    def createRouteTarget_VpcPeer(self, destCidrBlock, target, destIpv6CidrBlock=None, dryRun=False):
        route = None
        if destIpv6CidrBlock != None:
            route = self.__rt.create_route(DestinationCidrBlock=destCidrBlock,
                                           DestinationIpv6CidrBlock=destIpv6CidrBlock,
                                           DryRun=dryRun, VpcPeeringConnectionId=target)
        else:
            route = self.__rt.create_route(DestinationCidrBlock=destCidrBlock,
                                           DryRun=dryRun, VpcPeeringConnectionId=target)
