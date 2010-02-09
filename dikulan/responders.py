# -*- coding: utf-8 -*-
import logging
from werkzeug import Response
from dikulan.utils import expose, render_template

log = logging.getLogger(__name__)

@expose("/")
@expose("/index")
def frontpage(request):
    return render_template("/pages/frontpage.mako")

@expose("/information")
def information(request):
    return render_template("/pages/information.mako")

@expose("/madmuligheder")
def foodoptions(request):
    return render_template("/pages/food-options.mako")

@expose("/turneringer-events")
def tournaments_events(request):
    return render_template("/pages/tournaments-events.mako")

@expose("/regler")
def rules(request):
    return render_template("/pages/rules.mako")

@expose("/pladsbestilling")
def seatbooking(request):
    return render_template("/pages/seatbooking.mako")

@expose("/pladsbestilling/statusimage")
def seatbooking_statusimage(request):
    return Response("Not implemented")

@expose("/galleri")
def gallery(request):
    return render_template("/pages/gallery.mako")

@expose("/kontakt")
def contact(request):
    return render_template("/pages/contact.mako")

@expose("/nyheder")
def news(request):
    return render_template("/pages/news.mako")

@expose("/user/login")
def user_login(request):
    return render_template("/pages/loginprompt.mako")

@expose("/user/login/auth")
def user_login_auth(request):
    return Response("Auth!")

@expose("/user/register")
def user_register(request):
    return Response("Register!")

def notfound(request):
    return render_template("/pages/errors/notfound.mako")
