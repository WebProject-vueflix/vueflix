<template>
  <div>
    <h1>GenreList</h1>
    {{ genres }}
    <ul>
      <li v-for="genre in genres" :key="genre.name">
        <div v-if="genre.unlike === true">
          <input @click="unlikeGenre(genre.id)" type="checkbox" id="genre" name="genre" checked>
          <label for="genre">{{ genre.name }}</label> 
        </div>
        <div v-if="genre.unlike === false">
          <input @click="unlikeGenre(genre.id)" type="checkbox" id="genre" name="genre">
          <label for="genre">{{ genre.name }}</label> 
        </div>
        <router-link :to="{ name: 'genre', params: { genrePk: genre.id } }">
          <button>상세보기</button>
        </router-link> 
      </li>
    </ul>
    <router-link :to="{ name: 'profile', params: { username: profile.username } }">
      <button>완료</button>
    </router-link>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";

export default {
  name: "GenreList",
  computed: {
    ...mapGetters(["genres", "profile"]),
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
