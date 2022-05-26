<template>
  <div>
    <!-- {{genre}} -->
    <!-- {{genre.popular_movies}} -->
    <h1><b>{{ genre.name }}</b></h1>
    <div class="justify-content-center">
      <span class="mx-3">unlike : {{ unlikeGen }}</span>
      <button class="btn btn-outline-danger" @click="unlikeGenre(genrePk)">싫어요</button>
      <router-link :to="{ name: 'profile', params: { username: currentUser.username } }">
        <button class="btn btn-outline-secondary mx-2">
          뒤로가기
        </button>
      </router-link>
    </div>
    <hr />
    <div class="container mb-5">
      <div class="d-flex justify-content-center row row row-cols-2 row-cols-sm-3 row-cols-md-4 row-cols-lg-6 g-0">
        <div
          class="card text-white bg-dark mb-3"
          style="width: 18rem"
          v-for="movie in genre.popular_movies" 
          :key="movie.id"
        >
          <div>
            <router-link :to="{ name: 'movie', params: { moviePk: movie.id } }">
              <img
                :src="`https://image.tmdb.org/t/p/original/${movie.poster_path}`"
                alt="사진"
                class="card-img-top mt-2"
                style="height: 380px"
              />
            </router-link>
            <p class="mt-3">
              {{ movie.title }}
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
// import MovieReviewForm from "@/components/MovieReviewForm.vue";
// import MovieActorList from "@/components/Movie/MovieActorList.vue";

export default {
  name: "GenreDetail",
  // components: { MovieActorList },
  data() {
    return {
      genrePk: this.$route.params.genrePk,
    };
  },
  computed: {
    ...mapGetters(["genre", "currentUser"]),
    unlikeGen() {
      if (this.genre.hate_users[0]){
        return 'O'
      }
      else{
        return 'X'
      }
    },
  },
  methods: {
    ...mapActions(["fetchGenre", "unlikeGenre"]),
  },
  created() {
    this.fetchGenre(this.genrePk);
    console.log("ok");
  },
};
</script>

<style>
</style>