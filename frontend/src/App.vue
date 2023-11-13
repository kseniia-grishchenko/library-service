<template>
  <el-container class="main-container">
    <el-header>
      <header-comp></header-comp>
      <book-header :bookTitle="bookTitle" v-if="showBookHeader"></book-header>
    </el-header>
    <el-main class="main-section">
      <auth-wrapper></auth-wrapper>
      <sign-up></sign-up>
      <sign-in></sign-in>
      <catalog-page @add-to-cart="handleAddToCart"></catalog-page>
      <book-page
        @book-selected="handleBookChange"
        @add-to-cart="handleAddToCart"
        :inCart="currentBookInCart"
      ></book-page>
      <user-profile></user-profile>
      <cart-page></cart-page>
      <checkout-page></checkout-page>
    </el-main>
  </el-container>
</template>

<script>
import { ElMessage, ElNotification } from 'element-plus';
import BookPage from './BookPage/BookPage.vue';
import CatalogPage from './CatalogPage/CatalogPage.vue';
import HeaderComp from './HeaderComp/HeaderComp.vue';
import SignUp from './SignUp/SignUp.vue';
import SignIn from './SignIn/SignIn.vue';
import BookHeader from './HeaderComp/BookHeader.vue';
import AuthWrapper from './AuthWrapper.vue';
import UserProfile from './UserProfile/UserProfile.vue';
import CartPage from './CartPage/CartPage.vue';
import CheckoutPage from './CheckoutPage/CheckoutPage.vue';

export default {
  data: () => ({
    bookTitle: '',
    showBookHeader: false,
    currentBookInCart: false
  }),
  methods: {
    handleBookChange(book) {
      this.currentBookInCart = false;
      this.bookTitle = book.title;

      const booksInCart = JSON.parse(localStorage.getItem('books')) || [];
      this.currentBookInCart = booksInCart.includes(book.id);
    },
    hashChangeHandler() {
      this.showBookHeader = !!location.hash.match(/#\/$|book\?id=(\d+)/);
    },
    handleAddToCart(bookId) {
      const booksInCart = JSON.parse(localStorage.getItem('books')) || [];
      let modifiedBooksInCart = [...booksInCart];
      if (booksInCart.includes(bookId)) {
        modifiedBooksInCart = booksInCart.filter((id) => id !== bookId);
      } else {
        modifiedBooksInCart.push(bookId);
      }
      if (modifiedBooksInCart.length > 3) {
        ElMessage({
          message: 'Warning, you can add max 3 books to the cart',
          type: 'warning'
        });
        return;
      }
      if (modifiedBooksInCart.length > booksInCart.length) {
        ElNotification({
          title: 'Success',
          message: 'Book added to the cart'
        });
      } else {
        ElNotification({
          title: 'Success',
          message: 'Book removed from the cart'
        });
      }
      this.currentBookInCart = modifiedBooksInCart.includes(bookId);
      localStorage.setItem('books', JSON.stringify(Array.from(new Set(modifiedBooksInCart))));
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
    CatalogPage,
    AuthWrapper,
    UserProfile,
    CartPage,
    CheckoutPage
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
