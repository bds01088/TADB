<template>
  <div v-if="ispickActorMovies" class="container row">
    <h1 class="m-5 text-start col-12" style="font-size:70px; font-family: 'Koulen', cursive;">Recommend Actor's Movie</h1>
    <div class="d-flex col-3">
      <div @click="goActor" class="card-body" style="padding:0px;">
        <img class="card-img-top" :src="profileimgURL" :alt="actorName">
        <div class="card-body d-flex justify-content-between" style="padding:0px;" >
          <h5><span class="col-9 text-start" style="font-size:15px;color:black;">{{actorName}}</span></h5>
          <h5><span class="rounded" style="font-size:1vw; background-color:#eae0d5; color:#5e503f;">{{actorScore}}</span></h5>
        </div>
      </div>
    </div>
    <div class="container justify-content-around d-flex col-9 border border-3" style="border-color: #30475E!important;">
      <div v-for="(character, index) in pickActorMovies" :key="`character-${index}`" class="container col-4 row">
        <reco-movie :character="character"></reco-movie>    
      </div>
    </div>
  </div>
</template>
<script>
import RecoMovie from '@/components/TheHome/RecoMovie.vue'
import {mapGetters} from 'vuex'
export default {
  name:'ReccommendMovie.vue',
  components:{ RecoMovie },
  computed:{
    ...mapGetters(['pickActorMovies', 'ispickActorMovies',]),
    profileimgURL (){ 
        return 'https://www.themoviedb.org/t/p/w300_and_h450_bestv2' + this.pickActorMovies[0].actor.profile_path
    },
    actorPk (){
      return this.pickActorMovies[0].actor.pk
    },
    actorScore (){
      if (this.pickActorMovies[0].actor.score){
      return Math.round(this.pickActorMovies[0].actor.score *10)/10}
      else {
        return "0.0"
      }
    },
    actorName(){
      return this.pickActorMovies[0].actor.name
    },
  },
  methods :{
    goActor() {
      this.$router.push({ name : 'ActorDetailView', params : {actorPk : this.pickActorMovies[0].actor.pk}})
    }
    }
}
</script>

<style scoped>
.card-body:hover { 
  cursor: pointer;
  transform: scale(1.1);
  transition: transform 1s;
  filter: brightness(70%);
}
</style>