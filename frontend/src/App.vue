<template>
  <div class="common-layout">
    <el-container>
      <el-header>
        <header-comp></header-comp>
      </el-header>
      <el-main>
        <catalog-page></catalog-page>
        <book-page></book-page>
      </el-main>
    </el-container>
  </div>
</template>

<script setup>
import BookPage from './BookPage/BookPage.vue';
import CatalogPage from './CatalogPage/CatalogPage.vue';
import HeaderComp from './HeaderComp/HeaderComp.vue';
</script>

<style scoped></style>
