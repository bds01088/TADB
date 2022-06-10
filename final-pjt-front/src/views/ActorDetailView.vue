<template>
  <div v-if="isActor" class="container my-2">
    <h2 class="text-start" style="font-weight:bold;">상세정보</h2>
    <actor-profile :actorData="actor" style="max-width: 1400px;"></actor-profile><br>
    <h2 class="text-start" style="font-weight:bold;">출연작</h2>
    <actor-movie :actor="actor" style="max-width: 1400px;"></actor-movie>
    <h3 style="font-weight:bold;">댓글</h3>
    <actor-comment :actor="actor"></actor-comment>
  </div>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import ActorProfile from '@/components/ActorDetail/ActorProfile.vue'
import ActorMovie from '@/components/ActorDetail/ActorMovie.vue'
import ActorComment from '@/components/ActorDetail/ActorComment.vue'
export default {
  name: 'ActorDetailView',
  components: {
    ActorProfile, ActorMovie, ActorComment
  },
  data(){
    return {
      actorPk : this.$route.params.actorPk
    }
  },
  computed: {
    ...mapGetters(['actor','isActor',])
  },
  methods: {
    ...mapActions(['fetchActor'])
  },
  created(){
    this.fetchActor(this.actorPk)

  },
}
</script>

<style>

</style>