<%inherit file="/main.mako"/>
<h1>Tilmelding</h1>

<p>
    Du betaler din billet med bankoverførsel. Når du har indtastet din e-mail,
    vil der komme en e-mail med vores bankoplysninger i.
</p>
<form method="post" action="${url_for("user_register")}">
<table>
    <tr>
        <th><label class="login-form-label" for="register-name">Navn:</label></th>
        <td>
            <input id="register-name" value=${esc_attr(name)} type="text" name="name"/>
            <p class="hint">
                Du <em>skal</em> angive dit navn for at kunne deltage.
            </p>
% if error_no_name:
    <p class="error-message">Du glemte at udfylde dit navn.</p>
% endif
        </td>
    </tr>
    <tr>
        <th><label class="login-form-label" for="register-email">E-mail:</label></th>
        <td>
            <input id="register-email" value=${esc_attr(email)} type="text" name="email"/>
            <p class="hint">
                Dette vil være den e-mail vi kontakter dig på fremover.
            </p>
% if error_email_taken:
    <p class="error-message">E-mailen er allerede registreret.</p>
% endif
% if error_invalid_email:
    <p class="error-message">Ugyldig e-mailadresse.</p>
% endif
% if error_no_email:
    <p class="error-message">Du glemte at udfylde en emailadresse.</p>
% endif
        </td>
    </tr>
    <tr>
        <th><label class="login-form-label" for="register-captcha">Er du et menneske?</label></th>
        <td>
            <input id="register-captcha" type="text" name="captcha"/>
            <p class="hint">
                For at hindre spam bedes du indtaste <em>bogstaverne</em> fra
                billedet herunder.
            </p>
            <img src="${url_for("captcha")}" alt="captcha"/>
% if error_captcha:
    <p class="error-message">Din indtastning matchede ikke med billedet. Prøv venligst igen.</p>
% endif
        </td>
    </tr>
    <tr>
        <th>&nbsp;</th>
        <td><input type="submit" value="Deltag i dikulan"/></td>
    </tr>
</table>
</form>
