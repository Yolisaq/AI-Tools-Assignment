# 🧠 Mastering the AI Toolkit

**AI Tools Assignment – Week 3**
**Course:** AI for Software Engineering
**Group Members:** [Insert Names]
**Date:** [Insert Date]

---

## 📘 Overview

This project demonstrates the use of popular **AI frameworks** and **tools** through three main tasks:

1. **Classical Machine Learning** using Scikit-learn
2. **Deep Learning (CNN)** using TensorFlow
3. **Natural Language Processing (NLP)** using spaCy

The assignment also includes sections on **Ethical AI**, **Code Optimization**, and a **Bonus Deployment Task** using Streamlit.

---

## 🧩 Project Structure

```
AI-Tools-Assignment/
│
├── AI_Tools_Assignment.ipynb     # Jupyter Notebook with all tasks
├── mnist_streamlit_app.py        # Streamlit web app for MNIST model
├── mnist_cnn_model.h5            # Saved CNN model (generated after training)
├── README.md                     # Project documentation
├── /screenshots/                 # Folder for output screenshots
│   ├── iris_results.png
│   ├── mnist_predictions.png
│   └── spacy_entities.png
└── /data/                        # Optional dataset storage
```

---

## 🧠 Part 1: Theoretical Understanding

**Topics Covered:**

* Differences between TensorFlow and PyTorch
* Jupyter Notebook use cases
* How spaCy enhances NLP compared to Python string operations
* Comparative analysis of Scikit-learn vs TensorFlow

---

## 💻 Part 2: Practical Implementation

### **Task 1: Classical ML (Scikit-learn – Iris Dataset)**

* Preprocessed the Iris dataset
* Trained a **Decision Tree Classifier**
* Evaluated using **accuracy**, **precision**, and **recall**

### **Task 2: Deep Learning (TensorFlow – MNIST)**

* Built a **CNN** to classify handwritten digits
* Achieved **>95% test accuracy**
* Visualized predictions on 5 random test samples

### **Task 3: NLP (spaCy – Amazon Product Reviews)**

* Performed **Named Entity Recognition (NER)**
* Conducted **rule-based sentiment analysis**

---

## ⚖️ Part 3: Ethics & Optimization

**Topics:**

* Identified potential **biases** in MNIST and text datasets
* Suggested mitigations using **TensorFlow Fairness Indicators** and **spaCy rule-based filters**
* Debugged dimension mismatch and loss function errors in TensorFlow

---

## 🚀 Bonus: Streamlit Web App (MNIST Classifier)

Run an interactive demo of the CNN model for handwritten digit classification.

**Launch the app locally:**

```bash
streamlit run mnist_streamlit_app.py
```

**Features:**

* Upload a handwritten digit image (28x28 grayscale)
* Or draw a digit directly on the canvas
* Displays the model’s prediction in real-time

**Dependencies:**

```bash
pip install streamlit tensorflow pillow numpy streamlit-drawable-canvas
```

---

## ⚙️ Installation Guide

### **1. Clone Repository**

```bash
git clone https://github.com/<your-username>/AI-Tools-Assignment.git
cd AI-Tools-Assignment
```

### **2. Create a Virtual Environment (optional)**

```bash
python -m venv venv
source venv/bin/activate  # (Linux/Mac)
venv\Scripts\activate     # (Windows)
```

### **3. Install Dependencies**

```bash
pip install -r requirements.txt
```

Or manually install key libraries:

```bash
pip install tensorflow scikit-learn spacy matplotlib numpy streamlit pillow
python -m spacy download en_core_web_sm
```

---

## 🧪 Running the Notebook

Open **AI_Tools_Assignment.ipynb** in Jupyter or Colab and execute each cell sequentially.
Include screenshots of:

* Model metrics
* CNN accuracy graph
* NER and sentiment output

---

## 👥 Team Roles

| Member   | Role              | Contribution                            |
| -------- | ----------------- | --------------------------------------- |
| [Yolisa Qadi] | Project Lead      | Coordination, TensorFlow Implementation |
| [Yolisa Qadi] | ML Engineer       | Scikit-learn Model                      |
| [Yolisa Qadi] | NLP Specialist    | spaCy & Sentiment Analysis              |
| [Yolisa Qadi] | DevOps/Deployment | Streamlit App & GitHub Setup            |
| [Yolisa Qadi] | Documentation     | Report Writing & Video Presentation     |

---

## 🧭 Learning Outcomes

* Gained proficiency in **TensorFlow, PyTorch, spaCy, and Scikit-learn**
* Improved teamwork and AI engineering collaboration
* Practiced ethical AI evaluation and model debugging
* Built a deployable **AI web app** using Streamlit

---

## 📚 References

* [TensorFlow Documentation](https://www.tensorflow.org/)
* [PyTorch Documentation](https://pytorch.org/)
* [Scikit-learn Documentation](https://scikit-learn.org/)
* [spaCy Documentation](https://spacy.io/)
* [Streamlit Documentation](https://docs.streamlit.io/)

---

✨ **Pro Tip:**
For the group video presentation, summarize each part in **30–40 seconds** per member — theory, implementation, ethics, and demo.

---
