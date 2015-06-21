# -*- coding:utf-8 -*-

try:
  import setuptools
  from setuptools import setup
except ImportError:
  print("Please install setuptools.")

import os
import sys
import info
import version


setup_options = info.INFO
setup_options["version"] = version.VERSION
setup_options.update(dict(
  packages         = ['slackweb'],
))

setup(**setup_options)
