<template>
  <div class="container-fluid">
      <div class="d-flex container-fluid justify-content-between align-items-center" id="navbar">
          <router-link class="mx-2 navbar-brand" :to="{ name: 'TheHomeView' }" style="font-size : 36px; color:#023047;">TADB</router-link>
          <div class="d-flex">
            <input v-show="isActors" style="width:20vw;" v-model="inputkeyword" @keyup.enter="findKeyword" class="form-control me-2" type="text" placeholder="Search" aria-label="Search">
            <button v-show="isActors" @click="findKeyword" class="btn btn-outline-success">Search</button>
            <div v-show="!isActors" class="spinner-border text-success" role="status">
              <span class="visually-hidden">Loading...</span>
            </div>
          </div>
          <div>
            <ul style="font-size: 20px;" class="navbar-nav me-2 d-flex justify-content-between">
              <li class="nav-item" v-if="!isLoggedIn">
                <router-link :to="{ name: 'LoginView' }">Login</router-link>| 
              </li>
              <li class="nav-item" v-if="!isLoggedIn">
                 <router-link :to="{ name: 'SignupView' }">Signup</router-link>
              </li>
              <li class="nav-item" v-if="isLoggedIn">
                <router-link v-if="isCurrentUser" :to="{ name: 'ProfileView', params: { username: currentUser.username } }">
                  {{ currentUser.username }}'s page|
                </router-link>
              </li>
              <li class="nav-item" v-if="isLoggedIn">
                <router-link :to="{ name: 'LogoutView' }">|Logout</router-link>
              </li>
            </ul>
          </div>
      </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
export default {
    name : 'NavBar',
    data (){
      return {
        inputkeyword : ''
      }
    },
    computed: {
      ...mapGetters(['isLoggedIn', 'currentUser', 'isCurrentUser', 'isActors']),
      username() {return this.currentUser.username ? this.currentUser.username : 'guest'},
    },
    methods : {
      ...mapActions(['fetchKeyword']),
      findKeyword() {
        if (this.inputkeyword !== ''){
          this.fetchKeyword(this.inputkeyword)
          this.$router.push({ name : 'SearchView', params : {keyword : this.inputkeyword}})
          .catch(error => {
            throw error
          })
          this.inputkeyword = ''
        }
        else {alert('검색어를 입력해주세요!')}
      }
    },
}
</script>

<style>

</style>