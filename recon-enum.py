#!/usr/bin/env python3
import os
import time
import datetime
import argparse
import subprocess
import requests

__author_ = '@securelyinsecure'

"""Subdomain enumeration script that creates/uses a dynamic resource script for recon-ng.
only 1 module needs api’s (/api/google_site) find instructions for that on the wiki.
uses google scraping, bing scraping, baidu scraping, netcraft, and bruteforces to find subdomains.
oringal by @jhaddix
https://github.com/jhaddix/domainAdditional
Addional funtionality and port to python by @securelyinsecure to toggle subdomain bruteforce (-B), domain suffix (-S), help -h
"""



parser = argparse.ArgumentParser(description='A small python script to create and run a domain'
                                             ' through recon-ng.  Based on original enum.sh script by @jhaddix')
parser.add_argument('-d', '--domain', help='specify a domain', required='True')
parser.add_argument('-B', '--brute', action='store_true', help='Toggle Brute force of subdomains (default=false)')
parser.add_argument('-S', '--suffix', action='store_true', help='Toggle Brute force of domain suffix (default=false)')
parser.add_argument('-R', '--reverse_resolve', action='store_true', help='Toggle reverse dns lookups of hosts (default=false)')
parser.add_argument('--reset_workspace', action='store_true', help='Reset recon-ng workspace for domain (default=false)')
args = parser.parse_args()

domain = args.domain


now = datetime.datetime.now()
tstamp = "{0}-{1}-{2}".format(now.month, now.day, now.year)
path = os.path.curdir
recon_path = "/usr/share/recon-ng/recon-ng"


def test_connection():
    if requests.head("http://google.com"):
        return True
    else:
        return False

if test_connection():
    print("connection tests passed, starting recon-ng")
    if os.path.exists("{0}{1}.resource".format(domain,tstamp)):
        os.remove("{0}{1}.resource".format(domain,tstamp))
    with open("{0}{1}.resource".format(domain, tstamp), 'w') as f:
        if args.reset_workspace:
            f.write("workspaces delete {0}{1}\n".format(domain, tstamp))
        f.write("workspaces select {0}{1}\n".format(domain, tstamp))
        f.write("use recon/domains-hosts/baidu_site\n")
        f.write("set SOURCE {0}\n".format(domain))
        f.write("run\n")
        f.write("use recon/domains-hosts/bing_domain_web\n")
        f.write("set SOURCE {0}\n".format(domain))
        f.write("run\n")
        f.write("use recon/domains-hosts/google_site_web\n")
        f.write("set SOURCE {0}\n".format(domain))
        f.write("run\n")
        f.write("use recon/domains-hosts/netcraft\n")
        f.write("set SOURCE {0}\n".format(domain))
        f.write("run\n")
        f.write("use recon/domains-hosts/yahoo_domain\n")
        f.write("set SOURCE {0}\n".format(domain))
        f.write("run\n")
        f.write("use recon/domains-hosts/google_site_api\n")
        f.write("set SOURCE {0}\n".format(domain))
        f.write("run\n")
        if args.brute:
            print("using domain bruteforce option.  Please be patient, this may take a bit")
            f.write("use recon/domains-hosts/brute_hosts\n")
            f.write("set SOURCE {0}\n".format(domain))
            f.write("run\n")
        if args.suffix:
            f.write("use /recon/domains-domains/brute-suffix\n")
            f.write("set SOURCE {0}\n".format(domain))
            f.write("run\n")
        f.write("use recon/hosts-hosts/resolve\n")
        f.write("set SOURCE query SELECT DISTINCT host FROM hosts WHERE host IS NOT NULL AND ip_address IS NULL\n")
        f.write("run\n")
        #if args.reverse_resolve:
            #f.write("use recon/hosts-hosts/reverse_resolve\n")
            #f.write("set SOURCE query SELECT DISTINCT ip_address FROM hosts WHERE ip_address IS NOT NULL\n")
            #f.write("run\n")
        f.write("use reporting/csv \n")
        f.write("set FILENAME {0}/{1}.csv\n".format(path, domain))
        f.write("run\n")
        f.write("exit\n")
    subprocess.call([recon_path,  "--no-check", "-r" "{0}{1}.resource".format(domain, tstamp)])
else:
    print("No connection to google.com.  Please check your internet connection and dns settings and tyr again")
    exit()





