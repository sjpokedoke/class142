import csv

with open("movies.csv") as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]
    headers = data[0]

headers.append("poster_link")

with open("final.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)

with open("movie_link.csv") as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies_link = data[1:]

for movie_item in all_movies:
    poster_found = any(movie_item[8] in movie_link_item for movie_link_item in all_movies_link)
    if poster_found:
        for movie_link_item in all_movies_link:
            if movie_item[8] == movie_link_item[0]:
                movie_item.append(movie_link_item[1])
                if len(movie_item) == 28:
                    with open("final.csv", "a+") as f:
                        csvwriter = csv.writer(f)
                        csvwriter.writerow(movie_item)