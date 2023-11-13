<template>
  <el-card class="leave-review-card">
    <template #header>
      <div class="header">
        <span>Leave a Review</span>
      </div>
    </template>

    <el-form ref="form" :model="reviewForm" label-position="top">
      <el-form-item label="Rating">
        <el-rate v-model="reviewForm.rating"></el-rate>
      </el-form-item>
      <el-form-item label="Your Review">
        <el-input
          type="textarea"
          v-model="reviewForm.content"
          :rows="4"
          placeholder="Share your thoughts about the book"
        ></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="submitReview">Submit Review</el-button>
      </el-form-item>
    </el-form>
  </el-card>
</template>

<script>
export default {
  data() {
    return {
      reviewForm: {
        rating: 0,
        content: ''
      }
    };
  },
  methods: {
    submitReview() {
      // Validate and submit review logic
      console.log('Review submitted:', this.reviewForm);
      this.resetForm();
    },
    resetForm() {
      this.reviewForm.rating = 0;
      this.reviewForm.content = '';
    }
  }
};
</script>

<style scoped>
.leave-review-card {
  max-width: 600px;
  margin: 20px auto;
}
</style>
