#!/usr/local/python34/bin/python3.4
import os
import sys

if __name__ == "__main__":

    from utils.config import Config

    settings_module = Config.get('config', 'main', 'settings_module', default='settings.production')

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
