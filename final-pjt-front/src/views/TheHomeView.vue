<template>
  <div class="container">
    <reccommend-movie></reccommend-movie>
    <actor-list></actor-list>
  </div>
</template>

<script>
// @ is an alias to /src
import ActorList from '@/components/TheHome/ActorList.vue'
import ReccommendMovie from '@/components/TheHome/RecommendMovie.vue'
export default {
  name: 'TheHomeView',
  components: {
    ActorList, ReccommendMovie
  }
}
</script>
