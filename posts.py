import os

from flask import render_template
import praw

SUBREDDIT = "cscareerquestions"

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


def list():
    reddit = create_reddit()
    titles = [x.title for x in reddit.subreddit(SUBREDDIT).hot(limit=5)]
    return render_template('posts.html', titles=titles)
