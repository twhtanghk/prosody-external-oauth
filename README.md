prosody-external-oauth
======================

Prosody external authentication for OAuth2

User supplied username and password will be sent to specified OAuth2 Provider
to verify the identity as specified in Section 4.3 of RFC 6749 (Resource Owner
Password Credentials Grant).

Configuration
-------------
Install python requests library
* run pip install -r requirements.txt
Edit env.py to define the following parameters
* clientId = "xmpp"
* clientPass = "xmpp-client"
* tokenUrl = "http://localhost:8001/org/oauth2/token/"
* userUrl = "http://localhost:8001/org/api/users/{0}/exists/"
* verify = True or False
* cert = '/etc/ssl/certs/selfSignedCert.pem'
It is required to specify the certificate file if https is used in tokenUrl and userUrl
with self-signed certificate. Please see [python requests library]
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

	echo auth:username:ttsoon.com:password |python oauth2.py 
	echo isuser:username:ttsoon.com |python oauth2.py 