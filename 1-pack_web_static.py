#!/usr/bin/python3
"""script that generates a .tgz archive"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """function do_pack"""
    local('mkdir -p versions')
    time = datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")
    file = "versions/web_static_{}.tgz".format(time)
    try:
        local('tar -czvf {} web_static'.format(file))
        return file
    except Exception:
        return None
