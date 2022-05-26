<template>
  <div>
    <h1>Community</h1>
    <div>
      <router-link
        :to="{ name: 'reviewNew' }"
        class="btn d-grid gap-2 d-md-flex justify-content-md-end"
      >
        <button class="btn btn-outline-light mb-2">New</button>
      </router-link>
    </div>
    <!-- <div class="card" style="width: 18rem"></div> -->
    <ol class="list-group list-group-numbered">
      <li
        v-for="review in community"
        :key="review.pk"
        class="
          list-group-item list-group-item-action list-group-item-warning
          d-flex
        "
      >
        <router-link
          :to="{ name: 'review', params: { reviewPk: review.pk } }"
          class="text-decoration-none ms-2 me-3"
        >
          {{ review.title }}
        </router-link>
        [{{ review.comment_count }}]

        <br />
      </li>
    </ol>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";

export default {
  name: "CommunityList",
  computed: {
    ...mapGetters(["isAuthor", "community"]),
  },
  methods: {
    ...mapActions(["fetchCommunity"]),
  },
  created() {
    this.fetchCommunity();
  },
};
</script>

<style>
</style>