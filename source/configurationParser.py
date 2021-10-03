#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from configparser import ConfigParser


def get_configuration(path, section):
    dict_config = {}
    if os.path.isfile(path):
        config = ConfigParser()
        config.read(path)
        if config.has_section(section):
            for element in config.items(section):
                dict_config[element[0]] = element[1]
        else:
            print("No section: " + str(section))
            return False, dict_config

        if len(dict_config) != 0:
            return True, dict_config
        else:
            print("Empty section")
            return False, dict_config
    else:
        print("File or directory not exist, adapt configParser.PATH_TO_INIT_FILE")
        return False, dict_config


def main():
    pass


if __name__ == "__main__":
    main()


