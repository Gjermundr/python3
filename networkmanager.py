from pysnmp.hlapi import *


def Walksnmp():
    OID = '1.3.6'

    for (errorIndication, errorStatus, errorIndex, varBinds) in nextCmd(SnmpEngine(),
           CommunityData('public'),
           UdpTransportTarget(('demo.snmplabs.com', 161)),
           ContextData(),
           ObjectType(ObjectIdentity(OID))):

        if errorIndication:
            print('Error indication: {}'.format(errorIndication))
            break

        elif errorStatus:
            print('Error status: {}'.format(errorStatus))
            break

        else:

            for varBind in varBinds:
                print('{} = {}'.format(varBind[0], varBind[1]))


def Getsnmp():
    base_OID = '1.3.6'

    errorIndication, errorStatus, errorIndex, varBinds = next(getCmd(SnmpEngine(),
               CommunityData('public'),
               UdpTransportTarget(('demo.snmplabs.com', 161)),
               ContextData(),
               ObjectType(ObjectIdentity(base_OID)))
    )


    if errorIndication:
        print('Error indication: {}'.format(errorIndication))

    elif errorStatus:
        print('Error status: {}'.format(errorStatus))

    else:
        for varBind in varBinds:
            print('{} = {}'.format(varBind[0], varBind[1]))


Getsnmp()