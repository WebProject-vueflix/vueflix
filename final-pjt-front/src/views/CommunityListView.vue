<template>
  <div>
    <h1>Community</h1>
    <div>
      <router-link :to="{ name: 'reviewNew' }">
        <button>New</button>
      </router-link>
    </div>

    <ul>
      <li v-for="review in community" :key="review.pk">
        {{ review.title }} [{{ review.comment_count }}]
        <br>
        <router-link 
          :to="{ name: 'review', params: {reviewPk: review.pk} }">
          게시글 보러가기
        </router-link>
      </li>
    </ul>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

  export default {
    name: 'CommunityList',
    computed: {
      ...mapGetters(['isAuthor', 'community'])
    },
    methods: {
      ...mapActions(['fetchCommunity'])
    },
    created() {
      this.fetchCommunity()
    },
  }
</script>

<style>

</style>