<?php
if(!isset($_GET['status'])) {
  header('Location: chall6.php?status=HackerNap');
}
?>
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>Removes Alert</title>
  </head>

  <style>
        body {
            background-color:black;
            text-align: center;
        }

        h1, h2, h3, h4, h5, h6 { 
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
  <hr>
  <p>
  Removes Alert
  </p>
  <p>
  Happy hacking ^_^
  </p>
</div>

<?php
    if(isset($_GET['status'])) {
    $status =  $_GET['status'];

    $status = preg_replace('/alert/', '', $status);

    echo $status;
    }
    ?>