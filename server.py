#!/usr/bin/env python3

import requests
import json
from snort import get_events
from flask import Flask, request

from config import BENIGN_LIST, MALICIOUS_LIST

app = Flask("Hasley")


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/ids/events/")
def events():
    min_id = request.args.get('min_id', 0)
    return json.dumps(list(get_events(min_id=min_id)))


@app.route("/vnet/reassign")
def reassign():
    pass


@app.route("/qos")
def host_qos():
    ip_list = lambda ips: [requests.get("http://" + ip + ":8000/insight.txt").text.strip() for ip in ips]
    return json.dumps({
        "benign": ip_list(BENIGN_LIST()),
        "malicious": ip_list(MALICIOUS_LIST())
    })
