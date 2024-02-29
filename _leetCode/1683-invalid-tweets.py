#Invalid Tweets
#https://leetcode.com/problems/invalid-tweets/description/
import pandas

caseData = {
    'tweet_id': [1, 2],
    'content': ['Vote for Biden', 'Let us make America great again!']
}

caseDataFrame = pandas.DataFrame(caseData)

if True:
    def invalid_tweets(tweets):
        return tweets[tweets['content'].str.len() > 15][['tweet_id']]
        
print(f"{invalid_tweets(caseDataFrame).to_markdown(index=False)}")