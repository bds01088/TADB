<template>
  <div>
    <account-error-list v-if="authError"></account-error-list>
    <form @submit.prevent="signup(data)" class="container" style="max-width: 600px;">
      <h1>Sign up</h1>
      <hr>
      <div class="row mb-3">
        <label for="username" class="text-start form-label">UserName:</label>
        <input v-model="data.username" type="text" class="form-control" id="username" placeholder="사용할 이름을 입력해 주세요." required/>
      </div>
      <div class="row mb-3">
        <label for="password1" class="text-start form-label">Password:</label>
        <input class="form-control" v-model="data.password1" type="password" id="password1" placeholder="사용할 비밀번호를 입력해 주세요." required />
      </div>
      <div class="row mb-3">
        <label for="password2" class="text-start form-label">Confirm Password:</label>
        <input class="form-control" v-model="data.password2" type="password" id="password2" placeholder="사용할 비밀번호를 확인을 위해 다시 입력해 주세요." required />
      </div>
      <div class="row mb-3">
        <button class="offset-10 col-2 btn btn-primary">Signup</button>
      </div>
    </form>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  import AccountErrorList from '@/components/Account/AccountErrorList.vue'

  export default {
    name: 'SignupView',
    components: {
      AccountErrorList,
    },
    data() {
      return {
        data: {username: '', password1: '', password2: '',}
      }
    },
    computed: {
      ...mapGetters(['authError'])
    },
    methods: {
      ...mapActions(['signup'])
    },
  }
</script>

<style></style>
