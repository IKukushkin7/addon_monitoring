ARG BUILD_FROM
FROM $BUILD_FROM

# Install requirements for add-on
RUN \
  apk add --no-cache \
    python3 py3-pip


# Python 3 HTTP Server serves the current working dir
# So let's set it to our add-on persistent data directory.
WORKDIR /data

# Copy data for add-on
COPY main.py /home/
COPY zigbee_iot_collection.sh /home/
COPY data_collection_zigbee_iot.py /home/
COPY print_in_log_addon.sh /home/
COPY reg_in_system.py /home/
COPY request_to_server.py /home/
COPY run.sh /
COPY data_collection_wifi_iot.py /home/
COPY data_collection_sys_options.py /home/

RUN chmod a+x /run.sh
RUN chmod a+x /home/zigbee_iot_collection.sh
RUN chmod a+x /home/print_in_log_addon.sh
RUN python3 -m pip install requests

CMD [ "/run.sh" ]
