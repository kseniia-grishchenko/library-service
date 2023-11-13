<template>
  <el-dialog title="Change Password" v-model:visible="modalVisible">
    <el-form ref="form" :model="form" label-position="top">
      <el-form-item label="Current Password">
        <el-input type="password" v-model="form.currentPassword"></el-input>
      </el-form-item>
      <el-form-item label="New Password">
        <el-input type="password" v-model="form.newPassword"></el-input>
      </el-form-item>
      <el-form-item label="Confirm New Password">
        <el-input type="password" v-model="form.confirmNewPassword"></el-input>
      </el-form-item>
    </el-form>
    <span class="dialog-footer">
      <el-button @click="$emit('not-visible')">Cancel</el-button>
      <el-button type="primary" @click="changePassword">Change Password</el-button>
    </span>
  </el-dialog>
</template>

<script>
export default {
  props: {
    visible: {
      type: Boolean,
      default: false
    }
  },
  data() {
    return {
      modalVisible: false,
      form: {
        currentPassword: '',
        newPassword: '',
        confirmNewPassword: ''
      }
    };
  },
  methods: {
    changePassword() {
      // Validate and change password logic
      console.log('Password changed:', this.form);
      this.$emit('not-visible');
    }
  },
  watch: {
    visible: {
      handler(value) {
        this.modalVisible = value;
      },
      immediate: true
    }
  }
};
</script>

<style scoped>
/* Add styles here */
</style>
