<template>
  <div>
    <h1>Home</h1>
    <ul>
      <li v-for="movie in movies" :key="movie.pk">
        <!-- 작성자
        {{ article.user.username }} :  -->
        {{ movie.title }}
        <!-- 글 이동 링크 (제목) -->
        <!-- <router-link :to="{ name: 'movies', params: { moviePk: movie.pk } }">
          {{ movie.title }}
        </router-link> -->
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
