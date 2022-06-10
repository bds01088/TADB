import axios from 'axios'
// import router from '@/router'
import drf from '@/api/drf'
import _ from 'lodash'

const HOST_URL = 'http://127.0.0.1:8000/api/v1/movies'

export default {
    state: {
        movies : [],
        keyword : '',
        pickActorMovies: [],
    },
    getters: {
        getMovies : state => state.movies,
        getKeyword : state => state.keyword,
        pickActorMovies: state => state.pickActorMovies,
        ispickActorMovies: state => !_.isEmpty(state.pickActorMovies),
    },
    mutations: {
        SET_MOVIES : (state, movies) => state.movies = movies,
        SET_KEYWORD : (state, keyword) => state.keyword = keyword,
        SET_PICKACTORMOVIES: (state, movies) => state.pickActorMovies = movies,
    },
    actions: {
        fetchMovies({commit}){
            axios.get(HOST_URL)
            .then(response => {
              commit('SET_MOVIES', response.data)
            })
            .catch(error => console.log(error.response))
        },
        fetchKeyword({commit}, keyword){
            commit('SET_KEYWORD', keyword)
        },
        fetchPICKACTORMOVIES({commit}, actorPk){
            axios.get(drf.actors.pick(actorPk))
              .then((res)=>commit('SET_PICKACTORMOVIES', res.data) )
        },
    },
    modules: {
    }
}