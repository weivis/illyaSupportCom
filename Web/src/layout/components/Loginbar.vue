<template>
  <div class="Loginbar">

    <div class="userbar" v-if="user">
      <el-dropdown>
        <span class="el-dropdown-link">
          欢迎你: {{user.userName}}
          <i class="el-icon-arrow-down el-icon--right"></i>
        </span>
        <el-dropdown-menu slot="dropdown">
          <el-dropdown-item @click.native="Logout_users">退出登录</el-dropdown-item>
        </el-dropdown-menu>
      </el-dropdown>
    </div>

    <div class="login" v-else>
        <router-link :to="loginurl" class="link">前往登录 | 注册</router-link>
    </div>

  </div>
</template>
<script>
export default {
  name: "Loginbar",
  data() {
    return {
        user: null,
        loginurl: '/auth/sgin-in'
    };
  },
  created() {
      let user = this.$authUser.getUser()
      console.log(user)
      this.user = user
  },
  methods: {
    Logout_users() {
      this.$http
        .authLogout(this.user.userToken)
        .then(response => {
          if (response.code === 200) {
            console.log('>用户退出登录')
            this.Logout_user();
            this.LogoutUserInfo();
            this.$router.go(0)
          }
        })
        .catch(error => {
          console.log("error", error);
        });
    }
  }
};
</script>
<style lang="scss" scoped>
.Loginbar{float: right;}
.login{ 
    height: 60px;line-height: 60px;;
    .link{font-size: 12px;color: #484848}
}
</style>