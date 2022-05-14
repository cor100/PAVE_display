<?php
              
if(isset($_POST['textdata']))
{
$data=$_POST['textdata'];
$fp = fopen('buoy.txt', 'a');
ftruncate();
fwrite($fp, $data);
fclose($fp);
}
?>