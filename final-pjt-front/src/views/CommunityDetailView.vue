<template>
  <div>
    <!-- <h1>{{ review }}</h1> -->
    <!-- {{ this.review.created_at }} -->
    <!-- <p>
      {{ review.content }}
    </p> -->
    <div class="card">
      <h5
        class="
          card-header
          mt-1
          pb-0
          d-flex
          justify-content-between
          align-items-baseline
        "
      >
        <h3 class="mb-0 text-start">
          {{ review.title }} <br />
          <br />
        </h3>
        <div v-if="isAuthor">
          <div class="d-grid gap-2 d-md-flex justify-content-md-end mt-0">
            <span me-2>{{ review.user.username }}</span>
            <router-link :to="{ name: 'reviewEdit', params: { reviewPk } }">
              <button class="btn btn-outline-light me-md-2 ms-2" type="button">
                Edit
              </button>
            </router-link>
            <button
              @click="deleteReview(reviewPk)"
              class="btn btn-outline-light"
              type="button"
            >
              Delete
            </button>
          </div>
        </div>
      </h5>
      <hr />
      <div class="card-title mb-3 d-flex justify-content-between">
        <!-- <span class="text-ligth">{{ review.updated_at }}</span> -->
        <h5 class="card-text text-ligth ms-3 text-start">
          {{ review.content }}
        </h5>
        <h6 class="mb-0 me-3 text-end">
          created | {{ createdate }}
          <br />
          updated | {{ updatedate }}
        </h6>
      </div>
    </div>
    <!-- <div v-if="isAuthor">
      <div class="d-grid gap-2 d-md-flex justify-content-md-end mt-4">
        <router-link :to="{ name: 'reviewEdit', params: { reviewPk } }">
          <button class="btn btn-outline-light me-md-2" type="button">
            Edit
          </button>
        </router-link>
        <button
          @click="deleteReview(reviewPk)"
          class="btn btn-outline-light"
          type="button"
        >
          Delete
        </button>
      </div>
    </div> -->
    <router-link :to="{ name: 'community' }">
      <button class="btn btn-outline-light mt-3">목록으로 돌아가기</button>
    </router-link>

    <!-- Review Like UI -->
    <!-- <div>
      Likeit:
      <button
        @click="likeReview(reviewPk)"
      >{{ likeCount }}</button>
    </div> -->

    <hr />
    <!-- Comment UI -->
    <h3 class="mb-3">[Comment]</h3>
    <comment-list :community_review="review.community_review"></comment-list>
    <!-- <ul>
      <li v-for="comment in review.community_review" :key="comment.pk">
        {{ comment.user.username }} : {{ comment.content }}
      </li>
    </ul>
    <comment-form></comment-form> -->
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
// import CommentForm from '@/components/CommentForm.vue'
import CommentList from "@/components/CommentList.vue";

export default {
  name: "CommuintyDetail",
  // components: { CommentForm },
  components: { CommentList },
  data() {
    return {
      reviewPk: this.$route.params.reviewPk,
    };
  },
  computed: {
    ...mapGetters(["isAuthor", "review", "comment"]),
    // likeCount() {
    //   return this.review.like_users?.length
    // }

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
    ...mapActions([
      "fetchReview",
      "deleteReview",
      "createComment",
      "deleteComment",
      // 'likeReview',
    ]),
  },
  created() {
    this.fetchReview(this.reviewPk);
  },
};
</script>

<style></style>
