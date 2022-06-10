import axios from 'axios'
import router from '@/router'
import drf from '@/api/drf'
import _ from 'lodash'
export default {
    state: { actors:[],   actor: {}, homeActors:{}, pickActor: {}, likedActors:{}, },
    getters: {
      actors: state => state.actors,
      actor: state => state.actor,
      isActors: state => !_.isEmpty(state.actors),
      isActor: state => !_.isEmpty(state.actor),
      homeActors : state => state.homeActors,
      pickActor: state => state.pickActor,
      likedActors: state => state.likedActors,
      isLikedActors: state => !_.isEmpty(state.likedActors),
    },
    mutations: {
      SET_ACTORS: (state, actors) => state.actors = actors,
      SET_ACTOR: (state, actor) => {
        actor.profile_path = 'https://www.themoviedb.org/t/p/w600_and_h900_bestv2/' + actor.profile_path
        state.actor = actor
      },
      SET_LIKEUSER: (state, likeusers) => state.actor.like_users =likeusers,
      SET_HOMEACTORS: (state, actors) => state.homeActors = actors,
      SET_PICKACTOR: (state) => state.pickActor = _.sample(state.homeActors),
      SET_PICKLIKEDACTORS: (state) => state.pickActor = _.sample(state.likedActors) ,
      SET_LIKEDACTORS: (state, actors) => state.likedActors = actors

    },
    actions: {
      fetchActors({commit}){
        axios.get(drf.actors.actors())
        .then(response => {
          commit('SET_ACTORS', response.data)
        })
        .catch(error =>console.log(error.response))
      
    },
      fetchHomeActors({commit,getters, dispatch}){
        commit
        axios.get(drf.actors.popular())
        .then(res => {commit('SET_HOMEACTORS', res.data)})
        .then(() => commit('SET_PICKACTOR') )
        .then(() => { if(!getters.isCurrentUser){dispatch('fetchPICKACTORMOVIES',getters.pickActor.id)}} )
        .catch(err=> console.log(err.response))
      },
      fetchActor({dispatch, commit, getters}, actorPk){
        axios({
          url: drf.actors.actorDetail(actorPk),
          method: 'GET',
          headers: getters.authHeader, 
        })
          .then(res=>
            {
            commit('SET_ACTOR', res.data)
            dispatch('fetchComments', res.data.id)})
          .catch(err => {
            if (err.response.status === 404){
              router.push({name:'NotFound404'})  
            } else if (err.response.status === 401){
              router.push({ name: 'LoginView'}) }
        })
      },
      changeScore({getters}, actorId){
        getters.actors.find(actor => {
          return actor.actor_id === actorId
        })
      },
      likeActor({ commit, getters}, actorPk) {
        axios({
          url: drf.actors.like(actorPk),
          method:'POST',
          headers: getters.authHeader,
        })
          .then(res =>
            {commit ('SET_LIKEUSER', res.data.like_users)
            commit('SET_PROFILE', {})
          }
           )
          .catch(err=> console.log(err.response))
      }
    },
    modules: {   
    },
}