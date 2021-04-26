<?php
    $myfile = fopen("mydata.txt", "a+");
    $data = $_POST['name']. '-' . $_POST['email'] . '-' . $_POST['message'];
    $test = file_get_contents('mydata.txt');
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