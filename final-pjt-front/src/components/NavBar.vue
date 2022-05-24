<template>
  <nav class="navbar sticky-top justify-content-end navbar-expand-lg navbar-light mb-4">    
    <div class="container-fluid">
      <img src="https://cdn.iconscout.com/icon/free/png-256/vue-282497.png" alt="Vueflix" width=35px>
        <div class="d-flex">
          <ul class="nav">
            <li class="nav-item">
              <div class="nav-link active">
                <router-link :to="{ name: 'movies' }">🏠Home</router-link>
              </div>
            </li>
            <li class="nav-item" v-if="!isLoggedIn">
              <div class="nav-link active">
                <router-link :to="{ name: 'login' }">🔓Login</router-link>
              </div>
            </li>
            <li class="nav-item" v-if="!isLoggedIn">
              <div class="nav-link active">
                <router-link :to="{ name: 'signup' }">🐥Signup</router-link>
              </div>
            </li>
            <li class="nav-item" v-if="isLoggedIn">
              <div class="nav-link active">
                <router-link :to="{ name: 'profile', params: { username } }">
                  👻{{ currentUser.username }}'s page
                </router-link>
              </div>
            </li>
            <li class="nav-item" v-if="isLoggedIn">
              <div class="nav-link active">
                <router-link :to="{ name: 'community' }">
                  👪🏻Community
                </router-link>
              </div>
            </li>
            <li class="nav-item" v-if="isLoggedIn">
              <div class="nav-link active">
                <router-link :to="{ name: 'logout' }">🔒Logout</router-link>
              </div>
            </li>
          </ul>
        </div>
    </div>
  </nav>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "NavBar",
  computed: {
    ...mapGetters(["isLoggedIn", "currentUser"]),
    username() {
      return this.currentUser.username ? this.currentUser.username : "guest";
    },
  },
};
</script>

<style>
nav {
  text-align: center;
  padding: 20px;
  z-index: 99;
  background-color: black;
  color: white;
  /* padding: 30px;
  background-color: #ccddff; */
}

nav a {
  /* font-weight: bold;
  color: #ccddff; */
  font-weight: bold;
  color: #2c3e50;
  text-decoration: none
}

nav a.router-link-exact-active {
  /* color: #141434; */
  color: #ffffff;
}
</style>
