<template>
  <div style="height:1000px;">
    <div v-if="searchMovies.length > 0">
      <h3>We Found {{searchMovies.length}} Movies</h3>
      <div class="container" style="height:800px;">
        <div class="card-container d-flex row row-cols-6">
          <search-movie
            v-for="movie in paginatedData"
            :key="movie.movie_id"
            :movie="movie"
          >
          </search-movie>      
        </div>    
      </div>
      <div class="btn-cover">
        <button :disabled="pageNum === 0" @click="prevPage" class="page-btn">
        이전
        </button>
        <span class="page-count">{{ pageNum + 1 }} / {{ pageCount }} 페이지</span>
        <button :disabled="pageNum >= pageCount - 1" @click="nextPage" class="page-btn">
        다음
        </button>
      </div>
    </div>
    <div v-else>
        <h3> Not found results </h3>
    </div>
  </div>
</template>

<script>
import SearchMovie from './SearchMovie.vue'
import { mapGetters } from 'vuex'

export default {
    name: "SearchMovieList",
    data () {
      return {
        pageNum: 0
      }
    },
    components: {
      SearchMovie
    },
    props : {
      keyword : String
    },
    computed : {
      ...mapGetters(['getMovies']),
      searchMovies() {
        const filtered = this.getMovies.filter((movie) =>
            movie.title.toLowerCase().includes(this.keyword.toLowerCase())
        )
        this.resetPage()
        return filtered
      },
      pageCount () {
        let listlen = this.searchMovies.length
        let listsize = 12
        let page = Math.floor(listlen/listsize)
        if (listlen%listsize > 0) page += 1
        return page
      },
      paginatedData() {
        const start = this.pageNum * 12
        const end = start + 12
        return this.searchMovies.slice(start, end)
      }
    },
    methods : {
      nextPage() {
        this.pageNum += 1
      },
      prevPage() {
        this.pageNum -= 1
      },
      resetPage(){ 
        this.pageNum = 0
      }
    }
}
</script>

<style>
.btn-cover {
  margin-top: 1.5rem;
  text-align: center;
}
.btn-cover .page-btn {
  width: 5rem;
  height: 2rem;
  letter-spacing: 0.5px;
}
.btn-cover .page-count {
  padding: 0 1rem;
}
</style>