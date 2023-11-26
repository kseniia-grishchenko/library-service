<template>
  <el-container v-if="active" class="sign-up">
    <el-form ref="registrationForm" :model="form" :rules="rules" label-position="top">
      <el-form-item label="Email / Username" prop="email" class="form-item">
        <el-input v-model="form.email"></el-input>
      </el-form-item>
      <el-form-item label="Password" prop="password" class="form-item">
        <el-input type="password" v-model="form.password"></el-input>
      </el-form-item>
      <el-form-item class="form-item btn">
        <el-button type="primary" @click="submitForm">Register</el-button>
      </el-form-item>
      <el-link href="#/sign-in">Already have an account? Sign in</el-link>
    </el-form>
  </el-container>
</template>

<script>
import { postRequestUnauthorized } from '../api.js';

export default {
  data() {
    return {
      active: false,
      form: {
        email: '',
        password: ''
      },
      rules: {
        email: [
          { required: true, message: 'Please input email or username', trigger: 'blur' },
          { type: 'email', message: 'Please input a valid email', trigger: ['blur', 'change'] }
        ],
        password: [
          { required: true, message: 'Please input password', trigger: 'blur' },
          { min: 6, message: 'Password length should be at least 6 characters', trigger: 'blur' }
        ]
      }
    };
  },
  methods: {
    submitForm() {
      this.$refs.registrationForm.validate(async (valid) => {
        if (!valid) return;
        // Handle registration logic here
        console.log(this.form);

        try {
          await postRequestUnauthorized('/api/users/', {
            email: this.form.email,
            password: this.form.password,
            first_name: '',
            last_name: ''
          });
          this.$notify({
            title: 'Success',
            message: 'Account created',
            type: 'success',
            showClose: false
          });
          location.hash = '#/sign-in';
        } catch (err) {
          this.$notify.error({
            title: 'Error occurred',
            message: JSON.stringify(err.response.data),
            showClose: false
          });
        }
      });
    },
    hashChangeHandler() {
      this.active = !!location.hash.match(/sign-up/);
    }
  },
  created() {
    window.addEventListener('hashchange', this.hashChangeHandler);
    this.hashChangeHandler();
  }
};
</script>

<style scoped>
.sign-up {
  justify-content: center;
  margin-top: 200px;
}

.form-item.btn {
  margin: 30px 0;
}
</style>
