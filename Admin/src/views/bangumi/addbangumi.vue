<template>
  <div>
    <div style="display: flex;">
      <div class="left">
        <el-row class="common rwoh">
          <el-upload
            class="content"
            drag
            action
            :http-request="upLoad"
            :show-file-list="false"
            multiple
          >
            <img :src="loadcover" style="width:100%" />
            <i class="el-icon-upload"></i>
            <div class="el-upload__text">
              将文件拖到此处，或
              <em>点击上传</em>
            </div>
            <!-- <div class="el-upload__tip" slot="tip">只能上传jpg/png文件，且不超过500kb</div> -->
          </el-upload>
        </el-row>
      </div>

      <div class="right">
        <el-row class="common rwoh">
          <el-input placeholder="请输入内容" v-model="name">
            <template slot="prepend">番剧名</template>
          </el-input>
        </el-row>

        <el-row class="common rwoh">
          <div class="common felmr">
            类型
            <el-radio-group v-model="classification" style="margin-right:15px">
              <el-radio-button label="1">番剧</el-radio-button>
              <el-radio-button label="2">剧场版</el-radio-button>
              <el-radio-button label="3">OVA</el-radio-button>
              <el-radio-button label="4">SP</el-radio-button>
            </el-radio-group>
          </div>

          <div class="common felmr">
            连载状态
            <el-radio-group v-model="upstatus">
              <el-radio-button :label="true">连载中</el-radio-button>
              <el-radio-button :label="false">已完结</el-radio-button>
            </el-radio-group>
          </div>

          <div class="common felmr">
            是否上架
            <el-radio-group v-model="status">
              <el-radio-button :label="1">是</el-radio-button>
              <el-radio-button :label="2">否</el-radio-button>
            </el-radio-group>
          </div>
        </el-row>

        <el-row class="common rwoh">
          <div class="common felmr">
            开播时间
            <el-date-picker
              v-model="openplay_time"
              type="date"
              placeholder="开播时间"
              format="yyyy 年 MM 月 dd 日"
              value-format="yyyy-MM-dd"
            ></el-date-picker>
          </div>

          <div class="common felmr">
            是否允许站内播放
            <el-select v-model="station_play" placeholder="请选择">
              <el-option label="允许" :value="true"></el-option>
              <el-option label="不开放" :value="false"></el-option>
            </el-select>
          </div>
        </el-row>

        <el-row class="common rwoh">
          <div class="common felmr">
            <el-input placeholder="请输入剧集数" v-model="setscount">
              <template slot="prepend">剧集数</template>
            </el-input>
          </div>

          <div class="common felmr">
            <el-input placeholder="权重" v-model="sort">
              <template slot="prepend">权重</template>
            </el-input>
          </div>
        </el-row>
      </div>
    </div>
    <div class="line"></div>
    <el-row class="common rwoh">
      番剧介绍
      <el-input type="textarea" :rows="5" placeholder="请输入内容" v-model="introduce"></el-input>
    </el-row>
    <el-row class="common rwoh">
      STAFF
      <el-input type="textarea" :rows="5" placeholder="请输入内容" v-model="staff"></el-input>
    </el-row>

    <el-button @click="save()">确定</el-button>
  </div>
</template>

<script>
export default {
  name: "addbangumi",
  data() {
    return {
      classification: "",
      openplay_time: "",
      name: "",
      setscount: "",
      introduce: "",
      cover: "",
      upstatus: false,
      staff: "",
      station_play: false,
      status: 2,
      sort: 0,
      loadcover: ""
    };
  },
  methods: {
    save() {
      let data = {
        classification: this.classification,
        openplay_time: this.openplay_time,
        name: this.name,
        setscount: this.setscount,
        introduce: this.introduce,
        cover: this.cover,
        upstatus: this.upstatus,
        staff: this.staff,
        station_play: this.station_play,
        status: this.status,
        sort: this.sort
      };
      this.$http
        .bangumiAddOrEdit(data)
        .then(response => {
          if (response.code == 200) {
            this.$message({
                message: response.msg,
                type: 'success'
            })
          }
        })
        .catch(error => {
          console.log("error", error);
        });
    },
    upLoad(file) {
      const formData = new FormData();
      formData.append("file", file.file);
      formData.append("uploadKey", "bangumicover");

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
  }
};
</script>

<style>
.el-upload-dragger {
  height: 300px !important;
  width: 230px !important;
  z-index: 1000;
}
</style>
<style lang="scss" scoped>
.left {
  width: 250px;
  height: 300px;
  float: left;
}
.right {
  width: calc(100% - 260px);
  min-height: 300px;
  float: right;
}
</style>