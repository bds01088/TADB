import Vue from 'vue'
import VueRouter from 'vue-router'
import TheHomeView from '@/views/TheHomeView.vue'
import ActorDetailView from '@/views/ActorDetailView.vue'
import LoginView from '@/views/LoginView.vue'
import LogoutView from '@/views/LogoutView.vue'
import MovieDetailView from '@/views/MovieDetailView.vue'
import ProfileView from '@/views/ProfileView.vue'
import SearchView from '@/views/SearchView.vue'
import SignupView from '@/views/SignupView.vue'
import NotFound404 from '@/views/NotFound404.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'TheHomeView',
    component: TheHomeView
  },
  {
    path: '/accounts/logout',
    name: 'LogoutView',
    component: LogoutView
  },
  {
    path: '/accounts/login',
    name: 'LoginView',
    component: LoginView
  },
  {
    path: '/accounts/signup',
    name: 'SignupView',
    component: SignupView
  },
  {
    path: '/accounts/:username',
    name: 'ProfileView',
    component: ProfileView
  },
  {
    path: '/movies/:movieid',
    name: 'MovieDetailView',
    component: MovieDetailView
  },
  {
    path: '/actors/:actorPk',
    name: 'ActorDetailView',
    component: ActorDetailView
  },
  {
    path: '/search/:keyword',
    name: 'SearchView',
    component: SearchView
  },
  {
    path: '/404',
    name: 'NotFound404',
    component: NotFound404
  },
  {
    path: '*',
    redirect: '/404',
  }
  
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
