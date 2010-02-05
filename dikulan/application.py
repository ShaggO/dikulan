from werkzeug import Request, Response, ClosingIterator
from dikulan.utils import local
class Application(object):
	def __init__(self):
		local.application = self
	def __call__(self, environ, start_response):
		start_response('200 OK', [('Content-Type', 'text/html')])
		return ["Test"]
