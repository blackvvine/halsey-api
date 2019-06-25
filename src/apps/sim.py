import requests

from config import BENIGN_LIST, MALICIOUS_LIST

def get_host_qos():

    # gets a file using HTTP request
    get = lambda ip, f: requests.get("http://%s:8000/%s" % (ip, f)).text.strip()

    # receives insight lists for a IP group
    ip_list = lambda ips: [{
        "mac": get(ip, "mac.txt"),
        "host": get(ip, "hostname.txt"),
        "insight": get(ip, "insight.txt"),
        "google-ip": ip
    } for ip in ips]

    return {
        "benign": ip_list(BENIGN_LIST()),
        "malicious": ip_list(MALICIOUS_LIST())
    }


def get_attack_stats():
    # gets a file using HTTP request
    get = lambda ip, f: requests.get("http://%s:8001/%s" % (ip, f)).text.strip()
    ls = [{
        "stats": get(ip, "stats"),
        "mac": get(ip, "mac.txt"),
        "host": get(ip, "hostname.txt"),
        "google-ip": ip
    } for ip in MALICIOUS_LIST()]
    return ls