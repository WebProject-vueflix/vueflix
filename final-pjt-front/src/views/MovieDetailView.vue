<template>
  <div>
    <h1>{{ movie.title }}</h1>
    <img :src="`https://image.tmdb.org/t/p/w300/${movie.poster_path}`" alt="사진">
    <!-- <p>{{movie}}</p> -->
    <p>평점 : {{ movie.vote_average }}</p>
    <p>
      배우 :
    </p>
    <div v-for="actor in movie.actors" :key="actor.id">
      <p>{{ actor.name }}({{ actor.character }} 역)</p>
      <!-- <img :src="`https://image.tmdb.org/t/p/w300/${actor.profile_path}`" alt="사진"> -->
    </div>
    <p>감독 : {{ movie.director[0].name }}</p>
    <img :src="`https://image.tmdb.org/t/p/w300/${movie.director[0].profile_path}`" alt="사진">
    <p>개봉일 : {{ movie.release_date }}</p>
    <!-- 영화예매 바로가기 하이퍼링크 -->
    <iframe :src="`https://www.youtube.com/embed/${movie.youtube_key}`"></iframe>
    <!-- 공유하기 -->
    <hr>
    <div v-for="actor in movie.actors" :key="actor.id">
      <p>{{ actor.name }}의 이 영화는 어때요?</p>
    </div>
  </div>
</template>

<script>
  import { mapGetters, mapActions } from 'vuex'
  export default {
    name: 'MovieDetail',
    data(){
      return {
        moviePk: this.$route.params.moviePk,
      }
    },
    computed: {
      ...mapGetters(['movie'])
    },
    methods: {
      ...mapActions([
        'fetchMovie',
    ])
  },
  created() {
    this.fetchMovie(this.moviePk)
  },
}
</script>

<style>

</style>