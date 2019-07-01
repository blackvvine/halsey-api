#!/usr/bin/env python3

import json

from apps import topo
from apps.ids import get_events, net_history
from flask import Flask, request, Response

from apps.sim import get_host_qos, get_attack_stats
from apps.vtn import get_vn, toggle_vn
from apps.topo import get_arp_table
from apps import vtn

from config import ALERTS, VNETS

app = Flask("Hasley")


def json_result(obj):
    return Response(json.dumps(obj), mimetype="application/json")


@app.route("/")
def hello():
    return "Salam Donya!"


@app.route("/ids/events")
def events_legacy():

    ids_min_id = request.args.get('ids_min_id', 0)
    ips_min_id = request.args.get('ips_min_id', 0)
    interval = request.args.get('interval', None)

    fetch = lambda server, min: list(get_events(server, min, interval))

    return json_result({
        "ids": fetch("ids", ids_min_id),
        "ips": fetch("ips", ips_min_id),
    })


@app.route("/v1/ids/events")
def events():

    interval = request.args.get('interval', None)
    fetch = lambda server: list(get_events(server, interval=interval))

    return json_result({
        vn["name"]: fetch(vn["name"])
        for vn in VNETS
    })


@app.route("/ids/hist")
def events_hist():
    interval = request.args.get('interval', 3600)
    buckets = request.args.get('buckets', 10)
    net = request.args.get('net', None)
    return json_result(net_history(net, interval, buckets))


@app.route("/vnet/get")
def get_host_vn():
    host = request.args.get('host')
    if not host:
        return json_result({"status": "400"}), 400
    return json_result(get_vn(host))


@app.route("/vnet/toggle")
def toggle_host_vn():
    host = request.args.get('host')
    if not host:
        return json_result({"status": "400"}), 400
    return json_result(toggle_vn(host))


@app.route("/v1/vnet/status")
def vnet_status():
    return json_result(vtn.status())


@app.route("/v1/vnet/info")
def get_alerts_info():
    return json_result(ALERTS)


@app.route("/sim/qos")
def host_qos():
    return json_result(get_host_qos())


@app.route("/sim/attack")
def host_attack_stats():
    return json_result(get_attack_stats())


@app.route("/v1/topo/arp")
def arp_table():
    return json_result(topo.get_arp_table())


@app.route("/v1/topo/sims")
def get_simulations():
    return json_result(topo.get_sims())


