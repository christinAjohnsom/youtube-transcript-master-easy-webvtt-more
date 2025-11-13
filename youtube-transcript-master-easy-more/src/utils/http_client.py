thonimport requests

def get_http_client():
    return requests.Session()