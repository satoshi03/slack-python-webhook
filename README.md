# Slack Bot for WebHook


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

<pre>
> import slackbot
> slackbot = slackbot.Slack(token='T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX')
> slackbot.notify("Maguro is a sushi", "#sushi")
> slackbot.notify("Tako is a sushi", "#sushi", username='sushi-bot', icon_emoji=':sushi:')
</pre>



