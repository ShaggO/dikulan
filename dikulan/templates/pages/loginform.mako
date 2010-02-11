<%inherit file="/main.mako"/>
<h1>Login</h1>
<p>
    Hvis du er registreret kan du logge ind ved hjælp af din e-mail og din
    adgangskode. Hvis du ikke er registreret endnu
    <a href="${url_for("user_register")}">kan du gøre det her.</a>
</p>
<form method="post" action="${url_for("user_login")}">
<table>
    <tr>
        <th><label class="login-form-label" for="login-username">Brugernavn:</label></th>
        <td><input id="login-username" type="text" name="username"/></td>
    </tr>
    <tr>
        <th><label class="login-form-label" for="login-password">Password:</label></th>
        <td><input id="login-password" type="password" name="password"/></td>
    </tr>
    <tr>
        <td colspan="2" id="login-submit"><input type="submit" value="Log ind"/></td>
    </tr>
</table>
</form>
