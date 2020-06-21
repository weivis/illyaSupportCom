<template>
  <div>
  </div>
</template>

<script>
export default {
  name: 'photos',
  data(){
    return{
    }
  },
  components: {
  },
  methods: {
  },
  created(){
    let user = this.$authUser.getUserToken()
    if (user == null) {
      this.$router.push({ name: "login"});
    }
  }
}
</script>
