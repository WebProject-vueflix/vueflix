import axios from 'axios'
import drf from '@/api/drf'
import router from '@/router'

import _ from 'lodash'

export default {
  state: {
    community: [],
    review: {},
  },
  getters: {
    community: state => state.community,
    review: state => state.review,
    isAuthor: (state, getters) => {
      return state.review.user?.username === getters.currentUser.username
    },
    isReview: state => !_.isEmpty(state.review),
  },
  mutations: {
    SET_COMMUNITY: (state, community) => state.community = community,
    SET_REVIEW: (state, review) => state.review = review,
    SET_REVIEW_COMMENTS: (state, community_review) => (state.review.community_review = community_review),
    SET_REVIEW_COMMENT: (state, comment) => (state.review.comment = comment),
  },

  actions: {
    fetchCommunity({ commit, getters }) {
      axios({
        url: drf.community.community(),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_COMMUNITY', res.data, console.log(res.data)))
        .catch(err => console.error(err.response, "힝"),)
    },
    fetchReview({ commit, getters }, reviewPk) {
      axios({
        url: drf.community.review(reviewPk),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_REVIEW', res.data))
        .catch(err => {
          console.error(err.response)
          if (err.response.status === 404) {
            router.push({ name: 'NotFound404' }),
              console.log("g힝")
          }
        })
    },
    createReview({ commit, getters }, review) {
      axios({
        url: drf.community.community(),
        method: 'post',
        data: review,
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_REVIEW', res.data)
          router.push({
            name: 'review',
            params: { reviewPk: getters.review.pk }
          })
        })
    },
    updateReview({ commit, getters }, { pk, title, content }) {
      axios({
        url: drf.community.review(pk),
        method: 'put',
        data: { title, content },
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_REVIEW', res.data)
          router.push({
            name: 'review',
            params: { reviewPk: getters.review.pk }
          })
        })
    },

    deleteReview({ commit, getters }, reviewPk) {
      if (confirm('정말 삭제하시겠습니까?')) {
        axios({
          url: drf.community.review(reviewPk),
          method: 'delete',
          headers: getters.authHeader,
        })
          .then(() => {
            commit('SET_REVIEW', {})
            // console.log('sdfjdsklfjsdlf')
            router.push({ name: 'community' })
          })
          .catch(err => console.error(err.response))
      }
    },
    // fetchComments({ commit, getters }, reviewPk) {
    //   axios({
    //     url: drf.community.comments(reviewPk),
    //     method: 'get',
    //     headers: getters.authHeader,
    //   })
    //     .then(res => commit('SET_REVIEW_COMMENTS', res.data))
    //     .catch(err => console.error(err.response))
    // },
    createComment({ commit, getters }, { reviewPk, content }) {
      const comment = { content }
      axios({
        url: drf.community.comments(reviewPk),
        method: 'post',
        data: comment,
        headers: getters.authHeader,
      })
        .then(res => {
          console.log(res.data)
          commit('SET_REVIEW_COMMENTS', res.data)
        })
        .catch(err => console.log(err, "힝"))
    },
    updateComment({ commit, getters }, { reviewPk, commentPk, content }) {
      const comment = { content }
      axios({
        url: drf.community.comment(reviewPk, commentPk),
        method: 'put',
        data: comment,
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_REVIEW_COMMENT', res.data)
        })
        .catch(err => console.error(err.response))
    },
    deleteComment({ commit, getters }, { reviewPk, commentPk }) {
      if (confirm('정말 삭제하시겠습니까?')) {
        axios({
          url: drf.community.comment(reviewPk, commentPk),
          method: 'delete',
          data: {},
          headers: getters.authHeader,
        })
          .then(res => {
            // console.log(res)
            commit('SET_REVIEW_COMMENTS', res.data)
            // router.push({ name: 'review' })
          })
          .catch(err => console.error(err.response))
      }
    },
  }
}