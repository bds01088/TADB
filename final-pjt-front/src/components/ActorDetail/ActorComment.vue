<template>
  <div >
    <div v-for="(comment, index) in this.paginatedData" :key="`comment-${index}`">
      <comment-list :comment="comment"></comment-list>
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
    <comment-form></comment-form>  
  </div>
</template>

<script>
import CommentList from '@/components/ActorDetail/CommentList.vue'
import CommentForm from '@/components/ActorDetail/CommentForm.vue'
import {mapGetters} from 'vuex'
export default {
  name:'ActorComment',
  components: {
    CommentList, CommentForm,
  },
  data () {
    return {
      pageNum: 0
    }
  },
  props:{actor:Object},
  computed:{
    ...mapGetters(['comments']), 
    pageCount () {
        let listlen = this.comments.length
        let listsize = 5
        let page = Math.floor(listlen/listsize)
        if (listlen%listsize > 0) page += 1
        return page
    },
    paginatedData() {
        const start = this.pageNum * 5
        const end = start + 5
        return this.comments.slice(start, end)
    }
  },
  methods : {
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