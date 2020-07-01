<template>
  <div>
    <div class="bill" :style="bill">
      <a class="a" href="/bangumi/info?id=4" target="_blank"></a>
    </div>

    <div class="Common page-width content">
      <div class="body-p">
        <div class="body-l">

          <div class="common-mp">
            <div class="li">
              <span class="title">アニメ</span>
              <div class="r-button">
                <a href="/bangumi" target="_blank">更多</a>
              </div>
            </div>
            <div class="content">
              <div v-for="(item, index) in moduledata_bangumi" :key="index">
                
                <el-link :href="'/bangumi/info?id=' + item.id" target="_blank" :underline="false" class="bangumiitem">
                <div class="cover">
                  <img :src="item.cover" style="width: 100%" />
                </div>
                <div class="r">
                  <div class="title">
                    {{item.name}}
                  </div>
                  <div class="info">
                    <div class="info">
                      <span class="mr">{{item.openplay_time}}开播</span>
                      <span class="mr">全{{item.setscount}}话</span>
                      <span class="mr" v-if="item.upstatus === true">连载中</span>
                      <span class="mr" v-if="item.upstatus === false">已完结</span>
                    </div>
                  </div>
                  <div class="button">立即观看</div>
                </div>
                </el-link>
              </div>
            </div>
          </div>

          <div class="common-mp">
            <div class="li">
              <span class="title">资源</span>
              <div class="r-button">
                <a href="/album" target="_blank">更多</a>
              </div>
            </div>
            <div class="content">
              <div class="album">
                <a href="/album" target="_blank"><div class="button">アニメ</div></a>
                <a href="/album" target="_blank"><div class="button">OST</div></a>
                <a href="/album" target="_blank"><div class="button">MMD Model</div></a>
                <a href="/album" target="_blank"><div class="button">Live2D</div></a>
              </div>
            </div>
          </div>

          <div class="common-mp">
            <div class="li">
              <span class="title">MAD·AMV</span>
              <div class="r-button">
                <a href="/doujin" target="_blank">更多</a>
              </div>
            </div>
            <div class="content">
              <el-row :gutter="20">
                <el-col
                  v-for="(item, index) in moduledata_madamv"
                  :key="index + 'madamv'"
                  :span="9"
                  :xs="12"
                  :lg="6"
                  class="madamvitem"
                >
                  <div>
                    <el-link :href="'/doujin'" target="_blank" :underline="false">
                    <img :src="item.cover" style="width: 100%" />
                    <div class="title">{{item.title}}</div>
                    </el-link>
                  </div>
                </el-col>
              </el-row>
            </div>
          </div>

        </div>
        <div class="body-r">
          <div class="common-mp">
            <div class="li">
              <span class="title">公式情報</span>
              <div class="r-button">
                <a href="/news" target="_blank">更多</a>
              </div>
            </div>
            <div class="content">
              <div v-for="(item, index) in moduledata_news" :key="index" class="newsitem">
                <el-link :href="'/news/item?id=' + item.id" target="_blank" :underline="false">
                  <div class="l">
                    <div class="cover">
                      <el-image
                        style="width:100%;height:100%;display:block;"
                        :src="item.cover"
                        fit="cover"
                      ></el-image>
                    </div>
                  </div>
                  <div class="r">
                    <div class="title">{{item.title}}</div>
                  </div>
                </el-link>
              </div>
            </div>
          </div>

          <div class="common-mp">
            <div class="li">
              <span class="title">絵を描く</span>
              <div class="r-button">
                <a href="/photo" target="_blank">更多</a>
              </div>
            </div>
            <div class="content">
              <el-row :gutter="10">
                <el-col
                  v-for="(item, index) in moduledata_photo"
                  :key="index + 'photo'"
                  :span="12"
                  class="photoitem"
                >
                  <div>
                    <el-link :href="'/photo'" target="_blank" :underline="false">
                    <img :src="item.cover" style="width: 100%" />
                    </el-link>
                  </div>
                </el-col>
              </el-row>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: "Home",
  data() {
    return {
      bill:
        "background-image: url(https://illya-support.weivird.com/static/com/bill/1.jpg);",
      moduledata_madamv: [],
      moduledata_bangumi: [],
      moduledata_news: [],
      moduledata_photo: []
    };
  },
  components: {},
  methods: {
    getindex() {
      this.$http
        .getindex({})
        .then(response => {
          if (response.code == 200) {
            console.log(response.data);
            this.moduledata_madamv = response.data.madamv;
            this.moduledata_bangumi = response.data.bangumi;
            this.moduledata_news = response.data.news;
            this.moduledata_photo = response.data.photo;
          }
        })
        .catch(error => {
          console.log("error", error);
        });
    },
    getList(n) {
      console.log(n);
    }
  },
  created() {
    this.getindex();
  }
};
</script>
<style lang="scss" scoped>
.bill {
  height: 384px;
  width: 100%;
  background-repeat: no-repeat;
  background-position: top;
  background-size: cover;
  position: relative;
  .a {
    position: absolute;
    width: 100%;
    height: 100%;
  }
}
.body-p {
  display: flow-root;
  .body-l {
    width: calc(100% - 450px);
    float: left;
  }
  .body-r {
    width: 400px;
    float: right;
  }
}
.common-mp {
  border-bottom: 1px solid #cecece;
  padding-bottom: 30px;
  .li {
    height: 20px;
    line-height: 20px;
    padding-top: 25px;
    padding-bottom: 25px;
    .title {
      font-size: 14px;
      font-weight: bold;
      color: #484848;
    }
    .r-button {
      padding-left: 10px;
      padding-right: 10px;
      height: 20px;
      float: right;
      font-size: 12px;
      border: 1px solid #ffa5b6;
      border-radius: 30px;
      a {
        color: #000;
      }
    }
  }
  .content {
    display: flow-root;
    width: 100%;
  }
}

.madamvitem {
  .title {
    font-size: 14px;
  }
}
.photoitem {
  overflow: hidden;
  margin-bottom: 5px;
}

.album{
  .button{
    padding-left: 40px;padding-right: 40px;line-height: 40px;height: 40px;background-color: #eaeaea;border-radius: 3px;color: #484848;font-weight: bold;float: left;margin-right: 25px;font-size: 14px;margin-bottom: 10px;
  }
}

.bangumiitem{
  width: calc(50% - 15px);padding-right: 15px;float: left;display: flow-root;margin-bottom: 25px;
  .cover{
    float: left;
    width: 145px;
    height: 193px;
    overflow: hidden;
  }
  .r{
    position: relative;
    float: right;
    width: calc(100% - 175px);
    height: 193px;
    .mr{margin-right: 10px;}
    .info{font-size: 14px;margin-top: 10px;}
    .title{font-size: 16px;font-weight: bold;color: #484848;margin-top: 40px;}
    .button{position: absolute;width: 138px;height: 45px;background-color: #ff4d7f;bottom: 0;left: 0;font-size: 14px;color: #fff;line-height: 45px;text-align: center;}
  }
}

.newsitem {
  display: flow-root;
  margin-bottom: 15px;
  .l {
    width: 200px;
    float: left;
  }
  .r {
    width: calc(100% - 215px);
    float: right;
    .title {
      font-size: 14px;
      font-weight: bold;
    }
  }
}

@media screen and (max-width: 1670px) {
  .body-p {
    display: flow-root;
    .body-l {
      width: calc(100% - 350px);
      float: left;
    }
    .body-r {
      width: 300px;
      float: right;
    }
  }
  .newsitem {
    display: flow-root;
    margin-bottom: 15px;
    .l {
      width: 150px;
      float: left;
    }
    .r {
      width: calc(100% - 165px);
      float: right;
      .title {
        font-size: 14px;
        font-weight: bold;
      }
    }
  }
}

@media screen and (max-width: 1200px) {
  .bangumiitem{
  width: 100%;padding-right: 15px;float: left;display: flow-root;margin-bottom: 25px;
}}

@media screen and (max-width: 800px) {
  .bangumiitem{
  width: 100%;padding-right: 15px;float: left;display: flow-root;margin-bottom: 25px;
}

  .body-p {
    display: flow-root;
    .body-l {
      width: 100%;
      float: left;
    }
    .body-r {
      width: 100%;
      float: right;
    }
  }
}
</style>