<template>
  <div>
    <p>{{ movie }}</p>
    <p>{{ movie.review_set }}</p>
    <h1>{{ movie.title }}</h1>
    <img
      :src="`https://image.tmdb.org/t/p/w300/${movie.poster_path}`"
      alt="사진"
    />
    <!-- <p>{{movie}}</p> -->
    <p>평점 : {{ movie.vote_average }}</p>
    <p>배우 :</p>
    <div v-for="actor in movie.actors" :key="actor.id">
      <p>{{ actor.name }}({{ actor.character }} 역)</p>
      <!-- <p>{{ actor }}</p> -->
      <!-- <img :src="`https://image.tmdb.org/t/p/w300/${actor.profile_path}`" alt="사진"> -->
    </div>
    <p>감독 : {{ movie.director[0].name }}</p>
    <img
      :src="`https://image.tmdb.org/t/p/w300/${movie.director[0].profile_path}`"
      alt="사진"
    />
    <p>개봉일 : {{ movie.release_date }}</p>
    <!-- 영화예매 바로가기 하이퍼링크 -->
    <iframe
      :src="`https://www.youtube.com/embed/${movie.youtube_key}`"
    ></iframe>
    <!-- 공유하기 -->
    <hr />
    <div v-for="actor in movie.actors" :key="actor.name">
      <p>{{ actor.name }}의 이 영화는 어때요?</p>
      <!-- <p>{{ actor }}</p> -->
      <movie-actor-list :actor="actor"></movie-actor-list>
    </div>

    <hr />
    <br />
    <br />
    <br />
    <hr />
    <movie-review-form> </movie-review-form>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import MovieReviewForm from "@/components/Movie/MovieReviewForm.vue";
import MovieActorList from "@/components/Movie/MovieActorList.vue";

export default {
  name: "MovieDetail",
  components: { MovieReviewForm, MovieActorList },
  data() {
    return {
      moviePk: this.$route.params.moviePk,
    };
  },
  computed: {
    ...mapGetters(["movie"]),
  },
  methods: {
    ...mapActions(["fetchMovie"]),
  },
  mounted() {
    this.fetchMovie(this.moviePk);
    console.log("mounted");
  },
};
</script>

<style>
</style>