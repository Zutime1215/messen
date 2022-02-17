<?php
                
function get_data() {
    extract($_REQUEST);
    // $time = date("g:i A");
    $messege = stripslashes(htmlspecialchars($msg));

    $file_name='log'. '.json';
    
    if(file_exists("$file_name")) {
        $current_data=file_get_contents("$file_name");
        $array_data=json_decode($current_data, true);
                        
        $extra=array(
            'id' => $iD,
            'nam' => $name,
            'msg' => $messege,
        );
        $array_data[]=$extra;
        echo "file exist<br/>";
        return json_encode($array_data);
    }
    else {
        $datae=array();
        $datae[]=array(
            'id' => $iD,
            'nam' => $name,
            'msg' => $messege,
        );
        echo "file not exist<br/>";
        return json_encode($datae);
    }
   
}

$file_name='log'. '.json';
extract($_REQUEST);
if ( $msg != null ) {

    if(file_put_contents("$file_name", get_data())) {
        echo 'success';
    }               
    else {
        echo 'There is some error';             
    }

}
    
?>
