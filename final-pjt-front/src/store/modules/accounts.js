import axios from 'axios'
import router from '@/router'
import drf from '@/api/drf'
import _ from 'lodash'

export default {
    state: {
      token: '', currentUser: {},
      profile: {}, authError: null,  
    },
    getters: {
      isLoggedIn: state => !!state.token,
      currentUser: state => state.currentUser,
      profile: state => state.profile,
      authError: state => state.authError,
      authHeader: state => ({Authorization: `Token ${state.token}`}),
      isCurrentUser: state=> !_.isEmpty(state.currentUser),
      isProfile: state=> !_.isEmpty(state.profile),
    },
    mutations: {
      SET_TOKEN:(state, token) => state.token = token,
      SET_CURRENT_USER: (state, user) => state.currentUser = user,
      SET_PROFILE: (state, profile) => state.profile = profile,
      SET_AUTH_ERROR: (state, error) => state.authError = error, 
    },
    actions: {
      saveToken({ commit }, token) { commit('SET_TOKEN', token) //토큰 저장
      localStorage.setItem('token', token) },
      removeToken({ commit }) {commit('SET_TOKEN', '') // 토큰 삭제
      localStorage.setItem('token', '') },

      fetchCurrentUser({commit, getters, dispatch}) {
        if (getters.isLoggedIn) {	
          axios({ url: drf.accounts.currentUserInfo(), method: 'GET',
            headers: getters.authHeader, }) 
            .then(res => { commit('SET_CURRENT_USER', res.data)
              dispatch('fetchLikedActors', res.data.username)}) 
            .catch(err => { if (err.response.status === 401) { dispatch('removeToken')
              router.push({ name: 'LoginView' }) }}) } },
 
      login({ commit, dispatch }, credentials) { 
        axios({ url: drf.accounts.login(),
          method: 'POST', data: credentials })
          .then(res => { const token = res.data.key 
            dispatch('saveToken', token) 
            dispatch('fetchCurrentUser')
            commit('SET_AUTH_ERROR', '')})
          .then(() => router.push({ name: 'TheHomeView' }))
          .catch(err => { commit('SET_AUTH_ERROR', err.response.data) }) },
          
      logout({ getters, dispatch, commit }) {
        axios({ url: drf.accounts.logout(), method: 'POST',
          headers: getters.authHeader, }) 
          .then(() => { dispatch('removeToken')
            commit('SET_PROFILE', {}) 
            router.push({ name: 'TheHomeView'}) })
          .catch(err => {console.error(err.response) }) },

      fetchProfile({ commit, getters }, username ) {
        axios({ url: drf.accounts.profile(username), 
          method: 'GET',
          headers: getters.authHeader})
          .then(res => {commit('SET_PROFILE', res.data)})
          .catch(err =>{
            if (err.response.status === 404) {
              router.push({ name: 'NotFound404' })
            }
          })
          },

      signup({ commit, dispatch }, credentials) {
        axios({ url: drf.accounts.signup(), method: 'post', data: credentials })
          .then(res => { const token = res.data.key
            dispatch('saveToken', token)
            dispatch('fetchCurrentUser')
            commit('SET_AUTH_ERROR', '')
            router.push({ name: 'TheHomeView' }) })
          .catch(err => { commit('SET_AUTH_ERROR', err.response.data) }) },

      fetchLikedActors({getters, commit, dispatch}, username){
        axios({
          url: drf.accounts.likedActors(username),
          method: 'GET',
          headers: getters.authHeader
         })
          .then(res => commit('SET_LIKEDACTORS', res.data.actors))
          .then(()=>
            {if (getters.isLikedActors) {commit('SET_PICKLIKEDACTORS')}} )
            
          .then(() => {dispatch('fetchPICKACTORMOVIES', getters.pickActor)} )
          .catch(err=> console.log(err.response))
      }
    },
}