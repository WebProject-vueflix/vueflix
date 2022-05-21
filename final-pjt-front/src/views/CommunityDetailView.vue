<template>
  <div>
    <h1>{{ review.title }}</h1>

    <p>
      {{ review.content }}
    </p>

    <div v-if="isAuthor">
      <router-link :to="{ name: 'reviewEdit', params: { reviewPk } }">
        <button>Edit</button>
      </router-link>
      |
      <button @click="deleteReview(reviewPk)">Delete</button>
    </div>

    <!-- Review Like UI -->
    <!-- <div>
      Likeit:
      <button
        @click="likeReview(reviewPk)"
      >{{ likeCount }}</button>
    </div> -->

    <hr />
    <!-- Comment UI -->
    <comment-list :comments="review.community_review"></comment-list>
    <!-- <ul>
      <li v-for="comment in review.community_review" :key="comment.pk">
        {{ comment.user.username }} : {{ comment.content }}
      </li>
    </ul>
    <comment-form></comment-form> -->

  </div>
</template>

<script>
  import { mapGetters, mapActions } from 'vuex'
  // import CommentForm from '@/components/CommentForm.vue'
  import CommentList from '@/components/CommentList.vue'

  export default {
    name: 'CommuintyDetail',
    // components: { CommentForm },
    components: { CommentList },
    data() {
      return {
        reviewPk: this.$route.params.reviewPk,
      }
    },
    computed: {
      ...mapGetters(['isAuthor', 'review']),
      // likeCount() {
      //   return this.review.like_users?.length
      // }
    },
    methods: {
      ...mapActions([
        'fetchReview',
        'deleteReview',
        'createComment',
        // 'likeReview',
      ])
    },
    created() {
      this.fetchReview(this.reviewPk)
    },
  }
</script>

<style></style>
