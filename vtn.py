#!/usr/bin/env python3

from utils import bash, logi
from config import GCP_KEY_JSON, GEMEL_PATH
from filepath.filepath import fp

from gemel.vnet import vtn as vnmanager

import json


# def _login():
#     logi("Authenticating to Google Cloud")
#     login = fp(GEMEL_PATH) + fp("provision/gcp-login.sh")
#     bash("%s --credentials %s" % (login, GCP_KEY_JSON))
#
#
# _login()


def move_host_to_vn(mac, vtn):
    vnmanager.reassign_vtn(mac, vtn, safe=True)
    return {"status": "OK"}


def get_vn(host_mac):
    res = vnmanager.get_current_interface(host_mac)
    return {"net": res[0] if res else "None"}


def toggle_vn(host_mac):
    vnmanager.toggle_vtn(host_mac)
    return {"status": "OK"}


