<?php           
if(isset($_POST['x']) && isset($_POST['y']))
{
$string = $_POST['x'].','.$_POST['y'];
$fp = fopen('/buoy.txt', 'a');
fwrite($fp, $string);
fclose($fp);
}
?>