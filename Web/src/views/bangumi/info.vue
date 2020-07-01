<template>
  <div>
    <div class="top">
      <div class="Common page-width content">
        <div class="left">
          <img :src="cover" style="width:100%" />
        </div>
        <div class="right">
          <div class="title">{{name}}</div>
          <div class="info">
            <span class="mr">{{openplay_time}}开播</span>
            <span class="mr">全{{setscount}}话</span>
            <span class="mr" v-if="upstatus === true">连载中</span>
            <span class="mr" v-if="upstatus === false">已完结</span>
          </div>
          <div class="introduce">{{introduce}}</div>
        </div>
      </div>
      <div class="filterm">
        <div :style="background" class="filter"></div>
      </div>
    </div>
    <div class="bottom Common page-width">
      <div class="left-content">
        <div class="page">
          <div class="p-name">播放源</div>
          <div class="p-content">
              <el-link v-for="(item, index) in playsource_list" :key="index" :href="item.url" target="_blank" :underline="false">
                <div class="PlaySource-button">{{item.source_name}}</div>
              </el-link>
          </div>
        </div>
        <div class="line"></div>
        <div class="page">
          <div class="p-name">CV</div>
          <div class="p-content">
            <div v-for="(item, index) in cv_list" :key="index" class="cv">
              <div class="head">
                <img :src="item.head" style="width:100%" />
              </div>
              <div class="info">
                <div class="name">{{item.people_name}}</div>
                <div class="role">{{item.role_name}}</div>
              </div>
            </div>
          </div>
        </div>
        <div class="line"></div>
      </div>
      <div class="right-content">
        <div class="page">
          <div class="p-name">STAFF</div>
          <div class="staff">{{staff}}</div>
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
      cover: "",
      classification: "",
      identification: "",
      introduce: "",
      name: "",
      openplay_time: "",
      setscount: "",
      sort: "",
      sourcecover: "",
      staff: "",
      station_play: "",
      upstatus: "",
      cv_list: [],
      playsource_list: [],
      background: ""
    };
  },
  methods: {
    query(id) {
      this.$http
        .bangumiInfo(id)
        .then(response => {
          if (response.code == 200) {
            let result = response.data.result;
            this.id = result.id;
            this.cover = result.cover;
            this.classification = result.classification;
            this.identification = result.identification;
            this.introduce = result.introduce;
            this.name = result.name;
            this.openplay_time = result.openplay_time;
            this.setscount = result.setscount;
            this.sort = result.sort;
            this.sourcecover = result.sourcecover;
            this.staff = result.staff;
            this.station_play = result.station_play;
            this.upstatus = result.upstatus;
            this.cv_list = response.data.cv;
            this.playsource_list = response.data.playsource;
            this.background = "background-image:url('" + result.cover + "')";
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
.filterm {
  height: inherit;
  width: 100%;
  position: absolute;
  overflow: hidden;
  left: 0;
  -webkit-transform: translateZ(0);
  transform: translateZ(0);
}
.filter {
  position: absolute;
  background-size: cover;
  background-position: 50%;
  width: 110%;
  min-width: 1120px;
  height: 496px;
  top: 50%;
  left: 50%;
  margin: -260px -55%;
  z-index: 10;
  background-repeat: no-repeat;
  -webkit-filter: blur(40px);
  -moz-filter: blur(40px);
  -ms-filter: blur(40px);
  filter: blur(40px);
  filter: progid:DXImageTransform.Microsoft.Blur(PixelRadius=10,MakeShadow=false);
}
.top {
  height: 399px;
  overflow: hidden;
  display: flex;
  .content {
    margin-top: 33px;
    z-index: 20;
    position: relative;
  }
  .left {
    width: 250px;
    height: 333px;
    float: left;
  }
  .right {
    width: calc(100% - 290px);
    float: right;
    color: #ffffff;
    .title {
      font-size: 24px;
      font-weight: bold;
      width: 100%;
      margin-top: 60px;
    }
    .info {
      height: 14px;
      font-size: 14px;
      width: 100%;
      margin-top: 15px;
      .mr {
        margin-right: 5px;
        float: left;
      }
    }
    .introduce {
      font-size: 12px;
      width: 100%;
      margin-top: 60px;
    }
  }
}
.line {
  width: 100%;
  height: 2px;
  background-color: #f4f4f4;
  margin-top: 35px;
  margin-bottom: 35px;
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
.staff {
  font-size: 12px;
  white-space: pre-wrap;
  line-height: 20px;
}
.PlaySource-button {
  padding-left: 45px;
  padding-right: 45px;
  height: 48px;
  line-height: 50px;
  margin-right: 25px;
  border: 2px solid #eeeeee;
  float: left;
}
.cv {
  float: left;
  display: flex;
  margin-right: 50px;
  margin-bottom: 20px;
  .head {
    height: 44.5px;
    width: 44.5px;
    border-radius: 50px;
    overflow: hidden;
    float: left;
    margin-right: 5px;
  }
  .info {
    float: left;
    height: 44.5px;
    .name {
      margin: 2px;
      font-size: 14px;
    }
    .role {
      margin-top: 4px;
      font-size: 12px;
    }
  }
}

@media screen and (max-width: 600px) {
  .filterm {
    height: 1200px;
  }
  .top {
    min-height: 850px;
    height: inherit;
    .content {
      margin-top: 0px;
    }
    .left {
      width: 100%;
      height: inherit;
    }
    .right {
      width: 100%;
      .title {
        width: 100%;
        margin-top: 10px;
      }
      .info {
        height: 14px;
        width: 100%;
        margin-top: 10px;
        .mr {
          margin-right: 5px;
        }
      }
      .introduce {
        width: 100%;
        margin-top: 10px;
      }
    }
  }
  .bottom {
    margin-top: 40px;
    display: flow-root;
    .left-content {
      width: 100%;
      float: left;
    }
    .right-content {
      width: 100%;
      float: right;
    }
  }
.PlaySource-button {
  padding-left: 15px;
  padding-right: 15px;
  height: 30px;
  line-height: 30px;
  margin-right: 25px;
  border: 2px solid #eeeeee;
  float: left;
}
.cv {
  display: flex;
  margin-right: 0px;
  width: 100%;
  margin-bottom: 15px;
  .head {
    height: 44.5px;
    width: 44.5px;
    border-radius: 50px;
    overflow: hidden;
    float: left;
    margin-right: 5px;
  }
  .info {
    float: left;
    height: 44.5px;
    .name {
      margin: 2px;
      font-size: 14px;
    }
    .role {
      margin-top: 4px;
      font-size: 12px;
    }
  }
}
}
</style>