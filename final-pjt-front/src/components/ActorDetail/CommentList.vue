<template>
  <div v-if="isComments" class="container mb-1">
    <div class="card">
      <div class="card-header row m-0 p-1">
        <h6 class="text-start col-8 mt-2">{{ character(this.comment.character).charactername }} 역/ {{title(character(this.comment.character))}}</h6>
        <div class="text-end col-4" v-if="this.comment.user.id === currentUser.pk">
          <button v-show="!isEditing" @click="editing(comment.id)" class=" btn btn-primary ms-auto">수정</button>
          <button v-show="!isEditing" @click="deleteComment(comment.id)" class="btn btn-danger">삭제</button>

          <button v-show="isEditing" @click="editComment(comment.id)" class="ms-auto btn btn-primary">수정</button>
          <button v-show="isEditing" @click="editing(comment.id)" class="btn btn-danger">취소</button>
        </div>
      </div>
      <div v-show="!isEditing" class="card-body">
        <div class="row">
          <p class="card-text text-start col-lg-8 col-sm-8">{{ comment.content }}</p>
          <div class="ms-auto col-lg-2 col-sm-4">
            <button class="card-text justify-content-end ms-auto btn btn-outline-danger mb-1" style="color:orange;">{{star(this.comment.score)}}</button>
            <p class="card-text justify-content-end" style="">작성일: {{ this.comment.time.slice(0,10) }}</p>
            <p class="m-0">작성자: {{ this.comment.user.username }}</p>
          </div>
        </div>
      </div>
      <div v-if="isEditing" class="card-body">
        <div class="container d-flex flex-row">
          <select v-if="isCommentData"  v-model="commentData.score" class="form-select mx-1" id="inputGroupSelect02" style="color:orange; width: 130px;" required>
              <option value="0">평점</option>
              <option value="2">★</option>
              <option value="4">★★</option>
              <option value="6">★★★</option>
              <option value="8">★★★★</option>
              <option value="10">★★★★★</option>
          </select>
          <input v-if="isCommentData" type="text" id="comment" class="form-control" v-model="commentData.content" required>
        </div>
      </div>
    </div> 
  </div>
</template>

<script>
import {mapGetters, mapActions} from 'vuex'
export default {
    name : "CommentList",
    data() {
      return {
      isEditing: false,
      score: this.comment.score.toString(),
      content: this.comment.content,
      }
    },
    props: {
      comment:Object,
    },
    computed: {
      ...mapGetters(['actor', 'isComments','currentUser', 'isCommentData', 'commentData', 'comments']),
    },
    methods: {
      ...mapActions(['deleteComment', 'editing', 'updateComment', 'fetchComment']),
      title(character){
      return this.actor.movie.find(movie => {
        return movie.pk === character.movie
        }).title
      },
      character(characterId){
        return this.actor.character_set.find(character =>{
          return character.id === characterId
        })
      },
      characterName(characterId){
        return this.actor.character_set.find(character =>{
          return character.id === characterId
        }).charactername
      },
      star(score){
        return '★'.repeat(score/2)
      },
      editComment(commentId){
        const data = {commentPk: commentId , content: this.commentData.content, score: parseInt(this.commentData.score)}
        this.updateComment(data)
        this.editing()
      },
      // 수정모드
        editing(commentPk){
          this.isEditing = !this.isEditing
          if (this.isEditing) {
            const comment = this.comments.find(comment=>{
              return comment.id === commentPk })
            this.fetchComment(comment)
          } else {
            this.fetchComment({})
          }   
        },
    }
}
</script>

<style>

</style>