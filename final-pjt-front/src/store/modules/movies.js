import axios from 'axios'
import drf from '@/api/drf'
import router from '@/router'

import _ from 'lodash'

export default {
  state: {
    movies: [],
    movie: {},
    actors: [],
    actor: {},
    director: {},
  },
  getters: {
    movies: state => state.movies,
    movie: state => state.movie,
    actors: state => state.actors,
    actor: state => state.actor,
    director: state => state.director,
    isAuthor: (state, getters) => {
      return state.movie.user?.username === getters.currentUser.username
    },
    isMovieReview: state => !_.isEmpty(state.review),
  },
  mutations: {
    SET_MOVIES: (state, movies) => state.movies = movies,
    SET_MOVIE: (state, movie) => state.movie = movie,
    SET_MOVIE_REVIEWS: (state, review_set) => (state.movie.review_set = review_set),
    SET_MOVIE_REVIEW: (state, comment) => (state.review.comment = comment),
    SET_ACTORS: (state, actors) => state.actors = actors,
    SET_ACTOR: (state, actor) => state.actor = actor,
    SET_DIRECTOR: (state, director) => state.director = director,

  },

  actions: {
    fetchMovies({ commit, getters }) {
      axios({
        url: drf.movies.movies(),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_MOVIES', res.data))
        .catch(err => console.error(err.response))
    },
    fetchMovie({ commit, getters }, moviePk) {
      axios({
        url: drf.movies.movie(moviePk),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_MOVIE', res.data)
          console.log(res.data)
        }
        )
        .catch(err => {
          console.error(err.response)
          if (err.response.status === 404) {
            router.push({ name: 'NotFound404' })
          }
        })
    },

    fetchActors({ commit, getters }) {
      axios({
        url: drf.movies.actors(),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_ACTORS', res.data)
          console.log(res.data)
        })
        .catch(err => {
          console.error(err.response)
          if (err.response.status === 404) {
            router.push({ name: 'NotFound404' })
          }
        })
    },
    fetchActor({ commit, getters }, actorPk) {
      axios({
        url: drf.movies.actor(actorPk),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_ACTOR', res.data)
          console.log(res.data)
        })
        .catch(err => {
          console.error(err.response)
          if (err.response.status === 404) {
            router.push({ name: 'NotFound404' })
          }
        })
    },
    fetchDirector({ commit, getters }, directorPk) {
      axios({
        url: drf.movies.director(directorPk),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_DIRECTOR', res.data)
          console.log(res.data)
        })
        .catch(err => {
          console.error(err.response)
          if (err.response.status === 404) {
            router.push({ name: 'NotFound404' })
          }
        })
    },
    likeMovie({ commit, getters }, moviePk) {
      axios({
        url: drf.movies.likeMovie(moviePk),
        method: 'post',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_MOVIE', res.data), console.log('hi'))
        .catch(err => console.error(err.response))
    },
    likeActor({ commit, getters }, actorPk) {
      axios({
        url: drf.movies.likeactor(actorPk),
        method: 'post',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_ACTOR', res.data), console.log('bye'))
        .catch(err => console.error(err.response))
    },
    likeDirector({ commit, getters }, directorPk) {
      axios({
        url: drf.movies.likedirector(directorPk),
        method: 'post',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_DIRECTOR', res.data), console.log('bye'))
        .catch(err => console.error(err.response))
    },
    createMovieReview({ commit, getters }, { moviePk, title, content, rank }) {
      const movieReview = { title, content, rank }
      console.log(movieReview)
      axios({
        url: drf.movies.reviews(moviePk),
        method: 'post',
        data: movieReview,
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_MOVIE_REVIEWS', res.data)
          console.log(res.data)
          console.log("asdf")
        })
        .catch(err => console.log(err.response, "힝"))
    },


    updateMovieReview({ commit, getters }, { moviePk, reviewPk, title, content, rank }) {
      const movieReview = { title, content, rank }
      // console.log(movieReview)
      axios({
        url: drf.movies.review(moviePk, reviewPk),
        method: 'put',
        data: movieReview,
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_MOVIE_REVIEWS', res.data)
          console.log(res.data)

        })
        .catch(err => console.error(err.response))
    },
    deleteMovieReview({ commit, getters }, { moviePk, reviewPk }) {
      if (confirm('정말 삭제하시겠습니까?')) {
        axios({
          url: drf.movies.review(moviePk, reviewPk),
          method: 'delete',
          data: {},
          headers: getters.authHeader,
        })
          .then(res => {
            commit('SET_MOVIE_REVIEWS', res.data)
            console.log(res)
            // router.push({ name: 'review' })
          })
          .catch(err => console.error(err.response))
      }
    },
  }
}