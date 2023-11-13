<template>
  <el-card class="cart-page" v-if="active">
    <template #header>
      <div class="header">
        <span>Your Cart</span>
      </div>
    </template>

    <div v-if="cartItems.length">
      <el-table :data="cartItems" style="width: 100%">
        <el-table-column prop="title" label="Title"></el-table-column>
        <el-table-column label="Authors" v-slot="{ row }">
          <span v-for="(author, index) in row.authors" :key="author.full_name">
            {{ author.full_name }}<span v-if="index < row.authors.length - 1">, </span>
          </span>
        </el-table-column>
        <el-table-column label="Operation">
          <template v-slot="{ row }">
            <el-button type="danger" size="mini" @click="removeFromCart(row)">Remove</el-button>
          </template>
        </el-table-column>
      </el-table>

      <div class="checkout">
        <el-link href="#/checkout">
          <el-button type="primary" @click="proceedToCheckout">Proceed to Checkout</el-button>
        </el-link>
      </div>
    </div>

    <div v-else class="empty-cart">Your cart is empty.</div>
  </el-card>
</template>

<script>
import books from '../assets/books.js';

export default {
  data() {
    return {
      active: false,
      cartItems: []
    };
  },
  methods: {
    removeFromCart(item) {
      this.cartItems = this.cartItems.filter((cartItem) => cartItem.id !== item.id);
      const bookIds = this.cartItems.map((item) => item.id);
      console.log(bookIds);
      localStorage.setItem('books', JSON.stringify(bookIds));
    },
    proceedToCheckout() {
      // Logic to proceed to checkout
      console.log('Proceeding to checkout with items:', this.cartItems);
      // Redirect to checkout page or handle checkout logic
    },
    hashChangeHandler() {
      this.active = !!location.hash.match(/cart/);
    }
  },
  created() {
    window.addEventListener('hashchange', this.hashChangeHandler);
    this.hashChangeHandler();

    const bookIds = JSON.parse(localStorage.getItem('books')) || [];
    this.cartItems = books.filter((book) => bookIds.includes(book.id));
  }
};
</script>

<style scoped>
.cart-page {
  max-width: 800px;
  margin: auto;
  flex-grow: 1;
}

.empty-cart {
  text-align: center;
  padding: 20px;
}

.checkout {
  margin-top: 20px;
  text-align: center;
}
</style>
