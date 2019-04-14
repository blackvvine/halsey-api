#!/usr/bin/env python3

from utils import bash, logi
from config import GCP_KEY_JSON, GEMEL_PATH
from filepath.filepath import fp

import json


def move_host_to_vn(mac, vtn):

    logi("Authenticating to Google Cloud")
    login = fp(GEMEL_PATH) + fp("provision/gcp-login.sh")
    bash("%s %s" % (login, GCP_KEY_JSON))

    logi("Moving host to VN")
    reassign = fp(GEMEL_PATH) + fp("vnet/reassign-vn.sh")
    bash("%s %s %s" % (reassign, mac, vtn))

    return json.dumps({"status": "OK"})

