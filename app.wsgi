#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sys import path
from os.path import dirname
path.append(dirname(__file__))

from dikulan.application import Application

application = Application(debug=False)
