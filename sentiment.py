import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob

# Data load karna
df = pd.read_csv("amazon_reviews.csv")

# Sirf pehle 100 reviews lenge (taaki fast chale)
df = df.head(100)

# Sentiment nikalne ka function
def get_sentiment(text):
    blob = TextBlob(str(text))
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Har review pe sentiment apply karna
df["Sentiment"] = df["reviewText"].apply(get_sentiment)

# Result dekhna
print(df[["reviewText", "Sentiment"]])

# Kitne positive/negative/neutral hain, count karna
print(df["Sentiment"].value_counts())

# Chart banana
df["Sentiment"].value_counts().plot(kind="bar", color=["green","gray","red"])
plt.title("Sentiment Analysis of Amazon Reviews")
plt.xlabel("Sentiment")
plt.ylabel("Count")
plt.savefig("sentiment_chart.png")
plt.show()