<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
    <CommonContentNav :conttype.sync="contentType" background_color="#000000" @conttype="getList(contentType)" button_color="#f4f4f4" button_style="1" :buttlist='buttlist'/>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import CommonContentNav from '@/components/CommonContentNav.vue'

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
    HelloWorld,
    CommonContentNav
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
