def fireworks(request):
    return """
    <!doctype html>
    <html>
    <head>
    <meta charset='utf-8'>
    <title>Setting Off Fireworks with Cloud Functions</title>
    <style>
    html,* { margin:0; padding:0}
    body { width:100%; height:100%;}
    .demo { margin:0 auto; width:100%; height:100%;}
    h1 { margin:150px auto 30px auto; text-align:center; font-family:'Roboto';}
    </style>
    </head>
    <body style='background-color:#060C59;'>
    <h1 style='padding-top:100px;font-size:48px;color:white;text-align:center;'>Dev Ops Guild Content from Nathan...<br>
        <img src='https://github.com/Nathands117/content-gc-serverless/blob/master/cloud-functions-demo/assets/fireworks-colors-night-sky-stock-image-black-background-233389298.png' alt='Dev Ops Guild'></h1>
    <div class='demo'>
    </div>
    <script src='https://code.jquery.com/jquery-3.1.1.min.js'></script>
    <script src='https://www.jqueryscript.net/demo/Realistic-Fireworks-Animations-Using-jQuery-And-Canvas-fireworks-js/jquery.fireworks.js'></script>
    <script>
    $('.demo').fireworks({ sound: true, opacity: 0.9, width: '100%', height: '100%' });
    </script>
    </body>
    </html>
    """
