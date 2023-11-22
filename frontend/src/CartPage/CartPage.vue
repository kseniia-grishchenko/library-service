<template>
  <el-card class="cart-page" v-if="active">
    <template #header>
      <div class="header">
        <span>Ваш кошик</span>
      </div>
    </template>

    <div v-if="cartItems.length">
      <el-table :data="cartItems" style="width: 100%">
        <el-table-column prop="title" label="Назва"></el-table-column>
        <el-table-column label="Автори" v-slot="{ row }">
          <span v-for="(author, index) in row.authors" :key="author.full_name">
            {{ author.full_name }}<span v-if="index < row.authors.length - 1">, </span>
          </span>
        </el-table-column>
        <el-table-column label="Редагувати">
          <template v-slot="{ row }">
            <el-button type="danger" size="mini" @click="removeFromCart(row)">Видалити</el-button>
          </template>
        </el-table-column>
      </el-table>

      <div class="checkout">
        <el-link href="#/checkout">
          <el-button type="primary" @click="proceedToCheckout">Перейти до оформлення</el-button>
        </el-link>
      </div>
    </div>

    <div v-else class="empty-cart">Your cart is empty.</div>
  </el-card>
</template>

<script>
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

      localStorage.setItem('books', JSON.stringify(this.cartItems));
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

    this.cartItems = JSON.parse(localStorage.getItem('books')) || [];
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
