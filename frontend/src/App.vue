<template>
  <el-container class="main-container">
    <el-header>
      <header-comp></header-comp>
      <book-header :bookTitle="bookTitle" v-if="showBookHeader"></book-header>
    </el-header>
    <el-main class="main-section">
      <sign-up></sign-up>
      <sign-in></sign-in>
      <catalog-page></catalog-page>
      <book-page @book-selected="handleBookChange"></book-page>
    </el-main>
  </el-container>
</template>

<script>
import BookPage from './BookPage/BookPage.vue';
import CatalogPage from './CatalogPage/CatalogPage.vue';
import HeaderComp from './HeaderComp/HeaderComp.vue';
import SignUp from './SignUp/SignUp.vue';
import SignIn from './SignIn/SignIn.vue';
import BookHeader from './HeaderComp/BookHeader.vue';

export default {
  data: () => ({
    bookTitle: '',
    showBookHeader: false
  }),
  methods: {
    handleBookChange(title) {
      this.bookTitle = title;
    },
    hashChangeHandler() {
      this.showBookHeader = !!location.hash.match(/#\/$|book\?id=(\d+)/);
    }
  },
  created() {
    window.addEventListener('hashchange', this.hashChangeHandler);
    this.hashChangeHandler();
  },
  components: {
    HeaderComp,
    BookHeader,
    SignUp,
    SignIn,
    BookPage,
    CatalogPage
  }
};
</script>

<style>
.main-container {
  display: grid;
  grid-template-rows: auto 1fr;
}
.main-section {
  display: flex;
  align-items: center;
}
.el-header {
  --el-header-height: auto;
}
</style>
