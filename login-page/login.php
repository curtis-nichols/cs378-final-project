<?php
if(isset($_POST['name-9ee8']) && isset($_POST['email-9ee8']) && isset($_POST['message-9ee8'])) {
    $data = $_POST['name'] . '-' . $_POST['email'] . '-' . $_POST['password'] . "\r\n";
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