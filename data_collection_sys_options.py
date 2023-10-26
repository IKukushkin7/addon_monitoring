import json
import subprocess


def get_state(bash_answer_ha_supervisor):
    data_json = json.loads(bash_answer_ha_supervisor)
    if data_json.get('message') != "Entity not found.":
        last_seen = data_json.get('state')
        return last_seen
    else:
        return "not_found_entity"


def parse_sys_options(lst_entity_sys_options):
    request_dict = {}
    for entity_sys_option in lst_entity_sys_options:
        answer_ha_supervisor = subprocess.check_output(
            ['bash', '/home/zigbee_iot_collection.sh', f'{entity_sys_option}'],
            universal_newlines=True)
        state_sys_options = get_state(answer_ha_supervisor)
        request_dict.update({entity_sys_option: state_sys_options})
    return request_dict
