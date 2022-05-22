<template>
  <form @submit.prevent="onSubmit">
    <div>
      <label for="title">title: </label>
      <input v-model="newReview.title" type="text" id="title" />
    </div>
    <div>
      <label for="content">content: </label>
      <textarea v-model="newReview.content" type="text" id="content"></textarea>
    </div>
    <div>
      <label for="rank">rank: </label>
      <input type="number" name="" id="rank" />
    </div>
    <button>Comment</button>
  </form>
</template>

<script>
import { mapActions } from "vuex";

export default {
  name: "ReviewForm",
  props: {
    movie: Object,
    action: String,
  },
  data() {
    return {
      newReview: {
        title: this.review_set.title,
        content: this.review_set.content,
        rank: this.review_set.rank,
      },
    };
  },

  methods: {
    ...mapActions(["createReview", "updateReview"]),
    onSubmit() {
      const payload = {
        ...this.newReview,
      };
      this.createReview({
        moviePK: this.movie.pk,
        content: payload,
      });
    },
  },
};
</script>

<style></style>