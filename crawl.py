import os

import praw

auth = {
  'script': os.environ['REDDIT_SCRIPT'],
  'secret': os.environ['REDDIT_SECRET'],
  'username': os.environ['REDDIT_USERNAME'],
  'password': os.environ['REDDIT_USERNAME']
}


def run():
  reddit = praw.Reddit(
    client_id=auth['script'],
    client_secret=auth['secret'],
    username=auth['username'],
    password=auth['password'],
    user_agent=f"lonelybot by {auth['username']}",
  )
  return reddit.user.me()