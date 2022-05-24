<template>
  <div>
    {{ profile.like_popular_movies }}
    {{ profile.movie_review }}
    <h1>{{ profile.username }}</h1>

    <h2>좋아요 한 영화</h2>
    <ul>
      <li v-for="movie in profile.like_popular_movies" :key="movie.pk">
        <div v-if="movie.poster_path != null">
          <img
            :src="`https://image.tmdb.org/t/p/w300/${movie.poster_path}`"
            alt="사진"
          />
        </div>
        <router-link :to="{ name: 'movie', params: { moviePk: movie.pk } }">
          {{ movie.title }}
        </router-link>
      </li>
    </ul>

    <h2>좋아요 한 배우</h2>
    <ul>
      <li v-for="actor in profile.like_actor" :key="actor.pk">
        <div v-if="actor.profile_path != null">
          <img
            :src="`https://image.tmdb.org/t/p/w300/${actor.profile_path}`"
            alt="사진"
          />
        </div>
        <router-link :to="{ name: 'actor', params: { actorPk: actor.pk } }">
          {{ actor.name }}
        </router-link>
      </li>
    </ul>

    <h2>좋아요 한 감독</h2>
    <ul>
      <li v-for="director in profile.like_director" :key="director.pk">
        <div v-if="director.profile_path != null">
          <img
            :src="`https://image.tmdb.org/t/p/w300/${director.profile_path}`"
            alt="사진"
          />
        </div>
        <router-link
          :to="{ name: 'director', params: { directorPk: director.pk } }"
        >
          {{ director.profile_path }}
          {{ director.name }}
        </router-link>
      </li>
    </ul>

    <h2>작성한 한줄평</h2>
    <ul>
      <li v-for="movie in profile.movie_review" :key="movie.popular_movie">
        <router-link
          :to="{ name: 'movie', params: { moviePk: movie.popular_movie.id } }"
        >
          {{ movie.popular_movie.title }}
        </router-link>
        - {{ movie.title }}
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