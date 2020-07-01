<template>
  <div class="layout-Header">
    <div class="header">
      <div class="Common page-width">
        <div class="logo">
          <router-link to="/">
            <div class="img">
              <img src="https://illya-support.weivird.com/static/logo.png" style="height:100%" />
            </div>
            <div class="lines"></div>
            <div class="title">
              China - Illya Aid com
              <br />中国地区応援サイト
            </div>
          </router-link>
        </div>
        <div class="nav" v-if="navop">
          <div v-for="(item, index) in list" :key="index" class="item">
            <router-link :to="item.link" class="title">
              <div class="jp">{{ item.jptitle }}</div>
              <span class="span">·</span>
              <div class="cn">{{ item.cntitle }}</div>
              <i class="el-icon-arrow-down"></i>
            </router-link>
          </div>
        </div>
        <div class="opennavbutton" v-if="navopbutton" @click="oepnnav()"><i class="el-icon-s-fold"></i></div>
        <loginbar/>
      </div>
    </div>
  </div>
</template>

<script>
import Loginbar from "./Loginbar.vue";
export default {
  name: "Header",
  components: {
    //定义组件
    Loginbar
  },
  methods:{
      oepnnav(){
          if (this.navop == false){
              this.navop = true
          }else{
              this.navop = false
          }
      }
  },
  data() {
    return {
      navop: true,
      navopbutton: false,
      screenWidth: document.body.clientWidth,
      list: [
        {
          jptitle: "どうじん",
          cntitle: "同人二次创作",
          link: "/doujin"
        },
        {
          jptitle: "公式情報",
          cntitle: "资讯",
          link: "/news"
        },
        {
          jptitle: "アニメ",
          cntitle: "动画",
          link: "/bangumi"
        },
        {
          jptitle: "アルバム",
          cntitle: "相簿",
          link: "/photo"
        },
        {
          jptitle: "",
          cntitle: "资源",
          link: "/album"
        },
        // {
        //   jptitle: "フォーラム",
        //   cntitle: "BBS",
        //   link: "/bbs"
        // }
      ]
    };
  },
  created(){
      console.log('true')
      if(document.body.clientWidth > 850){
          this.navop = true
          this.navopbutton = false
      }else{
          this.navop = false
          this.navopbutton = true
      }
  },
  watch: {
    screenWidth(val) {
      // 为了避免频繁触发resize函数导致页面卡顿，使用定时器
      if (!this.timer) {
        // 一旦监听到的screenWidth值改变，就将其重新赋给data里的screenWidth
        this.screenWidth = val;
        this.timer = true;
        let that = this;
        setTimeout(function() {
          // 打印screenWidth变化的值
          if (that.screenWidth < 850) {
              that.navop = false
              that.navopbutton = true
          } else {
            that.navop = true;
            that.navopbutton = false
          }
          console.log(that.screenWidth);
          that.timer = false;
        }, 400);
      }
    }
  },
  mounted() {
    const that = this;
    window.onresize = () => {
      return (() => {
        window.screenWidth = document.body.clientWidth;
        that.screenWidth = window.screenWidth;
      })();
    };
  },
};
</script>

<style lang="scss" scoped>
.opennavbutton{float: right;height: 60px;width: 60px;line-height: 60px;font-size: 32px;text-align: right;}
.header {
  display: flow-root;
  width: 100%;
  height: 60px;
  border-bottom: 1px solid #f4f4f4;
}
.logo {
  display: flow-root;
  float: left;
  .img {
    padding-top: 13px;
    padding-bottom: 13px;
    float: left;
  }
  .lines {
    margin: 13px;
    background-color: #000;
    width: 1px;
    float: left;
    height: 34px;
  }
  .title {
    color: #484848;
    padding: 13px;
    line-height: 18px;
    white-space: pre-wrap;
    float: left;
    text-align: left;
    font-size: 12px;
    padding-left: 0px;
  }
}
.nav {
  float: left;
  .item {
    height: 60px;
    font-size: 12px;
    line-height: 60px;
    padding-left: 15px;
    padding-right: 15px;
    float: left;
    .title {
      color: #484848;
      .jp {
        float: left;
      }
      .span {
        float: left;
      }
      .cn {
        float: left;
      }
    }
  }
}
.loginbar {
}
@media screen and (max-width: 1650px) {
  .nav {
    float: left;
    .item {
      height: 60px;
      font-size: 12px;
      line-height: 60px;
      padding-left: 5px;
      padding-right: 5px;
      float: left;
      .title {
        color: #484848;
        .jp {
          float: left;
        }
        .span {
          float: left;
        }
        .cn {
          float: left;
        }
      }
    }
  }
}
@media screen and (max-width: 1450px) {
  .header {
    display: flow-root;
    width: 100%;
    height: 100px;
    border-bottom: 1px solid #f4f4f4;
    position: relative;
  }
  .nav {
    position: absolute;
    height: 40px;
    top: 60px;
    border-top: 1px solid #f4f4f4;
    width: calc(100% - 100px);
    float: left;
    .item {
      height: 40px;
      font-size: 12px;
      line-height: 40px;
      padding-left: 15px;
      padding-right: 15px;
      float: left;
      .title {
        color: #484848;
        .jp {
          float: left;
        }
        .span {
          float: left;
        }
        .cn {
          float: left;
        }
      }
    }
  }
}
@media screen and (max-width: 1000px) {
  .header {
    display: flow-root;
    width: 100%;
    height: 100px;
    border-bottom: 1px solid #f4f4f4;
    position: relative;
  }
  .nav {
    position: absolute;
    height: 40px;
    top: 60px;
    border-top: 1px solid #f4f4f4;
    width: calc(100% - 80px);
    float: left;
    .item {
      height: 40px;
      font-size: 12px;
      line-height: 40px;
      padding-left: 5px;
      padding-right: 5px;
      float: left;
      .title {
        color: #484848;
        .jp {
          float: left;
        }
        .span {
          float: left;
        }
        .cn {
          float: left;
        }
      }
    }
  }
}
@media screen and (max-width: 850px) {
  .header {
    display: flow-root;
    width: 100%;
    height: 60px;
    border-bottom: 1px solid #f4f4f4;
    position: relative;
  }
  .nav {
    position: absolute;
    height: 40px;
    top: 60px;
    height: 1000px;
    z-index: 999;
    width: 150px;
    background-color: #fff;
    border: 1px solid #e4e2e2;
    right: 0%;
    padding: 25px;
    .item {
      border-bottom: 1px solid #cecece;
      width: 100%;
      height: 50px;
      font-size: 12px;
      line-height: 50px;
      padding-left: 5px;
      padding-right: 5px;
      float: left;
      .title {
        color: #484848;
        .jp {
          float: left;
        }
        .span {
          float: left;
        }
        .cn {
          float: left;
        }
      }
    }
  }
}
@media screen and (max-width: 700px) {
  .opennavbutton{float: right;height: 60px;width: 40px;line-height: 60px;font-size: 32px;text-align: right;}
}
</style>