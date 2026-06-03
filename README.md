# Sentiment Analysis using LSTM and GRU

## Project Overview

This project performs Sentiment Analysis on movie reviews using Deep Learning and Natural Language Processing (NLP).

The objective is to classify movie reviews as:

- Positive
- Negative

The project combines NLP preprocessing, Deep Learning sequence models, and Selenium-based web scraping to build an end-to-end sentiment classification pipeline.

The complete workflow is:

Web Scraping → Data Cleaning → NLP Preprocessing → Tokenization → Sequence Padding → LSTM/GRU Training → Model Evaluation → Sentiment Prediction

## Why This Project Was Built

- To understand real-world NLP workflows
- To learn sequence modeling using Deep Learning
- To compare LSTM and GRU architectures
- To work with movie review sentiment classification
- To integrate web scraping with NLP and Deep Learning

## Dataset

### Training Dataset

The model was trained using the IMDB Movie Reviews Dataset containing labeled reviews with sentiment classes:

- Positive
- Negative

### Scraped Dataset

Additional movie reviews were collected using Selenium-based web scraping from movie review pages.

These reviews were not used for training because they did not contain sentiment labels.

Instead, they were used as unseen real-world reviews for sentiment prediction after model training.

## Web Scraping Methodology

### Tools Used

- Selenium
- Chrome WebDriver
- webdriver-manager

### Scraping Workflow

1. Open movie review pages using Selenium.
2. Scroll dynamically to load additional reviews.
3. Extract review text using webpage selectors.
4. Filter invalid or empty reviews.
5. Save extracted reviews into CSV format.

## NLP Pipeline

### Data Cleaning

- Lowercase conversion
- Punctuation removal
- Stopword removal
- Text normalization
- Noise removal

### Tokenization

Converts words into numerical IDs.

Example:

movie is amazing

→

[12, 5, 89]

### Sequence Padding

Reviews have different lengths. Padding ensures all sequences have the same length before being passed to LSTM and GRU models.

### Train-Test Split

- 80% Training
- 20% Testing

## Deep Learning Models

### LSTM (Long Short-Term Memory)

- Captures long-term dependencies
- Learns contextual information
- Handles sequential relationships

### GRU (Gated Recurrent Unit)

- Trains faster
- Uses fewer parameters
- Computationally efficient

## Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1-Score

## Results

| Model | Accuracy |
|---------|---------|
| LSTM | ~88% |
| GRU | ~89% |

## Sentiment Prediction on Scraped Reviews

After training on the IMDB dataset, the GRU model was used to predict sentiment on real-world movie reviews collected through Selenium.

## Skills Demonstrated

- Python
- NLP
- Deep Learning
- LSTM
- GRU
- Selenium
- Web Scraping
- TensorFlow/Keras
- Model Evaluation
- Sequence Modeling

## Conclusion

This project demonstrates a complete NLP and Deep Learning pipeline for sentiment classification using web scraping, text preprocessing, sequence modeling, and sentiment prediction.
