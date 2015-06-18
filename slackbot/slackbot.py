#-*- coding: utf-8 -*-


# 3rd party library
import urllib2
import urllib
import json


WEBHOOK_URL_PREFIX = "https://hooks.slack.com/services/"


class SlackBot():

    def ___init__(self, token="", channel="", username="", icon_emoji=""):
        self.token = token
        self.channel = channel
        self.username = username
        self.icon_emoji = icon_emoji

    def notify(self, message):
        payload = self.make_payload(message)
        payload_json = json.dumps(payload)
        data = urllib.urlencode({"payload": payload_json})
        url = urllib.parse.urljoin(WEBHOOK_URL_PREFIX, self.token)
        req = urllib2.Request(url)
        req.add_data(data)
        urllib2.urlopen(req)

    def make_payload(self, message):
        payload = {}
        if self.channel:
            payload["channel"] = self.channel
        if self.username:
            payload["username"] = self.username
        if self.icon_emoji:
            payload["icon_emoji"] = self.icon_emoji
        payload["text"] = message
        return payload


class SlackBotException(Exception):
    pass
