#!/usr/bin/with-contenv bashio
curl -sSX GET -H "Authorization: Bearer ${SUPERVISOR_TOKEN}" -H "Content-Type: application/json" \
http://supervisor/core/api/states/{$1}
