<script setup>
import CatalogPage from './CatalogPage/CatalogPage.vue';
import HeaderComp from './HeaderComp/HeaderComp.vue';
</script>

<template>
  <div class="common-layout">
    <el-container>
      <el-header>
        <header-comp></header-comp>
      </el-header>
      <el-main>
        <catalog-page></catalog-page>
      </el-main>
    </el-container>
  </div>
</template>

<style scoped></style>
