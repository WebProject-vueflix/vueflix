import axios from 'axios'
import drf from '@/api/drf'
// import router from '@/router'

// import _ from 'lodash'

export default {
  state: {
    community: [],
    review: {},
  },
  getters: {
    community: state => state.community,
    review: state => state.review,
  },
  mutations: {
    SET_COMMUNITY: (state, community) => state.community = community,
    SET_REVIEW: (state, review) => state.review = review,
  },

  actions: {
    fetchCommunity({ commit, getters }) {
      axios({
        url: drf.community.community(),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_COMMUNITY', res.data))
        .catch(err => console.error(err.response))
    },
  }
}