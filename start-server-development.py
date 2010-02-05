#!/usr/bin/env python
# -*- coding: utf-8 -*-
from werkzeug import run_simple
from dikulan.application import Application

run_simple(
    "127.0.0.1", 5000, Application(), use_debugger=True, use_reloader=True
)
