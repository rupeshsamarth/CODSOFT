import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
movies = pd.read_csv("movies.csv")

# Convert genres into vectors
cv = CountVectorizer()
vectors = cv.fit_transform(movies["genre"])

# Calculate similarity
similarity = cosine_similarity(vectors)


def recommend(movie_name):
    movie_name = movie_name.lower()

    movie_index = None

    for i in range(len(movies)):
        if movies.iloc[i]["title"].lower() == movie_name:
            movie_index = i
            break

    if movie_index is None:
        print("Movie not found!")
        return

    distances = list(enumerate(similarity[movie_index]))

    distances = sorted(distances, key=lambda x: x[1], reverse=True)

    print("\nRecommended Movies:\n")

    count = 0

    for movie in distances:
        if movie[0] != movie_index:
            print("-", movies.iloc[movie[0]]["title"])
            count += 1

        if count == 5:
            break


print("=" * 45)
print("      MOVIE RECOMMENDATION SYSTEM")
print("=" * 45)

print("\nAvailable Movies:\n")

for movie in movies["title"]:
    print("-", movie)

movie = input("\nEnter Movie Name: ")

recommend(movie)