#!/usr/bin/python3
""" Function that deploys """
from fabric.api import *


env.hosts = ['35.231.33.237', '34.74.155.163']
env.user = "ubuntu"


def do_clean(number=0):
    """ CLEANS """
    path = '/data/web_static/releases'
    if number = 0
        local('cd versions ; ls -t | head -n -1 | xargs rm -rf')
        run('cd {} ; ls -t | head -n -1 | xargs rm -rf'.format(path))
    local('cd versions ; ls -t | head -n -{} | xargs rm -rf'.format(number))
    run('cd {} ; ls -t | head -n -{} | xargs rm -rf'.format(path, number))
