<template>
  <router-link style="text-decoration:none; color:black;" v-if="actorPk" class="card-title d-inline" :to="{ name: 'ActorDetailView', params: { actorPk: actorPk } }">
    <div class="card p-0 border-0 col m-3 mb-5" style="width:80%">
      <img :src="profileimgURL" class="card-img-top" :alt="actor.name">
      <div class="card-body p-0 d-flex justify-content-between">
        <h5><span class="" style="font-size:1vw;color:black;">{{actor.name}}</span></h5>
        <h5><span class="rounded" style="font-size:1vw; background-color:#eae0d5; color:#5e503f;">{{actorScore}}</span></h5>
      </div>
    </div>
  </router-link>  
</template>

<script>
export default {
    name : "TheActor",
    props : {
        actor : Object,
    },
    computed :{
        profileimgURL (){ 
            return 'https://www.themoviedb.org/t/p/w300_and_h450_bestv2' + this.actor.profile_path
        },
        actorPk (){
          return this.actor.id
        },
        actorScore (){
          if (this.actor.score){
          return Math.round(this.actor.score *10)/10}
          else {
            return "0.0"
          }
        },
    }
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