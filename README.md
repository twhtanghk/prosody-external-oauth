prosody-external-oauth
======================

Prosody external authentication for OAuth2

User supplied username and password will be sent to specified OAuth2 Provider
to verify the identity as specified in Section 4.3 of RFC 6749 (Resource Owner
Password Credentials Grant) or RFC 6750 (Bearer Token). Either password or
bearer token can be used to verify the user identify.

Configuration
-------------
Install python requests library
* run pip install -r requirements.txt

Edit env.py to define the following parameters
* clientId = "xmpp"
* clientPass = "xmpp-client"
* tokenUrl = "https://ttsoon.com/org/oauth2/token/"
* userUrl = "https://ttsoon.com/org/api/users/{0}/exists/"
* verify = False or cabundle file

It is required to specify the cabundle file if https connected to sever
with self-signed certificate in tokenUrl and userUrl. Please see [python requests library]
(http://docs.python-requests.org/en/latest/user/advanced/#ssl-cert-verification)
for details.

Logging
-------
Edit env.py to define logger log level (INFO/ERROR/DEBUG/FATAL) for all oauth2 requests.

	'loggers': {
        'requests': {
            'handlers': ['logfile'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'oauth2': {
            'handlers': ['logfile'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }

Testing
-------
Run oauth2.py with the parameter as specified in [prosody external auth]
(http://code.google.com/p/prosody-modules/wiki/mod_auth_external)

	cat | python oauth2.py 
	auth:username:ttsoon.com:password 
	isuser:username:ttsoon.com 