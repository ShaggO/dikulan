# -*- coding: utf-8 -*-
import logging
from werkzeug import Response, redirect
from dikulan.utils import expose, render_template, pool, url_for, local
from dikulan.lib.session import Session


log = logging.getLogger(__name__)

@expose("/")
@expose("/index")
def frontpage():
    response = Response()
    render_template("/pages/frontpage.mako", response)
    return response

@expose("/information")
def information():
    response = Response()
    render_template("/pages/information.mako", response)
    return response

@expose("/madmuligheder")
def foodoptions():
    response = Response()
    render_template("/pages/food-options.mako", response)
    return response

@expose("/turneringer-events")
def tournaments_events():
    response = Response()
    render_template("/pages/tournaments-events.mako", response)
    return response

@expose("/regler")
def rules():
    response = Response()
    render_template("/pages/rules.mako", response)
    return response

@expose("/pladsbestilling")
def seatbooking():
    response = Response()
    render_template("/pages/seatbooking.mako", response)
    return response

@expose("/pladsbestilling/statusimage")
def seatbooking_statusimage():
    response = Response()
    "Not implemented"
    return response

@expose("/galleri")
def gallery():
    response = Response()
    render_template("/pages/gallery.mako", response)
    return response

@expose("/kontakt")
def contact():
    response = Response()
    render_template("/pages/contact.mako", response)
    return response

@expose("/nyheder")
def news():
    response = Response()
    render_template("/pages/news.mako", response)
    return response

@expose("/user/login")
def user_login():
    from dikulan.model.user import user_id_by_auth, AuthFailureException
    auth_failure = False
    if local.request.method == "POST":
        email = local.request.form.get("email", "")
        password = local.request.form.get("password", "")
        if email == "" or password == "":
            auth_failure = True
        if not auth_failure:
            try:
                local.session["user_id"] = user_id_by_auth(email, password)
                return redirect(url_for("user_profile"))
            except AuthFailureException:
                auth_failure = True

    response = Response()
    render_template("/pages/loginform.mako", response,
        auth_failure = auth_failure
    )
    return response

@expose("/user/register")
def user_register():
    return notfound()
    from dikulan.model.user import add_user, EmailExists, InvalidEmail
    response = Response()
    error_email_taken = False
    error_invalid_email = False
    error_invalid_password = False
    error_no_email = False
    error_no_password = False

    email = ""
    if (local.request.method == "POST"):
        email = local.request.form.get("email", "")
        password = local.request.form.get("password", "")
        if email == "":
            error_no_email = True
        if password == "":
            error_no_password = True
        if not error_no_email and not error_no_password:
            try:
                add_user(email, password)
                return redirect(url_for("user_login"))
            except EmailExists:
                error_email_taken = True
            except InvalidEmail:
                error_invalid_email = True
    
    render_template(
        "/pages/registrationform.mako", response,
        email=email,
        error_email_taken=error_email_taken,
        error_invalid_email=error_invalid_email,
        error_invalid_password=error_invalid_password,
        error_no_email=error_no_email,
        error_no_password=error_no_password,
    )
    return response

@expose("/user/profile")
def user_profile():
    return notfound()
    response = Response()
    email = local.session.get("user_id", "[Ukendt Bruger]")
    render_template("/pages/userprofile.mako", response,
        email = str(email)
    )
    return response

@expose("/user/logout")
def user_logout():
    local.session["user_id"] = None
    return redirect(url_for("frontpage"))

def notfound():
    response = Response()
    render_template("/pages/errors/notfound.mako", response)
    return response

def error():
	response = Response()
	render_template("/pages/errors/error.mako", response)
	return response
