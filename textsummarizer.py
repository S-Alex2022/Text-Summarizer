import nltk
nltk.download('punkt')
nltk.download('stopwords')
from flask import Flask, render_template, request
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer


def summarize_text(text):
    # Tokenize the text into sentences
    sentences = sent_tokenize(text)

    # Remove stopwords and perform stemming
    stop_words = set(stopwords.words('english'))
    stemmer = PorterStemmer()
    word_frequencies = {}
    for sentence in sentences:
        for word in nltk.word_tokenize(sentence):
            if word.casefold() not in stop_words:
                stemmed_word = stemmer.stem(word)
                if stemmed_word in word_frequencies:
                    word_frequencies[stemmed_word] += 1
                else:
                    word_frequencies[stemmed_word] = 1

    # Calculate sentence scores based on word frequencies
    sentence_scores = {}
    for sentence in sentences:
        for word in nltk.word_tokenize(sentence):
            stemmed_word = stemmer.stem(word)
            if stemmed_word in word_frequencies:
                if sentence in sentence_scores:
                    sentence_scores[sentence] += word_frequencies[stemmed_word]
                else:
                    sentence_scores[sentence] = word_frequencies[stemmed_word]

    # Sort sentences by scores in descending order
    sorted_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)

    # Select the top N sentences as the summary
    summary_sentences = sorted_sentences[:3]  # You can adjust the number of sentences in the summary

    # Join the summary sentences into a single string
    summary = ' '.join(summary_sentences)
    return summary
