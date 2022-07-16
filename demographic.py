import pandas as pd
import numpy as np

df = pd.read_csv("final.csv")

C = df["vote_average"].mean()
m = df["vote_count"].quantile(0.9)
q_movies = df.copy().loc[df["vote_count"]>=m]

def weightedrating(x, m = m, C = C):
    v = x["vote_count"]
    R = x["vote_average"]
    return (v/(v+m) * R) + (m/(v+m) * C)

q_movies["score"] = q_movies.apply(weightedrating, axis = 1)
output = q_movies[["title_x", "vote_count", "vote_average", "poster_link"]].head(20).values.tolist()