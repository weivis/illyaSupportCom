<template>
  <div class="Main">
    <div class="content-main main-content width-normal">
      <div class="loginbox">
        <div class="login-title">魔法少女伊莉雅同人站 - 管理员登录入口</div>
        <el-input
          v-model="email"
          class="txt-input"
          placeholder="Email 邮箱"
          prefix-icon="el-icon-user"
        ></el-input>
        <el-input
          v-model="password"
          class="txt-input"
          placeholder="Password 密码"
          prefix-icon="el-icon-key"
          show-password
        ></el-input>
        <div style="text-align:center;margin-top: 110px;">
          <el-button type="primary" round align="center" @click.native="loginstart">立即登录</el-button>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "login",
  created() {
  },
  data(){
    return {
      email: "",
      password: "",
      RegisterUrl: ""
    };
  },
  methods: {
    seedauth(){
      var regEmail = /^[A-Za-z0-9\u4e00-\u9fa5]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$/
        if (this.email != '' && !regEmail.test(this.email)) {
            this.$message({
                message: '邮箱格式不正确',
                type: 'error'
            })
            return false
            // this.email = ''
        } else {
          if (this.password == ''){
            this.$message({
                message: '密码不能为空',
                type: 'error'
            })
            return false
          } else {
            return true
          }
        }
    },
    loginstart() {
      if (this.seedauth() == false){
        return console.log('终止')
      }
      this.$message({
          message: '正在登录中',
          type: 'success'
      })
      console.log(this.email)
      console.log(this.password)
      this.$http
        .authAdminLogin(this.email, this.password)
        .then(response => {
          if (response.code == 200){
              this.$authUser.setUserToken(response.data.token, response.data.username, response.data.head)
              this.$router.push({ name: "Home"});
          }
        })
        .catch(error => {
          console.log("error", error);
        });
    }
  }
};
</script>
<style type="css">
.el-divider__text {
  background-color: #fbfbfb;
  color: #9e9e9e;
}
</style>

<style lang="scss" scoped>
a, li, ul{
    text-decoration:none;
    list-style-type:none;
  }

html, body {
  margin: 0;
  padding: 0;
  border: 0;
}
.Main {
  min-height: calc(100vh - 0px);
  position: relative;
  overflow: hidden;
    width: 100%;
    height: 100%;
    background-image: url(http://127.0.0.1:8888/static/admin/image/login.jpg) !important;
    background-repeat: no-repeat;
    background-size: cover;
    background-position: center;
  .loginbox {
    border-radius: 3px;
    width: 300px;
    height: 300px;
    z-index: 999;
    float: right;
    margin-top: 200px;
    background-color: #fbfbfb;
    margin-right: 10%;
    border: 1px solid #f4f4f4;
    padding: 20px;
  }
  .login-title {
    color: #8a8a8a;
    margin: 0;
    border: 0;
    width: 100%;
    padding: 0;
    font-size: 14px;
  }
  .txt-input {
    position: relative;
    font-size: 14px;
    display: inline-block;
    width: 100%;
    margin-top: 20px;
  }
}
</style>