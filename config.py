#!/usr/bin/env python

from os.path import dirname, join
from logging import DEBUG

MYSQL_DB_USER = "snort"
MYSQL_DB_PASS = "snort"
MYSQL_DB_URL = "10.142.0.25"
MYSQL_DB_NAME = "snort"

GCP_KEY_JSON = join(dirname(__file__), "key.json")

GEMEL_PATH = "/opt/gemel-sdn"

LOG_LEVEL = DEBUG
