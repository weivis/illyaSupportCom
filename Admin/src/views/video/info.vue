<template>
  <div>
    <el-dialog title="请输入退回的理由" :visible.sync="backinfo_win" width="30%">
    <el-input
    type="textarea"
    :rows="4"
    placeholder="退回原因"
    v-model="backinfo_input">
    </el-input>
      <span slot="footer" class="dialog-footer">
        <el-button @click="backinfo_win = false">取 消</el-button>
        <el-button type="primary" @click="verify_back()">确 定</el-button>
      </span>
    </el-dialog>

    <div class="Common page-width">
      <div class="l">
        <iframe
          :src="'https://xbeibeix.com/api/bilibili/biliplayer/?url=' + videoloadurl"
          allowfullscreen="true"
          class="iframe"
          scrolling="yes"
          frameborder="0"
        ></iframe>
      </div>
      <div class="r">
        <div class="mb">
          稿件状态:
          <span v-if="verify_type == 1">审核通过</span>
          <span v-if="verify_type == 2">等待审核</span>
          <span v-if="verify_type == 3">退回</span>
        </div>
        <div class="mb">
            退回原因:<br/>
          {{verify_falseinfo}}
        </div>
        <div class="button" @click="verify_ok()">通过审核</div>
        <div class="button" @click="backrollr()">回滚到等待审核</div>
        <div class="button" @click="backinfo_win = true">退回</div>
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
      videoloadurl: "",
      verify_type: "",
      backinfo_input: "",
      backinfo_win:false,
      verify_falseinfo:""
    };
  },
  methods: {
    verify_back() {
      this.$http
        .VideoAdminVerify({
          id: this.id,
          verify_type: 3,
          verify_falseinfo: this.backinfo_input
        })
        .then(response => {
          if (response.code == 200) {
              this.backinfo_win = false
            this.$Message({
              message: response.msg,
              duration: 5 * 1000
            });
            this.query(this.$route.query.id);
          }
        })
        .catch(error => {
          console.log("error", error);
        });
    },
    backrollr() {
      this.$http
        .VideoAdminVerify({ id: this.id, verify_type: 2 })
        .then(response => {
          if (response.code == 200) {
            this.$Message({
              message: response.msg,
              duration: 5 * 1000
            });
            this.query(this.$route.query.id);
          }
        })
        .catch(error => {
          console.log("error", error);
        });
    },
    verify_ok() {
      this.$http
        .VideoAdminVerify({ id: this.id, verify_type: 1 })
        .then(response => {
          if (response.code == 200) {
            this.$Message({
              message: response.msg,
              duration: 5 * 1000
            });
            this.query(this.$route.query.id);
          }
        })
        .catch(error => {
          console.log("error", error);
        });
    },
    query(id) {
      this.$http
        .VideoQuery({ id: id })
        .then(response => {
          if (response.code == 200) {
            this.verify_type = response.data.verify_type;
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
            this.verify_falseinfo = response.data.verify_falseinfo;
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
.l {
  width: calc(100% - 260px);
  float: left;
}
.r {
  width: 180px;
  float: right;
  border-left: 1px solid #cecece;
  min-height: calc(100vh - 50px);
  padding: 25px;
  padding-top: 0;
  .button {
    border: 1px solid #cecece;
    width: 100%;
    height: 40px;
    text-align: center;
    font-size: 14px;
    line-height: 40px;
    margin-bottom: 15px;
  }
  .mb {
    margin-bottom: 15px;
  }
}
.iframe {
  width: 100%;
  height: 570px;
}
</style>