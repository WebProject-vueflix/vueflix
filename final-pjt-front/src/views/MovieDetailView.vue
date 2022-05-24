<template>
  <div>
    <!-- {{movie}} -->
    <!-- <p>{{ movie.actors }}</p> -->
    <!-- <p>{{ movie.review_set }}</p> -->
    <h1>{{ movie.title }}</h1>
    <img
      :src="`https://image.tmdb.org/t/p/w300/${movie.poster_path}`"
      alt="사진"
    />
    <p>요약 : {{ movie.overview }}</p>
    <p>평점 : ⭐ {{ movie.vote_average }} / 10.0</p>
    <p v-if="movie.review_set.length != 0">사용자평점 : ⭐ {{rankAvg}} / 5.00</p>
    <p v-else>사용자평점 : 한줄평을 입력해주세요</p>
    <div>
      Likeit : {{ likeCount }}
      <button @click="likeMovie(moviePk)">좋아요</button>
    </div>
    <p>배우 :</p>

    <div v-for="actor in movie.actors" :key="actor.id">
      <div v-if="actor.profile_path != null">
        <img
          :src="`https://image.tmdb.org/t/p/w200/${actor.profile_path}`"
          alt="사진"
        />
        <p>{{ actor.name }}({{ actor.character }} 역)</p>
      </div>
      <!-- <router-link :to="{ name: 'actor', params: { actorPk: actor.id } }">
        <p>{{ actor.name }}({{ actor.character }} 역)</p>
      </router-link> -->
    </div>
    <p>감독 : {{ movie.director[0].name }}</p>
    <!-- {{ movie.director[0].id }} -->
    <div v-if="movie.director[0].profile_path != null">
      <img
        :src="`https://image.tmdb.org/t/p/w200/${movie.director[0].profile_path}`"
        alt="사진"
      />
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
    <p>개봉일 : {{ movie.release_date }}</p>
    <!-- 영화예매 바로가기 하이퍼링크 -->
    <iframe
      :src="`https://www.youtube.com/embed/${movie.youtube_key}`"
    ></iframe>
    <!-- 공유하기 -->
    <hr />
    <div v-for="movieactor in movie.actors" :key="movieactor.name">
      <div v-if="movieactor.popular_movies.length >= 2">  
        <h3><b>{{ movieactor.name }} 배우님의 이 영화는 어때요?</b></h3>
        <router-link :to="{ name: 'actor', params: { actorPk: movieactor.id } }">
          <p>더 보러가기</p>
        </router-link>
        <div v-for="num in movieactor.popular_movies.length" :key="num">
          <div v-if="num <= `${n}`">
            <!-- {{num}} -->
          <!-- <div v-for="newmovie in movieactor.popular_movies" :key="newmovie.title"> -->
            <div v-if="movieactor.popular_movies[num-1].id != movie.id">
              <img
                :src="`https://image.tmdb.org/t/p/w200/${movieactor.popular_movies[num-1].poster_path}`"
                alt="사진"
              />
              <p>{{ movieactor.popular_movies[num-1].title }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
    <hr>
    <div v-if="movie.director[0].popular_movies.length >= 2">  
      <h3><b>{{ movie.director[0].name }} 감독님의 이 영화는 어때요?</b></h3>
      <router-link :to="{ name: 'director', params: { directorPk: movie.director[0].id } }">
        <p>더 보러가기</p>
      </router-link>
      <div v-for="num in movie.director[0].popular_movies.length" :key="num">
        <div v-if="num <= `${n}`">
          <!-- {{num}} -->
        <!-- <div v-for="newmovie in movieactor.popular_movies" :key="newmovie.title"> -->
          <div v-if="movie.director[0].popular_movies[num-1].id != movie.id">
            <img
              :src="`https://image.tmdb.org/t/p/w200/${movie.director[0].popular_movies[num-1].poster_path}`"
              alt="사진"
            />
            <p>{{ movie.director[0].popular_movies[num-1].title }}</p>
          </div>
        </div>
      </div>
    </div>
    <!-- <div v-for="review in movie.review_set" :key="review.id">
      {{ sum_rank }} : {{ review.rank }}
    </div> -->
    <hr />
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
      let sum = 0
      for(let idx of this.movie.review_set) {
        sum = sum + idx.rank
      }
      // sum = sum + int(this.movie.review_set.rank)
      let len = this.movie.review_set?.length
      return (sum / len).toPrecision(3)
      // return sum
    }
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
</style>