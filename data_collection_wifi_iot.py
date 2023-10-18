import json
import subprocess


# text = subprocess.check_output(['./req.sh', 'sensor.cpu_temperature'], universal_newlines=True)
# print(type(text))
#
# text_json = json.loads(text)
# print(type(text_json))
# req = text_json['state']
# print(req)


def get_state(bash_answer_ha_supervisor):
    data_json = json.loads(bash_answer_ha_supervisor)
    # last_seen = data_json.get('attributes').get('last_seen')
    last_seen = data_json.get('state')
    return last_seen


def parse_wifi_devices(lst_entity_wifi_devices):
    request_dict = {}
    for entity_wifi_device in lst_entity_wifi_devices:
        answer_ha_supervisor = subprocess.check_output(['bash', 'zigbee_iot_collection.sh', f'{entity_wifi_device}'],
                                                       universal_newlines=True)
        state_wifi_device = get_state(answer_ha_supervisor)
        request_dict.update({entity_wifi_device: state_wifi_device})
    return request_dict
