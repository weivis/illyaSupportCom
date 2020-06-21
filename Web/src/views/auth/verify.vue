<template>
  <div>
    <el-dialog title="请输入注册时的邮箱" :visible.sync="resendemail_win" width="30%">
  <el-input placeholder="请输入内容" v-model="resendemail_input">
    <template slot="prepend">邮箱</template>
  </el-input>
      <span slot="footer" class="dialog-footer">
        <el-button @click="resendemail_win = false">取 消</el-button>
        <el-button type="primary" @click="reSendMmail()">确 定</el-button>
      </span>
    </el-dialog>

    <div class="page" :style="background">
      <div class="Common page-width">
        {{pst}}
        <div class="p" v-if="pst === 0">
          <div class="icon">
            <i class="el-icon-loading" style="display:table-cell; vertical-align:middle;"></i>
          </div>
          <div class="title">正在验证中</div>
        </div>

        <div class="p" v-if="pst === 1">
          <div class="icon">
            <i class="el-icon-circle-check" style="display:table-cell; vertical-align:middle;"></i>
          </div>
          <div class="title">验证成功 正在为你跳转到登录页面</div>
        </div>


        <div class="p" v-if="pst === 10">
          <div class="icon">
            <i class="el-icon-warning-outline" style="display:table-cell; vertical-align:middle;"></i>
          </div>
          <div class="title">你的验证码可能已经失效 可以点击以下按钮重新发送</div>
          <div class="button" style="margin-top:40px" @click="resendemail_win = true">重新发送</div>
        </div>

        <div class="p" v-if="pst === 11">
          <div class="icon">
            <i class="el-icon-warning-outline" style="display:table-cell; vertical-align:middle;"></i>
          </div>
          <div class="title">该邮箱以验证完成 无法重复发送注册验证码</div>
        </div>

        <div class="p" v-if="pst === 9">
          <div class="icon">
            <i class="el-icon-circle-check" style="display:table-cell; vertical-align:middle;"></i>
          </div>
          <div class="title">重新发送验证码成功</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "verify",
  data() {
    return {
      vcode: "",
      pst: 0,
      background:"background-image: url(http://127.0.0.1:8888/static/com/image/verify-background.jpg);",
      resendemail_win:false,
      resendemail_input: ''
    };
  },
  methods: {
    verifyOk(){
        setTimeout(()=>{
            this.$router.push({ name: "login"});
        },3000);
    },
    reSendMmail(){
      this.$http
        .authRegisterAgainSendemail(this.resendemail_input)
        .then(response => {
          if (response.code == 200) {
            this.pst = 9;
            this.resendemail_win = false
            this.verifyOk()
          }
        })
        .catch(error => {
          console.log("error", error);
        });
    },
    SendVcode() {
      this.$http
        .authVerifyRegisterVcode(this.vcode)
        .then(response => {
          if (response.code == 200) {
            this.pst = 1;
          }
          if (response.code == 400) {
            this.pst = 10;
          }
          if (response.code == 401) {
            this.pst = 11;
          }
        })
        .catch(error => {
          console.log("error", error);
        });
    }
  },
  created() {
    this.vcode = this.$route.query.vcode;
    this.SendVcode();
  }
};
</script>

<style lang="scss" scoped>
.page {
  min-height: calc(100vh - 60px);
  width: 100%;
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  overflow: hidden;
}
.p {
  position: relative;
  padding: 30px;
  max-width: 400px;
  height: 400px;
  background-color: rgba(255, 255, 255, 0.93);
  margin: 0 auto;
  margin-top: 10%;
  .icon {
    width: 100%;
    height: 50%;
    text-align: center;
    line-height: 50%;
    font-size: 48px;
    display: table;
  }
  .title {
    width: 100%;
    text-align: center;
    font-size: 24px;
  }
  .button {
    width: 50%;
    background-color: #fff;
    height: 40px;
    line-height: 40px;
    text-align: center;
    position: absolute;
    left: 0;
    right: 0;
    margin: 0 auto;
    border: 1px solid #cecece;
    border-radius: 2px;
  }
}
</style>

