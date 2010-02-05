#!/usr/bin/env python
# -*- coding: utf-8 -*-
from werkzeug import run_simple
from cherrypy import wsgiserver
from dikulan.application import Application

#server = wsgiserver.CherryPyWSGIServer(("127.0.0.1", 5000), Application())
#try:
#    server.start()
#except KeyboardInterrupt:
#    server.stop()

run_simple(
    "127.0.0.1",
    5000,
    Application(),
    use_debugger=True,
    use_reloader=True
)
