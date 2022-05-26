<template>
  <div>
    <!-- <p>{{ movie.review_set }}</p> -->
    <h1><b>{{ director.name }}</b></h1>
    <div>
      <span class="justify-content-center px-3">Likeit : {{ likeDir }}</span>
      <button class="btn btn-outline-primary" @click="likeDirector(directorPk)">좋아요</button>
    </div>
    <hr />
    <div class="container">
      <h2 class="mb-4">{{ director.name }} 감독님의 이 영화는 어때요?</h2>
      <div class="d-flex justify-content-center row row row-cols-2 row-cols-sm-3 row-cols-md-4 row-cols-lg-6 g-0">
        <br>
        <div
          class="card text-white bg-dark mb-3"
          style="width: 18rem"
          v-for="movie in director.popular_movies" 
          :key="movie.id"
        >
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
</template>

<script>
import { mapGetters, mapActions } from "vuex";
// import MovieReviewForm from "@/components/MovieReviewForm.vue";
// import MovieActorList from "@/components/Movie/MovieActorList.vue";

export default {
  name: "DirectorDetail",
  // components: { MovieActorList },
  data() {
    return {
      directorPk: this.$route.params.directorPk,
    };
  },
  computed: {
    ...mapGetters(["director"]),
    likeDir() {
      return this.director.like_users?.length;
    },
  },
  methods: {
    ...mapActions(["fetchDirector", "likeDirector"]),
  },
  created() {
    this.fetchDirector(this.directorPk);
    console.log("ok");
  },
};
</script>

<style>
</style>