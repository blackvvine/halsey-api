#!/usr/bin/env python3

import MySQLdb as my
import config as conf


def get_db():
    db=my.connect(conf.MYSQL_DB_URL, conf.MYSQL_DB_USER, conf.MYSQL_DB_PASS, conf.MYSQL_DB_NAME)
    return db


def get_events(min_id=0):

    db = get_db()
    c = db.cursor()
    c.execute("""
        select e.cid, e.sid, sig_id, sig_name, ip_src, ip_dst, ip_len, ip_id from event e
            inner join signature s on e.signature = s.sig_id
                inner join iphdr i on i.cid = e.cid
                    where e.cid > {min_id}
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


