<template>
  <div></div>
</template>

<script>
export default {
  data: () => ({
    protectedRoutes: ['user-profile']
  }),
  methods: {
    hashChangeHandler() {
      // const accessToken = JSON.parse(localStorage.getItem('access'));
      const accessToken = true;
      const [, currentRoute] = location.hash.split('#/');
      if (this.protectedRoutes.includes(currentRoute) && !accessToken) {
        location.hash = '#/sign-in';
      }
    }
  },
  created() {
    window.addEventListener('hashchange', this.hashChangeHandler);
    this.hashChangeHandler();
  }
};
</script>

<style></style>
