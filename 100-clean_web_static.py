#!/usr/bin/python3
""" Function that deploys """
from fabric.api import *


env.hosts = ['35.231.33.237', '34.74.155.163']
env.user = "ubuntu"


def do_clean(number=0):
    """ CLEANS """
    local('cd versions ; ls -t | head -n -{} | xargs rm -rf'.format(number))
    path = '/data/web_static/releases'
    run('cd {} ; ls -t | head -n -{} | xargs rm -rf'.format(path, number))
