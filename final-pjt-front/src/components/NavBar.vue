<template>
  <nav>
    <ul>
      <li>
        <router-link :to="{ name: 'movies' }">Home</router-link>
      </li>
      <li v-if="!isLoggedIn">
        <router-link :to="{ name: 'login' }">Login</router-link>
      </li>
      <li v-if="!isLoggedIn">
        <router-link :to="{ name: 'signup' }">Signup</router-link>
      </li>
      <!-- <li v-if="isLoggedIn">
        <div v-if="is_staff">
          <router-link :to="{ name: 'admin' }">admin</router-link>
        </div>
      </li> -->
      <!-- <li v-if="isLoggedIn">
        <router-link :to="{ name: 'actors' }">actors</router-link>
      </li> -->
      <li v-if="isLoggedIn">
        <router-link :to="{ name: 'profile', params: { username } }">
          {{ currentUser.username }}'s page
        </router-link>
      </li>
      <li v-if="isLoggedIn">
        <router-link :to="{ name: 'community' }">
          Community
        </router-link>
      </li>
      <li v-if="isLoggedIn">
        <router-link :to="{ name: 'logout' }">Logout</router-link>
      </li>
    </ul>
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

<style></style>
