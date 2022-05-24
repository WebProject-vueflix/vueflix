// import axios from "axios";

// const request = axios.create({
//   baseURL: "https://api.themoviedb.org/3/",
//   params: {
//     api_key: "cb772a50acc4cd6917b12854484b9d91",
//     language: "ko-KR",
//   },
  
// });
// // https://image.tmdb.org/t/p/w300/ApiBzeaa95TNYliSbQ8pJv4Fje7.jpg
// export const movieApi = {
//   nowPlaying: () => request.get("movie/now_playing"),
//   popular: () => request.get("movie/popular"),
//   upComing: () => request.get("movie/upcoming"),
//   // append to response에 대한 설명 https://developers.themoviedb.org/3/get1ting-started/append-to-response
//   movieDetail: (moviePk) =>
//     request.get(`movies/${moviePk}`, {
//       params: { append_to_response: "videos" },
//     }),

//   search: (keyword) =>
//     request.get("search/movie", {
//       params: {
//         query: keyword,
//       },
//     }),
// };