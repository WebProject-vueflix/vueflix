<template>
  <div>
    <h1>Home</h1>
    <!-- {{ movies }} -->
    <ul>
      <li v-for="movie in movies" :key="movie.id">
        <router-link :to="{ name: 'movie', params: { moviePk: movie.id } }">
          {{ movie.title }}
        </router-link>
        ({{ movie.like_count }})
      </li>
    </ul>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";

export default {
  name: "MovieList",
  computed: {
    ...mapGetters(["movies"]),
  },
  methods: {
    ...mapActions(["fetchMovies"]),
  },
  created() {
    this.fetchMovies();
  },
};
</script>

<style></style>
