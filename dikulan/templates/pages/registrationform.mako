<%inherit file="/main.mako"/>
<h1>Registrer</h1>
<form method="post" action="${url_for("user_register")}">
<table>
    <tr>
        <th><label class="login-form-label" for="register-email">Brugernavn:</label></th>
        <td><input id="register-email" type="text" name="username"/></td>
    </tr>
    <tr>
        <th><label class="login-form-label" for="register-password">Password:</label></th>
        <td><input id="register-password" type="password" name="password"/></td>
    </tr>
    <tr>
        <td colspan="2" id="register-submit"><input type="submit" value="Opret"/></td>
    </tr>
</table>
</form>
