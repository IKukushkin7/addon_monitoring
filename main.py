import json
import subprocess
import time
from data_collection_zigbee_iot import parse_value_last_seen
from data_collection_wifi_iot import parse_wifi_devices
from data_collection_sys_options import parse_sys_options
from reg_in_system import *
from request_to_server import *


# text = subprocess.check_output(['./req.sh', 'sensor.cpu_temperature'], universal_newlines=True)
# print(type(text))
#
# text_json = json.loads(text)
# print(type(text_json))
# req = text_json['state']
# print(req)


# get lists zigbee devices
def get_zigbee_devices():
    try:
        with open('/data/options.json', 'r') as f:
            data = json.load(f)
        return data.get('zigbee_devices')
    except Exception:
        print('check addon configuration file')
        return "NONE"


def get_token_ha():
    try:
        with open('/data/options.json', 'r') as f:
            data = json.load(f)
        return data.get('token_ha')
    except Exception:
        print('check addon configuration file')
        return "NONE"


def get_wifi_devices():
    try:
        with open('/data/options.json', 'r') as f:
            data = json.load(f)
        return data.get('wifi_device_entity')
    except Exception:
        print('check addon configuration file')
        return "NONE"


def get_sys_options():
    try:
        with open('/data/options.json', 'r') as f:
            data = json.load(f)
        return data.get('system_monitor_entity')
    except Exception:
        print('check addon configuration file')
        return "NONE"


def get_hostname_server():
    try:
        with open('/data/options.json', 'r') as f:
            data = json.load(f)
        return data.get('host_server')
    except Exception:
        print('check addon configuration file host_server')
        return "NONE"


def get_hostname_hub():
    try:
        with open('/data/options.json', 'r') as f:
            data = json.load(f)
        return data.get('hostname_hub')
    except Exception:
        print('check addon configuration file hostname_hub')
        return "NONE"


def get_system_monitor_entity():
    try:
        with open('/data/options.json', 'r') as f:
            data = json.load(f)
        return data.get('system_monitor_entity')
    except Exception:
        print('check addon configuration file')
        return "NONE"


def get_name_hub():
    try:
        with open('/data/options.json', 'r') as f:
            data = json.load(f)
        return data.get('name_hub')
    except Exception:
        print('check addon configuration file')
        return "NONE"


if __name__ == '__main__':
    host_server = get_hostname_server()
    host_hub = get_hostname_hub()
    zigbee_devices = get_zigbee_devices()
    wifi_devices = get_wifi_devices()
    sys_options = get_sys_options()
    name_hub = get_name_hub()  # get_name_hub
    code_hub = get_hub_id()
    token_ha = get_token_ha()
    subprocess.call(['bash', '/home/print_in_log_addon.sh', f'{zigbee_devices}'])
    if host_server == "NONE" or host_hub == "NONE" or zigbee_devices == "NONE" or wifi_devices == "NONE" or sys_options == "NONE" or name_hub == "NONE" or code_hub == "NONE" or token_ha == "NONE":
        subprocess.call(['bash', '/home/print_in_log_addon.sh', 'Check addon configuration file!!!'])
    else:
        if check_old_new_hub(code_hub):
            cheker = check_already_init_hub(code_hub, name_hub, host_server)
            if cheker is True:
                while True:
                    print('ok its work')
                    # data about zigbee devices
                    dict_lastseen_zigbee_iot = parse_value_last_seen(zigbee_devices)
                    # data system monitor hub
                    dict_states_sys_options = parse_sys_options(sys_options)
                    # data wifi devices
                    dict_states_wifi_devices = parse_wifi_devices(wifi_devices)

                    ######
                    subprocess.call(['bash', '/home/print_in_log_addon.sh', f'{dict_lastseen_zigbee_iot}'])
                    subprocess.call(['bash', '/home/print_in_log_addon.sh', f'{dict_states_wifi_devices}'])
                    subprocess.call(['bash', '/home/print_in_log_addon.sh', f'{dict_states_sys_options}'])
                    #####
                    # request_to_server = f'{{"name_hub": "{name_hub}","zigbee_device": f"{dict_lastseen_zigbee_iot}","wifi_device": f"{dict_states_wifi_devices}","system_options": f"{dict_states_sys_options}"}}'
                    request_to_server = {"name_hub": f"{name_hub}", "zigbee_device": f'{dict_lastseen_zigbee_iot}',
                                         "wifi_device": f'{dict_states_wifi_devices}',
                                         "system_options": f'{dict_states_sys_options}'}
                    send_main_data(host_server, request_to_server)
                    time.sleep(300)
            elif cheker is None:
                pass
            else:
                init_in_system(name_hub, host_hub, code_hub, host_server, token_ha)
        else:
            subprocess.call(['bash', '/home/print_in_log_addon.sh', f'{set_id_hub(host_server, name_hub)}'])

#######################################################################################################################
# host_server = get_hostname_server()
# zigbee_devices = get_zigbee_devices()
# wifi_devices = get_wifi_devices()
# sys_options = get_sys_options()
# name_hub = ""  # get_name_hub
# while True:
#     print('ok its work')
#     # data about zigbee devices
#     dict_lastseen_zigbee_iot = parse_value_last_seen(zigbee_devices)
#     # data system monitor hub
#     dict_states_sys_options = parse_sys_options(sys_options)
#     # data wifi devices
#     dict_states_wifi_devices = parse_wifi_devices(wifi_devices)
#
#     ######
#     subprocess.call(['bash', '/home/print_in_log_addon.sh', f'{dict_lastseen_zigbee_iot}'])
#     subprocess.call(['bash', '/home/print_in_log_addon.sh', f'{dict_states_wifi_devices}'])
#     subprocess.call(['bash', '/home/print_in_log_addon.sh', f'{dict_states_sys_options}'])
#     #####
#     request_to_server = f'{{"name_hub": name_hub,"zigbee_device": f"{dict_lastseen_zigbee_iot}","wifi_device": f"{dict_states_wifi_devices}","system_options": f"{dict_states_sys_options}"}}'
#     send_main_data(host_server, request_to_server)
#     time.sleep(300)
