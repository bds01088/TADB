import Vue from 'vue'
import Vuex from 'vuex'
import accounts from '@/store/modules/accounts'
import actors from '@/store/modules/actors'
import movies from '@/store/modules/movies'
import comments from '@/store/modules/comments'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    accounts, actors, movies, comments
  }
})
