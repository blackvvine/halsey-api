#!/usr/bin/env python3

import requests
import json
from snort import get_events
from flask import Flask, request
from vtn import get_vn

from config import BENIGN_LIST, MALICIOUS_LIST

app = Flask("Hasley")


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/ids/events/")
def events():
    
    ids_min_id = request.args.get('ids_min_id', 0)
    ips_min_id = request.args.get('ips_min_id', 0)
    
    fetch = lambda server, min: list(get_events(server, min))
    
    return json.dumps({
        "ids": fetch("ids", ids_min_id),
        "ips": fetch("ips", ips_min_id),
    })


@app.route("/vnet/get")
def get_host_vn():
    host = request.args.get('host')
    return json.dumps(get_vn(host))


@app.route("/vnet/reassign")
def reassign():
    pass


@app.route("/vnet/get")
def getvn():

    name = request.args.get('name')
    return


@app.route("/qos")
def host_qos():
    # gets a file using HTTP request
    get = lambda ip, f: requests.get("http://%s:8000/%s.txt" % (ip, f)).text.strip()
    # receives insight lists for a IP group
    ip_list = lambda ips: [{"mac": get(ip, "mac"), "host": get(ip, "hostname"), "insight": get(ip, "insight")}
                           for ip in ips]
    return json.dumps({
        "benign": ip_list(BENIGN_LIST()),
        "malicious": ip_list(MALICIOUS_LIST())
    })

