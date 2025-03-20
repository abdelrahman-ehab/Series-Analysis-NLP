# Naruto TV Series NLP Analysis

This repository contains a comprehensive NLP analysis of the *Naruto* anime series. The project is divided into three primary models that explore various aspects of the series—from thematic analysis of dialogue to character interaction mapping and specialized classification of ninja techniques.

## Overview

- **Theme Classification:**  
  Leverages zero-shot classification to analyze subtitles from over 200 episodes and extract key dialogue themes.
  
- **Character Network Generator:**  
  Uses NLP and graph libraries to generate a visual network of character interactions from subtitle data.
  
- **Text Classifier:**  
  Scrapes data from online sources and classifies various ninja techniques into distinct categories.

## Models

### 1. Theme Classification

- **Objective:**  
  Classify the dialogue themes from *Naruto* subtitles.
  
- **Approach:**  
  Implements zero-shot classification using Facebook's Large MNLI BART model. Dialogues are classified into the following themes:
  - `friendship`
  - `hope`
  - `battle`
  - `self development`
  - `betrayal`
  - `love`
  - `dialogue`
  

### 2. Character Network Generator

- **Objective:**  
  Generate a network graph illustrating character interactions based on subtitle dialogues.
  
- **Approach:**  
  Utilizes NLP libraries (NLTK, spaCy, spaCy Transformers) in conjunction with graph libraries (NetworkX and Pyvis) to construct and visualize the character network.
  


### 3. Text Classifier

- **Objective:**  
  Classify various ninja techniques scraped from *Naruto* fandom pages.
  
- **Approach:**  
  Employs web scraping (Scrapy, Beautiful Soup) to collect data and uses the `distilbert-base-uncased` model from Hugging Face Transformers to categorize techniques into:
  - `ninjutsu`
  - `taijutsu`
  - `genjutsu`
  

## Dependencies

Each model has its own set of dependencies:

- **Theme Classification:**
  - Hugging Face Transformers (BART for MNLI)
  - PyTorch or TensorFlow
  
- **Character Network Generator:**
  - NLTK
  - spaCy & spaCy Transformers
  - NetworkX
  - Pyvis
  
- **Text Classifier:**
  - Scrapy
  - Beautiful Soup
  - Hugging Face Transformers (DistilBERT)

Please refer to the individual notebooks for the full list of requirements and installation commands.

## Data Sources

- **Subtitles:**  
  Subtitle files for over 200 episodes of *Naruto* are used for theme classification and character network generation.
  
- **Web Scraping:**  
  Data for classifying ninja techniques is scraped from *Naruto* fandom website.


