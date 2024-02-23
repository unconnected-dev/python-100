import pandas

movies_data = {
   'movie_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
   'title': ['The Shawshank Redemption', 'The Godfather', 'The Dark Knight', 'Pulp Fiction', 'Forrest Gump', 'Inception', 'The Matrix', 'Schindler\'s List', 'The Lord of the Rings: The Return of the King', 'Fight Club'],
   'genre': ['Drama', 'Crime', 'Action', 'Crime', 'Drama', 'Sci-Fi', 'Action', 'Biography', 'Adventure', 'Drama'],
   'year': [1994, 1972, 2008, 1994, 1994, 2010, 1999, 1993, 2003, 1999]
}

movies_data_frame = pandas.DataFrame(movies_data)

users_data = {
   'user_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
   'username': ['user1', 'user2', 'user3', 'user4', 'user5', 'user6', 'user7', 'user8', 'user9', 'user10']
}

users_data_frame = pandas.DataFrame(users_data)

ratings_data = {
   'user_id':  [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9],
   'movie_id': [1, 2, 1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10],
   'rating':   [5, 4, 4, 5, 4, 3, 5, 4, 5, 4, 3, 4, 5, 4, 3, 5, 4, 5]
}
ratings_data_frame = pandas.DataFrame(ratings_data)


#Find all movies released in the year 1994
if False:
    print(f"{movies_data_frame.loc[movies_data_frame['year'] == 1994, 'title']}")

#List all users who have given ratings
if False:
    rated_users = users_data_frame.loc[users_data_frame['user_id'].isin(ratings_data_frame['user_id']), ['username']]
    print(f"{rated_users}")

#Get the titles of all movies rated by user with id 3
if False:
    rated_movies_ids = ratings_data_frame.loc[(ratings_data_frame['user_id'] == 3),'movie_id']
    print(f"{movies_data_frame.loc[movies_data_frame['movie_id'].isin(rated_movies_ids),'title']}")

#Find the average rating given to the movie The Godfather
if False:
    godfather_ratings = ratings_data_frame[ratings_data_frame['movie_id'] == movies_data_frame[movies_data_frame['title'] == 'The Godfather']['movie_id'].values[0]]
    average_rating = godfather_ratings['rating'].mean()
    print(f"{average_rating}")
   
#List all the users who have no given ratings yet
if False:
    users_without_ratings = users_data_frame.loc[~users_data_frame['user_id'].isin(ratings_data_frame['user_id']), ['username']]
    print(f"{users_without_ratings}")
   
#Get the genre of the movie with the highest rating
if False:
    max_rated_movie_id = ratings_data_frame.groupby('movie_id')['rating'].mean().idxmax()
    genre_of_movie = movies_data_frame.loc[(movies_data_frame['movie_id'] == max_rated_movie_id), ['genre']]
    print(f"{genre_of_movie}")

#Find the username of the user who gave the lowest rating overall
if False:
    user_with_min_rating = ratings_data_frame.groupby('user_id')['rating'].mean().idxmin()
    username = users_data_frame.loc[(users_data_frame['user_id'] == user_with_min_rating),['username']]
    print(f"{username}")

#List all the movies with the genre Action released after 2000
if False:
    print(f"{movies_data_frame.loc[(movies_data_frame['year'] > 2000) & (movies_data_frame['genre'] == 'Action'), ['title']]}")
   
#Count the number of ratings given by each user
if False:
    user_ratings_counts = ratings_data_frame['user_id'].value_counts().reset_index()
    user_ratings_counts.columns = ['user_id', 'ratings_count']
    print(f"{user_ratings_counts}")

#Find the movie title with the highest average rating
if False:
    highest_average_rating = ratings_data_frame.groupby('movie_id')['rating'].mean().idxmax()
    movie_title = movies_data_frame.loc[movies_data_frame['movie_id'] == highest_average_rating,['title']]
    print(f"{movie_title}")