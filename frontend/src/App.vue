<template>
  <el-container class="main-container">
    <el-header>
      <header-comp></header-comp>
      <book-header :bookTitle="bookTitle" v-if="showBookHeader"></book-header>
    </el-header>
    <el-main class="main-section">
      <auth-wrapper></auth-wrapper>
      <sign-up v-if="!user"></sign-up>
      <sign-in v-if="!user" @log-in="handleLogIn"></sign-in>
      <catalog-page @add-to-cart="handleAddToCart"></catalog-page>
      <book-page
        @book-selected="handleBookChange"
        @add-to-cart="handleAddToCart"
        :inCart="currentBookInCart"
      ></book-page>
      <user-profile></user-profile>
      <cart-page></cart-page>
      <checkout-page></checkout-page>
      <order-history></order-history>
    </el-main>
  </el-container>
</template>

<script>
import { jwtDecode } from 'jwt-decode';

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
import { getRequest, postRequest } from './api';
import OrderHistory from './OrderHistory/OrderHistory.vue';

export default {
  data: () => ({
    bookTitle: '',
    showBookHeader: false,
    currentBookInCart: false,
    user: null
  }),
  methods: {
    async logIn() {
      const accessToken = localStorage.getItem('access');
      if (!accessToken) return;

      const { exp } = jwtDecode(accessToken);
      this.expiresAt = exp;

      if (this.expiresAt * 1e3 > Date.now()) {
        await this.fetchUser();
        return;
      }

      this.refreshToken();
    },

    async fetchUser() {
      try {
        const { data: user } = await getRequest('/api/users/me/');

        this.user = user;
      } catch (err) {
        console.log(err);
        console.error(err.response.data);
      }
    },

    async refreshToken() {
      try {
        const { data } = await postRequest('/api/users/token/refresh/', {
          refresh: localStorage.getItem('refresh')
        });

        const { access } = data;

        localStorage.setItem('access', access);
        this.logIn();
      } catch (err) {
        console.error(err.response.data);
      }
    },

    async handleLogIn() {
      await this.logIn();
      location.hash = '#/';
    },

    handleBookChange(book) {
      this.currentBookInCart = false;
      this.bookTitle = book.title;

      const booksInCart = JSON.parse(localStorage.getItem('books')) || [];
      this.currentBookInCart = booksInCart.includes(book.id);
    },
    hashChangeHandler() {
      this.showBookHeader = !!location.hash.match(/#\/$|book\?id=(\d+)/);
    },
    handleAddToCart(book) {
      const booksInCart = JSON.parse(localStorage.getItem('books')) || [];
      let modifiedBooksInCart = [...booksInCart];
      const booksIds = booksInCart.map(({ id }) => id);
      if (booksIds.includes(book.id)) {
        modifiedBooksInCart = booksInCart.filter((b) => b.id !== book.id);
      } else {
        modifiedBooksInCart.push(book);
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
      const modifiedBookIds = modifiedBooksInCart.map(({ id }) => id);
      this.currentBookInCart = modifiedBookIds.includes(book.id);
      localStorage.setItem('books', JSON.stringify(Array.from(new Set(modifiedBooksInCart))));
    }
  },
  created() {
    window.addEventListener('hashchange', this.hashChangeHandler);
    this.hashChangeHandler();
    this.refreshToken();
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
    CheckoutPage,
    OrderHistory
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
