#!/usr/bin/env python3

from utils import bash, logi
from config import GCP_KEY_JSON, GEMEL_PATH
from filepath.filepath import fp

import json


def _login():
    logi("Authenticating to Google Cloud")
    login = fp(GEMEL_PATH) + fp("provision/gcp-login.sh")
    bash("%s %s" % (login, GCP_KEY_JSON))


_login()


def move_host_to_vn(mac, vtn):

    logi("Moving host to VN")
    reassign = fp(GEMEL_PATH) + fp("vnet/reassign-vn.sh")
    bash("%s %s %s" % (reassign, mac, vtn))

    return {"status": "OK"}


def get_vn(name):

    logi("Moving host to VN")
    get_vn = fp(GEMEL_PATH) + fp("vnet/get-vn.sh")
    vn = bash("%s %s" % (get_vn, name))

    return {"net": vn}


