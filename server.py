#!/usr/bin/env python3

import json
from snort import get_events
from flask import Flask, request

app = Flask("Hasley")

@app.route("/")
def hello():
    return "Hello World!"


@app.route("/ids/events/")
def events():
    min_id = request.args.get('min_id', 0)
    return json.dumps(list(get_events(min_id=min_id)))



