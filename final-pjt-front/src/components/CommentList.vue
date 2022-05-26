<template>
  <div class="comment-list">
    <!-- {{ community_review }} -->
    <ul class="ps-0">
      <comment-item
        v-for="comment in community_review"
        :comment="comment"
        :key="comment.pk"
        class="list-group list-group-flush list-group-item-warning"
      >
      </comment-item>
    </ul>

    <comment-form></comment-form>
  </div>
</template>

<script>
import CommentForm from "@/components/CommentForm.vue";
import CommentItem from "@/components/CommentItem.vue";
// import { mapGetters, mapActions } from 'vuex'

export default {
  name: "CommentList",
  components: { CommentForm, CommentItem },
  props: { community_review: Array },
};
</script>

<style></style>