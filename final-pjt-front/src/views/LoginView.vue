<template>
  <div>
    <account-error-list v-if="authError"></account-error-list>
    <form @submit.prevent="login(credentials)" class="container" style="max-width: 600px;">
      <h1>LogIn</h1>
      <hr>
      <div class="row mb-3">
        <label for="username" class="text-start form-label">Username</label>
        <input v-model="credentials.username" type="text" class="form-control" id="username" placeholder="ID를 입력해 주세요." required>
      </div>
      <div class="row mb-3">
        <label for="password" class="text-start form-label">Password</label>
        <input v-model="credentials.password" type="password" class="form-control" id="password" placeholder="비밀번호를 입력해 주세요." required>
      </div>
      <div class="row mb-3">
        <button type="submit" class="btn btn-primary">Login</button>    
      </div>
      <hr>
      <div class="row mb-3">  
        <p class="col-9 my-1">아직 저희 TADB의 계정을 생성하지 않았나요?</p>
        <router-link class="col-3 btn btn-primary" :to="{name: 'SignupView'}" >Signup</router-link>
      </div>
    </form>
  </div>
</template>
<script>
  import { mapActions, mapGetters } from 'vuex'
  import AccountErrorList from '@/components/Account/AccountErrorList.vue'
  export default {name: 'LoginView', components: {AccountErrorList,},
    data() { return { credentials: { username: '', password: '', }}},
    computed: {...mapGetters(['authError'])}, 
    methods: {...mapActions(['login'])},} 
</script>