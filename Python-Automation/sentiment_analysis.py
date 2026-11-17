
from pathlib import Path

import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Define project paths
BASE_DIR = Path(__file__).resolve().parent
PROJECT_DIR = BASE_DIR.parent

INPUT_FILE = PROJECT_DIR / "Dataset" / "Insurance-Customer-Feedback.xlsx"
OUTPUT_FILE = PROJECT_DIR / "Dataset" / "Insurance_Sentiment_Results.xlsx"

# Initialize VADER
analyzer = SentimentIntensityAnalyzer()


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


# Main execution
def main():

    # Read Excel file
    df = pd.read_excel(INPUT_FILE)

    # Apply sentiment analysis
    df[["Sentiment", "Compound Score"]] = df["Feedback"].apply(
        analyze_sentiment
    )

    # Export results
    df.to_excel(OUTPUT_FILE, index=False)

    print("Sentiment analysis completed!")
    print(f"Total records processed: {len(df)}")
    print(f"Results saved to: {OUTPUT_FILE}")

    print(df[["Customer Name", "Sentiment", "Compound Score"]])


if __name__ == "__main__":
    main()

