<%inherit file="/xhtml11.mako"/>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
    <title>DIKULAN - The Challenge</title>
    <link media="screen" rel="stylesheet" type="text/css" href="/static/css/underside/screen.css"/>
</head>
<body>
    <div id="main">
        <div id="top">
            <img alt="" src="/static/images/page-top.png"/>
        </div>
        <div id="middle">
            <div id="middle-content">                    
                <ul id="menu">
                    <li class="menu-item"><a href="${url_for("frontpage")}">Forside</a></li>
                    <li class="menu-item"><a href="${url_for("information")}">Information</a></li>
                    <li class="menu-item"><a href="${url_for("foodoptions")}">Madmuligheder</a></li>
                    <li class="menu-item"><a href="${url_for("tournaments_events")}">Turneringer/events</a></li>
                    <li class="menu-item"><a href="${url_for("rules")}">Regler</a></li>
                    <li class="menu-item"><a href="${url_for("seatbooking")}">Pladsreservation</a></li>
                    <li class="menu-item"><a href="${url_for("gallery")}">Galleri</a></li>
                    <li class="menu-item"><a href="${url_for("contact")}">Kontakt</a></li>
                    <li class="menu-item"><a href="${url_for("news")}">Nyheder</a></li>
                    <li class="menu-item"><a href="${url_for("login")}">Login</a></li>
                </ul>
                <div id="main-content">
                    ${next.body()}
                </div>
            </div>
        </div>
        <div id="bottom">
            <img id="top" alt="" src="/static/images/page-bottom.png"/>
        </div>
    </div>
</body>
