import axios from 'axios'
// import router from '@/router'
import drf from '@/api/drf'
import _ from 'lodash'

export default {
    state: {
       comments: [],
       commentData: { },
     },
    getters: {
      comments: state => state.comments,
      commentData: state =>  state.commentData,
      isCommentData: state => !_.isEmpty(state.commentData),
      isComments: state=> !_.isEmpty(state.comments),
    },
    mutations: {
      SET_COMMENTS: (state, comments) => state.comments = comments,
      SET_COMMENTDATA: (state, comment) => state.commentData = comment,
    },
    actions: {
        createComment({ dispatch, getters }, { characterPk, content, score }) {
            const comment = { content, score }   
            axios({
              url: drf.comment.commentCreate(characterPk),
              method: 'POST',
              data: comment,
              headers: getters.authHeader,
            }) //입력 후 새 댓글 내용으로 바꾸기
              .then(() => {
                dispatch('fetchComments', getters.actor.id)
                dispatch('fetchActor', getters.actor.id)
                dispatch('fetchHomeActors')
              })
              .catch(err => console.error(err.response))
          },

          updateComment({ dispatch, getters }, { commentPk, content, score }) {
            const comment = { content, score }      
            axios({
              url: drf.comment.comment(commentPk),
              method: 'PUT',
              data: comment,
              headers: getters.authHeader,
            })
              .then(() => {
                dispatch('fetchComments', getters.actor.id)
                dispatch('fetchActor', getters.actor.id)
                dispatch('fetchHomeActors')
              })
              .catch(err => console.error(err.response))
          },
      
          deleteComment({ dispatch, getters }, commentPk) {
              if (confirm('평가를 삭제할까요?')) {
                axios({
                  url: drf.comment.comment(commentPk),
                  method: 'DELETE',
                  headers: getters.authHeader,
                })
                  .then(() => {
                    dispatch('fetchComments', getters.actor.id)
                    dispatch('fetchActor', getters.actor.id)
                    dispatch('fetchHomeActors')
                  })
                  .catch(err => console.error(err.response))
              }
            },

        // 매번사용할 댓글 목록 불러오기  
        fetchComments({commit, getters}, actorPk){
          axios({
            url: drf.comment.comments(actorPk),
            method: 'GET',
            headers: getters.authHeader 
          })
            .then(res => {commit('SET_COMMENTS', res.data)
        })
            .catch(err => console.error(err.response)) 
        },
        fetchComment({commit}, data) {
          commit('SET_COMMENTDATA', data)
        }
     },
    modules: {
    }
}