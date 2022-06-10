<template>
  <div v-if="isProfile" class="container" style="max-width: 800px;">
    <h2 class="text-start my-4">개인정보</h2>
    <div class="card my-2 container" style="max-width: 800px;">
      <div class="row my-4">
        <div class="col-4">
          <img :src="image" class="img-fluid rounded-start" :alt="profile.username">
        </div>
        <div class="col-8 d-flex align-content-between">
          <div class="card-body">
            <h5 class="card-title"> {{ profile.username }}님의 프로필 </h5><hr>
            <p class="card-text row">상세정보</p>
            <p class="card-text row alert alert-primary" style="max-height: 80px; height: 80px;"> {{ profile.overview }}</p>
            <p class="card-text"><small class="text-muted row text-start">가입일: {{ time }}</small></p>
          </div>
        </div>
      </div>
    </div>
    <h2 class="text-start my-4">선호배우</h2>
    <profile-actor-list :actors="actors"></profile-actor-list>
  </div>
</template>

<script>
import ProfileActorList from '@/components/Account/ProfileActorList.vue'
import {mapGetters, mapActions} from 'vuex'
export default {
  name: 'ProfileView',
  components: {ProfileActorList},
  data(){
    return {
      username : this.$route.params.username,
    }
  },
  computed:{
    ...mapGetters(['profile', 'isProfile']),
    image (){
      return 'http://127.0.0.1:8000' + this.profile.image
    },
    time () {
      return  this.profile.date_joined.slice(0,10)
    },
    actors(){
      return this.profile.actors
    }
  },
  methods:{
    ...mapActions(['fetchProfile']),
  },
  created(){
    this.fetchProfile(this.username)
  },



}
</script>

<style>

</style>