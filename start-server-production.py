#!/usr/bin/env python
# -*- coding: utf-8 -*-
from cherrypy import wsgiserver
from dikulan.application import Application

server = wsgiserver.CherryPyWSGIServer(("0.0.0.0", 5000), Application())
try:
    server.start()
except KeyboardInterrupt:
    server.stop()
