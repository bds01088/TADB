<template>
  <div id="app" style="font-family: 'Roboto', sans-serif;">
    <nav style="padding:0px; background-color:#e5e5e5;" class="navbar navbar-expand-lg navbar-light">
      <nav-bar></nav-bar>
    </nav>
    <router-view/>
    <footer-bar style="background-color:#e5e5e5;"></footer-bar>
  </div>
</template>

<script>
  import FooterBar from '@/components/FooterBar.vue'
  import NavBar from '@/components/NavBar.vue'
  import { mapActions } from 'vuex'
  export default {
    name: 'App',
    components: {FooterBar, NavBar},
    methods: {
      ...mapActions(['fetchActors','fetchMovies', 'fetchHomeActors'])
    },
    created() {
      this.fetchActors(),
      this.fetchMovies(),
      this.fetchHomeActors()
    },
  }
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}

</style>
