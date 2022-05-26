<template>
  <li class="movie-review-item">
    <!-- <p>{{ review.title }}</p> -->
    <!-- <p>{{ review }}</p> -->

    <span v-if="!isEditing">
      <p class="text-start">제목: {{ payload.title }}</p>
      <p class="text-start">내용: {{ payload.content }}</p>
      <p class="text-start">평점: {{ payload.rank }}</p>
      <!-- {{ payload.newMovieReview }} -->
      <p class="text-start">
        작성자:
        <router-link
          :to="{ name: 'profile', params: { username: review.user.username } }"
        >
          {{ review.user.username }}
        </router-link>
      </p>
      <h6 class="mb-0 me-3 text-start">
        created | {{ createdate }}
        <br />
        updated | {{ updatedate }}
      </h6>
    </span>

    <span v-if="isEditing">
      <div>
        <span class="text-dark">제목: </span>
        <input type="text" v-model="payload.title" />
      </div>
      <br />
      <span class="text-dark">내용: </span>

      <input type="text" v-model="payload.content" />
      <br />
      <span></span>
      <select v-model="payload.rank">
        <option disabled value="">평점을 선택하세요</option>
        <option value="1">⭐</option>
        <option value="2">⭐⭐</option>
        <option value="3">⭐⭐⭐</option>
        <option value="4">⭐⭐⭐⭐</option>
        <option value="5">⭐⭐⭐⭐⭐</option>
      </select>
      <!-- <input type="selectbox" v-model="payload.rank"> -->
      <br />
      <button @click="onUpdate">Update</button> |
      <button @click="switchIsEditing">Cancle</button>
    </span>

    <p
      v-if="currentUser.username === review.user.username && !isEditing"
      class="d-inline"
    >
      <button @click="switchIsEditing">Edit</button> |
      <button @click="deleteMovieReview(payload)">Delete</button>
    </p>
  </li>
</template>

<script>
import { mapGetters, mapActions } from "vuex";

export default {
  name: "MovieReviewItem",
  props: { review: Object },
  data() {
    return {
      isEditing: false,
      payload: {
        moviePk: this.review.popular_movie,
        reviewPk: this.review.id,
        title: this.review.title,
        content: this.review.content,
        rank: this.review.rank,
      },
    };
  },
  computed: {
    ...mapGetters(["currentUser"]),
    createdate() {
      let a = this.review.created_at.substring(0, 10);
      let b = this.review.created_at.substring(11, 19);
      return a + " " + b;
    },
    updatedate() {
      let c = this.review.updated_at.substring(0, 10);
      let d = this.review.updated_at.substring(11, 19);
      return c + " " + d;
    },
  },
  methods: {
    ...mapActions(["updateMovieReview", "deleteMovieReview"]),
    switchIsEditing() {
      this.isEditing = !this.isEditing;
    },
    onUpdate() {
      this.updateMovieReview(this.payload);
      this.isEditing = false;
    },
  },
};
</script>

<style></style>