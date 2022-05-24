<template>
  <div id="app">
    <nav-bar></nav-bar>
    <div class="container">
      <router-view />
    </div>
    <footer class="relative-bottom d-flex flex-column justify-content-center 
      align-items-center py-2 mt-5">
      <span>@Vueflix Movie Final PJT</span>
      <span>대표 : <strong>seunghyo & aeri</strong></span>
    </footer>
  </div>
</template>

<script>
  import NavBar from '@/components/NavBar.vue'

  import { mapActions } from 'vuex'

  export default {
    name: 'App',
    components: { NavBar },
    methods: {
      ...mapActions(['fetchCurrentUser'])
    },
    created() {
      this.fetchCurrentUser()
    }
  }
</script>

<style>
/* #app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
} */
#app {
  background-color: rgb(20, 20, 20);
  /* font-family: Avenir, Helvetica, Arial, sans-serif; */
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; */
  /* color: #ffffff; */
  min-height: 100vh;
}

footer {
  /* background-color: #ccddff; */
  background-color: rgb(20, 20, 20);
}
</style>
