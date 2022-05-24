import Vue from 'vue'
import Vuex from 'vuex'

// import articles from './modules/articles'
import accounts from './modules/accounts'
import movies from './modules/movies'
import community from './modules/community'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    loading: true,
  },
  mutations: {
    SET_LOADING(state, data){
      state.loading = data;
    },
  },
  modules: { accounts, movies, community,},
})
