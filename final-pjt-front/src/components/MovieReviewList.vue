<template>
  <div class="movie-review-list">
    <!-- {{ review_set }} -->
    <ul class="list-group list-group-flush">
      <movie-review-item
        v-for="review in review_set"
        :review="review"
        :key="review.id"
        class="
          list-group-item
          d-flex
          justify-content-between
          align-items-end
          list-group-item-warning
        "
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