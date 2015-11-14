import os
import yaml
import logging.config


def read_from_file():
    if os.getenv('DEVELOP', None):
        config_file = "development.yaml"
    elif os.getenv('SLAVE', None):
        config_file = "slave.yaml"
    else:
        config_file = "production.yaml"

    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),os.path.join('log_confs', config_file)), 'rt') as f:
        config = yaml.load(f.read())
        logging.config.dictConfig(config)
