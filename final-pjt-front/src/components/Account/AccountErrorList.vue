<template>
  <div class="account-error-list container text-start" style="max-width: 600px;" >
    <ul v-for="(errors, field) in authError" :key="field">
      <ul v-for="(error, index) in errors" :key="index" >
        <p>{{index +1}}. {{error}}</p>
      </ul>
    </ul>
  </div>
</template>
<script>
  import {mapGetters} from 'vuex'
  export default {
    name: 'AccountErrorList',
    computed: {
      ...mapGetters(['authError']) 
    },
    }
</script>
<style>.account-error-list {color: red;}</style>