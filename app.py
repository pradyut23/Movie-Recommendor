import streamlit as st
from recommendor import recommendor

st.set_option("deprecation.showfileUploaderEncoding", False)
st.markdown('<style>body{background-image: url("https://i.redd.it/4fxxbm4opjd31.jpg"); background-repeat: no-repeat; background-attachment: fixed; background-size: 100% 100%;} body::before{content: ""; position: absolute; top: 0px; right: 0px; bottom: 0px; left: 0px; background-color: rgba(1,1,1,0.95);}</style>',unsafe_allow_html=True)
st.markdown('<style>body{color: #B3B6B7 ; text-align: center;}</style>',unsafe_allow_html=True)

st.title("MOVIE RECOMMENDOR")
st.write("")
st.subheader("Content Based Recommendor System")
st.write("The system recommends movies on the basis of your likeness of a particular genre")
st.write("")
st.write("")
st.write("")

st.sidebar.header("Enter movie name and rating")
st.sidebar.markdown("")

userLikes=[]
n=1
n=st.sidebar.text_input('How many movies do you want to enter?',value=0)
i=0
while i<int(n):
    movies={}
    movie=st.sidebar.text_input("Movie Title",key=i)
    rating=st.sidebar.slider("Rating",min_value=0.01,max_value=5.01,key=i)
    movies["title"]=movie
    movies["rating"]=rating
    userLikes.append(movies)
    i+=1

st.sidebar.markdown("")
st.sidebar.markdown("")
st.sidebar.markdown("")
st.sidebar.markdown("")
st.sidebar.markdown("")
st.sidebar.markdown("")
year=st.sidebar.text_input("Do you want movies after a specific year, if yes, mention the year?",value=1900)
noOfMovies=st.sidebar.number_input("How many movies do you want?",value=10)

if st.sidebar.button("Done",key=1):
    recommended=recommendor(userLikes,year,noOfMovies)
    st.write(recommended)
