<template>
  <form @submit.prevent="onSubmit">
    <!-- <label for="review">한줄평: </label> -->
    <div class="d-grid justify-content-center">
      <div class="row mt-5">
        <label for="title" class="col-form-label col-2">
          <p>title:</p>
        </label>
        <div class="col-10">
          <input
            type="text"
            class="form-control"
            id="title"
            v-model="newMovieReview.title"
            required
          />
        </div>
        <!-- <div class="col-10">
          <input
            type="text"
            class="form-control"
            id="title"
            placeholder="title"
            v-model="newMovieReview.title"
            required
          />
        </div> -->
      </div>
      <div class="row">
        <label for="content" class="col-form-label col-2"><p>text:</p></label>
        <div class="col-10">
          <input
            type="text"
            class="form-control"
            id="content"
            v-model="newMovieReview.content"
            required
          />
        </div>
      </div>
      <div class="row">
        <label for="rank" class="col-form-label col-2"><p>rank:</p></label>
        <!-- <input type="selectbox" id="rank" v-model="newMovieReview.rank" required /> -->
        <div class="col-10">
          <select v-model="newMovieReview.rank" class="form-select">
            <option disabled value="">평점을 선택하세요</option>
            <option value="1">⭐</option>
            <option value="2">⭐⭐</option>
            <option value="3">⭐⭐⭐</option>
            <option value="4">⭐⭐⭐⭐</option>
            <option value="5">⭐⭐⭐⭐⭐</option>
          </select>
        </div>
        <!-- <input type="text" id="rank" v-model="newMovieReview.rank" required /> -->
      </div>
    </div>
    <!-- review 객체  확인하기 위해 객체 전체 리스트 -->
    <!-- <p>{{ review }}</p> -->
    <div class="d-grid gap-2 d-md-flex justify-content-md-end">
      <button class="btn btn-outline-light">Comment</button>
    </div>
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
        rank: null,
      },
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
        ...this.newMovieReview,
      });
      // this.newMovieReview = []
      // this.newMovieReview = ""
      this.newMovieReview.title = "";
      this.newMovieReview.content = "";
      this.newMovieReview.rank = null;
    },
  },
};
</script>

<style></style>