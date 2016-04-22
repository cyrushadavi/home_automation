import harmony
import config
import argparse



config_dict = config.get_dict_of_params()
args = argparse.Namespace()

def watch_tv():
    args.activity='watch tv'
    args.email=config_dict['harmony_email']
    args.harmony_ip=config_dict['harmony_ip']
    args.harmony_port=5222
    args.password=config_dict['harmony_password']
    harmony.start_activity(args)

def watch_fire_tv():
    args.activity='watch fire tv'
    args.email=config_dict['harmony_email']
    args.harmony_ip=config_dict['harmony_ip']
    args.harmony_port=5222
    args.password=config_dict['harmony_password']
    harmony.start_activity(args)

def turn_off():
    args.activity='-1'
    args.email=config_dict['harmony_email']
    args.harmony_ip=config_dict['harmony_ip']
    args.harmony_port=5222
    args.password=config_dict['harmony_password']
    harmony.start_activity(args)
