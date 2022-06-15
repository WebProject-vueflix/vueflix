<template>
  <div>
    <h1>GenreList</h1>
    {{ genres[5].hate_users }}
    {{ currentUser.username }}
    <!-- {{ currentUser }} -->
    <ul class="list-group list-group-horizontal-2">
      <li
        class="list-group-item list-group-item-action list-group-item-dark"
        v-for="genre in genres"
        :key="genre.name"
      >
        {{ genre.hate_users }}
        <div v-if="genre.hate_users.length >= 1">
          <div v-for="hate_user in genre.hate_users" :key="hate_user.id">
            <!-- {{ hate_user.username }} -->
            <div v-if="hate_user.username === currentUser.username">
              <input
                @click="unlikeGenre(genre.id)"
                type="checkbox"
                id="genre"
                name="genre"
                checked
                class="form-check-input me-1"
                value=""
                aria-label="..."
              />
              <label for="genre" class="text-dark">{{ genre.name }}</label>
            </div>
            <div v-else>
              <input
                @click="unlikeGenre(genre.id)"
                type="checkbox"
                id="genre"
                name="genre"
                class="form-check-input me-1"
                value=""
                aria-label="..."
              />
              <label for="genre" class="text-dark">{{ genre.name }}</label>
            </div>
          </div>
        </div>
        <div v-else>
          <input
            @click="unlikeGenre(genre.id)"
            type="checkbox"
            id="genre"
            name="genre"
            class="form-check-input me-1"
            value=""
            aria-label="..."
          />
          <label for="genre" class="text-dark">{{ genre.name }}</label>
        </div>
        <router-link :to="{ name: 'genre', params: { genrePk: genre.id } }">
          <button>상세보기</button>
        </router-link>
      </li>
      <!-- <router-link :to="{ name: 'genre', params: { genrePk: genre.id } }">
          <button>{{ genre.name }}</button>
        </router-link> -->
    </ul>
    <router-link
      :to="{ name: 'profile', params: { username: currentUser.username } }"
    >
      <button class="btn btn-outline-light mt-3">완료</button>
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
