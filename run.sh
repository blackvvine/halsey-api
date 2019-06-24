#!/usr/bin/env bash

DIR=$(dirname $0)

portnum() {
    cat src/halsey.yml | grep port | grep -oE '[[:digit:]]+'
}

port=$(portnum)
daemon=""

if [[ "$1" == "daemon" ]]
then
    daemon="-d"
fi

docker run $daemon -it --rm -p $port:$port -v $(pwd)/src:/root/halsey iman/halsey:1
