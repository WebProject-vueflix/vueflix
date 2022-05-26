<template>
  <form @submit.prevent="onSubmit">
    <div class="d-flex align-items-baseline">
      <!-- <label for="comment" class="col-form-label">comment: </label> -->
      <input
        type="text"
        id="comment"
        v-model="content"
        required
        class="form-control col-4 d-inline"
        placeholder="comment"
      />
      <!-- review 객체  확인하기 위해 객체 전체 리스트 -->
      <!-- <p>{{ review }}</p> -->
      <button class="mx-2 btn btn-outline-light">Comment</button>
    </div>
  </form>
</template>

<script>
import { mapGetters, mapActions } from "vuex";

export default {
  name: "CommentForm",
  data() {
    return {
      content: "",
    };
  },
  computed: {
    ...mapGetters(["review"]),
  },
  methods: {
    ...mapActions(["createComment"]),
    onSubmit() {
      this.createComment({ reviewPk: this.review.pk, content: this.content });
      this.content = "";
    },
  },
};
</script>

<style></style>