<template>
  <div>
    <!-- <h1>bye</h1> -->
    <!-- <p>{{ actor }}</p>
    <p>{{ actor.id }}</p>-->
    <p>{{ actorPK }}</p>
    <!-- <p>{{ actor_movie }}</p> -->
    <p>{{ actor_movie }}</p>

    <li v-for="movie in actor_movie" :key="movie.id">
      {{ movie }}
    </li>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";

export default {
  name: "MovieActorList",
  props: { actor: Object },
  data() {
    return {
      actorPK: this.actor.id,
    };
  },
  computed: {
    ...mapGetters(["actor_movie"]),
  },
  methods: {
    ...mapActions(["fetchActorMovies"]),
  },
  mounted() {
    this.fetchActorMovies(this.actorPK);
    console.log("beforeMount");
  },
};
</script>

<style>
</style>s