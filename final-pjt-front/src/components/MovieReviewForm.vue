<template>
  <form @submit.prevent="onSubmit">
    <!-- <label for="review">한줄평: </label> -->
    <div>
      <label for="title">title:</label>
      <input type="text" id="title" v-model="newMovieReview.title" required />
    </div>
    <div>
      <label for="content">content:</label>
      <input
        type="text"
        id="content"
        v-model="newMovieReview.content"
        required
      />
    </div>
    <div>
      <label for="rank">rank:</label>
      <!-- <input type="selectbox" id="rank" v-model="newMovieReview.rank" required /> -->
      <select v-model="newMovieReview.rank">
        <option disabled value="">평점을 선택하세요</option>
        <option value="1">⭐</option>
        <option value="2">⭐⭐</option>
        <option value="3">⭐⭐⭐</option>
        <option value="4">⭐⭐⭐⭐</option>
        <option value="5">⭐⭐⭐⭐⭐</option>
      </select>
      <!-- <input type="text" id="rank" v-model="newMovieReview.rank" required /> -->
    </div>
    <!-- review 객체  확인하기 위해 객체 전체 리스트 -->
    <!-- <p>{{ review }}</p> -->
    <button>Comment</button>
  </form>
</template>

<script>
import { mapGetters, mapActions } from "vuex";

export default {
  name: "MovieReviewForm",
  data() {
    return {
      newMovieReview: {
        // moviePk: this.$route.params.moviePk,
        title: "",
        content: "",
        rank: ""
      }
    };
  },
  computed: {
    ...mapGetters(["movie"]),
  },
  methods: {
    ...mapActions(["createMovieReview"]),
    onSubmit() {
      this.createMovieReview({
        moviePk: this.movie.id, 
        ...this.newMovieReview
      })
      // this.newMovieReview = []
      // this.newMovieReview = ""
      this.newMovieReview.title = ""
      this.newMovieReview.content = ""
      this.newMovieReview.rank = ""
    },
  },
};
</script>

<style></style>