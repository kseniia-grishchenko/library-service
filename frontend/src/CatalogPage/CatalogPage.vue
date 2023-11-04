<template>
  <p class="greeting">{{ greeting }}</p>
  <el-page-header @back="goBack">
    <template #content>
      <span class="text-large font-600 mr-3"> Title </span>
    </template>
  </el-page-header>
  <el-main>
    <div class="items-container">
      <div v-for="book in allBooks" :key="book.id">
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
</template>

<script setup>
import { Picture as IconPicture } from '@element-plus/icons-vue';
import { ref } from 'vue';
import books from '../assets/books.js';

const allBooks = ref(books);
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
