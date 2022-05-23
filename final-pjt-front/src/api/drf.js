const HOST = 'http://localhost:8000/api/v1/'

const ACCOUNTS = 'accounts/'
const MOVIES = 'movies/'
const COMMUNITY = 'community/'
const COMMENTS = 'comments/'
const REVIEWS = 'reviews/'
const ACTOR = 'actor/'
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
    likeMovie: moviePk => HOST + MOVIES + `${moviePk}/` + 'like/',
    reviews: moviePk => HOST + MOVIES + `${moviePk}/` + REVIEWS,
    review: (moviePk, reviewPk) => HOST + MOVIES + `${moviePk}/` + REVIEWS + `${reviewPk}/`,
    actors: () => HOST + MOVIES + ACTOR,
    actor: actorPk => HOST + MOVIES + ACTOR + `${actorPk}/`
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
