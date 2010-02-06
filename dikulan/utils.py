# -*- coding: utf-8 -*-
from werkzeug import Local, LocalManager
from werkzeug.routing import Map, Rule

local = Local()
local_manager = LocalManager([local])
application = local('application')
