import os

import yaml


class AppConf:
    __instance = None
    __conf = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            env = os.getenv('ENV')
            dirname = os.path.dirname(os.path.abspath(__file__))
            filename = dirname + '/config/{}.yaml'
            with open(filename.format(env), 'r') as f:
                conf = yaml.safe_load(f)
                cls.__conf = conf
        return cls.__instance

    def get_conf(self):
        return self.__conf
