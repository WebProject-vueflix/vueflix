<template>
  <li class="movie-review-item">
    
    <!-- <p>{{ review.title }}</p> -->
    <!-- <p>{{ review }}</p> -->

    <span v-if="!isEditing">
      <p>제목: {{ payload.title }} </p>
      <p>내용: {{ payload.content }}</p>
      <p>평점: {{ payload.rank }}</p>
      <!-- {{ payload.newMovieReview }} -->
    </span>
    <p>작성자: 
    <router-link :to="{ name: 'profile', params: { username: review.user.username } }">
      {{ review.user.username }}
    </router-link></p>

    <span v-if="isEditing">
      <input type="text" v-model="payload.title">
      <input type="text" v-model="payload.content">
      <input type="text" v-model="payload.rank">
      <button @click="onUpdate">Update</button> |
      <button @click="switchIsEditing">Cancle</button>
    </span>

    <span v-if="currentUser.username === review.user.username && !isEditing">
      <button @click="switchIsEditing">Edit</button> |
      <button @click="deleteMovieReview(payload)">Delete</button>
    </span>
  </li>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'MovieReviewItem',
  props: { review: Object },
  data() {
    return {
      isEditing: false,
      payload: {
        moviePk: this.review.popular_movie,
        reviewPk: this.review.id,
        title: this.review.title,
        content: this.review.content,
        rank: this.review.rank
      },
    }
  },
  computed: {
    ...mapGetters(['currentUser']),
  },
  methods: {
    ...mapActions(['updateMovieReview', 'deleteMovieReview']),
    switchIsEditing() {
      this.isEditing = !this.isEditing
    },
    onUpdate() {
      this.updateMovieReview(this.payload)
      this.isEditing = false
    }
  },

}
</script>

<style></style>