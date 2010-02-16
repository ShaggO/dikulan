<%inherit file="/main.mako"/>
<h1>Tilmelding</h1>
<form method="post" action="${url_for("user_register")}">
<table>
    <tr>
        <th><label class="login-form-label" for="register-email">E-mail:</label></th>
        <td>
            <input id="register-email" value=${esc_attr(email)} type="text" name="email"/>
            <p class="hint">
                Vi skal bruge din e-mail til diverse statusopdatering før og 
                under LAN'et.
            </p>
            <p class="hint">Desuden skal du bruge denne til at logge ind med
                fremover.
            </p>
% if error_email_taken:
<p class="error-message">Der findes allerede en bruger med denne email.</p>
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
        <th><label class="login-form-label" for="register-password">Password:</label></th>
        <td>
            <input id="register-password" type="password" name="password"/>
            <p class="hint">
                Passwordet sørger for at det kun er dig der kan logge ind med din e-mail.
            </p>
% if error_no_password:
    <p class="error-message">Du glemte at udfylde et password.</p>
% endif
        </td>
    </tr>
    <tr>
        <th><label class="login-form-label" for="register-ticketid">Billetnummer:</label></th>
        <td>
            <input id="register-ticketid" type="text" name="ticketid"/>
            <p class="hint">
                Du kan kun oprette dig som bruger hvis du har en billet. Indtast
                dit billetnummer her.
            </p>
        </td>
    </tr>
    <tr>
        <th><label class="login-form-label" for="register-captcha">Captcha:</label></th>
        <td>
            <input id="register-password" type="password" name="password"/>
            <p class="hint">
                For at hindre <a href=" http://en.wikipedia.org/wiki/Brute_force_attack">
                bruteforce angreb</a> bedes du indtaste tallende fra billedet.
            </p>
            <img src="${url_for("captcha")}" alt="captcha"/>
        </td>
    </tr>
    <tr>
        <th>&nbsp;</th>
        <td><input type="submit" value="Opret"/></td>
    </tr>
</table>
</form>
