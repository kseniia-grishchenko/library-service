<template>
  <div>
    <review-card v-for="review in reviews" :key="review.id" :review="review"></review-card>
  </div>
</template>

<script>
import reviews from '../assets/reviews.js';
import ReviewCard from './ReviewCard.vue';

export default {
  props: {
    bookId: {
      type: Number
    }
  },
  data() {
    return {
      reviews: []
    };
  },
  watch: {
    bookId: {
      handler(id) {
        this.reviews = reviews.filter((review) => review.bookId === id);
      },
      immediate: true
    }
  },
  components: {
    ReviewCard
  }
};
</script>
