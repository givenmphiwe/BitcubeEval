<?php
$myemail = "given@gmail.com";
$mypass  = "1234";

if(isset($_POST)['login'])){
    $email = $_POST['email'];
    $pass  = $_POST['password'];
    $rem   = $_POST['remember'];
    if( $email == $myemail and $pass = $mypass){
        if( isset($_POST['remember']) ){
            setcookies('email', $email, time()+60*60*7);
            setcookies('email', $email, time()+60*60*7);
        }
        session_start();
        $_SESSION['email'] = $email;
        header("location: profile.html");
        
    }else{
        echo "ERROR Please use the provided login details<br> try again <a 
        href='login.php'";
    }
}else{
    header("location: profile.html");
}
?>
