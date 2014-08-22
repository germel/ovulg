def CiscoScan(device, snmp_comm, snmp_pass=''):
    from pysnmp.entity.rfc3413.oneliner import cmdgen
    
    if snmp_comm:
        community = snmp_comm
    else:
        community = 'public'
        
    cmdGen = cmdgen.CommandGenerator()
    
    errorIndication, errorStatus, errorIndex, varBindTable = cmdGen.bulkCmd(
        cmdgen.CommunityData(community),
        cmdgen.UdpTransportTarget((device, 161)),
        0, 1,
        '1.3.6.1.4.1.9.9.23.1.2.1.1.4', # neihbor's IP address
        '1.3.6.1.4.1.9.9.23.1.2.1.1.6', # neighbor's name
        '1.3.6.1.4.1.9.9.23.1.2.1.1.7', # interface where neighbor is connected
    )
    
    # Check for errors and print out results
    if errorIndication:
        return(errorIndication)
    else:
        if errorStatus:
            return(
                print('%s at %s' % (
                errorStatus.prettyPrint(),
                errorIndex and varBinds[int(errorIndex)-1] or '?')
                )
            )
        else:
            return(varBindTable)
