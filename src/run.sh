#!/usr/bin/env bash

start() {

    # kill previous instances
    ps aux | grep flask | grep -v grep | awk '{ print $2 }' | xargs kill

    # start server
    FLASK_APP=server.py flask run -p 8080 -h 0.0.0.0

}

start

while inotifywait -qqre modify $(pwd)
do
    start
done
