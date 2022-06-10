<template>
  <div>
    <h1 class="d-flex m-3 justify-content-start">Results of {{getKeyword}}</h1>
    <hr>
    <h2 class="d-flex m-5 justify-content-start">Actors</h2>
    <search-actor-list :keyword="getKeyword"></search-actor-list>
    <hr>
    <h2 class="d-flex m-5 justify-content-start">Movies</h2>
    <search-movie-list :keyword="getKeyword"></search-movie-list>
  </div>
</template>

<script>
import SearchActorList from '@/components/Search/SearchActorList.vue'
import SearchMovieList from '@/components/Search/SearchMovieList.vue'
import {mapGetters} from 'vuex'

export default {
  name: 'SearchView',
  components :{
    SearchActorList,
    SearchMovieList 
  },
  computed : {
    ...mapGetters(['getKeyword'])
  }
}
</script>

<style>

</style>