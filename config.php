<?php
if(!empty($_POST)){
	$configData = $_POST["data"];
	$file = fopen("configData.json", "w");
	fwrite($file, $configData);
	fclose($file);
	//echo exec("sudo ./sendConfig.py");
	echo shell_exec("/usr/bin/python3 /var/www/html/IoT/sendConfig.py");
	
}else{
	echo exec('python ./sendConfig.py');
	
	//exec("sudo ./ledzisko.py");
	//echo exec("ledzisko.py");
}


?>
