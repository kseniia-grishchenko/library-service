<template>
  <div>
    <el-header>
      <el-page-header title="All books" @back="handleBack">
        <template #content v-if="bookTitle">
          <span>{{ bookTitle }}</span>
        </template>
      </el-page-header>
    </el-header>
  </div>
</template>

<script>
export default {
  props: {
    bookTitle: {
      type: String,
      default: ''
    }
  },
  methods: {
    handleBack() {
      location.hash = '#/';
    }
  }
};
</script>

<style scoped></style>
