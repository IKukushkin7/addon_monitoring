import json
import subprocess
import time



def get_last_seen(bash_answer_ha_supervisor):
    data_json = json.loads(bash_answer_ha_supervisor)
    if data_json.get('message') != "Entity not found.":
        last_seen = data_json.get('attributes').get('last_seen')
        battery = data_json.get('attributes').get('battery')
        print(battery)
        lst_dev = [f'{last_seen}', f'{battery}']
        return lst_dev
    else:
        return "not_found_entity"


def parse_value_last_seen(lst_entity_devices):
    request_dict = {}
    for entity_device in lst_entity_devices:
        answer_ha_supervisor = subprocess.check_output(['bash', '/home/zigbee_iot_collection.sh', f'{entity_device}'],
                                                       universal_newlines=True)
        if answer_ha_supervisor == "502: Bad Gateway":
            time.sleep(120)
            answer_ha_supervisor = subprocess.check_output(
                ['bash', '/home/zigbee_iot_collection.sh', f'{entity_device}'],
                universal_newlines=True)
            subprocess.call(['bash', '/home/print_in_log_addon.sh', 'if 1'])
            last_seen = get_last_seen(answer_ha_supervisor)
            request_dict.update({f"{entity_device}": f"{last_seen}"})
        else:
            subprocess.call(['bash', '/home/print_in_log_addon.sh', 'if 2'])
            last_seen = get_last_seen(answer_ha_supervisor)
            request_dict.update({f"{entity_device}": f"{last_seen}"})

            request_dict.update({f"{entity_device}": last_seen})

    print(request_dict)
    return request_dict
