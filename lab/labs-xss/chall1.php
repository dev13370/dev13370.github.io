<?php
if(isset($_GET['showme'])) {
} else {
header('Location:'.$_SERVER['PHP_SELF'].'?'.'showme=page');
die;
}
?>
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title> HACK THE HackerNap Labs</title>
    <style>
        body {
            background-color:black;
            text-align: center;
        }

        h1 { 
          color:coral;
        }
        .xss-typing {
          color:chocolate;
          font-family: monospace;
          overflow: hidden; 
          white-space: nowrap; 
          margin: 50px auto; 
          letter-spacing: .1em;
          animation: 
          typing 5.9s steps(100, end),
          blink-caret .5s step-end infinite;
          text-align: center;
          margin-top: 40px;
          font-size: 40px;
        }


        @keyframes typing {
          from { width: 0 }
          to { width: 100% }
        }
    </style>
  </head>
  <body>
  <div class="xss-typing">
  <p>
  البرمجة النصية عبر المواقع Xss
  </p>
  <p>
  لنبدأ من الرابط
  </p>
  <p>
  Happy hacking ^_^
  </p>
</div>
     
	<?php

	 if(isset($_GET['showme'])) {
        $value = $_GET['showme'];
        echo $value;
}
?>
  </body>
</html>