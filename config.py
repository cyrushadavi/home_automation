def get_dict_of_params():
    config = {}
    f = open('./config.cfg','r')
    for line in f.read().splitlines():
        split = line.split(':')
        config[split[0]] = split[1]
    return config