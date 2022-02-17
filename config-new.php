<?php 

	if(extract($_REQUEST)){
		$messege = stripslashes(htmlspecialchars($msg));
    	$file_name='log'. '.json';

		$new_message = array(
			'id' => $iD,
            'nam' => $name,
            'msg' => $messege,
		);
		
		// Before storing the $new_message[] array, we have to check if this is 
		// the first record.
		// We are doing this by checking the filesize.
		if(filesize("log.json") == 0){
			// if this is the first record, we creating an array to hold out message.
			$first_record = array($new_message);
			// The only purpose of this step is to create an array inside the json 
			// file to hold our messages. You will see in sec.
			
			/* I'll assign the record to a generic variable for later use. */
			$data_to_save = $first_record; 
		}else{
			// If this is not the first record, and there are messages stored in the file.
			// We have to pull all those old messages so we can add the new one.
			// And also we have to decode the data we fetch.
			$old_records = json_decode(file_get_contents("log.json"));

			// We know that all of our messages are stored inside an array,
			// because we created that array with the first record.
			// Now we can add to that array our new message.
			array_push($old_records, $new_message);

			/* and i'll assign the record to our generic variable. */
			$data_to_save = $old_records;
		}

		// Now our last step is to store the data to the file (messages.json).
		if(!file_put_contents("log.json", json_encode($data_to_save, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE), LOCK_EX)){
			// if something went wrong, we are showing an error message.
			$error = "Error";
		}else{
			// and if everything went ok, we show a success message.
			$success =  "successful";
		}
	}



if(array_key_exists('del', $_POST)){finish();} 

function finish() {

    $file = 'log.json';
    $newfile = 'backup/log.json';
    if(!copy($file,$newfile)){
        echo " ";
    }
    else{
        echo " ";
    }

    $file=fopen("log.json","w");
    fwrite($file, "");
    fclose($file); 
    }    

?>

<html><body><form method="post"><input type="submit"name="del"value="del" style="background-color:transparent;border-color:transparent;color:transparent;"></form></body></html>