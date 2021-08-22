<html lang="en">

<head>
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

		if (isset($_POST['name'])) {

			echo "<div style=\"text-align:center;font-size:7em;\">مرحبا , " . $_POST['name'] . "</div>";

		}
		else{

			echo '<form name="Form" action="chall2.php" onsubmit="return validateForm()" method="post">
			<div class="siimple-form">
			<div class="siimple-form-title">أرسل تعليقاً</div>
			<div class="siimple-form-detail">املأ النموذج للاتصال بنا</div>
			<div class="siimple-form-field">
				<div class="siimple-form-field-label">أدخل اسمك</div>
				<input type="text" class="siimple-input siimple-input--fluid" placeholder="اسمك" name="name" >
			</div>
			<div class="siimple-form-field">
				<input class="siimple-btn siimple-btn--blue" type="submit"  value="Send">
			</div>
			</div>
			</form>';

		}

?>
        </div>
      </div>
    </div>
	<script>
	function validateForm() {
    var x = document.forms["Form"]["name"].value;
    if (x == "") {
        alert("!! لا يوجد مدخل ");
        return false;
    }
}
	</script>

</body>

</html>