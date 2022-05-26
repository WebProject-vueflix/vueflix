<template>
  <form @submit.prevent="onSubmit">
    <div class="mb-3">
      <label for="title" class="form-label">title: </label>
      <input
        v-model="newReview.title"
        type="text"
        id="title"
        class="form-control"
      />
    </div>
    <div>
      <label for="content" class="form-label">content: </label>
      <textarea
        v-model="newReview.content"
        type="text"
        id="content"
        class="form-control"
        style="height: 100px"
      ></textarea>
    </div>
    <!-- <br /> -->
    <div class="d-grid gap-2 d-md-flex justify-content-md-end mt-4">
      <button class="btn btn-outline-light">{{ action }}</button>
    </div>
  </form>
</template>

<script>
import { mapActions } from "vuex";

export default {
  name: "ReviewForm",
  props: {
    review: Object,
    action: String,
  },
  data() {
    return {
      newReview: {
        title: this.review.title,
        content: this.review.content,
      },
    };
  },

  methods: {
    ...mapActions(["createReview", "updateReview"]),
    onSubmit() {
      if (this.action === "create") {
        this.createReview(this.newReview);
      } else if (this.action === "update") {
        const payload = {
          pk: this.review.pk,
          ...this.newReview,
        };
        this.updateReview(payload);
      }
    },
  },
};
</script>

<style></style>
