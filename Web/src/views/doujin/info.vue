<template>
  <div>
    <!-- <div class="Common page-width">
      <iframe :src="'https://xbeibeix.com/api/bilibili/biliplayer/?url=' + videoloadurl" allowfullscreen="true" class="iframe" width="100%" scrolling="yes" frameborder="0"></iframe>
    </div>-->
    <!-- <video :src="'https://xbeibeix.com/api/bilibili/biliplayer/?url=' + 'BV1XC4y1h7yb'" controls="controls">
    您的浏览器不支持 video 标签。
    </video>-->
    <div class="Common page-width">
      <div class="videoinfo">
        <div class="top">{{title}}</div>
        <div class="bra"></div>
        <div class="content"></div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "info",
  data() {
    return {
      id: 0,
      loadcover: "",
      cover: "",
      classification: "",
      content_classification: 0,
      title: "",
      introduce: "",
      source_type: 1,
      original_type: 1,
      original_url: "",
      original_author: "",
      videoloadurl: ""
    };
  },
  methods: {
    query(id) {
      this.$http
        .VideoQuery({ id: id })
        .then(response => {
          if (response.code == 200) {
            this.id = response.data.id;
            this.cover = response.data.filecover;
            this.loadcover = response.data.cover;
            this.classification = response.data.classification;
            this.content_classification = response.data.content_classification;
            this.title = response.data.title;
            this.introduce = response.data.introduce;
            this.source_type = response.data.source_type;
            this.original_type = response.data.original_type;
            this.original_url = response.data.original_url;
            this.original_author = response.data.original_author;
            this.videoloadurl = response.data.videoloadurl;
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
.videoinfo {
  margin-top: 30px;
  height: 160px;
  margin-bottom: 10px;
  .top {
    height: 40px;line-height: 40px;
    width: 100%;
    font-size: 18px;
    border-bottom: 1px solid #cecece;
  }
  .content {
    width: 100%;
    height: 150px;
  }
}
.iframe {
  height: calc(100vw - 100vh);
  min-height: 640px;
  max-height: 720px;
}
@media screen and (max-width: 800px) {
  .iframe {
    height: calc(100vw - 140vh);
    min-height: 440px;
    max-height: 720px;
  }
}
</style>