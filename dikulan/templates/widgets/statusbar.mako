## -*- coding: utf-8 -*-
<div id="statusbar">
% if is_logged_in:
    <p>
        Du er logget ind som <a href="${url_for("user_profile")}">${name}</a>
    </p>
    <ul>
        <li><a href="${url_for("user_profile")}">Profil side</a>.</li>
        <li><a href="${url_for("user_logout")}">Log ud</a>.</li>
    </ul>
% else:
    <p>
        Du er ikke logget ind. <a href="${url_for("user_login")}">
        Klik her for at logge ind</a>.
    </p>
% endif
</div>
