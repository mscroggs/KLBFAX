import json

def load_json(url):
    feed = load(url)
    return json.loads(feed)

def load(url):
    try:
        import urllib2
        v = 2
    except:
        import urllib.request
        v = 3
    if v == 2:
        response = urllib2.urlopen(url)
        return response.read()
    if v == 3:
        response = urllib.request.urlopen(url)
        out = response.read()
        try:
            return out.decode(response.info().get_content_charset('utf-8'))
        except:
            return out

