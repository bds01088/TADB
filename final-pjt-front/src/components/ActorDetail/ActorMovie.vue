<template>
  <div class="card-container">
    <div class="row">
      <div v-for="movie in paginatedData" :key="movie.pk" class="col-sm-6 col-md-4 col-xl-3">
        <div class="card mb-5">
          <img :src="movie.poster_path" class="card-img-top" :alt="movie.title">
          <div class="card-body ">
            <div class="card-title row">
              <h5><div class="col badge bg-secondary">{{ movie.title }}</div></h5>
              <h5><div class="col badge bg-secondary">{{character(movie.pk)}}</div></h5>
            </div>
            <div class="card-text row">
              <div class="col-7">
                <h6 class="d-flex card-text text-start" style="">배우 점수: <span class="mx-1">{{ score(movie.pk) }}</span></h6>
                <h6 class="d-flex card-text text-start">영화 점수: <span class="mx-1">{{movie.vote_average}}</span></h6>
              </div>
              <div class="col-5">
                <button @click="goTMDB(movie.movie_id)" class="btn text-light text-end" style="background-color:#22333b;">TMDB</button>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="btn-cover mb-5">
        <button :disabled="pageNum === 0" @click="prevPage" class="page-btn">
        이전
        </button>
        <span class="page-count">{{ pageNum + 1 }} / {{ pageCount }} 페이지</span>
        <button :disabled="pageNum >= pageCount - 1" @click="nextPage" class="page-btn">
        다음
        </button>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: 'ActorMovie',
  props:{actor:Object},
  data () {
    return {
      pageNum: 0
    }
  },
  computed:{
    movies(){
      this.actor.movie.map(movie => {
        movie.poster_path = 'https://www.themoviedb.org/t/p/w600_and_h900_bestv2' + movie.poster_path
      })
      return this.actor.movie
    }, 
    pageCount () {
        let listlen = this.movies.length
        let listsize = 8
        let page = Math.floor(listlen/listsize)
        if (listlen%listsize > 0) page += 1
        return page
    },
    paginatedData() {
        const start = this.pageNum * 8
        const end = start + 8
        return this.movies.slice(start, end)
    }
  },
  methods: {
    character(movieid){
      return (this.actor.character_set.find((character) => {
        return character.movie === movieid 
      })).charactername
    },
    score(movieid){
      if ((this.actor.character_set.find((character) => {
        return character.movie === movieid })).score) {
      return Math.round((this.actor.character_set.find((character) => {
        return character.movie === movieid })).score *10)/10 }
      else {
        return 0
      }
    },
    goTMDB (movieid) {
        window.open("about:blank").location.href='https://www.themoviedb.org/movie/'+ movieid
    },
    nextPage() {
      this.pageNum += 1
    },
    prevPage() {
      this.pageNum -= 1
    },
  }
}
</script>

<style>

</style>