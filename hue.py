from beautifulhue.api import Bridge
import time
from random import choice
import config

config_dict = config.get_dict_of_params()

bridge = Bridge(device={'ip': config_dict['hue_ip']}, user={'name': config_dict['hue_user']})
# bridge = pyhue.Bridge('192.168.1.211', '3330f3b32f409f0f303cbeab3da6e87')



# resource = {'which':'all', 'verbose':True}
# print bridge.light.get(resource)
def blue_party():
    while True:
        #val = choice([(0,0),(.25,0),(.1,.1),(.5,.3),(.7,.7),(.25,0),(.167,.04)])
        brightness =  choice([150,255])
        resource = {
            'which': 4,
            'data': {
                'state': {
                    'on': True,
                    'xy': choice([(0,0),(.25,0),(.1,.1),(.5,.3),(.7,.7),(.25,0),(.167,.04)]),#val,
                    # 'sat':
                    'bri': brightness
                }
            }
        }
        bridge.light.update(resource)
        time.sleep(.2)
        resource = {
            'which': 2,
            'data': {
                'state': {
                    'on': True,
                    'xy': choice([(0,0),(.25,0),(.1,.1),(.5,.3),(.7,.7),(.25,0),(.167,.04)]),#val,
                    # 'sat':
                    'bri': brightness
                }
            }
        }
        bridge.light.update(resource)
        time.sleep(.2)
        resource = {
            'which': 1,
            'data': {
                'state': {
                    'on': True,
                    'xy': choice([(0,0),(.25,0),(.1,.1),(.5,.3),(.7,.7),(.25,0),(.167,.04)]),#val,
                    # 'sat':
                    'bri': brightness
                }
            }
        }
        bridge.light.update(resource)
        time.sleep(1)


def toggle_living_room(state=True):
    resource = {
        'which': 0,
        'data': {
            'action': {
                'on': state
            }
        }
    }
    bridge.group.update(resource)
