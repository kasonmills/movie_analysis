import pandas as pd
import csv
import re
import datetime
import time
import calendar

movie = pd.read_csv("raw_data.csv")
movie["date"] = pd.to_datetime(movie["release_date"])
modify1 = movie.drop(columns=["release_date","id", "popularity", "vote_count", "number", "overview"])
modify7 = movie.drop(columns=["number", "id", "release_date", "vote_count", "overview", "date"])
modify2 = modify1.drop_duplicates()
modify8 = modify7.drop_duplicates()

"""
this is a bit of test code I used as I was learning more about pandas and how the data was being read in/out and how it could be
displayed on the screen. I purposefully commented out all the lines that were for testing/figuring out pandas so I knew how to
manipulate my data. All the uncommented lines of code are needed to run the program effectively.

Credit for the data set: Kaggle.com

Movie Information:

Movie ID: A unique identifier for each movie.
Title: The name of the movie.
Genre: The genre(s) of the movie, often categorized into multiple types like Action, Comedy, Drama, etc.
Release Year: The year the movie was released.
Runtime: The length of the movie in minutes.
Overview/Synopsis: A brief description or plot summary of the movie.
Ratings Information:

Rating: The average rating given to the movie, usually on a scale of 1 to 10.
Number of Votes: The total count of votes or ratings the movie has received.
"""
# print(movie.head(5))
# print(movie.columns)
# print(movie[["release_date", "title"]])
# print(movie.loc[movie["title"] == "lord of the rings"])
# print(movie.describe())
# print(movie.sort_values(["title", "vote_average"], ascending=(1,0)))
# print(modified.loc[modified["release_date"].str.contains("2000")])
# print(modified.loc[modified["release_date"].str.contains("20[a-z]*", flags= re.I, regex=True)])
# print(modified.groupby(["vote_average"]).mean().sort_values(["vote_average"] > 5, ascending=True))
# print(modified.groupby(["release_date", "title"]).count()["vote_count"])
# print(modify2.head(5))

"""
Question one: Is there a connection between the popularity of a movie and a higher rating out of ten?

Question two: Are there a higher rating on average for movies that have come out more recently? 
"""
# to answer question one
print(modify8.nlargest(20, columns=["popularity"]))

# just for reference
# print(modify2.describe())
# to answer question two

modify5 = modify2[(modify2["date"].dt.year < 2000)]
modify6 = modify5[(modify5['vote_average'] > 5)]
modify3 = modify2[(modify2["date"].dt.year >= 2000)]
modify4 = modify3[(modify3["vote_average"] > 5)]

print(modify6.nlargest(10, columns=["vote_average"]))
print(modify4.nlargest(10, columns=["vote_average"]))