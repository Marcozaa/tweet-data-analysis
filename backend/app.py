from flask import Flask
import script
import twint
import pandas as pd

from flask import request
app = Flask(__name__)


@app.route("/")
def hello_world():
    topic = request.args.get('topic')
    c = twint.Config()

    c.Search = [topic]       # topic
    c.Limit = 100      # number of Tweets to scrape
    c.Store_csv = True       # store tweets in a csv file
    c.Output = topic +".csv"     # path to csv file

    twint.run.Search(c)
