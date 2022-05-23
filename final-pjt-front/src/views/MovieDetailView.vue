<template>
  <div>
    <p>{{ movie }}</p>
    <!-- <p>{{ movie.review_set }}</p> -->
    <h1>{{ movie.title }}</h1>
    <img
      :src="`https://image.tmdb.org/t/p/w300/${movie.poster_path}`"
      alt="사진"
    />
    <div>
      Likeit:
      <button @click="likeMovie(moviePk)">{{ likeCount }}</button>
    </div>
    <!-- <p>{{movie}}</p> -->
    <p>평점 : {{ movie.vote_average }}</p>
    <p>배우 :</p>
    <div v-for="actor in movie.actors" :key="actor.id">
      <img
        :src="`https://image.tmdb.org/t/p/w300/${actor.profile_path}`"
        alt="사진"
      />
      <router-link :to="{ name: 'actor', params: { actorPk: actor.id } }">
        <p>{{ actor.name }}({{ actor.character }} 역)</p>
      </router-link>
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
    <div v-for="movieactor in movie.actors" :key="movieactor.id">
      <p>{{ movieactor.name }}의 이 영화는 어때요?</p>
      <div v-for="newmovie in movieactor.popular_movies" :key="newmovie.id">
        <router-link :to="{ name: 'movie', params: { moviePk: newmovie.id } }">
          <img
            :src="`https://image.tmdb.org/t/p/w300/${newmovie.poster_path}`"
            alt="사진"
          />
        </router-link>
        <p>{{ newmovie.title }}</p>
      </div>
    </div>
    <div v-for="review in movie.review_set" :key="review.id">
      {{ sum_rank }} : {{ review.rank }}
    </div>
    <hr />
    <!-- <h2>한줄평</h2>
    <div v-for="review in movie.review_set" :key="review.id">
      <b>제목: {{ review.title }}</b>
      <p>내용: {{ review.content }}</p>
      <p>평점: {{ review.rank }}</p>
      <p>작성자: {{ review.user.username }}</p>
      <br>
    </div> -->
    <h2>한줄평 ({{ movie.review_set.length }})명</h2>
    <movie-review-list :review_set="movie.review_set"></movie-review-list>
    <!-- <movie-review-form> </movie-review-form> -->
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import MovieReviewList from "@/components/MovieReviewList.vue";
// import MovieReviewForm from "@/components/MovieReviewForm.vue";
// import MovieActorList from "@/components/Movie/MovieActorList.vue";
// let sum_rank = 0;
export default {
  name: "MovieDetail",
  components: { MovieReviewList },
  data() {
    return {
      moviePk: this.$route.params.moviePk,
    };
  },
  computed: {
    ...mapGetters(["movie", "actor"]),
    likeCount() {
      return this.movie.like_users?.length;
    },
  },
  methods: {
    ...mapActions(["fetchMovie", "likeMovie"]),
  },
  created() {
    this.fetchMovie(this.moviePk);
    console.log("ok");
  },
};
</script>

<style>
</style>