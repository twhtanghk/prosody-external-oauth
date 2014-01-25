#!/usr/bin/env python

import sys
import json
import base64
import requests
import logging
from os.path import expanduser

try:    
    sys.path.append(expanduser("~/.python"))
    from env import clientId, clientPass, tokenUrl, userUrl, verify, cert
except ImportError:
    pass

logger = logging.getLogger('oauth2')

def auth(args):
    username = args[1]
    domain = args[2]
    password = args[3]
    code = base64.b64encode("{0}:{1}".format(clientId, clientPass))
    data = {
        'grant_type': "password",
        'username': username,
        'password': password
    }
    headers = { 'Authorization': "Basic ${0}".format(code) }
    r = requests.post(tokenUrl, data, headers=headers, verify=verify, cert=cert)
    logger.debug(r.content)
    return 1 if r.status_code == 200 else 0
    
def isuser(args):
    username = args[1]
    domain = args[2]
    r = requests.get(userUrl.format(username), verify=verify, cert=cert)
    logger.debug(r.content)
    return 1 if r.status_code == 200 else 0
    
def setpass(args):
    return 0
    
def proccess(line):
    args = line.split(':')
    func = { 'auth': auth, 'isuser': isuser, 'setpass': setpass }
    if (args[0] in func):
        return func[args[0]](args)
    return 0    
    
logger.debug('start')
while 1:
    line = sys.stdin.readline().rstrip("\n")
    sys.stdout.write(str(proccess(line)) + "\n")
    sys.stdout.flush()
logger.debug('end')