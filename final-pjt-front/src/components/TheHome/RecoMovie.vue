<template>
  <div class="d-flex align-self-center">
    <div @click="goTMDB" class="card" style="border:0px;">
      <img class="card-img-top" :src="poster_path" :alt="title">
      <div class="card-body p-0 d-flex justify-content-between">
        <div class="row align-items-center">
          <span class="text-start" style="font-size:0.9vw;">{{title}}</span>
          <p class="text-start mb-0" style="font-size:0.9vw;">{{character.charactername}} 역</p>
        </div>
        <div class="row align-items-center">
          <h5><span class="rounded" style="font-size:0.5vw; background-color:#eae0d5; color:#5e503f;">{{character.movie.vote_average}}</span></h5>
          <h5><span class="rounded" style="font-size:0.5vw; background-color:#eae0d5; color:#5e503f;">{{character.score}}</span></h5>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'RecoMovie',
  props:{character:Object},
  computed:{
    title(){
      return this.character.movie.title
    },
    poster_path (){
      return 'https://www.themoviedb.org/t/p/w600_and_h900_bestv2/' + this.character.movie.poster_path  
    },
    score(){
      return this.character.movie.score
    }  
  },
  methods : {
    goTMDB () {
    window.open("about:blank").location.href='https://www.themoviedb.org/movie/'+ this.character.movie.movie_id
    }
  },  
}
</script>

<style scoped>
.card:hover { 
  cursor: pointer;
  transform: scale(1.1);
  transition: transform 1s;
  filter: brightness(70%);
}
</style>