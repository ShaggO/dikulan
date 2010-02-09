<%inherit file="/main.mako"/>
<h1>Login</h1>
<p>
    Hvis du er registreret kan du logge ind ved hjælp af din e-mail og din
    adgangskode. Hvis du ikke er registreret endnu
    <a href="${url_for("user_register")}">kan du gøre det her.</a>
</p>
<form>
<table>
    <tr>
        <th>Brugernavn:</th>
        <td><input type="text" name="username"/></td>
    </tr>
    <tr>
        <th>Password:</th>
        <td><input type="password" name="password"/></td>
    </tr>
    <tr>
        <td colspan="2" id="login-submit"><input type="submit" value="Log ind"/></td>
    </tr>
</table>
</form>
