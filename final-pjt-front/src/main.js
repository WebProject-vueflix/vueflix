import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

// import VueCookies from 'vue-cookies'
// import VueCompositionApi from '@vue/composition-api';

// vuetify
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'
Vue.config.productionTip = false

Vue.config.productionTip = false;
// Vue.use(VueCompositionApi);
// Vue.use(VueCookies);
window.Kakao.init('191fff6ed0bb7cb0ef068a491aaa4a00');

Vue.use(Vuetify);

new Vue({
  router,
  store,
  vuetify: new Vuetify(),
  render: h => h(App)
}).$mount('#app')
