#!/usr/bin/env python

import sys
import json
import base64
import requests
import logging
from os.path import expanduser

try:    
    sys.path.append(expanduser("~/.python"))
    from env import authType, clientId, clientPass, tokenUrl, userUrl, verify
except ImportError:
    pass

logger = logging.getLogger('oauth2')

def authResource(args):
    username = args[1]
    domain = args[2]
    password = args[3]
    code = base64.b64encode("{0}:{1}".format(clientId, clientPass))
    data = {
        'grant_type': "password",
        'username': username,
        'password': password
    }
    headers = { 'Authorization': "Basic {0}".format(code) }
    r = requests.post(tokenUrl, data, headers=headers, verify=verify)
    logger.debug(r.content)
    return 1 if r.status_code == 200 else 0
    
def authBearer(args):
    username = args[1]
    domain = args[2]
    password = args[3]
    headers = { 'Authorization': "Bearer {0}".format(password) }
    r = requests.get(tokenUrl, headers=headers, verify=verify)
    logger.debug(r.content)
    return 1 if r.status_code == 200 and r.json()['username'] == username else 0
    
def auth(args):
    func = { 'Resource': authResource, 'Bearer': authBearer }
    return func[authType](args)
    
def isuser(args):
    username = args[1]
    domain = args[2]
    r = requests.get(userUrl.format(username), verify=verify)
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