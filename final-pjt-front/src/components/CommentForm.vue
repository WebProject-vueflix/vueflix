<template>
  <form @submit.prevent="onSubmit">
    <label for="comment">comment: </label>
    <input type="text" id="comment" v-model="content" required />
    <!-- review 객체  확인하기 위해 객체 전체 리스트 -->
    <!-- <p>{{ review }}</p> -->
    <button>Comment</button>
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