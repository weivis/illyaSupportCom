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
            </div>
            <div class="page">
                <div class="p-name">CV</div>
            </div>
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

{
  "code": 200, 
  "data": {
    "cv": [], 
    "playsource": [], 
    "result": {
      "classification": 1, 
      "cover": "http://127.0.0.1:8888/static/com/bangumi/cover/20200618015107053.jpg", 
      "id": 3, 
      "identification": "lyqxKdsMbangumi1592416281", 
      "introduce": "\u6d4b\u8bd5", 
      "name": "\u6d4b\u8bd5", 
      "openplay_time": "2020-06-02", 
      "setscount": 10, 
      "sort": 0, 
      "sourcecover": "20200618015107053.jpg", 
      "staff": "\u6d4b\u8bd5", 
      "station_play": false, 
      "status": 1, 
      "upstatus": false
    }
  }, 
  "msg": "ok"
}

<style lang="scss" scoped>
.filterm {
  height: 399px;
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
      margin-top: 33px;;
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
    .title{
        font-size: 24px;
        font-weight: bold;
        width: 100%;
        margin-top: 60px;
    }
    .info{
        height: 14px;
        font-size: 14px;
        width: 100%;
        margin-top: 15px;
        .mr {
            margin-right: 5px;
            float: left;
        }
    }
    .introduce{
        font-size: 12px;
        width: 100%;
        margin-top: 60px;
    }
  }
}
.bottom{
    margin-top: 40px;
    display: flex;
    .left-content{width: calc(100% - 280px);float: left;}
    .right-content{width: 250px;float: right;}
}
.page{
    margin-bottom: 30px;
    .p-name{
        font-weight: bold;
        color: #000;
        font-size: 18px;
        width: 100%;
        margin-bottom: 22px;
    }
}
.staff{
    font-size: 12px;
    white-space:pre-wrap;
}

</style>