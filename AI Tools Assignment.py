# AI Tools Assignment Starter Notebook
# Theme: "Mastering the AI Toolkit" 🛠️🧠
# Authors: [Your Group Names]
# Date: [Insert Date]

# ======================================================
# Part 1: Classical ML with Iris Dataset (Scikit-learn)
# ======================================================

# Import libraries
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score

# Load Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Check data shapes
print("Feature shape:", X.shape)
print("Labels shape:", y.shape)

# Split data into training and test sets (80/20 split)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Decision Tree Classifier
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)

# Predict on test set
y_pred = clf.predict(X_test)

# Evaluate model
print("=== Iris Classifier Performance ===")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred, average='macro'))
print("Recall:", recall_score(y_test, y_pred, average='macro'))

# ======================================================
# Part 2: Deep Learning CNN with MNIST (TensorFlow)
# ======================================================

# Import TensorFlow and Keras
import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt
import numpy as np

# Load MNIST dataset
(X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()

# Normalize data (0-1 range)
X_train = X_train / 255.0
X_test = X_test / 255.0

# Reshape data for CNN input (28x28x1)
X_train = X_train.reshape(-1,28,28,1)
X_test = X_test.reshape(-1,28,28,1)

# One-hot encode labels
y_train = tf.keras.utils.to_categorical(y_train, 10)
y_test_categorical = tf.keras.utils.to_categorical(y_test, 10)

# Build CNN model
model = models.Sequential([
    layers.Conv2D(32, (3,3), activation='relu', input_shape=(28,28,1)),
    layers.MaxPooling2D((2,2)),
    layers.Conv2D(64, (3,3), activation='relu'),
    layers.MaxPooling2D((2,2)),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])

# Compile model
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Train model
history = model.fit(X_train, y_train, epochs=5, batch_size=64, validation_split=0.1)

# Evaluate model
test_loss, test_acc = model.evaluate(X_test, y_test_categorical)
print("=== MNIST CNN Performance ===")
print("Test Accuracy:", test_acc)

# Visualize predictions on 5 sample images
sample_indices = np.random.choice(len(X_test), 5, replace=False)
for i in sample_indices:
    plt.imshow(X_test[i].reshape(28,28), cmap='gray')
    plt.title(f"Predicted: {np.argmax(model.predict(X_test[i].reshape(1,28,28,1)))} | True: {y_test[i]}")
    plt.show()

# ======================================================
# Part 3: NLP with spaCy (Amazon Product Reviews)
# ======================================================

# Install spaCy model if needed
# !python -m spacy download en_core_web_sm

import spacy

# Load English NLP model
nlp = spacy.load("en_core_web_sm")

# Example Amazon product reviews
reviews = [
    "I love the Apple iPhone 13! The camera is amazing.",
    "Samsung Galaxy S21 is good, but battery life is poor.",
    "The Sony headphones have excellent sound quality."
]

# Named Entity Recognition (NER) and basic sentiment
positive_words = ["love", "excellent", "amazing", "great", "good"]
negative_words = ["poor", "bad", "terrible", "hate"]

for review in reviews:
    d
    print("Entities:")
    for ent in doc.ents:
        print(f" - {ent.text} ({ent.label_})")
    
    # Simple sentiment analysis
    sentiment_score = sum([1 for word in review.split() if word.lower() in positive_words]) - \
                      sum([ 1 for word in review.split() if word.lower() in negative_words])
    sentiment = "Positive" if sentiment_score > 0 else "Negative" if sentiment_score < 0 else "Neutral"
    print("Sentiment:", sentiment)
