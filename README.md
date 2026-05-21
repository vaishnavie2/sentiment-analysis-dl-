# Deep Learning Based Sentiment Analysis on Bollywood Movie Reviews using LSTM and GRU

This README contains the complete project explanation, workflow, models, problems faced, solutions, and interview preparation notes.

## Technologies Used
- Python
- TensorFlow
- Keras
- NLP
- Selenium
- Pandas

## Models Used
- LSTM
- GRU

## Final Accuracy
- LSTM: ~88%
- GRU: ~89%

## Key Features
- Web scraping
- NLP preprocessing
- Sentiment analysis
- Deep Learning model comparison


# Project Overview

This project performs sentiment analysis on Bollywood movie reviews using Deep Learning and Natural Language Processing.

The goal of the project is to classify reviews into positive or negative sentiments and compare the performance of LSTM and GRU models.

The project includes:
- data collection
- web scraping
- NLP preprocessing
- tokenization
- padding
- Deep Learning
- model evaluation
- accuracy comparison

# Problems Faced

1. Dynamic page loading during scraping
2. Empty review extraction
3. Timeout issues
4. CSV saving permission issues
5. Small dataset size

# Solutions

- Used Selenium waits and scrolling
- Updated CSS selectors
- Added exception handling
- Closed CSV before saving
- Combined scraped data with additional datasets

# Conclusion

GRU slightly outperformed LSTM while training faster on this dataset.
