<template>
  <div class="d-flex card-container">
      <div @click="goTMDB" class="card-body">
        <img class="card-img-top" :src="posterimgURL" :alt="movie.title">
        <span style="font-size:1vw;">{{movie.title}}</span>
      </div>
  </div>
</template>

<script>
export default {
    name : "SearchMovie",
    props: {
        movie : Object
    },
    computed :{
        posterimgURL (){ 
            return 'https://www.themoviedb.org/t/p/w220_and_h330_face/' + this.movie.poster_path
        }
    },
    methods : {
        goTMDB () {
            window.open("about:blank").location.href='https://www.themoviedb.org/movie/'+this.movie.movie_id
        }
    }    
}
</script>

<style scoped>
.card-container:hover { 
  cursor: pointer;
  transform: scale(1.1);
  transition: transform 1s;
  filter: brightness(70%);
}
</style>