#!/usr/bin/env python
# encoding: utf-8
# https://gist.github.com/yanofsky/5436496/

import tweepy #https://github.com/tweepy/tweepy
import datetime as dt
import ConfigParser

#Twitter API credentials

def get_all_tweets(screen_name):
    	#Twitter only allows access to a users most recent 3240 tweets with this method
     config = ConfigParser.RawConfigParser()
     config.read('settings.cfg')
     consumer_key = config.get('Twitter OAuth', 'CONSUMER_KEY')
     consumer_secret = config.get('Twitter OAuth', 'CONSUMER_SECRET')
     access_key = config.get('Twitter OAuth', 'ACCESS_TOKEN_KEY')
     access_secret = config.get('Twitter OAuth', 'ACCESS_TOKEN_SECRET')
    	#authorize twitter, initialize tweepy
     auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
     auth.set_access_token(access_key, access_secret)
     api = tweepy.API(auth)
    	
     #initialize a list to hold all the tweepy Tweets
     alltweets = []	
    	
     #make initial request for most recent tweets (200 is the maximum allowed count)
     new_tweets = api.user_timeline(screen_name = screen_name,count=200)
    	
     #save most recent tweets
     alltweets.extend(new_tweets)
     #transform the tweepy tweets into a 2D array that will populate the csv	
     yesterday = dt.datetime.utcnow() - dt.timedelta(days=1)
     outtweets = [[tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets if tweet.created_at > yesterday]
     outtweets = sorted(outtweets, key=lambda tweet: tweet[0])     
     #write the csv	
#     print outtweets
     table_string="<!DOCTYPE html>\n<html>\n<head>\n<link rel=\"stylesheet\" type=\"text/css\" href=\"styles.css\">\n</head>\n<body>\n<h1>will_note: <span style=\"font-size:0.5em\">a twitter notebook</span></h1><table>\n"
     for row in outtweets:
         table_string += "<tr>" + \
         "<td class=\"date\">" + \
          row[0].strftime("%b %d, %Y %I:%M") + \
         "</td>" + \
         "<td class=\"note\">" + \
          row[1] + \
         "</td>" + \
         "</tr>\n"
     table_string +="</table>\n</body></html>"
     text_file = open("notebook.html", "w")
     text_file.write(table_string)
     text_file.close()
#     with open('%s_tweets.csv' % screen_name, 'wb') as f:
#         writer = csv.writer(f)
#         writer.writerow(["created_at","text"])
#         writer.writerows(outtweets)
#	
#     pass


if __name__ == '__main__':
	#pass in the username of the account you want to download
     get_all_tweets("will_note")
