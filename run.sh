#!/usr/bin/with-contenv bashio

echo "Hello world!"

#curl -X GET -H "Authorization: Bearer ${SUPERVISOR_TOKEN}" -H "Content-Type: application/json" \
#http://supervisor/core/api/states/sensor.cpu_temperature

#curl -L -H "Authorization: Bearer $SUPERVISOR_TOKEN" http://supervisor/network/info

python3 /home/main.py
#python3 /home/test.py
#python3 -m http.server 8000
