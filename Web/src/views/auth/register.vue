<template>
  <div class="page" :style="background">
    <div class="Common page-width content">
      <div class="reg-page" v-if="ok==true">
        <div class="title row">感谢你的注册</div>
        <div class="info">验证邮件已经在发送到你邮箱的路上 完成邮箱认证后即可登录</div>
      </div>
      <div class="reg-page" v-if="ok==false">
        <div class="title row">注册账户</div>
        <el-input placeholder="请输入你的邮箱 例如xxx@xxx.com" v-model="input_email" class="row">
          <template slot="prepend">邮箱</template>
        </el-input>
        <el-input placeholder="请输入内容" v-model="input_username" class="row">
          <template slot="prepend">用户名</template>
        </el-input>
        <el-input placeholder="登陆密码" v-model="input_password" class="row" show-password>
          <template slot="prepend">密码</template>
        </el-input>
        <el-input placeholder="重复输入一次登录密码" v-model="input_repassword" class="row" show-password>
          <template slot="prepend" style="width: 100px;">再输入一次密码</template>
        </el-input>
        <div class="bytton" @click="SendRegister()">立即注册</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "register",
  data() {
    return {
      ok: false,
      input_email: "",
      input_password: "",
      input_repassword: "",
      input_username: "",
      background:
        "background-image: url(http://127.0.0.1:8888/static/com/image/register-background.jpg);"
    };
  },
  methods: {
    SendRegister() {
      this.$http
        .authRegister(
          this.input_email,
          this.input_password,
          this.input_repassword,
          this.input_username
        )
        .then(response => {
          if (response.code == 200) {
            this.ok = true;
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