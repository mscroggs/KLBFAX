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
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        req = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(req)
        out = response.read()
        try:
            return out.decode(response.info().get_content_charset('utf-8'))
        except:
            return out

