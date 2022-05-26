<template>
  <div class="home">
    <h1><b>Home</b></h1>
    <hr />
    <!-- {{ movies }} -->
    <div class="container mb-5">
      <div
        class="d-flex justify-content-center row row row-cols-2 row-cols-sm-3 row-cols-md-4 row-cols-lg-6 g-0"
      >
        <div
          class="card text-white bg-dark mb-3"
          style="width: 18rem"
          v-for="movie in movies"
          :key="movie.id"
        >
          <div>
            <router-link :to="{ name: 'movie', params: { moviePk: movie.id } }">
              <img
                :src="`https://image.tmdb.org/t/p/original/${movie.poster_path}`"
                class="card-img-top mt-2"
                alt="..."
                style="height: 380px"

              />
            </router-link>
            <!-- <br /> -->
            <!-- <br /> -->
            <p class="mt-3">
              ✍🏻{{ movie.review_count }} 💓{{ movie.like_count }}
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";

export default {
  name: "MovieList",
  computed: {
    ...mapGetters(["movies"]),
  },
  methods: {
    ...mapActions(["fetchMovies"]),
  },
  created() {
    this.fetchMovies();
  },
};
</script>

<style>
div {
  text-align: center;
  color: aliceblue;
}
.card-body {
  color: black;
}

.modal-header {
  color: black;
}
.modal-body {
  color: black;
}
.card-footer {
  background: transparent;
  border-top: 0px;
}
</style>
