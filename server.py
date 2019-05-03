#!/usr/bin/env python3

import requests
import json
from snort import get_events, net_history
from flask import Flask, request
from vtn import get_vn, toggle_vn

from config import BENIGN_LIST, MALICIOUS_LIST

app = Flask("Hasley")


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/ids/events")
def events():
    
    ids_min_id = request.args.get('ids_min_id', 0)
    ips_min_id = request.args.get('ips_min_id', 0)
    
    fetch = lambda server, min: list(get_events(server, min))
    
    return json.dumps({
        "ids": fetch("ids", ids_min_id),
        "ips": fetch("ips", ips_min_id),
    })


@app.route("/ids/hist")
def events_hist():
    interval = request.args.get('interval', 3600)
    buckets = request.args.get('buckets', 10)
    net = request.args.get('net', None)
    return json.dumps(net_history(net, interval, buckets))


@app.route("/vnet/get")
def get_host_vn():
    host = request.args.get('host')
    return json.dumps(get_vn(host))


@app.route("/vnet/toggle")
def toggle_host_vn():
    host = request.args.get('host')
    return json.dumps(toggle_vn(host))


@app.route("/sim/qos")
def host_qos():

    # gets a file using HTTP request
    get = lambda ip, f: requests.get("http://%s:8000/%s" % (ip, f)).text.strip()

    # receives insight lists for a IP group
    ip_list = lambda ips: [{
        "mac": get(ip, "mac"),
        "host": get(ip, "hostname"),
        "insight": get(ip, "insight"),
        "google-ip": ip
    } for ip in ips]

    return json.dumps({
        "benign": ip_list(BENIGN_LIST()),
        "malicious": ip_list(MALICIOUS_LIST())
    })


@app.route("/sim/attack")
def host_attack_stats():

    # gets a file using HTTP request
    get = lambda ip, f: requests.get("http://%s:8001/%s" % (ip, f)).text.strip()

    ls = [{
        "stats": get(ip, "stats"),
        "mac": get(ip, "mac"),
        "host": get(ip, "hostname"),
        "google-ip": ip
    } for ip in MALICIOUS_LIST()]

    return json.dumps(ls)


