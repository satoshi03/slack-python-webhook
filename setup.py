# -*- coding:utf-8 -*-

try:
  import setuptools
  from setuptools import setup
except ImportError:
  print("Please install setuptools.")

setup_options = dict(
    name        = "slackweb",
    description = "slack bot for incomming webhook",
    author      = "satoshi03",
    author_email = "innamisatoshi@gmail.com",
    license     = "MIT License",
    url         = "https://github.com/satoshi03/slack-python-webhook",
    classifiers = [
      "Programming Language :: Python :: 2.7",
      "Programming Language :: Python :: 3",
      "Programming Language :: Python :: 3.3",
      "License :: OSI Approved :: MIT License"
    ]
)
setup_options["version"] = "1.0.2"
setup_options.update(dict(
  packages         = ['slackweb'],
))

setup(**setup_options)
