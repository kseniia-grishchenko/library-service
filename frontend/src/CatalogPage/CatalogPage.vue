<template>
  <el-container v-if="active">
    <el-container>
      <el-aside v-loading="filtersLoading">
        <filter-select
          section-name="Жанри"
          :filter-options="genres"
          :checked-options="checkedGenres"
          @filter-changed="handleGenreFilterChange"
          @filter-reset="resetGenres"
        ></filter-select>
        <filter-select
          section-name="Автори"
          :filter-options="authors"
          :checked-options="checkedAuthors"
          @filter-changed="handleAuthorFilterChange"
          @filter-reset="resetAuthors"
        ></filter-select>
      </el-aside>
      <el-main>
        <div class="items-container" v-loading="booksLoading">
          <el-card
            :body-style="{ padding: '10px' }"
            v-for="book in filteredItems"
            :key="book.id"
            @click="redirectToBookPage(book.id)"
          >
            <el-button class="add-to-cart" @click.stop="$emit('add-to-cart', book)">
              <el-icon><ShoppingCart /></el-icon>
            </el-button>
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
                <span class="author" v-for="(author, index) in book.authors" :key="index">
                  {{ author.full_name }}
                </span>
              </div>
            </div>
          </el-card>
        </div>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
import { Picture as IconPicture, ShoppingCart } from '@element-plus/icons-vue';
import FilterSelect from './FilterSelect.vue';
import { getRequest } from '../api';

export default {
  data() {
    return {
      active: false,
      books: [],
      genres: [],
      authors: [],
      checkedGenres: [],
      checkedAuthors: [],
      filtersLoading: false,
      booksLoading: false
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
    },
    redirectToBookPage(bookId) {
      location.hash = `#/book?id=${bookId}`;
    },
    hashChangeHandler() {
      this.active = !!location.hash.match(/#\/$/);
    },

    async fetchBooks() {
      this.booksLoading = true;
      const { data: books } = await getRequest('/api/books');
      this.books = books;
      this.booksLoading = false;
    },

    async fetchGenres() {
      const { data: genres } = await getRequest('/api/books/genres');
      this.genres = genres;
    },

    async fetchAuthors() {
      const { data: authors } = await getRequest('/api/books/authors');
      this.authors = authors;
    }
  },
  watch: {
    async active(value) {
      if (!value) return;

      this.fetchBooks();

      this.filtersLoading = true;
      await this.fetchGenres();
      await this.fetchAuthors();
      this.filtersLoading = false;
    }
  },
  created() {
    window.addEventListener('hashchange', this.hashChangeHandler);
    this.hashChangeHandler();
  },
  components: {
    FilterSelect,
    IconPicture,
    ShoppingCart
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
  position: relative;
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

.add-to-cart {
  position: absolute;
  right: 10px;
  z-index: 1;
  display: none;
}

.el-card:hover .add-to-cart {
  display: initial;
}
</style>
