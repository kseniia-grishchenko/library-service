<template>
  <div class="filter">
    <div class="header">
      <span>{{ sectionName }}</span>
      <el-button @click="resetFilters">Очистити</el-button>
    </div>
    <div>
      <el-checkbox-group v-model="modifiedOptions">
        <el-checkbox
          v-for="filter in filterOptions"
          :key="filter.name || filter.full_name"
          :label="filter.name || filter.full_name"
          @change="() => handleFilterChange(filter.name || filter.full_name)"
          :checked="checkedOptions.includes(filter.name || filter.full_name)"
        ></el-checkbox>
      </el-checkbox-group>
    </div>
  </div>
</template>

<script>
export default {
  data: () => ({
    modifiedOptions: []
  }),
  props: {
    sectionName: String,
    filterOptions: Array,
    checkedOptions: Array
  },
  methods: {
    handleFilterChange(name) {
      this.$emit('filter-changed', name);
    },
    resetFilters() {
      this.$emit('filter-reset');
    }
  },
  watch: {
    checkedOptions: {
      handler(val) {
        this.modifiedOptions = val;
      },
      immediate: true
    }
  }
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
