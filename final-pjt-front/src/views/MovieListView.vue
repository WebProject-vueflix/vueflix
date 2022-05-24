<template>
  <div class="home">
    <h1><b>Home</b></h1>
    <hr />
    <!-- {{ movies }} -->
    <div class="container mb-5">
      <div
        class="row row row-cols-2 row-cols-sm-3 row-cols-md-4 row-cols-lg-6 g-0"
      >
        <div
          class="card text-white bg-dark mb-3"
          style="max-width: 18rem"
          v-for="movie in movies"
          :key="movie.id"
        >
          <div>
            <router-link :to="{ name: 'movie', params: { moviePk: movie.id } }">
              <img
                :src="`https://image.tmdb.org/t/p/original/${movie.poster_path}`"
                class="card-img-top mt-2"
                alt="..."
                style="height: 275px"
              />
            </router-link>
            <!-- <br /> -->
            <!-- <br /> -->
            <p class="mt-3">
              ✍🏻{{ movie.review_count }} 💓{{ movie.like_count }}
            </p>
          </div>

          <div class="modal" :id="`largeModal-${movie.id}`" tabindex="-1">
            <div class="modal-dialog">
              <div class="modal-content">
                <div class="modal-header">
                  <h4 class="modal-title fw-bold">🎥 {{ movie.title }}</h4>
                  <button
                    type="button"
                    class="btn-close"
                    data-bs-dismiss="modal"
                    aria-label="Close"
                  ></button>
                </div>
                <div class="modal-body">
                  <img
                    :src="`https://image.tmdb.org/t/p/w300/${movie.poster_path}`"
                    alt=""
                  />
                  <hr />
                  <p class="text-start">개봉일 : {{ movie.release_date }}</p>
                  <p class="text-start">
                    평점 : ⭐ {{ movie.vote_average }} / 10
                  </p>
                  <!-- <p class="text-start">내용 : {{ movie.release_date }}</p> -->
                </div>
                <div class="modal-footer">
                  <button
                    type="button"
                    class="btn btn-outline-danger btn-sm"
                    data-bs-dismiss="modal"
                  >
                    Close
                  </button>
                </div>
              </div>
            </div>
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
    ...mapActions(["SET_LOADING", "fetchMovies"]),
  },
  created() {
    this.SET_LOADING(true);
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
