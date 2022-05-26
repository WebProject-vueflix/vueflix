const HOST = 'http://localhost:8000/api/v1/'

const ACCOUNTS = 'accounts/'
const MOVIES = 'movies/'
const RECOMMEND = 'recommended/'
const COMMUNITY = 'community/'
const COMMENTS = 'comments/'
const REVIEWS = 'reviews/'
const ACTOR = 'actor/'
const GENRE = 'genre/'
const DIRECTOR = 'director/'
const LIKE = 'like/'
const UNLIKE = 'unlike/'
export default {
  accounts: {
    login: () => HOST + ACCOUNTS + 'login/',
    logout: () => HOST + ACCOUNTS + 'logout/',
    signup: () => HOST + ACCOUNTS + 'signup/',
    // Token 으로 현재 user 판단
    currentUserInfo: () => HOST + ACCOUNTS + 'user/',
    // username으로 프로필 제공
    profile: username => HOST + ACCOUNTS + 'profile/' + username,
  },

  movies: {
    movies: () => HOST + MOVIES,
    movie: moviePk => HOST + MOVIES + `${moviePk}/`,
    recommend: () => HOST + MOVIES + RECOMMEND,
    genres: () => HOST + MOVIES + GENRE,
    genre: genrePk => HOST + MOVIES + GENRE + `${genrePk}/`,
    unlikeGenre: genrePk => HOST + MOVIES + GENRE + `${genrePk}/` + UNLIKE,
    likeMovie: moviePk => HOST + MOVIES + `${moviePk}/` + LIKE,
    reviews: moviePk => HOST + MOVIES + `${moviePk}/` + REVIEWS,
    review: (moviePk, reviewPk) => HOST + MOVIES + `${moviePk}/` + REVIEWS + `${reviewPk}/`,
    actors: () => HOST + MOVIES + ACTOR,
    actor: actorPk => HOST + MOVIES + ACTOR + `${actorPk}/`,
    likeactor: actorPk => HOST + MOVIES + ACTOR + `${actorPk}/` + LIKE,
    director: directorPk => HOST + MOVIES + DIRECTOR + `${directorPk}/`,
    likedirector: directorPk => HOST + MOVIES + DIRECTOR + `${directorPk}/` + LIKE,
  },

  community: {
    community: () => HOST + COMMUNITY,
    // /community/1/
    review: reviewPk => HOST + COMMUNITY + `${reviewPk}/`,
    comments: reviewPk => HOST + COMMUNITY + `${reviewPk}/` + COMMENTS,
    comment: (reviewPk, commentPk) =>
      HOST + COMMUNITY + `${reviewPk}/` + COMMENTS + `${commentPk}/`,
  },
}
