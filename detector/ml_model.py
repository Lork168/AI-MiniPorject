import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score

def train_model():
    df = pd.read_csv("dataset/spam.csv")

    df["label_num"] = df["label"].map({"ham": 0, "spam": 1})

    X = df["text"]
    y = df["label_num"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = Pipeline([
        ("tfidf", TfidfVectorizer()),
        ("classifier", MultinomialNB())
    ])

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    print("Model Accuracy:", accuracy)

    with open("detector/spam_model.pkl", "wb") as file:
        pickle.dump(model, file)

    print("Model saved as detector/spam_model.pkl")

if __name__ == "__main__":
    train_model()