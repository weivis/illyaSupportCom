<template>
  <div>
    <div class="Common page-width">
      <div class="top">
        <div class="left">
          <img :src="cover" style="width:100%" />
        </div>
        <div class="rgiht">
          <div class="type">
            <div class="item" v-if="classification === 1">番剧</div>
            <div class="item" v-if="classification === 2">OST</div>
            <div class="item" v-if="classification === 3">MMD</div>
            <div class="item" v-if="classification === 4">Live2D</div>
          </div>
          <div class="title">{{name}}</div>
          <div class="introduce">{{introduce}}</div>
        </div>
      </div>

      <div class="bottom">
        <div class="left-content">
          <div class="page">
            <div class="p-name">下载列表</div>
            <div class="p-content">
              <div v-for="(item, index) in dowlist" :key="index" class="dowitem">
                <div class="title">
                  <div class="source">{{item.dowsource_name}}</div>
                  <div class="name">{{item.name}}</div>
                </div>
                <div class="info">{{item.dowinfo}}</div>
                <div class="feedback" @click="feedback(item.id)">失效反馈</div>
              </div>
            </div>
          </div>
        </div>

        <div class="right-content">
          <div class="page relation_bangumi">
            <div class="p-name">相关</div>
            <div class="p-content">
              <div class="cover">
                <img :src="relation_bangumi_cover" style="width:100%" />
              </div>
              <div class="title">{{relation_bangumi_name}}</div>
              <a
                :underline="false"
                :href="'/bangumi/info?id=' + relation_bangumi_id"
                target="_blank"
                style="width: 100%;"
              >
                <div class="button">立即观看</div>
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "info",
  data() {
    return {
      id: "",
      identification: "",
      cover: "",
      classification: "",
      introduce: "",
      relation_bangumi_id: "",
      show_index: "",
      status: "",
      name: "",
      relation_bangumi_cover: "",
      relation_bangumi_name: "",
      dowlist: ""
    };
  },
  methods: {
    feedback(id) {
      let user = this.$authUser.getUserToken();
      if (user) {
        this.$http
          .AlbumDowurlFeedback(id)
          .then(response => {
            if (response.code == 200) {
              this.$Message({
                message: "反馈成功",
                duration: 5 * 1000
              });
            }
          })
          .catch(error => {
            console.log("error", error);
          });
      } else {
        this.$Message({
          message: "请先登录!!!!!!",
          type: "error",
          duration: 5 * 1000
        });
      }
    },
    query(id) {
      this.$http
        .AlbumInfo(id)
        .then(response => {
          if (response.code == 200) {
            this.getUrlList(this.$route.query.id);
            let result = response.data.result;
            this.id = result.id;
            this.cover = result.cover;
            this.classification = result.classification;
            this.name = result.name;
            this.introduce = result.introduce;
            this.relation_bangumi_id = result.relation_bangumi_id;
            if (result.relation_bangumi_id) {
              let relation_bangumi = response.data.relation_bangumi;
              this.relation_bangumi_cover = relation_bangumi.cover;
              this.relation_bangumi_name = relation_bangumi.name;
            }
          }
        })
        .catch(error => {
          console.log("error", error);
        });
    },
    getUrlList(id) {
      this.$http
        .AlbumDowurlList({ id: id })
        .then(response => {
          if (response.code == 200) {
            this.dowlist = response.data;
          }
        })
        .catch(error => {
          console.log("error", error);
        });
    }
  },
  components: {},
  created() {
    this.query(this.$route.query.id);
  }
};
</script>

<style lang="scss" scoped>
.top {
  display: flow-root;
  width: 100%;
  .left {
    float: left;
    width: 250px;
    height: 250px;
  }
  .rgiht {
    float: right;
    width: calc(100% - 280px);
    .type {
      width: 100%;
      height: 30px;
      .item {
        padding-left: 22px;
        padding-right: 22px;
        line-height: 30px;
        font-weight: bold;
        font-size: 18px;
        color: #fff;
        background-color: #fd3258;
        float: left;
      }
    }
    .title {
      font-size: 18px;
      width: 100%;
      margin-top: 20px;
    }
    .introduce {
      margin-top: 20px;
      width: 100%;
      font-size: 12px;
    }
  }
}
.bottom {
  margin-top: 40px;
  display: flow-root;
  .left-content {
    width: calc(100% - 320px);
    float: left;
  }
  .right-content {
    width: 250px;
    float: right;
  }
}
.page {
  margin-bottom: 30px;
  .p-name {
    font-weight: bold;
    color: #000;
    font-size: 18px;
    width: 100%;
    margin-bottom: 22px;
  }
  .p-content {
    width: 100%;
    display: flow-root;
  }
}
.relation_bangumi {
  width: 100%;
  .cover {
    width: 100%;
  }
  .title {
    width: 100%;
    color: #484848;
    margin-top: 15px;
    font-size: 14px;
    font-weight: bold;
    margin-top: 15px;
  }
  .button {
    width: 100%;
    border: 2px solid #eeeeee;
    margin-top: 17px;
    height: 40px;
    text-align: center;
    line-height: 40px;
    font-size: 14px;
    font-weight: bold;
    color: #5e5e5e;
  }
}
.dowitem {
  position: relative;
  padding: 20px;
  border: 2px solid #f4f4f4;
  margin-bottom: 20px;
  display: flow-root;
  .title {
    line-height: 18px;
    width: 100%;
    display: flow-root;
    .source {
      float: left;
      margin-right: 20px;
      color: #000;
      font-size: 14px;
      font-weight: bold;
    }
    .name {
      float: left;
      font-size: 14px;
    }
  }
  .info {
    width: 100%;
    margin-top: 15px;
    font-size: 14px;
    color: #000;
  }
  .feedback {
    width: 85px;
    height: 30px;
    position: absolute;
    right: 40px;
    top: 30px;
    border: 1px solid #bbbbbb;
    font-size: 12px;
    line-height: 30px;
    text-align: center;
  }
  .feedback:hover {
    border: 1px solid #0072ff96;
  }
}
</style>