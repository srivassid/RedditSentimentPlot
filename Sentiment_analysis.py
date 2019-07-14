from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
analyser = SentimentIntensityAnalyzer()

def read_data():
    df =  pd.read_csv("comments_rAll_topDay_2.csv")
    print(df.head())
    return df

def sentiment_analyser_score(df):
    # for row in sentence.iterrows():
    #     print(row)
    # print(df.head())
    df_sentiment = pd.DataFrame(columns=["neg","neu","pos","compound"])
    values = list(df.values.flatten())
    for row in values:
        score = analyser.polarity_scores(row)
        print(score)
        df_sentiment = df_sentiment.append({"neg":score["neg"],"neu":score["neu"],"pos":score["pos"],"compound":score["compound"]},
                                           ignore_index=True)
    df_sentiment.to_csv("sentiment_rAll_topDay.csv",sep=",",index=False)

if __name__ == '__main__':
    df = read_data()
    sentiment_analyser_score(df)