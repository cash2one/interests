# -*- encoding: utf-8 -*-
__author__ = 'yangxiantiao'

import yaml
import os
import six
from .singleton import Singleton
from .exception import ConfigNotFoundExcept


def is_readable(path):
    '''
    Check if a given path is readable by the current user.

    :param path: The path to check
    :returns: True or False
    '''

    if os.access(path, os.F_OK) and os.access(path, os.R_OK):
        # The path exists and is readable
        return True

    # The path does not exist
    return False


def _read_conf_file(path):
    '''
    Read in a config file from a given path and process it into a dictionary
    @params path string:
    '''
    with open(path, 'r', encoding='utf8') as conf_file:
        try:
            conf_opts = yaml.safe_load(conf_file.read()) or {}
        except yaml.YAMLError as err:
            print(
                'Error parsing configuration file: {0} - {1}'.format(path, err)
            )
            conf_opts = {}
        # only interpret documents as a valid conf, not things like strings,
        # which might have been caused by invalid yaml syntax
        if not isinstance(conf_opts, dict):
            print(
                'Error parsing configuration file: {0} - conf should be a '
                'document, not {1}.'.format(path, type(conf_opts))
            )
            conf_opts = {}
        # allow using numeric ids: convert int to string
        for key, value in six.iteritems(conf_opts.copy()):
            if six.PY2:
                # We do not want unicode settings
                conf_opts[key] = value.encode('utf-8')
        return conf_opts


def load_config(path, is_find_template=False):
    '''
    Returns configuration dict from parsing either the file described by
    ``path`` or the environment variable described by ``env_var`` as YAML.
    '''
    if path is None:
        # When the passed path is None, we just want the configuration
        # defaults, not actually loading the whole configuration.
        return {}

    # If the configuration file is missing, attempt to copy the template,
    # after removing the first header line.
    if not os.path.isfile(path) and is_find_template:
        template = '{0}.template'.format(path)
        if os.path.isfile(template):
            print('Writing {0} based on {1}'.format(path, template))
            with open(path, 'w') as out:
                with open(template, 'r') as ifile:
                    ifile.readline()  # skip first line
                    out.write(ifile.read())

    if is_readable(path):
        opts = _read_conf_file(path)
        return opts

    print('Missing configuration file: {0}'.format(path))
    return {}


def load_conf(conf_dir, is_find_template=True):
    '''
    根据目录读取文件夹里面所有以.yaml结尾的文件，以文件名（去掉文件后缀.yaml）作为key
    @conf_dir string: 配置文件路径，项目规定使用etc
    @is_find_template bool: 当文件夹内存在以.template结尾的文件，先拷贝一份配置在读取
    '''
    configs = dict()
    if os.path.exists(conf_dir):
        conf_files = os.listdir(conf_dir)
        for path in conf_files:
            if os.path.isfile(os.path.join(conf_dir, path)):
                # 自动通过template文件生成配置
                if path.endswith('.template'):
                    conf_file_name = path.replace('.template', '')
                    conf_file_path = os.path.join(conf_dir, conf_file_name)
                    if not os.path.exists(conf_file_path) and conf_file_path.endswith('.yaml'):
                        sub_file_name = conf_file_name.rstrip('.yaml')
                        configs[sub_file_name] = load_config(conf_file_path,
                                                             is_find_template=is_find_template)

                # 只处理以yaml结尾的配置
                elif path.endswith('.yaml'):
                    sub_file_name = path.rstrip('.yaml')
                    conf_file_path = os.path.join(conf_dir, path)
                    configs[sub_file_name] = load_config(conf_file_path)

    return configs


class Config(Singleton):
    '''
    根据执行路径加载系统的配置，只加载.yaml结尾或者以.yaml.template结尾的文件
    '''

    config = dict()

    @classmethod
    def get(cls, *args, **kwargs):
        '''
        获取系统配置
        @param args list: 配置字典的层次key
        @param kwargs dict: 如果kwargs中存在default，
                       获取不到配置的时返回的default指定的默认值，
                       不存在default时则返回None
        return:
        '''
        if not cls.config:
            project_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
            config_dir = os.path.join(project_dir, 'etc')
            cls.config = load_conf(config_dir, is_find_template=True)

        result = cls.config
        for key in args:
            if key in result.keys():
                result = result.get(key)
            else:
                if 'default' in kwargs.keys() and kwargs['default']:
                    result = kwargs.get('default')
                    return result
                else:
                    raise ConfigNotFoundExcept('config not found in {}.yaml'.format(args[0]))

        return result



