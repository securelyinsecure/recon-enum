Requires Python3
Requires requests

`Easy_install3 requests` |
`pip3 install requests`

Subdomain enumeration script that creates/uses a dynamic resource script for recon-ng.
only 1 module needs api’s (/api/google_site) find instructions for that on the wiki.
uses google scraping, bing scraping, baidu scraping, netcraft, and bruteforces to find subdomains.
oringal by @jhaddix
https://github.com/jhaddix/domain

Recon-ng by @LaNMaSteR53 - https://bitbucket.org/LaNMaSteR53/recon-ng

Addional funtionality and port to python by @securelyinsecure:

usage: 

`recon-enum.py [-h] -d  [-B] [-S] [-R] [--reset_workspace]`

optional arguments

`-h, --help            show this help message and exit`
  
`-d DOMAIN, --domain DOMAIN specify a domain`
  
`-B, --brute           Toggle Brute force of subdomains (default=false)`
  
`-S, --suffix          Toggle Brute force of domain suffix (default=false)`
  
`  -R, --reverse_resolve Toggle reverse dns lookups of hosts (default=false)`
  
` --reset_workspace     Reset recon-ng workspace for domain (default=false)`
