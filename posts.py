import os
import time

from flask import render_template
import humanize
import praw

SUBREDDIT = "cscareerquestions"
MAX_COMMENTS = 2

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
    def __init__(self, submission):
        self.submission = submission
        self.title = submission.title
        self.url = submission.url
        self.num_comments = submission.num_comments
        self.ago = self.ago_string()

    def ago_string(self):
        created = self.submission.created_utc
        return humanize.naturaltime(time.time() - created)

def get_submissions(subreddit):
    reddit = create_reddit()
    subreddit = reddit.subreddit(subreddit)
    new_posts = subreddit.new()
    posts = [x for x in new_posts if x.num_comments <= MAX_COMMENTS]
    return [Post(x) for x in posts]


def list():
    reddit = create_reddit()
    posts = get_submissions(SUBREDDIT)
    return render_template('posts.html', posts=posts)
