<template>
  <div>
    <!-- {{ profile.like_popular_movies }}
    {{ profile.movie_review }} -->
    <h1><b>{{ profile.username }}'s Page</b></h1>
    <hr>
    <div class="card">
      <div class="card-body">
        <h2 class="mb-4"><b>Don't recommended</b></h2>
        <ul class="list-inline">
          <li class="list-inline-item" v-for="genre in profile.hate_genres" :key="genre.name+'f'">
            <router-link :to="{ name: 'genre', params: { genrePk: genre.id } }">
              <button class="btn btn-sm btn-outline-light">{{genre.name}}</button>
            </router-link>
          </li>
        </ul>
        <router-link :to="{ name: 'genres' }">
          <button class="btn btn-sm btn-outline-secondary">설정 변경</button>
        </router-link>
      </div>
    </div>
    <hr>
    <div class="container mb-5">
      <h2 class="mb-4"><b>좋아요 누른 영화</b></h2>
      <div class="d-flex justify-content-center row row row-cols-3 row-cols-sm-3 row-cols-md-4 row-cols-lg-6 g-0">
        <div
          class="card text-white bg-dark mb-3"
          style="width: 18rem"
          v-for="movie in profile.like_popular_movies" 
          :key="movie.pk+'l'"
        >
          <div v-if="movie.poster_path != null">
            <router-link :to="{ name: 'movie', params: { moviePk: movie.pk } }">
              <img
                :src="`https://image.tmdb.org/t/p/original/${movie.poster_path}`"
                alt="사진"
                class="card-img-top mt-2"
                  style="height: 380px"
              />
            </router-link>
          </div>
            <span class="align-item-center">
              {{ movie.title }}
            </span>
        </div>
      </div>
    </div>
    <div class="container mb-5">
      <h2 class="mb-4"><b>좋아요 누른 배우</b></h2>
      <div class="d-flex justify-content-center row row row-cols-3 row-cols-sm-3 row-cols-md-4 row-cols-lg-6 g-0">
        <div
          class="card text-white bg-dark mb-3"
          style="width: 18rem"
          v-for="actor in profile.like_actor" 
          :key="actor.pk+'r'"
        >
          <div v-if="actor.profile_path != null">
            <router-link :to="{ name: 'actor', params: { actorPk: actor.pk } }">
              <img
                :src="`https://image.tmdb.org/t/p/original/${actor.profile_path}`"
                alt="사진"
                class="card-img-top mt-2"
                  style="height: 380px"
              />
            </router-link>
          </div>
          <span class="align-item-center">
            {{ actor.name }}
          </span>
        </div>
      </div>
    </div>
    <div class="container mb-5">
      <h2 class="mb-4"><b>좋아요 누른 감독</b></h2>
      <div class="d-flex justify-content-center row row row-cols-3 row-cols-sm-3 row-cols-md-4 row-cols-lg-6 g-0">
        <div
          class="card text-white bg-dark mb-3"
          style="width: 18rem"
          v-for="director in profile.like_director" 
          :key="director.pk+'s'"
        >
          <div v-if="director.profile_path != null">
            <router-link :to="{ name: 'director', params: { directorPk: director.pk } }">
              <img
                :src="`https://image.tmdb.org/t/p/original/${director.profile_path}`"
                alt="사진"
                class="card-img-top mt-2"
                  style="height: 380px"
              />
            </router-link>
          </div>
          <span class="align-item-center">
            {{ director.profile_path }}
            {{ director.name }}
          </span>
        </div>
      </div>
    </div>
    <h2><b>작성한 한줄평</b></h2>
    <div class="list-group" v-for="movie in profile.movie_review" :key="movie.title+'a'">
      <router-link :to="{ name: 'movie', params: { moviePk: movie.popular_movie.id } }" 
        class="list-group-item list-group-item-action list-group-item-warning" aria-current="true">
        {{ movie.popular_movie.title }} - {{ movie.title }}
      </router-link>
    </div>
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
div h2{
  color: aliceblue;
}
</style>