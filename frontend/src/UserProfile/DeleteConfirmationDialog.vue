<template>
  <el-dialog title="Confirm Deletion" v-model:visible="modalVisible">
    <p>Are you sure you want to delete your account? This action cannot be undone.</p>
    <template #footer>
      <span class="dialog-footer">
        <el-button @click="$emit('not-visible')">Cancel</el-button>
        <el-button type="danger" @click="confirmDeletion">Delete Account</el-button>
      </span>
    </template>
  </el-dialog>
</template>

<script>
export default {
  data: () => ({
    modalVisible: false
  }),
  props: {
    visible: {
      type: Boolean,
      default: false
    }
  },
  emits: ['confirmDelete'],
  methods: {
    confirmDeletion() {
      this.$emit('confirmDelete');
      this.$emit('not-visible');
    }
  },
  watch: {
    visible: {
      handler(value) {
        console.log(value);
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
