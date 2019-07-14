import praw
import pandas as pd

pd.set_option('display.float_format', lambda x: '%.3f' % x)
pd.set_option('display.max_rows', 250)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

def initialize_reddit_app():
    # print(pd.read_csv("credentials.csv",header=None,usecols=[0]))
    client_id = pd.read_csv("credentials.csv",usecols=[0]).values[0][0]
    client_secret = pd.read_csv("credentials.csv",usecols=[1]).values[0][0]
    user_agent = pd.read_csv("credentials.csv",usecols=[2]).values[0][0]

    reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent=user_agent)
    return  reddit

def get_posts(reddit):
    posts = []
    hot_posts = reddit.subreddit('all').top('day',limit=50)
    for post in hot_posts:
        posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])
        # print(post.title)
    posts = pd.DataFrame(posts,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created'])
    # print(posts.head(50))
    print(posts["num_comments"].sum())
    # print([posts["id"]])
    return posts["id"]

def get_comments(reddit,posts_id):
    df_comments = pd.DataFrame()
    for id in posts_id:
        submission = reddit.submission(id=id)
        submission.comments.replace_more(limit=None)

        for comment in submission.comments.list():
            print(comment.body)
            df_comments = df_comments.append([comment.body],ignore_index=True)
    df_comments.to_csv("comments_rAll_topDay_2.csv",sep=",",index=False)
    # for top_level_comment in submission.comments:
    #     print(top_level_comment.body)

def credentials():
    print((pd.read_csv("credentials.csv",usecols=[0]).values[0][0]))
    print(pd.read_csv("comments_rAll_topDay_2.csv").shape)
if __name__ == '__main__':
    reddit = initialize_reddit_app()
    # posts_id = get_posts(reddit)
    credentials()
    # get_comments(reddit,posts_id)