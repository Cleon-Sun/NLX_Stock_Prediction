import pandas as pd
import datetime as dt 
import praw
import requests
import datetime as dt
import csv
import pandas as pd

def days_since_start(timestamp, start_date='2021-06-01'):
    timestamp = pd.to_datetime(timestamp)
    start_date = pd.to_datetime(start_date)
    return (timestamp - start_date).days


def get_reddit():
    # Initialize PRAW with your Reddit application credentials
    reddit = praw.Reddit(
        client_id='cBV1oxSEXF3Go4tSZY8erQ',
        client_secret='dHRocC-zyVr3yBepHZAkn91S8AnI5Q',
        user_agent='scrape'
    )

    subreddit_list  = ['wallstreetbets', 'stocks', 'investing']
    # For example, use 'wallstreetbets'
    # subreddit = reddit.subreddit('stocks')
    query = 'GameStop'

    # Define the time period
    start_epoch = int(dt.datetime(2021, 6, 1).timestamp())
    end_epoch = int(dt.datetime(2021, 8, 31).timestamp())

    df_reddit =[]
    # Search for submissions in the defined time period
    for sub in subreddit_list:
        subreddit = reddit.subreddit(sub)
        for submission in subreddit.search(query, limit=10000):
            t = submission.created_utc
            # print(t)
            if start_epoch <= int(t) <= end_epoch:
                # print(f"Text: {submission.selftext}") 
                # print(submission.title, submission.url)
                title = submission.title
                post_date = dt.datetime.fromtimestamp(submission.created_utc)
                # print(f"Submission Date: {post_date}")
                df_reddit.append([post_date, title])

            # Additional code to scrape comments, etc.
    df_reddit=pd.DataFrame(df_reddit, columns = ['date', 'title']).sort_values('date').drop_duplicates().reset_index(drop=True)
    df_reddit.to_csv('reddit.csv', index=False)
    
