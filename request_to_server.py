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
        'hostname_hub': hostname_hub,
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

    return answer












