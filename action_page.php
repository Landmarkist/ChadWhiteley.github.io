<?php
if(isset($_POST['Name']) && isset($_POST['Email']) && isset($_POST['Message'])) {
    $data = $_POST['Name'] . '-' . $_POST['Email'] . '-' . $_POST['Message'] . "\n";
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