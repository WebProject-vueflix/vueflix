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
  },
  getters: {
    movies: state => state.movies,
    movie: state => state.movie,
    // isAuthor: (state, getters) => {
    //   return state.movie.user?.username === getters.currentUser.username
    // },
    actors: state => state.actors,
    actor: state => state.actor,
    isMovieReview: state => !_.isEmpty(state.review),
  },
  mutations: {
    SET_MOVIES: (state, movies) => state.movies = movies,
    SET_MOVIE: (state, movie) => state.movie = movie,
    // SET_NEW_MOVIE: (state, newmovie) => state.movie = newmovie,
    SET_MOVIE_REVIEWS: (state, review_set) => (state.movie.review_set = review_set),
    SET_MOVIE_REVIEW: (state, comment) => (state.review.comment = comment),
    SET_ACTORS: (state, actors) => state.actors = actors,
    SET_ACTOR: (state, actor) => state.actor = actor,
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
    // fetchNewMovie({ commit, getters }, moviePk) {
    //   axios({
    //     url: drf.movies.movie(moviePk),
    //     method: 'get',
    //     headers: getters.authHeader,
    //   })
    //     .then(res => {
    //       commit('SET_NEW_MOVIE', res.data)
    //       console.log(res.data)
    //     }
    //     )
    //     .catch(err => {
    //       console.error(err.response)
    //       if (err.response.status === 404) {
    //         router.push({ name: 'NotFound404' })
    //       }
    //     })
    // },
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