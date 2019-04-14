#!/usr/bin/env python
import re
from os.path import dirname, join
from logging import DEBUG

MYSQL_DB_USER = "snort"
MYSQL_DB_PASS = "snort"
MYSQL_DB_URL = "10.142.0.25"
MYSQL_DB_NAME = "snort"

GCP_KEY_JSON = join(dirname(__file__), "key.json")

GEMEL_PATH = "/opt/gemel-sdn"

LOG_LEVEL = DEBUG


def _read(mpath):
    p = re.compile(r"(\d{1,3}\.?){4}")
    with open(join(dirname(__file__), mpath)) as f:
        return [l for l in f.read().split("\n") if p.match(l)]


def BENIGN_LIST():
    return _read("benign.txt")


def MALICIOUS_LIST():
    return _read("malicious.txt")

