# -*- coding: utf-8 -*-
from werkzeug import Request, Response, SharedDataMiddleware
from dikulan.utils import local, url_map, root_path
from os.path import dirname, join
from werkzeug.exceptions import NotFound
import logging
import dikulan.responders as responders
from dikulan.lib.session import Session

log = logging.getLogger(__name__)

class Application(object):
    def __init__(self):
        local.application = self
        self.dispatch = SharedDataMiddleware( self.dispatch, {
                "/static" : join(root_path, "static")
            }
        )
    
    def dispatch(self, environ, start_response):
        url_adapter = url_map.bind_to_environ(environ)
        local.url_adapter = url_adapter
        local.request = Request(environ)
        local.session = Session()
        try:
            endpoint, params = url_adapter.match()
            response = getattr(responders,endpoint)(**params)
        except NotFound:
            response = getattr(responders,"notfound")()
        local.session.set_cookie(response)
        local.session.save_session()
        return response(environ, start_response)
        
    def __call__(self, environ, start_response):
        local.application = self
        return self.dispatch(environ, start_response)
