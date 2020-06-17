<template>
  <div>
    
    <el-row class="common rwoh">
      <el-upload
        class="upload-demo"
        :show-file-list="false"
        drag
        action
        :http-request="upLoad"
        multiple>
        <img v-if="loadcover" :src="loadcover" style="width: 100%" >
        <i class="el-icon-upload"></i>
        <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
      </el-upload>
    </el-row>

    <el-row class="common rwoh">
      文章类目
      <el-radio-group v-model="classification" style="margin-right:15px">
        <el-radio-button :label="1">官方资讯</el-radio-button>
        <el-radio-button :label="2">手办</el-radio-button>
      </el-radio-group>
    </el-row>

    <el-row class="common rwoh">
      <el-input placeholder="请输入内容" v-model="title">
        <template slot="prepend">文章名</template>
      </el-input>
    </el-row>

    <el-row class="common rwoh">
      <el-input placeholder="请输入内容" v-model="introduce">
        <template slot="prepend">介绍</template>
      </el-input>
    </el-row>

    <el-row class="common rwoh"><editor v-model="content" :content='content' class="editor"/></el-row>

    <el-row class="common rwoh"><el-button @click="save()">确定</el-button></el-row>

  </div>
</template>

<script>
import editor from "@/components/Editor.vue";
export default {
  name: "add",
  data() {
    return {
      title: "",
      classification: "",
      introduce: "",
      content:"",
      cover: "",
      loadcover: "",
    };
  },
  methods: {
    save() {
      let data = {
        title:this.title,
        classification:this.classification,
        introduce:this.introduce,
        content:this.content,
        cover:this.cover
      };
      this.$http
        .ArticleAddoredit(data)
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
      formData.append("uploadKey", "articlecover");

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
  components: {
    editor
  }
};
</script>

<style>
  .avatar-uploader .el-upload {
    border: 1px dashed #d9d9d9;
    border-radius: 6px;
    cursor: pointer;
    position: relative;
    overflow: hidden;
  }
  .avatar-uploader .el-upload:hover {
    border-color: #409EFF;
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