import os

from flask import render_template
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

def get_submissions(subreddit):
    reddit = create_reddit()
    subreddit = reddit.subreddit(subreddit)
    new_posts = subreddit.new()
    posts = [x for x in new_posts if x.num_comments <= MAX_COMMENTS]
    return posts


def list():
    reddit = create_reddit()
    posts = get_submissions(SUBREDDIT)
    return render_template('posts.html', posts=posts)
