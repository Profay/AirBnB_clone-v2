#!/usr/bin/python3
'''distributes an archive to your web servers'''

from os.path import exists
from datetime import datetime
from fabric.api import put, run, env, local
env.hosts = ['50.19.193.215', '54.227.31.122']


def do_pack():
    '''function do_pack'''
    local('mkdir -p versions')
    time = datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")
    file = "versions/web_static_{}.tgz".format(time)
    try:
        local('tar -czvf {} web_static'.format(file))
        return file
    except Exception:
        return None


def do_deploy(archive_path):
    '''function do_deploy'''
    if not exists(archive_path):
        return False
    try:
        path = '/data/web_static/releases/'
        file_name = archive_path.split('/')[1]
        no_extention = file_name.split('.')[0]
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_extention))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_name, path, no_extention))
        run('rm /tmp/{}'.format(file_name))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_extention))
        run('rm -rf {}{}/web_static'.format(path, no_extention))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_extention))
        print('New version deployed!')
        return True
    except Exception:
        return False

def deploy():
    '''function deploy'''
    archive = do_pack()
    if archive is None:
        return False
    return do_deploy(archive)
