<template>
  <div>
    <h1>Login</h1>

    <account-error-list v-if="authError"></account-error-list>


    <form @submit.prevent="login(credentials)">
      <div>
        <label for="username">username: </label>
        <input v-model="credentials.username" type="text" id="username" required />
      </div>

      <div>
        <label for="password">password: </label>
        <input v-model="credentials.password" type="password" id="password" required />
      </div>

      <button>Login</button>
      <section class="test">
        <div v-on:click="kakaoLoginBtn">카카오 연동</div>
      </section>
    </form>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  import AccountErrorList from '@/components/AccountErrorList.vue'

  export default {
    name: 'LoginView',
    components: {
      AccountErrorList,
    },
    data() {
      return {
        credentials: {
          username: '',
          password: '',
        }
      }
    },
  computed: {
      ...mapGetters(['authError'])
    },
    methods: {
      ...mapActions(['login']),
      kakaoLoginBtn:function(){
        window.Kakao.init('aa452c5f84c318521e387a223f19ccdd') // Kakao Developers에서 요약 정보 -> JavaScript 키

        if (window.Kakao.Auth.getAccessToken()) {
          window.Kakao.API.request({
            url: '/v1/user/unlink',
            success: function (response) {
              console.log(response)
            },
            fail: function (error) {
              console.log(error)
            },
          })
          window.Kakao.Auth.setAccessToken(undefined)
        }


        window.Kakao.Auth.login({
          success: function () {
            window.Kakao.API.request({
              url: '/v2/user/me',
              data: {
                property_keys: ["kakao_account.email"]
              },
              success: async function (response) {
                console.log(response);
              },
              fail: function (error) {
                console.log(error)
              }
            })
          },
          fail: function (error) {
            console.log(error)
          },
        })
      }
    }
  }
</script>

<style scoped>
  .LoginView{ display:flex; justify-content: center; align-items: center; height:100vh; }
  div{ width: 200px; height:40px; background-color:#fdd101; color:white; display:flex; align-items: center; justify-content: center; cursor:pointer; }
</style>
