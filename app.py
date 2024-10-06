from flask import Flask, render_template, request
from textsummarizer import summarize_text
app = Flask(__name__)
@app.route('/')


def home():
    return render_template('index.html')
@app.route('/summarize', methods=['POST'])


def summarize():
    text = request.form['text']
    summary = summarize_text(text)  # Call the text summarization function
    return render_template('result.html', summary=summary)


if __name__ == '__main__':
    app.run(debug=True)
