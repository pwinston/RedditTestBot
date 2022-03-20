import os
import time

from flask import render_template
import humanize
import praw

SUBREDDIT = "cscareerquestions"
MAX_COMMENTS = 3

auth = {
    'script': os.environ['REDDIT_SCRIPT'],
    'secret': os.environ['REDDIT_SECRET'],
    'username': os.environ['REDDIT_USERNAME'],
    'password': os.environ['REDDIT_PASSWORD']
}


def create_reddit():
    # For now using Application Type Script w/ Password Flow
    # See "Authenticating via OAuth" in PRAW docs.
    return praw.Reddit(
        client_id=auth['script'],
        client_secret=auth['secret'],
        username=auth['username'],
        password=auth['password'],
        user_agent=f"lonelybot by {auth['username']}",
    )

class Post:
    def __init__(self, now, submission):
        self.now = now
        self.obj = submission
        self.ago = self.ago_string()

    def ago_string(self):
        created = self.obj.created_utc
        return humanize.naturaltime(self.now - created)

def get_submissions(subreddit):
    reddit = create_reddit()
    subreddit = reddit.subreddit(subreddit)
    new_posts = subreddit.new()
    now = time.time()
    posts = [x for x in new_posts if x.num_comments <= MAX_COMMENTS]
    return [Post(now, x) for x in posts]


def list():
    reddit = create_reddit()
    items = get_submissions(SUBREDDIT)
    return render_template('posts.html', items=items)
