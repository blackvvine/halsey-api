#!/usr/bin/env python3

from utils import bash, logi
from config import GCP_KEY_JSON, GEMEL_PATH
from filepath.filepath import fp

import json


# def _login():
#     logi("Authenticating to Google Cloud")
#     login = fp(GEMEL_PATH) + fp("provision/gcp-login.sh")
#     bash("%s --credentials %s" % (login, GCP_KEY_JSON))
#
#
# _login()


def move_host_to_vn(mac, vtn):

    logi("Moving host to VN")
    reassign = fp(GEMEL_PATH) + fp("vnet/reassign-vn.sh")
    bash("%s -i %s -n %s" % (reassign, mac, vtn))

    return {"status": "OK"}


def get_vn(name):

    logi("Getting host %s's VN" % name)
    get_vn = fp(GEMEL_PATH) + fp("vnet/get-vn.sh")
    out = bash("bash  %s %s" % (get_vn, name))

    vn_name = out.split(b"\n")[-2].decode("ascii")

    return {"net": vn_name}


def toggle_vn(name, vn):

    logi("Getting host %s's VN" % name)
    get_vn = fp(GEMEL_PATH) + fp("vnet/toggle-vn-nat.sh")
    bash("bash  %s %s %s" % (get_vn, name, vn))

    return {"status": "OK"}


