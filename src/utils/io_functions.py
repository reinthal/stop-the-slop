import requests as rq


def get_ip() -> str:
    return rq.get("https://api.ipify.org").text
