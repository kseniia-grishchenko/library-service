<template>
  <div class="user-profile" v-if="active">
    <el-card class="box-card">
      <template #header>
        <div class="clearfix">
          <span>Профіль користувача</span>
        </div>
      </template>

      <el-form :model="user" label-position="top">
        <el-form-item label="Імʼя">
          <el-input v-model="user.username" :disabled="!isEditing"></el-input>
        </el-form-item>
        <el-form-item label="Електронна пошта">
          <el-input v-model="user.email" :disabled="!isEditing"></el-input>
        </el-form-item>
        <!-- Add other fields as necessary -->

        <el-form-item v-if="isEditing">
          <el-button type="primary" @click="updateProfile">Зберегти зміни</el-button>
          <el-button @click="isEditing = false">Скасувати</el-button>
        </el-form-item>
        <el-form-item v-else>
          <el-button @click="isEditing = true">Редагувати профіль</el-button>
        </el-form-item>
      </el-form>

      <el-button><el-link href="#/orders">Переглянути історію замовлень</el-link></el-button>
      <el-button @click="isChangePasswordDialogVisible = true">Змінити пароль</el-button>

      <el-button type="danger" @click="promptDeleteConfirmation">Видалити акаунт</el-button>
    </el-card>

    <change-password-dialog
      v-model="isChangePasswordDialogVisible"
      @not-visible="isChangePasswordDialogVisible = false"
    ></change-password-dialog>
    <delete-confirmation-dialog
      v-model="isDeleteConfirmationDialogVisible"
      @not-visible="isDeleteConfirmationDialogVisible = false"
      @confirmDelete="deleteAccount"
    ></delete-confirmation-dialog>
  </div>
</template>

<script>
import ChangePasswordDialog from './ChangePasswordDialog.vue';
import DeleteConfirmationDialog from './DeleteConfirmationDialog.vue';

export default {
  name: 'UserProfile',
  components: {
    ChangePasswordDialog,
    DeleteConfirmationDialog
  },
  data() {
    return {
      active: false,
      user: {
        username: 'JohnDoe',
        email: 'johndoe@example.com'
        // other fields...
      },
      isEditing: false,
      isChangePasswordDialogVisible: false,
      isDeleteConfirmationDialogVisible: false
    };
  },
  methods: {
    updateProfile() {
      // Logic to update profile
      this.isEditing = false;
      console.log('Profile updated:', this.user);
    },
    promptDeleteConfirmation() {
      this.isDeleteConfirmationDialogVisible = true;
    },
    deleteAccount() {
      // Logic to delete account
      console.log('Account deleted');
    },
    hashChangeHandler() {
      this.active = !!location.hash.match(/user-profile/);
    }
  },
  created() {
    window.addEventListener('hashchange', this.hashChangeHandler);
    this.hashChangeHandler();
  }
};
</script>

<style scoped>
.user-profile {
  flex-grow: 1;
  display: flex;
  flex-direction: column;
  gap: 20px;
  margin-top: 100px;
}
</style>
