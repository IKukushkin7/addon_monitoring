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


def parse_yandex_station(lst_entity_yandex_station):
    request_dict = {}
    for entity_yandex_station in lst_entity_yandex_station:
        answer_ha_supervisor = subprocess.check_output(['bash', '/home/zigbee_iot_collection.sh', f'{entity_yandex_station}'],
                                                       universal_newlines=True)
        state_yandex_station = get_state(answer_ha_supervisor)
        request_dict.update({entity_yandex_station: state_yandex_station})
    return request_dict

