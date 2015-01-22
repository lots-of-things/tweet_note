# tweet_note
A tiny twitter notebook for myself

I got a head start from yanofsky's tweet_dumper.py
https://gist.github.com/yanofsky/5436496/

You have to set up the access tokens in order to make it work for your own account.  
https://themepacific.com/how-to-generate-api-key-consumer-token-access-key-for-twitter-oauth/994/
Mine are in a config file that I'm not sharing with you.

After those are set up, you run 

  python tweet_note.py

and it currently pulls in the last day's tweets and puts them on the local html document called notebook.html

Open the html and you'll have a pretty list of timestamps and notes.
