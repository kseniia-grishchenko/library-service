<template>
  <el-card class="review-card">
    <div class="review-header">
      <span class="reviewer-name">{{ review.reviewerName }}</span>
      <span class="review-date">{{ formattedDate }}</span>
    </div>
    <el-rate :value="review.rating" disabled show-score class="review-rating"></el-rate>
    <div class="review-content">
      {{ review.content }}
    </div>
  </el-card>
</template>

<script>
export default {
  name: 'ReviewCard',
  props: {
    review: {
      type: Object,
      required: true
    }
  },
  computed: {
    formattedDate() {
      const date = new Date(this.review.date);
      return date.toLocaleDateString(undefined, { year: 'numeric', month: 'long', day: 'numeric' });
    }
  }
};
</script>

<style scoped>
.review-card {
  margin-bottom: 20px;
}

.review-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
}

.reviewer-name {
  font-weight: bold;
}

.review-date {
  color: #999;
  font-size: 0.85em;
}

.review-rating {
  margin-bottom: 10px;
}

.review-content {
  line-height: 1.5;
}
</style>
