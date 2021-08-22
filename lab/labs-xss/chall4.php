<?php
session_start();

$userinfo = array(
                'naplon'=>'naplon',
                'admin'=>'admin'
                );



if(isset($_POST['username'])) {
  if(isset($userinfo[$_POST['username']])){if($userinfo[$_POST['username']] == $_POST['password']) {
      $_SESSION['username'] = $_POST['username'];
  }else {
    header('Location: chall4.php?message=wrong user name or password');

  }

}else{header('Location: chall4.php?message=wrong user name or password');}




}
?>
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>Xss Login Page</title>
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
     سجل دخولك 
  </p>
  <p>
  Happy hacking ^_^
  </p>
</div>
          <?php
          if(isset($_GET['message'])) {
           $status =  '<div class="siimple-alert siimple-alert--error">' . $_GET['message'] . '</div>';
       	echo $status;
       }

           ?>
		<?php


    if(isset($_SESSION['username'])){
      echo '<span style="text-align:center;font-size:2em;;">You are logged in as ' . $_SESSION['username'] . '</span>';
      echo '<br><br><a class="siimple-btn siimple-btn--blue" href="javascript:delete_cookie(\'PHPSESSID\');" >Logout</a>';
    }
		else{

			echo '<form name="myForm" action="chall4.php"  method="post">
			<div class="siimple-form">
			<div class="siimple-form-title">Login Page</div>
			<div class="siimple-form-detail">Login with username and password</div>
			<div class="siimple-form-field">
				<div class="siimple-form-field-label">Username</div>
				<input type="text" class="siimple-input siimple-input--fluid" placeholder="username" name="username">
			</div>
			<div class="siimple-form-field">
				<div class="siimple-form-field-label">Password</div>
				<input type="password" class="siimple-input siimple-input--fluid" placeholder="password" name="password">
			</div>
			<div class="siimple-form-field">
				<input class="siimple-btn siimple-btn--blue" type="submit"  value="Login">
			</div>
			</div>
			</form>';

		}

?>
  </body>
</html>