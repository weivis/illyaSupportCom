<template>
  <div></div>
</template>

<script>
export default {
  name: "info",
  data() {
    return {
      id: ""
    };
  },
  methods: {
    query(id) {
      this.$http
        .bangumiInfo(id)
        .then(response => {
          if (response.code == 200) {
            let result = response.data.result;
          }
        })
        .catch(error => {
          console.log("error", error);
        });
    }
  },
  components: {},
  created() {
    this.query(this.$route.query.id);
  }
};
</script>

<style lang="scss" scoped>
</style>