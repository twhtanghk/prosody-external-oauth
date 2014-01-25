import logging.config

clientId = "xmpp"
clientPass = "xmpp-client"
tokenUrl = "http://ttsoon.com:8001/org/oauth2/token/"
userUrl = "http://ttsoon.com:8001/org/api/users/{0}/exists/"
verify = False
cert = ''

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
