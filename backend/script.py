
'''
import twint
import pandas as pd

c = twint.Config()

c.Search = ['Russia']       # topic
c.Limit = 100      # number of Tweets to scrape
c.Store_csv = True       # store tweets in a csv file
c.Output = "russia2.csv"     # path to csv file

twint.run.Search(c)
'''
