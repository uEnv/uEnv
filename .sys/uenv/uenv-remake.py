#!/usr/bin/env python3

import os.path
import json

__author__ = 'Alexander Popov'
__version__ = '0.1.0'
__license__ = 'MIT'

if __name__ == '__main__':
    # Проверяю наличие файла packages.installed.json
    if not os.path.isfile('X:\\.sys\\cubo\\packages.installed.json'):
        print('packages.installed.json file not found.\nReinstall uEnv.')
        quit(-1)
    else:
        # загруэаю список пакетов
        PACKAGES = dict()

        with open('X:\\.sys\\cubo\\packages.installed.json', 'r',
                  encoding='utf-8') as f:
            PACKAGES = json.loads(f.read())

    print('Installed {0} packages.'.format(len(PACKAGES)))
    print('Remake uEnv.bat file.')

    UENV_BAT = '@echo off\n'

    # сбор всех путей пакетов
    PACKAGES_PATH = list()

    for package in PACKAGES:
        for path in PACKAGES[package]['path']:
            PACKAGES_PATH.append(path)

    for item in PACKAGES_PATH:
        UENV_BAT += '{0}\n'.format(item)

    UENV_BAT += 'start "uEnv BETA_20170403-1" \
cmd.exe /s /k .\.sys\clink-0.4.8\clink_x86.exe inject'

    with open('x:\\uEnv.bat', 'w+', encoding='utf-8') as f:
        f.write(UENV_BAT)
