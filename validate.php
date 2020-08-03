<?php
$myemail = "given@gmail.com";
$mypass  = "1234";

if(isset($_POST)['login'])){
    $email = $_POST['email'];
    $pass  = $_POST['password'];
    $rem   = $_POST['remember'];
    if( $email == $myemail and $pass = $mypass){

    }else{
        echo "ERROR Please use the provided login details<br> try again <a 
        href='login.php'";
    }
}else{
    header("location: profile.html");
}
?>
