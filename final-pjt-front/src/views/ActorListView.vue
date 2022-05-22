<template>
  <div>
    <h1>ActorList</h1>
    <!-- {{ movies }} -->
    <ul>
      <li v-for="actor in actors" :key="actor.pk">
        <router-link :to="{ name: 'actor', params: { actorPk: actor.id } }">
          {{ actor.id }}
        </router-link>
      </li>
    </ul>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";

export default {
  name: "ActorList",
  computed: {
    ...mapGetters(["actors"]),
  },
  methods: {
    ...mapActions(["fetchActors"]),
  },
  created() {
    this.fetchActors();
  },
};
</script>

<style></style>
