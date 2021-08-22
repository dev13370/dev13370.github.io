<html lang="en">

<head>
    <title>Stored Xss</title>
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
     !! ماذا تستطيع ان تفعل هنا 
  </p>
  <p>
  Happy hacking ^_^
  </p>
</div>


		<?php

		if (isset($_POST['fname'])) {

			$name =  $_POST['fname'];
      $handle = fopen("chall3-list.csv", "a");
	     $line = array($name);
       fputcsv($handle, $line);
       fclose($handle);

		}
		else{

			echo '<form name="myForm" action="chall3.php" action="index.php" enctype="application/x-www-form-urlencoded" method="post">
			<div class="siimple-form">
			<div class="siimple-form-title">شارك كومنت معا المجتمع</div>
			<div class="siimple-form-field">
				<input type="text" class="siimple-input siimple-input--fluid" placeholder="اسمك" name="fname">
			</div>
			<div class="siimple-form-field">
				<input class="siimple-btn siimple-btn--blue" type="submit"  value="Send">
			</div>
			</div>
			</form>';

		}

?>

<h2>جميع الكومنتات التي جمعناها حتى الآن</h2>
<?php

$f = fopen("chall3-list.csv", "r");
while (($line = fgetcsv($f)) !== false) {
  foreach ($line as $cell) {
echo $cell . "<br>";
}


}
fclose($f);


?>
        
</body>

</html>