<template>
  <div>
    <h1>Signup</h1>

    <account-error-list v-if="authError"></account-error-list>

    <form @submit.prevent="signup(credentials)">
      <div class="row align-items-center justify-content-center mt-5">
        <div class="col-auto">
          <label for="username">Username: </label>
        </div>
        <div class="col-auto">
          <input
            v-model="credentials.username"
            type="text"
            id="username"
            class="form-control"
            required
          />
        </div>
      </div>

      <div class="col-auto"></div>

      <div class="row align-items-center justify-content-center">
        <div class="col-auto">
          <label for="password1">Password: </label>
        </div>
        <div class="col-auto">
          <input
            v-model="credentials.password1"
            type="password"
            id="password1"
            required
            class="form-control"
          />
        </div>
      </div>
      <div class="row align-items-center justify-content-center mt-3">
        <div class="col-auto">
          <label for="password2"
            >Password <br />
            Confirmation:</label
          >
        </div>
        <div class="col-auto">
          <input
            v-model="credentials.password2"
            type="password"
            id="password2"
            class="form-control"
            required
          />
        </div>
      </div>
      <div>
        <button class="btn btn-outline-light mt-3">Signup</button>
      </div>
    </form>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import AccountErrorList from "@/components/AccountErrorList.vue";

export default {
  name: "SignupView",
  components: {
    AccountErrorList,
  },
  data() {
    return {
      credentials: {
        username: "",
        password1: "",
        password2: "",
      },
    };
  },
  computed: {
    ...mapGetters(["authError"]),
  },
  methods: {
    ...mapActions(["signup"]),
  },
};
</script>

<style></style>
