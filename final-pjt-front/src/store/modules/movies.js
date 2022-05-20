import axios from 'axios'
import drf from '@/api/drf'
import router from '@/router'

import _ from 'lodash'

export default {
  state: {
    moveies: [],
    movie: []
  },
  getters: {
    movies: state => state.movies,
    movie: state => state.movie,
    // isAuthor: (state, getters) => {
    //   return state.movie.user?.username === getters.currentUser.username
    // },
    // isArticle: state => !_.isEmpty(state.article),
  },
  mutations: {
    SET_MOVIES: (state, movies) => state.movies = movies,
    SET_MOVIE: (state, movie) => state.movie = movie,
    // SET_ARTICLE_COMMENTS: (state, comments) => (state.article.comments = comments),
  },

  actions: {
    fetchMovies({ commit, getters }) {
      console.log('fetchMovie')
      axios({
        url: drf.movies.movies(),
        method: 'get',
        headers: getters.authHeader,
      })
      console.log('axios응답')
        .then(res => commit('SET_MOVIES', res.data))
        .catch(err => console.error(err.response))
    },
  }
}