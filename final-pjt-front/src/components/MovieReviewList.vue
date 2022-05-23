<template>
  <div class="movie-review-list">
    <ul>
      <movie-review-item
        v-for="review in review_set"
        :review="review"
        :key="review.id"
      >
      </movie-review-item>
    </ul>
    <movie-review-form></movie-review-form>
  </div>
</template>

<script>
import MovieReviewForm from "@/components/MovieReviewForm.vue";
import MovieReviewItem from "@/components/MovieReviewItem.vue";
// import { mapGetters, mapActions } from 'vuex'

export default {
  name: "MovieReviewList",
  components: { MovieReviewForm, MovieReviewItem },
  props: { review_set: Array },
};
</script>

<style></style>