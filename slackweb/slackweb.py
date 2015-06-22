# -*- coding: utf-8 -*-


# 3rd party library
try:
    from urllib.parse import urljoin
    from urllib.parse import urlencode
    import urllib.request as urlrequest
except ImportError:
    from urlparse import urljoin
    from urllib import urlencode
    import urllib2 as urlrequest
import json


class Slack():

    def __init__(self, url=""):
        self.url = url
        self.opener = urlrequest.build_opener(urlrequest.HTTPHandler())

    def notify(self, **kwargs):
        """
        Send message to slack API
        """
        return self.send(kwargs)

    def send(self, payload):
        """
        Send payload to slack API
        """
        payload_json = json.dumps(payload)
        data = urlencode({"payload": payload_json})
        req = urlrequest.Request(self.url)
        response = self.opener.open(req, data.encode('utf-8')).read()
        return response.decode('utf-8')
