<template>
  <div class="header">
    <span><el-link href="#/">Online бібліотека</el-link></span>
    <el-input v-model="input" placeholder="Я шукаю..." :prefix-icon="Search" />
    <el-link href="#/user-profile">
      <el-button>
        <el-icon><User /></el-icon>
      </el-button>
    </el-link>
    <el-link href="#/cart">
      <el-button>
        <el-icon><ShoppingCart /></el-icon>
      </el-button>
    </el-link>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { Search, User, ShoppingCart } from '@element-plus/icons-vue';
const input = ref('');
</script>

<style scoped>
.header {
  display: grid;
  grid-template-columns: auto 1fr auto auto;
  justify-content: space-between;
  gap: 8px;
  padding: 20px 8px;
  align-items: center;
}
</style>
