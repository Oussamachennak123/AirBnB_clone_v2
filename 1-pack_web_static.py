#!/usr/bin/python3
"""
Fabric script that generates a tgz archive from the contents of the web_static
folder of the AirBnB Clone repo
"""

from os.path import isdir
from datetime import datetime
from fabric.api import local


def do_pack():
    """generates a tgz archive"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")  # time
        if isdir("versions") is False:
            local("mkdir versions")
        file__name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file__name))
        return file__name
    except:
        return None
