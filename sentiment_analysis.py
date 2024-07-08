from transformers import pipeline

def analyze_sentiment(text):
    # Initialize sentiment analysis pipeline
    sentiment_pipeline = pipeline("sentiment-analysis")
    
    # Perform sentiment analysis
    result = sentiment_pipeline(text)[0]
    
    # Extract sentiment and score
    sentiment = result['label']
    score = result['score']
    
    return sentiment, score

def main():
    print("Welcome to the Sentiment Analysis Tool!")
    print("Enter a sentence to analyze its sentiment (or 'quit' to exit):")
    
    while True:
        user_input = input("> ")
        
        if user_input.lower() == 'quit':
            print("Thank you for using the Sentiment Analysis Tool. Goodbye!")
            break
        
        sentiment, score = analyze_sentiment(user_input)
        
        print(f"Sentiment: {sentiment}")
        print(f"Confidence: {score:.2f}")
        print()

if __name__ == "__main__":
    main()