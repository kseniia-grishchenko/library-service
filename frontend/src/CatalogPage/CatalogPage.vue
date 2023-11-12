<template>
  <el-container>
    <el-header>
      <el-page-header @back="goBack">
        <template #content>
          <span class="text-large font-600 mr-3"> Title </span>
        </template>
      </el-page-header>
    </el-header>
    <el-container>
      <el-aside>
        <filter-select
          section-name="Genres"
          :filter-options="genres"
          :checked-options="checkedGenres"
          @filter-changed="handleGenreFilterChange"
          @filter-reset="resetGenres"
        ></filter-select>
        <filter-select
          section-name="Authors"
          :filter-options="authors"
          :checked-options="checkedAuthors"
          @filter-changed="handleAuthorFilterChange"
          @filter-reset="resetAuthors"
        ></filter-select>
      </el-aside>
      <el-main>
        <div class="items-container">
          <div v-for="book in filteredItems" :key="book.id">
            <el-card :body-style="{ padding: '10px' }">
              <el-image :src="book.image" fit="contain">
                <template #error>
                  <div class="image-slot">
                    <el-icon><icon-picture /></el-icon>
                  </div>
                </template>
              </el-image>
              <div style="padding: 14px">
                <span class="title">{{ book.title }}</span>
                <div class="bottom">
                  <span class="author">{{ book.author }}</span>
                </div>
              </div>
            </el-card>
          </div>
        </div>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
import { Picture as IconPicture } from '@element-plus/icons-vue';
import FilterSelect from './FilterSelect.vue';
import books from '../assets/books.js';
import genres from '../assets/genres.js';
import authors from '../assets/authors.js';

export default {
  components: {
    FilterSelect,
    IconPicture
  },
  data() {
    return {
      books,
      genres,
      authors,
      checkedGenres: [],
      checkedAuthors: []
    };
  },
  computed: {
    filteredItems() {
      if (!this.checkedGenres.length && !this.checkedAuthors.length) return this.books;

      let filteredBooks = this.books;

      if (this.checkedGenres.length) {
        filteredBooks = filteredBooks.filter((book) => {
          const bookGenres = book.genres.map((genre) => genre.name);
          return bookGenres.some((genre) => this.checkedGenres.includes(genre));
        });
      }
      if (this.checkedAuthors.length) {
        filteredBooks = filteredBooks.filter((book) => {
          const bookAuthors = book.authors.map((author) => author.full_name);
          return bookAuthors.some((author) => this.checkedAuthors.includes(author));
        });
      }

      return filteredBooks;
    }
  },
  methods: {
    goBack() {
      // Implement goBack logic
    },
    handleGenreFilterChange(genreName) {
      const index = this.checkedGenres.indexOf(genreName);
      if (index > -1) {
        this.checkedGenres.splice(index, 1);
      } else {
        this.checkedGenres.push(genreName);
      }
    },
    handleAuthorFilterChange(authorName) {
      const index = this.checkedAuthors.indexOf(authorName);
      if (index > -1) {
        this.checkedAuthors.splice(index, 1);
      } else {
        this.checkedAuthors.push(authorName);
      }
    },
    resetGenres() {
      this.checkedGenres = [];
    },
    resetAuthors() {
      this.checkedAuthors = [];
    }
  }
};
</script>

<style scoped>
.items-container {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
}

.el-card {
  max-width: 300px;
}

.el-image {
  padding: 0 5px;
  max-width: 300px;
  max-height: 200px;
  width: 100%;
  height: 200px;
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
}
.image-slot .el-icon {
  font-size: 30px;
}

.title {
  font-weight: 500;
  font-size: 16px;
  color: #222;
}

.author {
  font-weight: 400;
  font-size: 14px;
  color: #78818d;
}
</style>
