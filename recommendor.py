import pandas as pd
import numpy as np

def recommendor(userLikes,year,n):
    #Importing the movies database
    #movies_df=pd.read_csv('movies.csv')

    #Removing the year from title and inserting as a seperate column
    movies_df['year']=movies_df.title.str.extract('(\(\d\d\d\d\))',expand=False)
    movies_df['year']=movies_df.year.str.extract('(\d\d\d\d)',expand=False)
    movies_df['title']=movies_df.title.str.replace('(\(\d\d\d\d\))','')
    movies_df['title']=movies_df['title'].apply(lambda x:x.strip())

    #Splitting the genres into a list
    movies_df['genres']=movies_df['genres'].str.split('|')

    #Applying One Hot Encoding and changing the genres into numerical values
    movies=movies_df.copy()
    for index,row in movies_df.iterrows():
        for genre in row['genres']:
            movies.at[index,genre]=1

    #Filling the columns with value nan to 0
    movies=movies.fillna(0)

    #Getting user ratings
    #Any number of entries can be given here
    userInput=userLikes
    inputMovies=pd.DataFrame(userInput)

    #Getting movieId from movies database
    inputId=movies_df[movies_df['title'].isin(inputMovies['title']).tolist()]
    inputMovies=pd.merge(inputId,inputMovies)

    inputMovies=inputMovies.drop('genres',1).drop('year',1)

    #Creating a user watched movie table
    userMovies=movies[movies['movieId'].isin(inputMovies['movieId'].tolist())]

    userMovies=userMovies.reset_index(drop=True)
    userGenres=userMovies.drop('movieId',1).drop('title',1).drop('genres',1).drop('year',1)

    #Creating a user profile
    userProfile=userGenres.transpose().dot(inputMovies['rating'])

    genreTable=movies.set_index(movies['movieId'])

    genreTable=genreTable.drop('movieId',1).drop('title',1).drop('genres',1).drop('year',1)

    #Creating the recommendation matrix by multiplying the genre matrix with the user profile matrix and summing and normalizing the result
    recommendTable=((genreTable*userProfile).sum(axis=1))/userProfile.sum()

    #The recommendation matrix is created with the recommendations for each film in the range [0,1]
    recommendTable=recommendTable.sort_values(ascending=False)

    #Using the movieId from the recommendation matrix extract the names of the top n recommendations from the movies database
    result=movies_df.loc[movies_df['movieId'].isin(recommendTable.head(n).keys())]
    result=result[result['year']>year]
    result=result.drop(['movieId'],axis=1)
    result=result.reset_index(drop=True)
    result.index+=1
    return result
