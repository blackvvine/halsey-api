#!/usr/bin/env python

import re
import yaml

from os.path import dirname, join
from logging import DEBUG


def _read_yml_conf():
    with open(join(dirname(__file__), "halsey.yml")) as f:
        return yaml.load(f.read(), Loader=yaml.FullLoader)


def _get_vn(seclevel):
    return [vn for vn in _read_yml_conf()["vnets"] if vn["security_level"] == seclevel][0]


NUM_VNETS = 2

_ids_net = _get_vn(1)
_ips_net = _get_vn(2)

DB_IDS = {
    "MYSQL_DB_URL": _ids_net["gateway-ip"],
    "MYSQL_DB_USER": _ids_net.get("db_user", "snort"),
    "MYSQL_DB_PASS": _ids_net.get("db_pass", "snort"),
    "MYSQL_DB_NAME": _ids_net.get("db_name", "snort"),
}

DB_IPS = {
    "MYSQL_DB_URL": _ips_net["gateway-ip"],
    "MYSQL_DB_USER": _ips_net.get("db_user", "snort"),
    "MYSQL_DB_PASS": _ips_net.get("db_pass", "snort"),
    "MYSQL_DB_NAME": _ips_net.get("db_name", "snort"),
}

GATEWAYS = [{"ip": n["gateway-ip"], "mac": n["gateway-mac"]} for n in
            (_get_vn(i) for i in range(1, NUM_VNETS + 1))]

GCP_KEY_JSON = join(dirname(__file__), "key.json")

GEMEL_PATH = "/opt/gemel-sdn"

LOG_LEVEL = DEBUG


def BENIGN_IP_LIST():
    return [h["internal_ip"] for h in _read_yml_conf()["simulations"]["benign"]]


def MALICIOUS_IP_LIST():
    return [h["internal_ip"] for h in _read_yml_conf()["simulations"]["malicious"]]


PORT = _read_yml_conf()["port"]


SIMULATIONS = _read_yml_conf()["simulations"]