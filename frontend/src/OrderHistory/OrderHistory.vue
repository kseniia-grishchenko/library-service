<template>
  <el-table :data="orders" style="width: 100%" v-if="active">
    <el-table-column prop="id" label="ID замовлення"></el-table-column>
    <el-table-column prop="username" label="Імʼя"></el-table-column>
    <el-table-column prop="address" label="Адреса"></el-table-column>
    <el-table-column prop="phone" label="Телефон"></el-table-column>
    <el-table-column prop="borrowings" label="Книги" min-width="300">
      <template #default="scope">
        <div v-for="borrowing in scope.row.borrowings" :key="borrowing.id" class="borrowing-info">
          <el-descriptions size="small" column="1" border>
            <el-descriptions-item label="ID">{{ borrowing.id }}</el-descriptions-item>
            <el-descriptions-item label="Дата позичення">{{
              formatDateTime(borrowing.borrow_date)
            }}</el-descriptions-item>
            <el-descriptions-item label="Очікувана дата повернення">{{
              formatDateTime(borrowing.expected_return_date)
            }}</el-descriptions-item>
            <el-descriptions-item label="Дата повернення">{{
              formatDateTime(borrowing.actual_return_date)
            }}</el-descriptions-item>
            <el-descriptions-item label="ID книги">{{ borrowing.book }}</el-descriptions-item>
            <el-descriptions-item label="Активне">{{
              borrowing.is_active ? 'Так' : 'Ні'
            }}</el-descriptions-item>
          </el-descriptions>
        </div>
      </template>
    </el-table-column>

    <el-table-column prop="is_sent" label="Статус">
      <template #default="scope">
        <el-tag type="success" v-if="scope.row.is_sent">Надіслано</el-tag>
        <el-tag type="info" v-else>В очікуванні</el-tag>
      </template>
    </el-table-column>
  </el-table>
</template>

<script>
import { getRequest } from '../api';

export default {
  data: () => ({
    active: false,
    orders: []
  }),
  methods: {
    async fetchOrders() {
      try {
        // Replace with your API endpoint
        const { data: orders } = await getRequest('/api/order/');
        this.orders = orders;
      } catch (error) {
        console.error('Error fetching orders:', error);
      }
    },
    hashChangeHandler() {
      this.active = !!location.hash.match('orders');
    },
    formatDateTime(dateStr) {
      const date = new Date(dateStr);
      return (
        date.toLocaleDateString(undefined, { day: 'numeric', month: 'long', year: 'numeric' }) +
        ' ' +
        date.toLocaleTimeString()
      );
    }
  },
  watch: {
    active(active) {
      if (!active) return;
      this.fetchOrders();
    }
  },
  created() {
    window.addEventListener('hashchange', this.hashChangeHandler);
    this.hashChangeHandler();
  }
};
</script>

<style>
.borrowing-info {
  padding-bottom: 16px;
  border-bottom: 1px solid #f0f0f0;
}

.borrowing-info:last-child {
  border-bottom: none;
}
</style>
