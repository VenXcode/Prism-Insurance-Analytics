
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialize sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Sample customer feedback
feedback = "Excellent service, very satisfied with my policy."

# Perform sentiment analysis
result = analyzer.polarity_scores(feedback)

print("Feedback:", feedback)
print("Sentiment Scores:", result)

# Classify sentiment
score = result["compound"]

if score >= 0.05:
    sentiment = "Positive"
elif score <= -0.05:
    sentiment = "Negative"
else:
    sentiment = "Neutral"

print("Final Sentiment:", sentiment)


import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialize VADER
analyzer = SentimentIntensityAnalyzer()

# Read Excel file
df = pd.read_excel("Insurance-Customer-Feedback.xlsx")

# Function to classify sentiment
def analyze_sentiment(feedback):
    if pd.isna(feedback) or str(feedback).strip() == "":
        return pd.Series(["Unknown", 0.0])

    scores = analyzer.polarity_scores(str(feedback))
    compound = scores["compound"]

    if compound >= 0.05:
        sentiment = "Positive"
    elif compound <= -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return pd.Series([sentiment, compound])

# Apply sentiment analysis
df[["Sentiment", "Compound Score"]] = df["Feedback"].apply(
    analyze_sentiment
)

# Export results
df.to_excel("Insurance_Sentiment_Results.xlsx", index=False)

print("Sentiment analysis completed!")
print(df[["Customer Name", "Sentiment", "Compound Score"]])
