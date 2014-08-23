from pyasn1.type import univ
import pysnmp, socket

def uCisco(snmp_response):
    ans = list()
    try:
        for i, j, k in snmp_response:
           m,n = i
           o,p = j
           q,r = k
           z = 0
           if '1.3.6.1.4.1.9.9.23.1.2.1.1.4' in str(m) and type(n) == pysnmp.proto.rfc1902.OctetString:
               try:
                   ip_ad = socket.inet_ntoa(n.asOctets())
                   ansip = str(ip_ad)
               except:
                   ansip = "Switch has no IP adress!!!"
    
           if '1.3.6.1.4.1.9.9.23.1.2.1.1.6' in str(o) and type(p) == pysnmp.proto.rfc1902.OctetString:
               try:
                   ansdesc = str(p)
               except:
                   ansdesc = 'Unnamed'
                
           if '1.3.6.1.4.1.9.9.23.1.2.1.1.7' in str(q) and type(r) == pysnmp.proto.rfc1902.OctetString:
               try:
                   ansint = str(r)
               except:
                   ansint = 'Unnamed'
    
               ans.append((ansip, ansdesc, ansint))
    except TypeError:
        ans.append(('Something went bad: ' + str(snmp_response)))
    return(ans)

def untangle(snmp_response, maker='cisco'):
    if maker == 'cisco':
        return(uCisco(snmp_response))