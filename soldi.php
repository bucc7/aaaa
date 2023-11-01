<DOCTYPE html>
<html>
    <head>
        <title>Soldi UI v1</title>
    </head>
    <body onload="return checkLoginStatus();">
        <script type="text/javascript">
            function checkLoginStatus() {
                const urlParams = new URLSearchParams(window.location.search);
                const hasLoggedIn = urlParams.get('hasLoggedIn');
                if (hasLoggedIn !== "true") {
                    window.location.href = "index.html?hasLoggedIn=false";
                    return false;
                }
            }
        </script>

        <p>we</p>
    </body>
</html>