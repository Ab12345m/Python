# Import required libraries
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

# Sample dataset (messages + labels)
messages = [
    "Win money now", 
    "Limited offer just for you", 
    "Call this number now", 
    "Hello how are you", 
    "Let's meet tomorrow", 
    "Are you available today", 
    "Congratulations you won a prize",
    "Free entry in a contest"
]

# Labels: 1 = Spam, 0 = Not Spam
labels = [1, 1, 1, 0, 0, 0, 1, 1]

# Convert text data into numerical form
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(messages)

# Split dataset into training and testing
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.3, random_state=42)

# Create and train model
model = MultinomialNB()
model.fit(X_train, y_train)

# Test the model
predictions = model.predict(X_test)

print("Predictions:", predictions)
print("Actual:", y_test)

# Test with new message
new_msg = ["Free money offer just for you"]
new_msg_vec = vectorizer.transform(new_msg)

result = model.predict(new_msg_vec)

if result[0] == 1:
    print("Spam Message")
else:
    print("Not Spam Message")