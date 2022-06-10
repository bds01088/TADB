<template>
  <router-link v-if="isData" style="text-decoration:none; color:black;"  :to="{ name: 'ActorDetailView', params: { actorPk: actorPk } }">
    <div class="card p-0 border-0 col m-3 mb-5" style="width:80%">
      <img :src="profileimgURL" class="card-img-top" alt="">
      <div class="card-body p-0 d-flex justify-content-between">
        <h5><span class="p-0 badge" style="font-size:0.8rem;color:black;">{{actor.name}}</span></h5>
        <h5><span class="rounded" style="font-size:20px; background-color:#eae0d5; color:#5e503f;">{{actorScore}}</span></h5>
      </div>
    </div>
  </router-link>
</template>

<script>
import _ from 'lodash'
export default {
  name: 'ProfileActor',
  props: {actor:Object},
  computed :{
    profileimgURL (){ 
        return 'https://www.themoviedb.org/t/p/w300_and_h450_bestv2' + this.actor.profile_path
    },
    actorPk (){
      return this.actor.pk
    },
    actorScore (){
      if (this.actor.score){
      return Math.round(this.actor.score *10)/10}
      else {
        return 0
      }
    },
    isData(){
      return !_.isEmpty(this.actor)
    }
  },
}
</script>

<style>

</style>