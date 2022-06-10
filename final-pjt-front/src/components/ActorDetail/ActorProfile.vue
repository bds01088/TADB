<template>
  <div>
    <div class="card border-0 my-2 container" style="max-width: 1400px;">
      <div class="row">
        <div class="col-4">
          <img :src="image" class="img-fluid rounded-start" :alt="actorData.name">
        </div>
        <div class="col-8 my-2">
          <h3>{{actorData.name}}</h3>
          <hr>
          <div class="row flex-column align-items-start">
            <div class="text-start">
              <p v-if="actorData.birthday" >출생: {{actorData.birthday}}</p>
              <p v-if="actorData.deathday" >사망: {{actorData.deathday}} </p>
              <p v-if="actorData.place_of_birth">출생지: {{actorData.place_of_birth}}</p>
            </div>
            <h5 class="text-end">배우 점수: <span class="rounded badge bg-danger"> {{actorScore}}</span></h5>
            <div class="d-flex">
              <button v-if="!isLike" class="btn ms-auto" style="background-color:#8CC0DE;" @click="likeActor(actorData.id)"> 선호배우 등록 / 현재 {{ like_count }}명 선호</button>
              <button v-if="isLike" class="btn ms-auto" style="background-color:#F47C7C;" @click="likeActor(actorData.id)"> 선호배우 해제 / 현재 {{ like_count }}명 선호</button>
            </div>
          </div> 
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {mapGetters, mapActions} from 'vuex'
export default {
  name: 'ActorProfile',
  props: {actorData:Object},
  computed:{
    ...mapGetters(['currentUser', 'actor']) ,
    image(){
      return this.actorData.profile_path
    },
    actorScore (){
      if (this.actorData.score){
        return Math.round(this.actorData.score *10)/10}
      else {
        return 0
      }
    },
    like_count() {
      return this.actorData.like_users.length
    },
    isLike(){
      return this.actorData.like_users.some(user => {
        return user.pk === this.currentUser.pk
      })
    }
  },
  methods: {
    ...mapActions(['likeActor']),
  }    
}
</script>

<style>

</style>