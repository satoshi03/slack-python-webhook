# Slack Bot for WebHook

Very simple slack client by using incoming-webhook.

## How to install

To install slack-python-webhook, simply:

<pre>
$ sudo pip install slackweb
</pre>

or from source:

<pre>
$ sudo python setup.py install
</pre>

## Getting started

Get a token of slack webhook on [slack page](https://my.slack.com/services/new/incoming-webhook/).

Instantiate:
<pre>
> import slackweb
> slack = slackweb.Slack(url="https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX")
</pre>

In case that you want to send a simple message:

<pre>
> slack.notify(text="Maguro is a sushi")
</pre>

In case that you want to send a custom message:

<pre>
> slack.notify(text="Tako is a sushi", channel="#sushi", username="sushi-bot", icon_emoji=":sushi:")
</pre>

If you want to use richly-formatted massages:

<pre>
> attachments = []
> attachment = {"title": "Sushi", "pretext": "Sushi _includes_ gunkanmaki", "text": "Eating *right now!*", "mrkdwn_in": ["text", "pretext"]}
> attachments.append(attachment)
> slack.notify(attachments=attachments)
</pre>

More detail description of message formatting, refer according pages:

- [Message Formatting](https://api.slack.com/docs/formatting)
- [Attachments](https://api.slack.com/docs/attachments)

