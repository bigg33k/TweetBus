import json
import twitter

api = twitter.Api()
api = twitter.Api(consumer_key='',consumer_secret='', access_token_key='', access_token_secret='')

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
    
