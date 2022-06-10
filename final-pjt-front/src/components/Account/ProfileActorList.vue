<template>
    <div class="card-container row">
      <div v-for="(actor, index) in actodsData" :key="`actor-${index}`" class="col-md-6 col-xl-3">
          <profile-actor :actor="actor"></profile-actor>    
      </div>
    </div>
</template>

<script>
import ProfileActor from '@/components/Account/ProfileActor.vue'
export default {
  name: 'ProfileActorList',
  components: {ProfileActor},
  props: {actors:Array},
  data() {
    return {
      actodsData: this.actors
    }
  },
  methods:{
    change(data){
      this.actodsData = data.sort()
      this.actodsData = this.actodsData.reverse()
    },
  },
  Mounted(){
    this.change(this.actodsData)
  }
}
</script>

<style>

</style>