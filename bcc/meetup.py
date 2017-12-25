""" Black Code Collective Meetup Api """
import os
import requests
import logging as log


class MEETUP(object):
    def __init__(self):
        self.base_url = 'https://api.meetup.com'
        self.key = "key={}".format(os.environ.get('MEETUP_API'))
        self.group_urlname = 'Black-Code-Collective'
        self.events = []

    def get_events(self):
        url = "{}/{}/events?{}".format(self.base_url, self.group_urlname, self.key)
        self.events = requests.get(url).json()
        log.info('updated meetup events')
