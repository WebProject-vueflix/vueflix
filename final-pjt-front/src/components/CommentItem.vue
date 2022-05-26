<template>
  <li
    class="
      list-group-item
      d-flex
      justify-content-between
      align-items-start
      ps-2
    "
  >
    <router-link
      :to="{ name: 'profile', params: { username: comment.user.username } }"
      class="btn ps-0 pb-0 pt-0"
    >
      <h5 class="text-dark mb-0">
        {{ comment.user.username }}
      </h5>
    </router-link>

    <h5 v-if="!isEditing" class="mb-2 ms-2">: {{ payload.content }}</h5>

    <span v-if="isEditing">
      <input type="text" v-model="payload.content" class="mx-3" />
      <button @click="onUpdate" class="btn btn-outline-dark">Update</button> |
      <button @click="switchIsEditing" class="btn btn-outline-dark">
        Cancle
      </button>
    </span>

    <span v-if="currentUser.username === comment.user.username && !isEditing">
      <button @click="switchIsEditing">Edit</button> |
      <button @click="deleteComment(payload)">Delete</button>
    </span>
  </li>
</template>

<script>
import { mapGetters, mapActions } from "vuex";

export default {
  name: "CommentItem",
  props: { comment: Object },
  data() {
    return {
      isEditing: false,
      payload: {
        reviewPk: this.comment.review,
        commentPk: this.comment.pk,
        content: this.comment.content,
      },
    };
  },
  computed: {
    ...mapGetters(["currentUser"]),
  },
  methods: {
    ...mapActions(["updateComment", "deleteComment"]),
    switchIsEditing() {
      this.isEditing = !this.isEditing;
    },
    onUpdate() {
      this.updateComment(this.payload);
      this.isEditing = false;
    },
  },
};
</script>

<style></style>