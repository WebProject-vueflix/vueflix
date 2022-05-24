<template>
  <div>
    <!-- {{ director }} -->
    <!-- <p>{{ movie.review_set }}</p> -->
    <h1>{{ director.name }}</h1>
    <div v-if="director.profile_path != null">
      <img
        :src="`https://image.tmdb.org/t/p/w300/${director.profile_path}`"
        alt="사진"
      />
    </div>
    <div>
      Likeit:{{ likeDir }}
      <button @click="likeDirector(directorPk)">좋아요</button>
    </div>
    <hr />
    <br />
    <h2>{{ director.name }} 감독님의 이 영화는 어때요?</h2>
    <br>
    <div v-for="movie in director.popular_movies" :key="movie.id">
      <router-link :to="{ name: 'movie', params: { moviePk: movie.id } }">
        <img
          :src="`https://image.tmdb.org/t/p/w300/${movie.poster_path}`"
          alt="사진"
        />
        {{ movie.title }}
      </router-link>
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