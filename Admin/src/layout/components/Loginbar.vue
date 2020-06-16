<template>
  <div class="HeaderLoginbar">
    <div class="userbar">
      <el-dropdown>
        <span class="el-dropdown-link">
          欢迎你: {{UserData.username}}
          <i class="el-icon-arrow-down el-icon--right"></i>
        </span>
        <el-dropdown-menu slot="dropdown">

          <el-dropdown-item @click.native="Logout_users">退出登录</el-dropdown-item>

        </el-dropdown-menu>
      </el-dropdown>
    </div>
  </div>
</template>
<script>
export default {
  name: "HeaderLoginbar",
  data() {
    return {
      UserData: {}
    };
  },
  created() {
    this.UserData = this.$authUser.getUserData()
    console.log(this.UserData)
  },
  methods: {
    Logout_users() {
      this.$http
        .authAdminLogout()
        .then(response => {
          if (response.code === 200) {
            console.log('>用户退出登录')
            this.$authUser.removeUserToken()
            this.$router.push({ name: "Login"});
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
.HeaderLoginbar {
  margin-left: 25px;
  float: right;
  height: 25px;
  line-height: 25px;
  font-size: 14px;
  a {
    color: #525252;
  }
  .username {
    float: right;
  }
  .visitor_login {
    float: right;
  }
}
</style>