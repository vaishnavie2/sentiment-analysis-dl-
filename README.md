
# 🎬 Sentiment Analysis using LSTM and GRU

## 📌 Project Overview

The dataset used in this project was created by combining custom web-scraped movie reviews with publicly available review datasets. The custom dataset was collected using Selenium-based web scraping from recent movie review pages, while additional public datasets were integrated to increase dataset size, improve data diversity, and enhance model generalization during Deep Learning training. This approach helped create a more realistic and balanced dataset for training LSTM and GRU models effectively.

This project focuses on performing Sentiment Analysis on movie reviews
using Deep Learning and Natural Language Processing (NLP).

The project demonstrates a complete end-to-end Deep Learning workflow:

Web Scraping → Data Cleaning → NLP → Tokenization → LSTM/GRU Modeling → Evaluation → Performance Comparison

The main objective was to classify movie reviews as:
- Positive
- Negative

using sequence-based Deep Learning architectures.

------------------------------------------------------------------------

# 🎯 Why This Project Was Built

- To implement real-world NLP pipelines
- To understand sequence modeling using Deep Learning
- To compare LSTM and GRU performance
- To work with real-world noisy textual data
- To combine web scraping with NLP and Deep Learning

------------------------------------------------------------------------

# 🌐 Web Scraping Methodology

### Tools Used:

- Selenium
- Chrome WebDriver
- webdriver-manager
- Dynamic page handling
- Scrolling automation

### Scraping Workflow:

1. Selenium browser was launched.
2. Review pages were opened dynamically.
3. Pages were scrolled to load more reviews.
4. Reviews were extracted using XPath/CSS selectors.
5. Invalid or extremely short reviews were filtered.
6. Extracted fields:
   - Review Text
   - Genre
   - Year
   - Movie Name
7. Dataset stored into CSV format.

------------------------------------------------------------------------

# ⚠ Challenges Faced During Scraping

## 1. Dynamic Content Loading

Some review pages loaded data dynamically using JavaScript.

### Solution:
Used Selenium instead of static scraping methods.

------------------------------------------------------------------------

## 2. Empty Review Extraction

Initially reviews were not being extracted properly.

### Cause:
Incorrect selectors and delayed rendering.

### Solution:
Inspected webpage structure and updated selectors.

------------------------------------------------------------------------

## 3. Timeout Errors

Some pages loaded slowly.

### Solution:
- Increased wait times
- Added exception handling
- Used try-except blocks

------------------------------------------------------------------------

## 4. Small Dataset Problem

Initially only a limited number of reviews were available.

### Solution:
Combined scraped data with additional public review datasets.

------------------------------------------------------------------------

# 📊 Notebook Workflow (Step-by-Step)

## 1. Data Loading

- Loaded CSV datasets
- Checked missing values
- Verified dataset shape

------------------------------------------------------------------------

## 2. Data Cleaning

Performed:
- Lowercase conversion
- Punctuation removal
- Stopword removal
- Noise cleaning
- Text normalization

------------------------------------------------------------------------

# 🧠 Why NLP Was Required

Deep Learning models cannot process raw text directly.

Text must first be converted into numerical representations.

NLP preprocessing helped:
- reduce noise
- standardize text
- improve learning quality

------------------------------------------------------------------------

## 3. Tokenization

Tokenizer converts words into numerical IDs.

Example:

movie is amazing

↓

[12, 5, 89]

------------------------------------------------------------------------

## 4. Sequence Padding

Different reviews have different lengths.

Padding ensures equal sequence length.

Example:

[1,2,3]

↓

[0,0,1,2,3]

------------------------------------------------------------------------

## 5. Train-Test Split

Used:
- 80% Training Data
- 20% Testing Data

Reason:
- sufficient learning data
- reliable model evaluation

------------------------------------------------------------------------

# 🤖 Deep Learning Models Used

## 1. LSTM (Long Short-Term Memory)

### Why LSTM?

LSTM captures:
- long-term dependencies
- sentence context
- sequence relationships

Architecture:
- Embedding Layer
- LSTM Layer
- Dropout Layer
- Dense Output Layer

------------------------------------------------------------------------

## 2. GRU (Gated Recurrent Unit)

### Why GRU?

GRU:
- trains faster
- uses fewer parameters
- computationally efficient

Architecture:
- Embedding Layer
- GRU Layer
- Dropout Layer
- Dense Output Layer

------------------------------------------------------------------------

# ❓ Why Not Simple RNN?

Simple RNN suffers from:
- vanishing gradient problem
- poor long-term memory retention

LSTM and GRU solve these problems more effectively.

------------------------------------------------------------------------

# 📈 Evaluation Metrics

Models were evaluated using:

- Accuracy
- Precision
- Recall
- F1-Score
- Validation Accuracy
- Accuracy Graphs

We did not rely only on accuracy because:
- dataset imbalance can mislead results
- F1-score gives better classification understanding

------------------------------------------------------------------------

# 🏆 Final Model Performance

| Model | Accuracy |
|-------|-----------|
| LSTM | ~88% |
| GRU | ~89% |

### Observation:

- GRU trained faster
- GRU slightly outperformed LSTM
- LSTM captured contextual dependencies effectively

------------------------------------------------------------------------

# 📉 Graph Analysis

Training accuracy increased steadily.

Validation accuracy stabilized after a few epochs.

This indicates:
- successful learning
- slight overfitting after continuous training

EarlyStopping was used to reduce overfitting.

------------------------------------------------------------------------

# 👥 Real-World Applications

This project can be useful for:

- OTT Platforms
- Movie Production Houses
- Media Analysts
- Marketing Teams

Applications:
- audience sentiment tracking
- review classification
- trend analysis
- recommendation systems

------------------------------------------------------------------------

# 🔮 Future Improvements

Possible future enhancements:

- Transformer/BERT implementation
- Multi-class sentiment analysis
- Real-time review prediction
- Streamlit/Flask deployment
- Hindi-English mixed sentiment analysis

------------------------------------------------------------------------

# 🧠 Key Learnings

- Handling dynamic web scraping
- Building NLP pipelines
- Understanding embeddings
- Working with sequence models
- Comparing Deep Learning architectures
- Handling overfitting in NLP tasks

------------------------------------------------------------------------

# 📁 Project Structure

ReviewSense/
│
├── notebook.ipynb
├── scraping.py
├── sample_dataset.csv
├── README.md
├── requirements.txt
└── images/

------------------------------------------------------------------------

# ▶️ How to Run the Project

## Install Dependencies

pip install pandas numpy nltk matplotlib scikit-learn tensorflow selenium webdriver-manager

------------------------------------------------------------------------

## Run Notebook

jupyter notebook

or open:

notebook.ipynb

in VS Code.

------------------------------------------------------------------------

# 🎯 Skills Demonstrated

- NLP
- Deep Learning
- LSTM
- GRU
- Text Preprocessing
- Web Scraping
- Sequence Modeling
- Model Evaluation
- TensorFlow/Keras
- Python Development

------------------------------------------------------------------------



# 🏁 Conclusion

This project demonstrates a practical Deep Learning based NLP pipeline built from scratch.

It combines:
- web scraping
- NLP preprocessing
- sequence modeling
- Deep Learning
- model evaluation

to perform sentiment analysis on real-world movie review datasets.
