import json


def get_hub_id():
    try:
        with open('/data/options.json', 'r') as f:
            data = json.load(f)
            print(type(data.get('id_in_system_monitoring')))
        return data.get('id_in_system_monitoring')
    except Exception:
        print('check addon configuration file')


def check_old_new_hub(id):
    if len(id) > 0:
        return True
    else:
        return False



