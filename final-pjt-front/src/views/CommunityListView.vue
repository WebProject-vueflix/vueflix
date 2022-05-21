<template>
  <div>
    <h1>Community</h1>
    <ul>
      <li v-for="review in community" :key="review.pk">
        {{ review.title }} : {{ review.content }}
      </li>
    </ul>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

  export default {
    name: 'CommunityList',
    computed: {
      ...mapGetters(['community'])
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