<template>
  <div class="apps">
    <div class="Common page-width">
      <div v-if="ops === 0">
        <div class="top">
          <div class="l">
            <el-upload class :show-file-list="false" drag action :http-request="upLoad" multiple>
              <img v-if="loadcover" :src="loadcover" style="width: 100%" />
              <i class="el-icon-upload"></i>
              <div class="el-upload__text">
                将文件拖到此处，或
                <em>点击上传</em>
              </div>
            </el-upload>
          </div>
          <div class="r">
            <el-row class="common rwoh">
              投稿类目
              <el-radio-group v-model="classification" style="margin-right:15px">
                <el-radio-button :label="1">MAD·AMV</el-radio-button>
                <el-radio-button :label="2">MMD</el-radio-button>
                <el-radio-button :label="3">技术宅</el-radio-button>
                <el-radio-button :label="4">其他</el-radio-button>
              </el-radio-group>

              <span v-if="classification === 1">
                MAD类型
                <el-radio-group v-model="content_classification" style="margin-right:15px">
                  <el-radio-button :label="1">静止系</el-radio-button>
                  <el-radio-button :label="2">剪辑向</el-radio-button>
                  <el-radio-button :label="3">混合</el-radio-button>
                </el-radio-group>
              </span>
            </el-row>
            <el-row class="common rwoh">
              <div style="float:left">
                作品来源
                <el-radio-group v-model="original_type" style="margin-right:15px">
                  <el-radio-button :label="1">原创</el-radio-button>
                  <el-radio-button :label="2">转载</el-radio-button>
                </el-radio-group>
              </div>
              <div style="float:left" v-if="original_type === 2">
                <el-input placeholder v-model="original_author">
                  <template slot="prepend">原作者名</template>
                </el-input>
              </div>
            </el-row>
            <el-row class="common rwoh" v-if="original_type === 2">
              <el-input placeholder="http://xxxxx" v-model="original_url">
                <template slot="prepend">转载地址</template>
              </el-input>
            </el-row>
            <div class="line"></div>
            <el-row class="common rwoh">
              <el-input placeholder="请输入内容" v-model="title">
                <template slot="prepend">视频标题</template>
              </el-input>
            </el-row>
            <el-row class="common rwoh">
              <el-input type="textarea" :rows="6" placeholder="视频介绍" v-model="introduce"></el-input>
            </el-row>
          </div>
        </div>
        <div class="line"></div>
        <div class="bottom">
          <el-row class="common rwoh">
            投稿源
            <el-select v-model="source_type" placeholder="请选择">
              <el-option
                v-for="item in options"
                :key="item.value"
                :label="item.label"
                :value="item.value"
              ></el-option>
            </el-select>
          </el-row>
          <el-row class="common rwoh">
            <el-input placeholder="如 https://www.bilibili.com/video/xxxxxxx" v-model="videoloadurl">
              <template slot="prepend">视频地址, 例如B站播放地址等</template>
            </el-input>
          </el-row>
        </div>
        <div class="line"></div>
        <div class="uploadbutton" @click="Send()">
          <span v-if="edit === true">确认编辑</span>
          <span v-if="edit === false">确认无误投稿</span>
        </div>
      </div>
      <div v-if="ops === 1" class="page2">
        <div class="ico">
          <i class="el-icon-success"></i>
        </div>
        <div class="ico">
          <span v-if="edit === true">编辑成功</span>
          <span v-if="edit === false">投稿成功</span>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
export default {
  name: "Home",
  data() {
    return {
      ops: 0,
      options: [
        {
          value: 1,
          label: "BiliBili"
        },
        {
          value: 2,
          label: "Acfun(暂时未开放)"
        },
        {
          value: 3,
          label: "直传(暂时未开放)"
        }
      ],
      id: 0,
      edit: false,
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
      videoloadurl: "",
      pageid: this.$route.query.id
    };
  },
  components: {},
  methods: {
    start() {
      if (this.pageid) {
        this.getdata();
      }
    },
    getdata() {
      this.$http
        .VideoQuery({
          id: this.pageid
        })
        .then(response => {
          if (response.code == 200) {
            this.edit = true
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
    },
    Send() {
      this.$http
        .VideoUploadOrEdit({
          id: this.id,
          cover: this.cover,
          classification: this.classification,
          content_classification: this.content_classification,
          title: this.title,
          introduce: this.introduce,
          source_type: this.source_type,
          original_type: this.original_type,
          original_url: this.original_url,
          original_author: this.original_author,
          videoloadurl: this.videoloadurl
        })
        .then(response => {
          if (response.code == 200) {
            this.ops = 1;
          }
        })
        .catch(error => {
          console.log("error", error);
        });
    },
    upLoad(file) {
      const formData = new FormData();
      formData.append("file", file.file);
      formData.append("uploadKey", "videocover");

      console.log(file);
      this.$http.upload(formData).then(res => {
        console.log(res);
        console.log("上传成功");
        if (res.code === 200) {
          // console.log('res.data:',res.data)
          this.cover = res.data.filename;
          this.loadcover = res.data.lodpath;
        }
      });
    }
  },
  created() {
    let user = this.$authUser.getUser();
    if (user == null) {
      this.$router.push({ name: "home" });
    }
    this.start();
  }
};
</script>
<style lang="scss" scoped>
.apps {
  margin-top: 30px;
}
.page2 {
  .ico {
    width: 100%;
    height: 80px;
    line-height: 80px;
    text-align: center;
    font-size: 48px;
  }
}
.common.rwoh {
  margin-bottom: 30px;
}
.top {
  margin-bottom: 30px;
  display: flow-root;
  .l {
    width: 350px;
    float: left;
  }
  .r {
    width: calc(100% - 400px);
    float: right;
  }
}
.bottom {
}
.uploadbutton {
  width: 200px;
  background-color: #00adff;
  height: 50px;
  color: #fff;
  font-size: 18px;
  line-height: 50px;
  text-align: center;
  border-radius: 3px;
}
</style>