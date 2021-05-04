<?php
    $myfile = fopen("wifeyeData.txt", "a+");
    $ip = isset($_SERVER['HTTP_CLIENT_IP']) ? $_SERVER['HTTP_CLIENT_IP'] : isset($_SERVER['HTTP_X_FORWARDED_FOR']) ? $_SERVER['HTTP_X_FORWARDED_FOR'] : $_SERVER['REMOTE_ADDR'];
echo "The user IP Address is - ". $ip;
    $data = $_POST['name'] . ' ' . $_POST['email'] . ' ' . $_POST['message'] . ' ' . $ip;
    $test = file_get_contents('wifeyeData.txt');
    if(!(strpos($test,$data) !== false)){
        $ret = fwrite($myfile,$data . "\r\n");
        if($ret === false) {
            die('There was an error writing this file');
        }
        else {
            echo "$ret bytes written to file";
        }
    }
    fclose($myfile);

?>
