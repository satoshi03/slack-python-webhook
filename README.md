# Slack Bot for WebHook

Very simple slack client by using incoming-webhook.

## How to install

To install slack-python-webhook, simply:

<pre>
$ sudo pip install -U git+https://github.com/satoshi03/slack-python-webhook
</pre>

or from source:

<pre>
$ sudo python setup.py install
</pre>

## Getting started

Get a token of slack webhook on [slack page](https://my.slack.com/services/new/incoming-webhook/).

In case that you want to send a simple message:

<pre>
> import slackbot
> slackbot = slackbot.Slack(token="T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX")
> slackbot.notify(text="Maguro is a sushi")
</pre>

In case that you want to send a custom message:

<pre>
> slackbot.notify(text="Tako is a sushi", channel="#sushi", username="sushi-bot", icon_emoji=":sushi:")
</pre>

If you want to use richly-formatted massages:

<pre>
> attachments = []
> attachment = {"title": "Sushi", "pretext": "Sushi _includes_ gunkanmaki", "text": "Eating *right now!*", "mrkdwn_in": ["text", "pretext"]}
> attachments.append(attachment)
> slackbot.notify(attachments=attachments)
</pre>

More detail description of message formatting, refer according pages:

- [Message Formatting](https://api.slack.com/docs/formatting)
- [Attachments](https://api.slack.com/docs/attachments)

