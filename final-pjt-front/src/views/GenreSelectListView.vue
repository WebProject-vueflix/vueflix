<template>
  <div>
    <h1>GenreList</h1>
    <!-- {{ genres }} -->
    <ul class="list-group list-group-horizontal-2">
      <li class="list-group-item" v-for="genre in genres" :key="genre.name">
        <div v-if="genre.unlike === true">
          <input @click="unlikeGenre(genre.id)" 
            type="checkbox" id="genre" name="genre" checked
            class="form-check-input me-1" value="" aria-label="...">
          <label for="genre" class="text-dark">{{ genre.name }}</label> 
        </div>
        <div v-if="genre.unlike === false">
          <input @click="unlikeGenre(genre.id)" 
            type="checkbox" id="genre" name="genre"
            class="form-check-input me-1" value="" aria-label="...">
          <label for="genre" class="text-dark">{{ genre.name }}</label> 
        </div>
        <router-link :to="{ name: 'genre', params: { genrePk: genre.id } }">
          <button>상세보기</button>
        </router-link> 
      </li>
    </ul>
    <router-link :to="{ name: 'profile', params: { username: currentUser.username } }">
      <button>완료</button>
    </router-link>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";

export default {
  name: "GenreList",
  computed: {
    ...mapGetters(["genres", "currentUser"]),
  },
  methods: {
    ...mapActions(["fetchGenres", "unlikeGenre"]),
  },
  created() {
    this.fetchGenres();
  },
};
</script>

<style></style>
