#DevScan
from pysnmp.entity.rfc3413.oneliner import cmdgen

#uCisco
from pyasn1.type import univ
import pysnmp, socket


def DevScan(ip_add, snmp_comm='public', snmp_pass='', maker='cisco'):
    if maker == 'cisco':
        oids = {
                'nei_ip' : '1.3.6.1.4.1.9.9.23.1.2.1.1.4',     # neihbor's IP address from CISCO MIB
                'nei_name' : '1.3.6.1.4.1.9.9.23.1.2.1.1.6',   # neighbor's name from CISCO MIB
                'nei_if' : '1.3.6.1.4.1.9.9.23.1.2.1.1.7',     # neighbor's interface from CISCO MIB
                'local_if' : '1.3.6.1.4.1.9.9.23.1.1.1.1.6',   # local interface from CISCO MIB
                }
    
    cmdGen = cmdgen.CommandGenerator()
    
    errorIndication, errorStatus, errorIndex, varBindTable = cmdGen.bulkCmd(
        cmdgen.CommunityData(snmp_comm),
        cmdgen.UdpTransportTarget((ip_add, 161)),
        0, 1,
        oids['nei_ip'],     # neihbor's IP address
        oids['nei_name'],   # neighbor's name
        oids['nei_if'],     # interface where neighbor is connected
        oids['local_if'],   # local interface
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
            #return(varBindTable)
            return(untangle(varBindTable, oids, maker))


def uCisco(snmp_response, oids):
    ans = list()
    #ans = [('Switch IP address', 'Switch Name', 'Local Interface', 'Remote Interface')]
    try:
        for i, j, k, l in snmp_response:
           m,n = i
           o,p = j
           q,r = k
           s,t = l
           if oids['nei_ip'] in str(m) and type(n) == pysnmp.proto.rfc1902.OctetString:
                try:
                    ip_ad = socket.inet_ntoa(n.asOctets())
                    ansip = str(ip_ad)
                except:
                    ansip = "0.0.0.0"
    
                if oids['nei_name'] in str(o) and type(p) == pysnmp.proto.rfc1902.OctetString:
                    try:
                        ansdesc = str(p)
                    except:
                        ansdesc = 'Switch has no name'
                else:
                    ansdesc = 'Someerror'
                
                if oids['nei_if'] in str(q) and type(r) == pysnmp.proto.rfc1902.OctetString:
                    try:
                        ansnint = str(r)
                    except:
                        ansnint = 'Magical remote interface...'
                else:
                    ansnint = 'Someerror'

                if oids['local_if'] in str(s) and type(t) == pysnmp.proto.rfc1902.OctetString:
                    try:
                        anslint = str(t)
                    except:
                        anslint = 'Magical local interface...'
                else:
                    anslint = 'Someerror'

                ans.append((ansip, ansdesc, anslint, ansnint))

    except TypeError:
        ans.append(('Something went bad: ' + str(snmp_response)))
    return(ans)

def untangle(snmp_response, oids, maker='cisco'):
    if maker == 'cisco':
        return(uCisco(snmp_response, oids))