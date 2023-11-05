<template>
  <div class="filter">
    <div class="header">
      <span>{{ sectionName }}</span>
      <el-button @click="$emit('filter-reset')">Clear all</el-button>
    </div>
    <div>
      <el-checkbox
        v-for="filter in modifiedFilterOptions"
        :label="filter.name || filter.full_name"
        @change="handleFilterChange(filter.name || filter.full_name)"
      ></el-checkbox>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const props = defineProps({
  sectionName: String,
  filterOptions: [],
  checkedOptions: []
});
const emit = defineEmits(['filter-changed', 'filter-reset']);

const modifiedFilterOptions = ref(props.filterOptions);

// replace name with id when API is ready
const handleFilterChange = (name) => {
  emit('filter-changed', name);
};
</script>

<style scoped>
.filter {
  margin-bottom: 20px;
}
.header {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 10px;
}
.header span {
  color: #222;
  font-weight: 500;
  font-size: 15px;
}
</style>
