from urllib2 import *
import StringIO

#password_mgr = HTTPPasswordMgrWithDefaultRealm()
url = "https://stream.twitter.com/1/statuses/sample.json"
password_mgr.add_password(None, url, 'raspbmcbig33k', 'd0ggie')
h = HTTPBasicAuthHandler(password_mgr)
opener = build_opener(h)
page = opener.open(url)
io = StringIO(page.read())
print io.getvalue()
io.close()
