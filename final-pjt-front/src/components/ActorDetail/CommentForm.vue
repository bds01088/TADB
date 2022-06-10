<template>
  <div>
    <form class="container" @submit.prevent="onSubmit">
      <div class="input-group mb-3">
        <div class="col-2">
          <select v-model="cha_pk" class="form-select" id="inputGroupSelect02" style="color:black;" required>
            <option value="">배역 선택</option>
            <option v-for="(character, index) in this.actor.character_set" :key="`cha-${index}`" :value="character.id">{{ character.charactername }} 역/  {{title(character)}}</option>
          </select>
          <select v-model="star" class="form-select" id="inputGroupSelect02" style="color:orange;" required>
            <option value="">평점</option>
            <option>★</option>
            <option>★★</option>
            <option>★★★</option>
            <option>★★★★</option>
            <option>★★★★★</option>
          </select>
        </div>
        <input type="text" id="comment" class="form-control col-9" v-model="content" required>
        <button class="btn col-2" style="background-color:#e8eddf">등록</button>
      </div>
    </form>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
export default {
    name : "CommentForm",
    //props:{actor:Object},
    data() {
    return {
      content: '',
      star: '',
      cha_pk: '',
      }
  },
  computed: {
    ...mapGetters(['actor']),
    score(){
      return this.star.length * 2
    },
  },
  methods: {
    ...mapActions(['createComment']),
    onSubmit() {
      // const character_id = this.actor.character_set.find(character=>{
      //   return charcter.actor === this.actor
      // })
      const payload ={ characterPk: this.cha_pk,
      content: this.content, score: this.score  }
      this.createComment(payload)
      this.content = ''
      this.star = ''
      this.cha_pk = ''
    },
    title(character){
      return this.actor.movie.find(movie => {
        return movie.pk === character.movie
      }).title
    },
  }
}
</script>

<style>

</style>