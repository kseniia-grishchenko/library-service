<template>
  <el-row v-if="active">
    <el-col :span="10">
      <div>
        <el-image :src="book.image" fit="contain">
          <template #error>
            <div class="image-slot">
              <el-icon><icon-picture /></el-icon>
            </div>
          </template>
        </el-image>
        <leave-review-card></leave-review-card>
      </div>
    </el-col>
    <el-col :span="2"></el-col>
    <el-col :span="12">
      <div class="header">
        <h3>{{ book.title }}</h3>
        <el-button @click="$emit('add-to-cart', book.id)">{{
          !inCart ? 'Add to cart' : 'Remove from cart'
        }}</el-button>
      </div>

      <div class="authors">
        <span class="author" v-for="(author, index) in book.authors" :key="index">
          {{ author.full_name }}
        </span>
      </div>
      <div class="description">{{ book.description }}</div>
      <div class="genres">
        <span class="genre" v-for="(genre, index) in book.genres" :key="index">
          {{ genre.name }}
        </span>
      </div>
      <review-list :bookId="book.id"></review-list>
    </el-col>
  </el-row>
</template>

<script>
import { Picture as IconPicture } from '@element-plus/icons-vue';
import books from '../assets/books.js';
import ReviewList from './ReviewList.vue';
import LeaveReviewCard from './LeaveReviewCard.vue';

export default {
  data: () => ({
    active: false,
    book: {}
  }),
  props: {
    inCart: {
      type: Boolean,
      default: false
    }
  },
  methods: {
    hashChangeHandler() {
      const match = location.hash.match(/book\?id=(\d+)/);
      this.active = !!match;
      this.book = {};
      if (!this.active) return;
      const [, bookId] = match;
      this.fetchBook(bookId);
    },
    fetchBook(bookId) {
      // replace with API call to /books?id=
      this.book = books.find((book) => book.id === Number(bookId));
    }
  },
  watch: {
    book(book) {
      this.$emit('book-selected', book);
    }
  },
  created() {
    window.addEventListener('hashchange', this.hashChangeHandler);
    this.hashChangeHandler();
  },
  components: {
    ReviewList,
    IconPicture,
    LeaveReviewCard
  }
};
</script>

<style scoped>
h3 {
  margin: 0;
  font-size: 24px;
  color: #222;
}

.authors {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.author {
  font-size: 16px;
  color: #626b77;
}

.description,
.genres {
  margin: 12px 0 24px;
}

.description {
  color: #5b636f;
  font-weight: 500;
  font-size: 14px;
}

.description::before {
  content: 'Description: ';
  margin-right: 8px;
  font-weight: 500;
  color: #222;
}

.genres {
  display: flex;
  align-items: flex-start;
  gap: 6px;
}

.genres span {
  color: #5b636f;
  font-weight: 500;
  font-size: 14px;
}

.genres:before {
  content: 'Genres: ';
  font-weight: 500;
  font-size: 15px;
  color: #222;
}

.section {
  font-size: 15px;
  color: #222;
  font-weight: 500;
}

.image-slot {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100%;
  background: var(--el-fill-color-light);
  color: var(--el-text-color-secondary);
  font-size: 30px;
  min-height: 400px;
}
.image-slot .el-icon {
  font-size: 30px;
}

.el-image {
  padding: 0 5px;
  width: 100%;
  height: 100%;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
</style>
