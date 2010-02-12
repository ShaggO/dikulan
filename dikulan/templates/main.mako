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
                    ${widget.sidemenu()}
                </ul>
                <div id="main-content">
                    ${widget.statusbar()}
                    ${next.body()}
                </div>
            </div>
        </div>
        <div id="bottom">
            <img alt="" src="/static/images/page-bottom.png"/>
        </div>
    </div>
</body>
