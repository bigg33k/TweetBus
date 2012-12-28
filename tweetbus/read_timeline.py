import requests
import json

r = requests.post('https://stream.twitter.com/1/statuses/home_timeline.json', auth=('RASPBMCBigg33k', 'd0ggie'), stream=True)

for line in r.iter_lines():
  if line: # filter out keep-alive new lines
    print json.loads(line)
