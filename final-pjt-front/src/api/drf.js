const HOST = 'http://localhost:8000/api/v1/'

const ACCOUNTS = 'accounts/'
const MOVIES = 'movies/'
const COMMENT = 'comment/'
const ACTORS = 'actors/'
const SEARCH = 'search/'
const HOME = 'home/'
const LIKE = 'like/'
const PICK = 'pick/'

export default {
  accounts: {
    login: () => HOST + ACCOUNTS + 'login/',
    logout: () => HOST + ACCOUNTS + 'logout/',
    signup: () => HOST + ACCOUNTS + 'signup/',
    // Token 으로 현재 user 판단
    currentUserInfo: () => HOST + ACCOUNTS + 'user/', 
    // username으로 프로필 제공
    profile: username => HOST + ACCOUNTS + username,
    // 좋아요 명단 받아오기
    likedActors: username => HOST + ACCOUNTS + `${username}/` + LIKE 
  },
  actors: {
    actors: () => HOST + ACTORS,
    actorDetail: (actorPK) => HOST + ACTORS + `${actorPK}/`,
    comment: (actorPk, commentPk) => HOST + `${actorPk}/` + `${commentPk}/`,
    like: (actorPk) => HOST + ACTORS + `${actorPk}/` + LIKE,
    popular: () => HOST + ACTORS + HOME,
    pick: (actorPk) => HOST + ACTORS + `${actorPk}/` + PICK,
  },
  comment: {
    comments: (actorPk) => HOST + ACTORS + `${actorPk}/` + COMMENT,
    commentCreate: (characterPk) => HOST + ACTORS + `${characterPk}/` + 'comments/',
    comment: (commentPk) => HOST + ACTORS + COMMENT +`${commentPk}/`,
  },

  movies: {
    movie: moviePk => HOST + MOVIES + `${moviePk}/`,
  },
  search: {
    search: (keyword) => HOST + SEARCH + `${keyword}/` 
  }
}