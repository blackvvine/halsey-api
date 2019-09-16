#!/usr/bin/env bash

DIR=$(dirname $0)

portnum() {
    cat $DIR/src/halsey.yml | grep port | grep -oE '[[:digit:]]+'
}

port=$(portnum)
daemon=""

if [[ "$1" == "daemon" ]]
then
    daemon="-d"
fi

docker run $daemon -it --rm -p $port:$port -v $DIR/src:/root/halsey iman/halsey:1
