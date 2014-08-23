from pysnmp.entity.rfc3413.oneliner import cmdgen
from corestuff.untangle import untangle

def DevScan(maker, ip_add, snmp_comm='public', snmp_pass=''):
    if maker == 'cisco':
        nei_ip = '1.3.6.1.4.1.9.9.23.1.2.1.1.4'     # neihbor's IP address from CISCO MIB
        nei_name = '1.3.6.1.4.1.9.9.23.1.2.1.1.6'   # neighbor's name from CISCO MIB
        nei_if = '1.3.6.1.4.1.9.9.23.1.2.1.1.7'     # neighbor interface from CISCO MIB
    
    cmdGen = cmdgen.CommandGenerator()
    
    errorIndication, errorStatus, errorIndex, varBindTable = cmdGen.bulkCmd(
        cmdgen.CommunityData(snmp_comm),
        cmdgen.UdpTransportTarget((ip_add, 161)),
        0, 1,
        nei_ip,     # neihbor's IP address
        nei_name,   # neighbor's name
        nei_if,     # interface where neighbor is connected
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
            return(untangle(varBindTable, maker))

def CiscoScan(device, snmp_comm, snmp_pass=''): #no longer used
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
