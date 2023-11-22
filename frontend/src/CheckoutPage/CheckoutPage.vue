<template>
  <el-card class="checkout-page" v-if="active">
    <template #header>
      <div class="header">
        <span>Оформлення замовлення</span>
      </div>
    </template>

    <el-form ref="form" :model="checkoutForm" label-position="top" v-if="selectedBooks.length">
      <el-form-item label="Повне імʼя">
        <el-input v-model="checkoutForm.fullName"></el-input>
      </el-form-item>
      <el-form-item label="Адреса">
        <el-input
          type="textarea"
          v-model="checkoutForm.address"
          rows="2"
          placeholder="Введіть повну адресу"
        ></el-input>
      </el-form-item>
      <el-form-item label="Телефонний номер">
        <el-input v-model="checkoutForm.contactNumber"></el-input>
      </el-form-item>

      <div>
        <el-table :data="selectedBooks" style="width: 100%">
          <el-table-column prop="title" label="Назва"></el-table-column>
          <el-table-column label="Автори" v-slot="{ row }">
            <span v-for="(author, index) in row.authors" :key="author.full_name">
              {{ author.full_name }}<span v-if="index < row.authors.length - 1">, </span>
            </span>
          </el-table-column>
        </el-table>
      </div>

      <div class="action-buttons">
        <el-button type="primary" @click="confirmCheckout">Підтвердити замовлення</el-button>
        <el-button @click="cancelCheckout">Відмінити</el-button>
      </div>
    </el-form>

    <div v-else class="empty-checkout">Кошик порожній</div>
  </el-card>
</template>

<script>
export default {
  data() {
    return {
      active: false,
      checkoutForm: {
        fullName: '',
        address: '',
        contactNumber: ''
      },
      selectedBooks: []
    };
  },
  methods: {
    confirmCheckout() {
      // Logic to confirm the checkout process
      console.log('Checkout confirmed with books:', this.selectedBooks);
      // Redirect to confirmation page or display a success message
    },
    cancelCheckout() {
      // Logic to handle cancellation of checkout
      console.log('Checkout cancelled');
      // Redirect back to cart or previous page
    },
    hashChangeHandler() {
      this.active = !!location.hash.match(/checkout/);
    }
  },
  created() {
    window.addEventListener('hashchange', this.hashChangeHandler);
    this.hashChangeHandler();

    this.selectedBooks = JSON.parse(localStorage.getItem('books')) || [];
  }
};
</script>

<style scoped>
.checkout-page {
  max-width: 800px;
  margin: auto;
  flex-grow: 1;
}

.empty-checkout {
  text-align: center;
  padding: 20px;
}

.action-buttons {
  margin-top: 20px;
  text-align: center;
}
</style>
