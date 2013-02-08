import json
import twitter

api = twitter.Api()
api = twitter.Api(consumer_key='jiWXHSOG32kXMIm4FMuLZw',consumer_secret='EiiExPr3LzvXIfn8L3bajhR0p1GWmp4de3rxtNCw98', access_token_key='1063047326-73oRKXWlgkHoKk2vJtdBxwbs7ZahTVXserWrvGS', access_token_secret='jueuqbdlYhbrlzhfVktui0daybZStoxa9eafXsWlio')

try:
    api.VerifyCredentials() 
    statuses = api.GetUserTimeline('raspbmcbigg33k')
    #tweets = json.loads(statuses)
    #print tweets['text']
    #print [s.text for s in statuses]
    status_post_num = len(statuses)
    #print status_post_num
    print statuses[status_post_num-1].text
except IOError:
    print "Some kind of error"
else:
    pass 
    
