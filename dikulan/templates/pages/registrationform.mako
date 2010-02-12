<%inherit file="/main.mako"/>
<h1>Registrer</h1>
<form method="post" action="${url_for("user_register")}">
<table>
    <tr>
        <th><label class="login-form-label" for="register-email">E-mail:</label></th>
        <td>
            <input id="register-email" value=${esc_attr(email)} type="text" name="email"/>
            <p class="hint">
                Vi vil kontakte dig på e-mailen for at bekræfte dens rigtighed.
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
        <td colspan="2" id="register-submit"><input type="submit" value="Opret"/></td>
    </tr>
</table>
</form>
