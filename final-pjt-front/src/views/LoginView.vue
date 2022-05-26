<template>
  <div>
    <h1>Login</h1>
    <form @submit.prevent="login(credentials)">
      <div class="row align-items-center justify-content-center mt-5">
        <div class="col-auto">
          <label for="username" class="col-form-label">username: </label>
        </div>
        <div class="col-auto">
          <input
            v-model="credentials.username"
            type="text"
            class="form-control"
            id="username"
            required
          />
        </div>
      </div>
      <div class="row align-items-center justify-content-center mt-3">
        <div class="col-auto">
          <label for="password" class="col-form-label">password: </label>
        </div>
        <div class="col-auto">
          <input
            v-model="credentials.password"
            type="password"
            class="form-control"
            aria-describedby="passwordHelpInline"
            id="password"
            required
          />
        </div>
      </div>
      <button type="submit" class="d-inline btn btn-primary mt-3">Login</button>
    </form>
    <account-error-list v-if="authError"></account-error-list>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import AccountErrorList from "@/components/AccountErrorList.vue";

export default {
  name: "LoginView",
  components: {
    AccountErrorList,
  },
  data() {
    return {
      credentials: {
        username: "",
        password: "",
      },
    };
  },
  computed: {
    ...mapGetters(["authError"]),
  },
  methods: {
    ...mapActions(["login"]),
  },
};
</script>

<style scoped>
.LoginView {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}
</style>
