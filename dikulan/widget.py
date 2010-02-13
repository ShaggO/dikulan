from dikulan.utils import render_widget, pool, url_for, local


def sidemenu():
    is_logged_in = local.session.get("user_id") != None
    return render_widget("widgets/sidemenu.mako",
        is_logged_in = is_logged_in
    )
    
def statusbar():
    from dikulan.model.user import get_email
    is_logged_in = local.session.get("user_id") != None
    email = ""
    if is_logged_in:
        email = get_email(local.session.get("user_id"))
    
    return render_widget("widgets/statusbar.mako",
        is_logged_in = is_logged_in,
        email = email
    )
