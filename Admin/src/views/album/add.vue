<template>
  <div>
    <el-row class="common rwoh">
      <el-upload
        class="upload-demo"
        :show-file-list="false"
        drag
        action
        :http-request="upLoad"
        multiple
      >
        <img v-if="loadcover" :src="loadcover" style="width: 100%" />
        <i class="el-icon-upload"></i>
        <div class="el-upload__text">
          将文件拖到此处，或
          <em>点击上传</em>
        </div>
      </el-upload>
    </el-row>

    <el-row class="common rwoh">
      资源分区
      <el-radio-group v-model="classification">
        <el-radio-button :label="1">番剧</el-radio-button>
        <el-radio-button :label="2">OST</el-radio-button>
        <el-radio-button :label="3">MMD</el-radio-button>
        <el-radio-button :label="4">Live2D</el-radio-button>
      </el-radio-group>
    </el-row>

    <el-row class="common rwoh">
      <el-input placeholder="请输入内容" v-model="name">
        <template slot="prepend">资源名</template>
      </el-input>
    </el-row>

    <el-row class="common rwoh">
      <el-input type="textarea" :rows="5" placeholder="资源介绍" v-model="introduce"></el-input>
    </el-row>

    <el-row class="common rwoh">
      <el-button @click="save()">确定</el-button>
    </el-row>
  </div>
</template>

<script>
export default {
  name: "add",
  data() {
    return {
      name: "",
      introduce: "",
      classification: "",
      cover: "",
      loadcover: ""
    };
  },
  methods: {
    save() {
      let data = {
          name: this.name,
          introduce: this.introduce,
          classification: this.classification,
          cover: this.cover
      };
      this.$http
        .AlbumAddOrEdit(data)
        .then(response => {
          if (response.code == 200) {
            this.$message({
              message: response.msg,
              type: "success"
            });
          }
        })
        .catch(error => {
          console.log("error", error);
        });
    },
    upLoad(file) {
      const formData = new FormData();
      formData.append("file", file.file);
      formData.append("uploadKey", "albumcover");

      console.log(file);
      this.$http.upload(formData).then(res => {
        console.log(res);
        console.log("上传成功");
        if (res.code === 200) {
          this.cover = res.data.filename;
          this.loadcover = res.data.lodpath;
        }
      });
    }
  }
};
</script>
<style>
.el-upload-dragger{width: 300px ;height: 300px ;}
.avatar-uploader .el-upload {
  border: 1px dashed #d9d9d9;
  border-radius: 6px;
  cursor: pointer;
  position: relative;
  overflow: hidden;
}
.avatar-uploader .el-upload:hover {
  border-color: #409eff;
}
.avatar-uploader-icon {
  font-size: 28px;
  color: #8c939d;
  width: 178px;
  height: 178px;
  line-height: 178px;
  text-align: center;
}
.avatar {
  width: 100%;
  display: block;
  height: initial;
}
</style>