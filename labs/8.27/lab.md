Reading Network Logs
AWS Flow Log Record Syntax
<version> <account-id> <interface-id> <src-addr> <dstaddr> <srcport> <dstport> <protocol> <packets> <bytes> <start(time)> <end(time)> <action> <log-status>

Log 1:
- network layer/transport layer, there are IP addresses
- AWS, refers to Amazon cloud 
- provides event data, data/time
- shows different IPs, ports and protocols (6, 17 refer to TCP/UDP protocols)
- firewall, accepting or rejecting the different actions

Log 2:
- AWS, refers to Amazon cloud
- provides IPs, ports and protocols (both IPv4 and IPv6)
- some data packets were not recorded, NODATA/SKIPDATA

Web Proxies:
- could be using Squid
- making HTTP GET requests
- provided HTTP codes back (304, 200) https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
    - 304 = not modified
    - 200 = ok
- date/time shown 
- TCP_HIT, TCP_NC_MISS, TCP_RESCAN_HIT https://support.symantec.com/us/en/article.tech242963.html
    - TCP_HIT = valid request in cache 
    - TCP_NC_MISS = request was returned from the original server, wasn't cacheable
    - TCP_RESCAN_HIT = request was in cache and rescanned because virus scanner ID in the request was different from current scanner
- shows what type of device was used (i.e. Windows, Mac) and the browser type (Mozilla/Firefox)
- shows whether the request was made through a proxy or directly

Firewalls:
- inbound allowed for Apache
- TCP/UDP
- 4 unique IP addresses shown 
- DHCP was blocked
- port 80 is allowed through firewall (HTTP)

Netflow:
- visitors are going to Amazon, DNS, Facebook, Google, Googleservices, HTTP, ICMP, LinkedIn, SSL, Twitter and Unknown
- using DNS, DNS Google, DNS Facebook, DNS Twitter
- there are three unique clients
- there seems to be a port scan, has same ip but the ports are different 

 DNS:
 - the headers: timestamp, src ip, src port, dst ip, dst port, protocol, website


Python:
- take in file iptablesyslog 
- split files on lines