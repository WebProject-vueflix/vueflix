<template>
  <div>
    <!-- {{movie}} -->
    <!-- <p>{{ movie.actors }}</p> -->
    <!-- <p>{{ movie.review_set }}</p> -->
    <!-- {{movie.id}} -->
    <h1 class="mb-4">
      <b>{{ movie.title }}</b>
    </h1>
    <hr />
    <div class="card mb-3 mt-4" style="max-width: 100rem">
      <div class="row g-0">
        <div
          class="col-md-4 d-flex align-items-center justify-content-center my-4"
        >
          <img
            :src="`https://image.tmdb.org/t/p/w300/${movie.poster_path}`"
            class="img-fluid rounded-start"
            alt="사진"
          />
        </div>
        <div class="col-md-8">
          <div class="card-body my-3">
            <p class="card-text text-start">
              <b>요약 : </b>{{ movie.overview }}
            </p>
            <p class="card-text text-start">
              <b>평점 : </b>⭐ {{ movie.vote_average }} / 10.0
            </p>
            <p v-if="movie.review_set.length > 0" class="card-text text-start">
              <b>사용자평점 : </b>⭐ {{ rankAvg }} / 5.00
            </p>
            <p v-else class="card-text text-start">
              <b>사용자평점 : </b>한줄평을 입력해주세요
            </p>
            <p class="card-text text-start">
              <b>장르 : </b>|
              <span v-for="genre in movie.genres" :key="genre.name">
                {{ genre.name }} |
              </span>
            </p>
            <p class="card-text text-start">
              <b>배우 : </b>
              <span v-for="actor in movie.actors" :key="actor.id">
                <span>{{ actor.name }}({{ actor.character }} 역)ㅤ</span>
              </span>
            </p>
            <p class="card-text text-start">
              <b>감독 : </b>{{ movie.director[0].name }}
            </p>
            <p class="card-text text-start">
              <b>개봉일 : </b>{{ movie.release_date }}
            </p>
            <br />
            <p class="card-text text-start"><b>Likeit : </b>{{ likeCount }}</p>
            <!-- Button trigger modal -->
            <!-- <button type="button" class="btn btn-danger video-btn" data-bs-toggle="modal" :data-src="`https://www.youtube.com/embed/${movie.youtube_key}`" data-bs-target="#myModal">
              영상 미리보기
            </button> -->
            <!-- <button type="button" class="btn btn-danger" data-bs-toggle="modal" data-bs-target="#staticBackdrop">
              영상 미리보기
            </button> -->
            <!-- Button trigger modal -->
            <div class="d-flex justify-content-end">
              <button
                type="button"
                class="btn btn-danger video-btn mx-4"
                data-bs-toggle="modal"
                :data-src="`https://www.youtube.com/embed/${movie.youtube_key}`"
                data-bs-target="#myModal"
              >
                영상 미리보기
              </button>
              <button
                class="btn btn btn-outline-warning"
                @click="likeMovie(moviePk)"
              >
                ❤️
              </button>
            </div>

            <!-- Modal -->
            <div
              class="modal fade"
              data-bs-backdrop="static"
              id="myModal"
              tabindex="-1"
              role="dialog"
              aria-labelledby="exampleModalLabel"
              aria-hidden="true"
            >
              <div class="modal-dialog modal-lg" role="document">
                <div class="modal-content">
                  <div class="modal-body">
                    <button
                      type="button"
                      class="btn-close"
                      data-bs-dismiss="modal"
                      aria-label="Close"
                    ></button>
                    <!-- 16:9 aspect ratio -->
                    <div id="area" class="ratio ratio-16x9">
                      <iframe
                        id="video"
                        class="embed-responsive-item"
                        :src="`https://www.youtube.com/embed/${movie.youtube_key}`"
                        allowscriptaccess="always"
                        allow="autoplay"
                      ></iframe>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div div class="card">
      <div class="card-header">
        배우 정보
        <div class="d-flex justify-content-center align-items-center mt-2">
          <div v-for="actor in movie.actors" :key="actor.id">
            <div v-if="actor.profile_path != null">
              <img
                :src="`https://image.tmdb.org/t/p/w300/${actor.profile_path}`"
                alt="사진"
                class="card-img-top mx-auto"
              />
              <div class="card-body">
                <p class="card-text">{{ actor.name }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- {{ movie.director[0].id }} -->
    <hr />
    <div v-if="movie.director[0].popular_movies.length >= 2">
      <span
        ><h3>
          <b>{{ movie.director[0].name }} 감독님의 이 영화는 어때요?</b>
        </h3></span
      >
      <router-link
        :to="{ name: 'director', params: { directorPk: movie.director[0].id } }"
      >
        <div class="d-flex justify-content-end">
          <span>더 보러가기</span>
        </div>
      </router-link>
      <div div class="card">
        <div class="d-flex justify-content-center align-items-center mt-2">
          <div
            v-for="num in movie.director[0].popular_movies.length"
            :key="num"
          >
            <div v-if="num <= `${n}`">
              <div
                v-if="movie.director[0].popular_movies[num - 1].id != movie.id"
              >
                <img
                  :src="`https://image.tmdb.org/t/p/w200/${
                    movie.director[0].popular_movies[num - 1].poster_path
                  }`"
                  alt="사진"
                  class="card-img-top mx-auto"
                />
                <div class="card-body">
                  <p>{{ movie.director[0].popular_movies[num - 1].title }}</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- <router-link
      :to="{ name: 'director', params: { directorPk: movie.director[0].id } }"
    >
      <div v-if="movie.director[0].profile_path != null">
        <img
          :src="`https://image.tmdb.org/t/p/w300/${movie.director[0].profile_path}`"
          alt="사진"
        />
      </div>
      <p>{{ movie.director[0].name }}</p>
    </router-link> -->
    <!-- 영화예매 바로가기 하이퍼링크 -->

    <!-- 공유하기 -->
    <hr />
    <div v-for="movieactor in movie.actors" :key="movieactor.name">
      <div v-if="movieactor.popular_movies.length >= 2">
        <span
          ><h3>
            <b>{{ movieactor.name }} 배우님의 이 영화는 어때요?</b>
          </h3></span
        >
        <router-link
          :to="{ name: 'actor', params: { actorPk: movieactor.id } }"
        >
          <div class="d-flex justify-content-end">
            <button>더 보러가기</button>
          </div>
        </router-link>
        <div div class="card">
          <div class="d-flex justify-content-center align-items-center mt-4">
            <div v-for="num in movieactor.popular_movies.length" :key="num">
              <div v-if="num <= `${n}`">
                <div v-if="movieactor.popular_movies[num - 1].id != movie.id">
                  <img
                    :src="`https://image.tmdb.org/t/p/w200/${
                      movieactor.popular_movies[num - 1].poster_path
                    }`"
                    alt="사진"
                    class="card-img-top mx-auto"
                    style="height: 300px"
                  />
                  <div class="card-body">
                    <p>{{ movieactor.popular_movies[num - 1].title }}</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <hr />
      </div>
    </div>
    <!-- <div v-for="review in movie.review_set" :key="review.id">
      {{ sum_rank }} : {{ review.rank }}
    </div> -->

    <!-- <h2>한줄평</h2>
    <div v-for="review in movie.review_set" :key="review.id">
      <b>제목: {{ review.title }}</b>
      <p>내용: {{ review.content }}</p>
      <p>평점: {{ review.rank }}</p>
      <p>작성자: {{ review.user.username }}</p>
      <br>
    </div> -->
    <!-- {{rankAvg}} -->
    <!-- {{this.movie.review_set}} -->
    <h2>한줄평 ({{ movie.review_set.length }})</h2>
    <movie-review-list :review_set="movie.review_set"></movie-review-list>
    <!-- <movie-review-form> </movie-review-form> -->
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import MovieReviewList from "@/components/MovieReviewList.vue";
// import MovieReviewForm from "@/components/MovieReviewForm.vue";
// import MovieActorList from "@/components/Movie/MovieActorList.vue";

export default {
  name: "MovieDetail",
  components: { MovieReviewList },
  data() {
    return {
      moviePk: this.$route.params.moviePk,
      n: 4,
    };
  },
  computed: {
    ...mapGetters(["movie", "actor"]),
    likeCount() {
      return this.movie.like_users?.length;
    },
    rankAvg() {
      let sum = 0;
      for (let idx of this.movie.review_set) {
        sum = sum + idx.rank;
      }
      // sum = sum + int(this.movie.review_set.rank)
      let len = this.movie.review_set?.length;
      return (sum / len).toPrecision(3);
      // return sum
    },
  },
  methods: {
    ...mapActions(["fetchMovie", "likeMovie", "likeActor"]),
  },
  created() {
    this.fetchMovie(this.moviePk);
    console.log("ok");
  },
};
</script>

<style>
div {
  color: aliceblue;
}
#area {
  position: relative; /* absolute는 부모가 relative일 때 부모를 따라간다. */
  width: 100%;
  height: 480px;
  padding-bottom: 56.25%; /* 16:9 비율 */
}

#video {
  position: absolute;
  width: 100%; /* 부모에 맞게 꽉 채운다. */
  height: 100%;
}
.modal-dialog {
  max-width: 1000px;
  margin: 30px auto;
}

.modal-body {
  position: relative;
  overflow-y: auto;
  max-height: 1000px;
  padding: 15px;
}

div.card {
  background-color: rgba(226, 182, 182, 0);
  border-color: rgb(245, 235, 197);
}
div.card p {
  color: white;
}
</style>