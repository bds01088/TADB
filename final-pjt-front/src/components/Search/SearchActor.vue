<template>
  <div class="d-flex card-container">
      <div @click="goActor" class="card-body">
        <img style="" class="card-img-top" :src="profileimgURL" :alt="actor.name">
        <span style="font-size:1vw;">{{actor.name}}</span>
      </div>
  </div>
</template>

<script>
export default {
    name : "SearchActor",
    props : {
        actor : Object
    },
    computed :{
        profileimgURL (){ 
            return 'https://image.tmdb.org/t/p/w138_and_h175_face/' + this.actor.profile_path
        }
    },
    methods :{
        goActor() {
            this.$router.push({ name : 'ActorDetailView', params : {actorPk : this.actor.actorPk}})
            console.log(this.$router.push({ name : 'ActorDetailView', params : {actorPk : this.actor.id}}))
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