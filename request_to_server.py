import requests
import subprocess

def check_already_init_hub(id, name_hub, host_server):
    data = {
        'id': id,
        'name_hub': name_hub
    }
    req = requests.post(f'{host_server}/check', data=data)
    answer = req.text
    if answer == "ok registr":
        return True
    else:
        return False


def init_in_system(name_hub, hostname_hub, code_hub, host_server, token_ha):
    data = {
        'name_hub': name_hub,
        # 'code': str_encoded,
        'hostname_hub': hostname_hub,
        # 'id': "ZV3XTUT2Jfw=*bbRuSEM9AfEdxqRm9gTSVg==*   # 'code': str_encoded,
        # 'hostname': "192.168.0.173",
        # # 'id': "ZV3XTUT2Jfw=*bbRuSEM9AfEdxqRm9gTSVg==*oMg+IzGlF0Bkx6Wgfxkmjw==*IFuvy1QOx8apHkSuYL0eFg=="
        # 'id': ""oMg+IzGlF0Bkx6Wgfxkmjw==*IFuvy1QOx8apHkSuYL0eFg=="
        'code_hub': code_hub,
        'token_ha': token_ha
    }
    req = requests.post(f'{host_server}/init', data=data)
    answer = req.text
    print(answer)

def check_already_init_hub(id, name_hub, host_server):
    data = {
        'id': id,
        'name_hub': name_hub
    }
    try:
        req = requests.post(f'{host_server}/check', data=data)
        answer = req.text
        if answer == "ok registr":
            return True
        else:
            return False
    except Exception:
        subprocess.call(['bash', '/home/print_in_log_addon.sh', 'Host server offline'])
        return None
# init_in_system("test_hub892", "https://myhome.ru", "1IX1MV5ADMniuH8=*o/i31wYmo544w5+U9n5B5g==*6W+8euOYBNKU5ZFWTKZLjg==*WRugi6on+LsGuJaRP6iwyg==", "http://127.0.0.1:5000", "cdscnsdnl")



def send_main_data(host_server, data):
    try:
        req = requests.post(f'{host_server}/main', data=data)
        answer = req.text
        print(answer)
    except Exception:
        subprocess.call(['bash', '/home/print_in_log_addon.sh', 'Host server offline, send data failed!'])



def set_id_hub(hostname_server, name_hub):
    data = {
        'name_hub': name_hub,
    }
    req = requests.get(f'{hostname_server}/get_id', data=data)
    answer = req.text
    # print(answer)
    return answer

# test_hub892
# request_to_server = {
#     "name_hub": "12345",
#     "zigbee_device": '{"1": "2"}',
#     "wifi_device": '{"2": "3"}',
#     'system_options': '{"sensor.cpu_temperature": "42.9", "sensor.memory_use_percent": "65.0"}'
# }
#
# # request_to_server = ''' '{"name_hub": "","zigbee_device": "{'switch.rev_skylight': 'off', 'sensor.processor_use': '20'}","wifi_device": "{'switch.skylight': 'off', 'sensor.humidity': 'unavailable'}","system_options": "{'sensor.cpu_temperature': '46.7', 'sensor.memory_use_percent': '58.5'}"}' '''
# send_main_data("http://127.0.0.1:5000", request_to_server)
# send_main_data("http://185.185.71.33:5606", request_to_server)
