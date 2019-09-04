#!/usr/bin/env python3
import sys
import re

count = {}
valid_ip = {}

pattern = re.compile('^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$')
def flatten(lis):
#    """Given a list, possibly nested to any level, return it flattened."""
   new_lis = []
   for item in lis:
       if type(item) == type([]):
           new_lis.extend(flatten(item))
       else:
           new_lis.append(item)
   return new_lis

def counter(ip_list):
    for ip in ip_list:
        if count.get(ip):
            count += 1
        else:
            count = 1
# validate ip using regex

def main():
    filename = sys.argv[1]
    f = open(filename, 'r')
    lines = f.readlines()
    ips = []
    for line in lines:
        #print(line)
        #process(line)
        ips.append(re.findall( r'[0-9]+(?:\.[0-9]+){3}', line))
    flatten_ips = flatten(ips)
    for ip in flatten_ips:
        if count.get(ip):
            count[ip] += 1
        else:
            count[ip] = 1
    for ip in flatten_ips:
        if pattern.match(ip):
             valid_ip[ip] = True
        else:
            valid_ip[ip] = False
    for ip in flatten_ips:
        
    print(valid_ip)

if __name__ == '__main__':
    main()