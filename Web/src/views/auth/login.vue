<template>
  <div>
    <div class="loginok" v-if="ok===true">
      <div class="Common page-width">登录成功 正在为你跳转到首页</div>
    </div>

    <div class="page" :style="background">
      <div class="Common page-width content">
        <div class="reg-page">
          <div class="title row">登录你的账户</div>
          <el-input placeholder="请输入你的邮箱 例如xxx@xxx.com" v-model="input_email" class="row">
            <template slot="prepend">邮箱</template>
          </el-input>
          <el-input placeholder="登陆密码" v-model="input_password" class="row" show-password>
            <template slot="prepend">密码</template>
          </el-input>
          <div class="bytton" @click="SendRegister()">立即登录</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "login",
  data() {
    return {
      ok: false,
      input_email: "",
      input_password: "",
      background:
        "background-image: url(https://illya-support.weivird.com/static/com/image/login-background.jpg);"
    };
  },
  methods: {
    SendRegister() {
      this.$http
        .authLogin(this.input_email, this.input_password)
        .then(response => {
          if (response.code == 200) {
            this.ok = true;
            this.$authUser.setUser(response.data.token, response.data.id, response.data.username, response.data.head)
            setTimeout(()=>{
                this.$router.push({ name: "home"});
            },3000);
          }
        })
        .catch(error => {
          console.log("error", error);
        });
    }
  },
  created() {
    let user = this.$authUser.getUser()
    if(user){
      this.$router.push({ name: "home"});
    }
  }
};
</script>

<style lang="scss" scoped>
.loginok {
  position: absolute;
  z-index: 9999;
  left: 0;
  right: 0;
  height: 60px;
  background-color: rgba(0, 121, 179, 0.48);
  line-height: 60px;
  color: #ffffff;
  font-weight: bold;
  font-size: 24px;
}
.content {
  position: relative;
}
.page {
  min-height: calc(100vh - 60px);
  width: 100%;
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  overflow: hidden;
}
.reg-page {
  padding: 30px;
  max-width: 350px;
  height: 400px;
  background-color: rgba(255, 255, 255, 0.93);
  margin: 0 auto;
  margin-top: 10%;
  .title {
    width: 100%;
    color: #000;
    font-size: 24px;
    text-align: center;
  }
  .info {
    width: 100%;
    text-align: center;
  }
  .row {
    margin-bottom: 30px;
  }
  .bytton {
    padding: 15px;
    background-color: #0082f1;
    color: #fff;
    font-size: 14px;
    text-align: center;
  }
}
@media screen and (min-width: 1300px) {
  .reg-page {
    padding: 50px;
    position: absolute;
    right: 0;
  }
}
@media screen and (min-width: 1000px) {
  .reg-page {
    position: absolute;
    right: 0;
  }
}
</style>