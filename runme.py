import pandas as pd
import streamlit as st
from ricebowl.processing import data_preproc
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import sigmoid_kernel


def filtering_data():
    movies = pd.read_csv('./movie_kaggle/movies.csv')
    credits = pd.read_csv('./movie_kaggle/credits.csv')
    movies = data_preproc.reformat_col_headers(movies)
    credits = data_preproc.reformat_col_headers(credits)
    final = pd.merge(movies, credits, left_on='id', right_on='movie_id')
    final['overview'] = final['overview'].fillna('')
    return final


def find_movies(title):
    data = filtering_data()
    # analyzer(word) - To analyze on words.
    # min_df(3) - To make sure words less than 3 character are removed. helps us remove suggestions like Superman 2.
    # stop_words(english) - To remove stopwords from being analysed.
    # strip_accents(unicode) - To match all kinds of french, spanish, tildes and other accents. Unicode is slower but manages everything.
    tfv = TfidfVectorizer(min_df=3, strip_accents='unicode',
                          stop_words='english', analyzer='word')
    tfv_mat = tfv.fit_transform(data['overview'])
    # Calculate cosine simiarity using sigmoid kernel for values to be between 0-1
    sig = sigmoid_kernel(tfv_mat, tfv_mat)
    indices = pd.Series(data.index, index=data['original_title']).drop_duplicates()
    idx = indices[title]
    score = list(enumerate(sig[idx]))
    score = sorted(score, key=lambda x: x[1], reverse=True)
    score = score[1:11]
    movie_indices = [i[0] for i in score]
    return data[['original_title', 'overview', 'vote_average', 'vote_count']].iloc[movie_indices].reset_index().drop(
        columns='index')


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)


def icon(icon_name):
    st.markdown(f'<i class="material-icons">{icon_name}</i>', unsafe_allow_html=True)


def check_closeness(movie):
    movie = movie.title()
    data = filtering_data()
    values = list(data['original_title'].unique())
    if '-' in movie:
        movie = movie.replace('-', ' ')
    if ' ' in movie:
        movie_words = movie.split(' ')
    else:
        movie_words = [movie]
    alternate_movies = []
    for i in values:
        for j in movie_words:
            if j != 'The' and j != 'A' and j in i:
                alternate_movies = alternate_movies + [i]
                break
        if len(alternate_movies) >= 5:
            break
    return alternate_movies


def main():
    data = filtering_data()
    values = list(data['original_title'].unique())
    st.title("Movie Recommender")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">We Recommend You Movies... </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    local_css("./style.css")
    remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')

    icon("search")
    movie = st.text_input("", "Search...")
    status = st.button("OK")
    # movie = st.selectbox('', values)

    movie = movie.title()
    if movie == 'Search...':
        return
    if movie not in values:
        st.success('Movie not found. Please check the spellings once.')
        alternate_movies = check_closeness(movie)
        if len(alternate_movies) > 0:
            st.success('Do you mean?:')
            for i in alternate_movies:
                st.success(i)
        return
    all_movies = find_movies(movie)

    for i in range(all_movies.shape[0]):
        s = "<div><span class='highlight red'><span class='bold'>{} - <span class='highlight blue'><span class='bold'>{} ({} votes)</span></span></span></span></div>".format(
            all_movies['original_title'].values[i], all_movies['vote_average'].values[i],
            all_movies['vote_count'].values[i])
        st.markdown(s, unsafe_allow_html=True)
        st.success("{}".format(all_movies['overview'].values[i]))
        # st.success(all_movies)


if __name__ == '__main__':
    # movies = find_movies('X-Men')
    # print(movies)
    main()
