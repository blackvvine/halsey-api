#!/usr/bin/env python3

import MySQLdb as my

from config import DB_IDS, DB_IPS


def get_db(conf):
    db = my.connect(conf["MYSQL_DB_URL"], conf["MYSQL_DB_USER"], conf["MYSQL_DB_PASS"], conf["MYSQL_DB_NAME"])
    return db


def get_events(net, min_id=0):

    db = get_db(DB_IPS if net.lower() == "ips" else DB_IDS)

    c = db.cursor()
    c.execute("""
        SELECT e.cid, e.sid, sig_id, sig_name, ip_src, ip_dst, ip_len, ip_id FROM EVENT e
            INNER JOIN signature s ON e.signature = s.sig_id
                INNER JOIN iphdr i ON i.cid = e.cid
                    WHERE e.cid >= {min_id}
    """.format(min_id=min_id))

    desc = c.description

    while True:
        row = c.fetchone()
        if not row:
            break
        yield {desc[i][0]: row[i] for i in range(len(row))}


if __name__ == "__main__":
    for r in get_events():
        print(r)


