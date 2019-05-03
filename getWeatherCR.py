#!/usr/bin/python
import requests
import json
import subprocess
import sys
import time
 
subprocess.call(['rm', '/var/www/html/log.html'])
subprocess.call(['touch','/var/www/html/log.html'])
subprocess.call(['chmod','777', '/var/www/html/log.html'])


html_start_payload = '''
<html>
<head>
<style>

body{
background-color:blue;

}
</style>
</head>
<body>
'''

html_end_payload = '</body></html>'



ids=['2950159','2835481','2939797','2825297','2911298','2907911','2886242']

start = 'http://localhost/test.php?c=' + html_start_payload +'<br>'
requests.get(start)  




  


for x in ids:
  api='https://api.openweathermap.org/data/2.5/weather?id='+ x + '&appid=2182e55fa2ce21a9bfe7d4629391fc8e'
  json_data = requests.get(api).json()
  
  #print(json.dumps(json_data, indent=4, sort_keys=True))
  json_name =  json_data['name']
  json_luftfeuchtigkeit =  json_data['main']['humidity']                  
  json_luftdruck =  json_data['main']['pressure']
  json_temperatur =  json_data['main']['temp']
  json_mindestwaerme =  json_data['main']['temp_min']
  json_maxwaerme =  json_data['main']['temp_max']
  json_descr =  json_data['weather'][0]['description']

  temp=json_temperatur - 273.15
  min=json_mindestwaerme -273.15
  max=json_maxwaerme -273.15
  payload = json_name +"\n"
  html_payload = '<div class="'+ x + '">'  + '<p>'+ json_name +"\n" +'<br>'

  payload += "Luftfeuchtigkeit: "+str(json_luftfeuchtigkeit)+"%\n" 
  html_payload += "Luftfeuchtigkeit: "+str(json_luftfeuchtigkeit)+"%\n" +'<br>'

  payload+= "Luftdruck: "+str(json_luftdruck)+" hpa\n" 
  html_payload += "Luftdruck: "+str(json_luftdruck)+" hpa\n" +'<br>' 

  payload += "Aktuelle Temperatur: "+str(min)+" C\n" 
  html_payload +=  "Aktuelle Temperatur: "+str(min)+" C\n"  +'<br>'

  payload += "Min: "+str(min)+" C\n"  
  html_payload +=  "Min: "+str(min)+" C\n"+'<br>'

  payload +=  "Max: "+str(max)+" C\n" 
  html_payload += "Max: "+str(max)+" C\n"  +'<br>'

  payload += "Status: "+str(json_descr) +"\n"
  html_payload += "Status: "+str(json_descr) +"\n"  + '</p></div>'

  link = "https://openweathermap.org/city/" + x
  test = 'http://localhost/test.php?c=' + html_payload +'<br>'
  requests.get(test)
  MESSAGE= "Das Wetter in:  " + payload + "\n" +link
  subprocess.call([
     'curl', '-s', '-X', 'POST' ,'https://api.telegram.org/bot801094352:AAF_fEESoQC_aNHEKLpAhOhPcmYhTZ7cX8k/sendMessage', '-d' ,'chat_id=' , '-d', 'text=' + MESSAGE 
  ])




end = 'http://localhost/test.php?c=' + html_end_payload
requests.get(end)
print("\n")
sys.exit(1)
