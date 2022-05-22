<template>
  <div>
    <!-- <p>{{ movie.review_set }}</p> -->
    <h1>{{ actor.name }}</h1>
    <img :src="`https://image.tmdb.org/t/p/w300/${actor.profile_path}`" alt="사진">
    <hr>
    <h2>{{ actor.name }}의 이 영화는 어때요?</h2>
    <div v-for="movie in actor.popular_movies" :key="movie.id">
      <router-link :to="{ name: 'movie', params: { moviePk: movie.id } }">
        <img :src="`https://image.tmdb.org/t/p/w300/${movie.poster_path}`" alt="사진">
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
  name: "ActorDetail",
  // components: { MovieActorList },
  data() {
    return {
      actorPk: this.$route.params.actorPk,
    };
  },
  computed: {
    ...mapGetters(["actor"]),
  },
  methods: {
    ...mapActions(["fetchActor"]),
  },
  created() {
    this.fetchActor(this.actorPk);
    console.log("ok");
  },
};
</script>

<style>
</style>