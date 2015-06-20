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


DEFAULT_WEBHOOK_URL = "https://hooks.slack.com/services/"


class SlackBot():

    def __init__(self, token="", url=DEFAULT_WEBHOOK_URL):
        self.token = token
        self.url = url

    def send_message(self, message, channel="", username="", icon_emoji="", icon_url=""):

        def make_payload(message, channel, username, icon_emoji):
            payload = {}
            if channel:
                payload["channel"] = channel
            if username:
                payload["username"] = username
            if icon_emoji:
                payload["icon_emoji"] = icon_emoji
            if icon_url:
                payload["icon_url"] = icon_url
            payload["text"] = message
            return payload

        payload = make_payload(message, channel, username, icon_emoji)
        self.send(payload)

    def send(self, payload):
        payload_json = json.dumps(payload)
        data = urlencode({"payload": payload_json})
        req_url = urljoin(self.url, self.token)
        req = urlrequest.Request(req_url)
        urlrequest.urlopen(req, data.encode('utf-8'))
