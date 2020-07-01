<template>

  <div class="Common page-width">
    <div class="main-content width-normal">
      <div>
        <div class="title">{{title}}</div>
        <div class="introduce">
          <!-- <span class="item">{{data.introduce}}</span> -->
          <!-- <el-divider direction="vertical"></el-divider> -->
          <span class="item">发布于: {{data.create_time}}</span>
        </div>
        <el-divider></el-divider>
        <div class="content" v-html="content"></div>
      </div>
    </div>
  </div>

</template>

<script>

export default {
  name: 'opusitem',
  data(){
    return{
      title:'',
      content:'',
      data:''
    }
  },
  created(){
    this.$http.ArticleInfo({id:this.$route.query.id})
    .then(response => {
      if (response.code == 200){
        this.title = response.data.title
        this.content = response.data.content
        this.data = response.data
        console.log(response.data)
      }
    })
    .catch(error => {
      console.log("error", error);
    });
  }
}
</script>

<style>
  img{max-width: 100% !important;}
</style>

<style lang="scss" scoped>
  .title{
    width: 100%;
    font-size: 24px;
    line-height: 24px;
    margin-top: 50px;
  }
  .introduce{
    color: #616161;
    font-size: 14px;
    width: 100%;
    overflow: hidden;
    margin-top: 10px;
  }
  .content{
    margin-top: 30px;
    .img{max-width: 100%;}
  }
  p{
    img{max-width: 100% !important;}
  }
</style>