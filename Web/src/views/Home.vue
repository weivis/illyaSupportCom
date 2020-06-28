<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'Home',
  data(){
    return{
      buttlist:[
        {
          title:'111',
          link:'11111111',
          conttype:1,
        }
      ],
      contentType:0
    }
  },
  components: {
  },
  methods: {
    getList(n){
      console.log(n)
    }
  },
  created(){
    let user = this.$authUser.getUserToken()
    if (user) {
      console.log('用户已登录')
    }else{
      console.log('用户未登录')
    }
  }
}
</script>
