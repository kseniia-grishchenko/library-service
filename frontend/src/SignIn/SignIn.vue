<template>
  <el-container v-if="active" class="sign-in">
    <el-form ref="registrationForm" :model="form" :rules="rules" label-position="top">
      <el-form-item label="Email / Username" prop="email" class="form-item">
        <el-input v-model="form.email"></el-input>
      </el-form-item>
      <el-form-item label="Password" prop="password" class="form-item">
        <el-input type="password" v-model="form.password"></el-input>
      </el-form-item>
      <el-form-item class="form-item btn">
        <el-button type="primary" @click="submitForm">Authorize</el-button>
      </el-form-item>
      <el-link href="#/sign-up">Don't have an account yet? Sign up</el-link>
    </el-form>
  </el-container>
</template>

<script>
import { postRequest } from '../api';

export default {
  data() {
    return {
      active: false,
      form: {
        email: '',
        password: ''
      },
      rules: {
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
        console.log(this.form);
        try {
          const {
            data: { access, refresh }
          } = await postRequest('/api/users/token/', {
            username: this.form.email,
            password: this.form.password
          });

          localStorage.setItem('access', access);
          localStorage.setItem('refresh', refresh);

          this.$emit('log-in');
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
      this.active = !!location.hash.match(/sign-in/);
    }
  },
  created() {
    window.addEventListener('hashchange', this.hashChangeHandler);
    this.hashChangeHandler();
  }
};
</script>

<style scoped>
.sign-in {
  justify-content: center;
  margin-top: 200px;
}

.form-item.btn {
  margin: 30px 0;
}
</style>
