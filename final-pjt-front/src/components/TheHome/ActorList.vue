<template>
  <div>
    <div class="container">
      <h1 class="m-5 text-start" style="font-size:70px; font-family: 'Koulen', cursive;">Actors</h1>
      <div class="row row-cols-4">
        <the-actor 
          v-for="actor in homeActors" 
          :key="actor.id" 
          :actor="actor">
        </the-actor>
      </div>
    </div>
  </div>
</template>

<script>
import TheActor from '@/components/TheHome/TheActor.vue'

import { mapGetters } from 'vuex'

export default {
    name : "ActorList",
    components : {
      TheActor,
    },
    computed: {
      ...mapGetters(['homeActors'])
    },
    
}
</script>

<style>

</style>