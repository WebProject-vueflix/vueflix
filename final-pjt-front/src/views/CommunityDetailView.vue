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

    <!-- Article Like UI -->
    <!-- <div>
      Likeit:
      <button
        @click="likeArticle(articlePk)"
      >{{ likeCount }}</button>
    </div> -->

    <hr />
    <!-- Comment UI -->
    <!-- <comment-list :comments="review.comments"></comment-list> -->
    <ul>
      <li v-for="comment in review.community_review" :key="comment.pk">
        {{ comment.user.username }} : {{ comment.content }}
      </li>
    </ul>

  </div>
</template>

<script>
  import { mapGetters, mapActions } from 'vuex'
  // import CommentList from '@/components/CommentList.vue'

  export default {
    name: 'CommuintyDetail',
    // components: { CommentList },
    data() {
      return {
        reviewPk: this.$route.params.reviewPk,
      }
    },
    computed: {
      ...mapGetters(['isAuthor', 'review']),
      // likeCount() {
      //   return this.article.like_users?.length
      // }
    },
    methods: {
      ...mapActions([
        'fetchReview',
        'deleteReview',
        // 'likeArticle',
      ])
    },
    created() {
      this.fetchReview(this.reviewPk)
    },
  }
</script>

<style></style>
