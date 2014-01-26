import logging.config

# authType = "Resource" or "Bearer"
authType = "Bearer"
clientId = "xmpp"
clientPass = "xmpp-client"
# tokenUrl = 
#    "https://ttsoon.com/org/oauth2/token/" for Resource
#    or "https://ttsoon.com/org/api/users/me/" for Bearer
tokenUrl = "https://ttsoon.com/org/api/users/me/"
userUrl = "https://ttsoon.com/org/api/users/{0}/exists/"
# False or cabundle file
verify = '/etc/ssl/certs/ca-certificates.crt'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(asctime)s %(message)s'
        },
    },
    'handlers': {
        'console':{
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
	'logfile': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': "prosody-external-oauth.log",
            'maxBytes': 50000,
            'backupCount': 2,
            'formatter': 'simple',
        },
    },
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
}
logging.config.dictConfig(LOGGING)
