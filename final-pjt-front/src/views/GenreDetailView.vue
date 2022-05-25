<template>
  <div>
    <!-- {{genre}} -->
    <!-- {{genre.popular_movies}} -->
    <h1>{{ genre.name }}</h1>
    <div>
      unlike : {{ unlikeGen }}
      <button @click="unlikeGenre(genrePk)">싫어요</button>
    </div>
    <br />
    <!-- <img
      :src="`https://image.tmdb.org/t/p/w300/${actor.profile_path}`"
      alt="사진"
    /> -->
    <hr />
    <!-- <h2>{{ movie.name }}의 이 영화는 어때요?</h2> -->
    <div v-for="movie in genre.popular_movies" :key="movie.id">
      <router-link :to="{ name: 'movie', params: { moviePk: movie.id } }">
        <img
          :src="`https://image.tmdb.org/t/p/w300/${movie.poster_path}`"
          alt="사진"
        />
      </router-link>
      {{ movie.title }}
      <!-- <router-link :to="{ name: 'genre', params: { genrePk: genre.id } }">
          <button>상세보기</button>
        </router-link>  -->
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
    ...mapGetters(["genre"]),
    unlikeGen() {
      return this.genre.hate_users?.name;
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