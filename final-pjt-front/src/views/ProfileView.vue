<template>
  <div>
    <h1>{{ profile.username }}</h1>

    <h2>좋아요 한 글</h2>
    <ul>
      <li v-for="movie in profile.like_popular_movies" :key="movie.pk">
        <router-link :to="{ name: 'movie', params: { moviePk: movie.pk } }">
          {{ movie.title }}
        </router-link>
      </li>
    </ul>

    <h2>작성한 한줄평</h2>
    <ul>
      <li v-for="movie in profile.movie_review" :key="movie.popular_movie">
        <router-link
          :to="{ name: 'movie', params: { moviePk: movie.popular_movie } }"
        >
          {{ movie.title }}
        </router-link>
      </li>
    </ul>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";

export default {
  name: "ProfileView",
  computed: {
    ...mapGetters(["profile"]),
  },
  methods: {
    ...mapActions(["fetchProfile"]),
  },
  created() {
    const payload = { username: this.$route.params.username };
    this.fetchProfile(payload);
  },
};
</script>

<style>
</style>