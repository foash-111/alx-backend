#!/usr/bin/env python3
"""just recab on flask framework by implement basic web application"""

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def hello():
    """render simple page"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
