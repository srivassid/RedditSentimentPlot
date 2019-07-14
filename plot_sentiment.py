import matplotlib.pyplot as plt
import pandas as pd

def read_data():
    return pd.read_csv("sentiment_rAll_topDay.csv")

def make_plot(df):
    df = df["compound"].rolling(400).mean()
    plt.plot(df)
    plt.xlabel("Comment Number")
    plt.ylabel("Compound Sentiment Score")
    plt.title("Running mean of Compound sentiment score of posts, r All, top Day, 50 posts.")
    plt.show()

if __name__ == '__main__':
    make_plot(read_data())