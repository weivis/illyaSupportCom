<template>
  <div>
    <el-dialog title="提示" :visible.sync="window_addurl" width="50%">
      <el-input placeholder="请输入内容" v-model="AddDowUrl_SourceName" class="funcbuttonrow">
        <template slot="prepend">下载来源(百度云 XXX)</template>
      </el-input>
      <el-input placeholder="请输入内容" v-model="AddDowUrl_name" class="funcbuttonrow">
        <template slot="prepend">资源名(320K Mp4)</template>
      </el-input>
      <el-input placeholder="请输入内容" v-model="AddDowUrl_dowinfo" class="funcbuttonrow">
        <template slot="prepend">下载信息</template>
      </el-input>
      <span slot="footer" class="dialog-footer">
        <el-button @click="window_addurl = false">取 消</el-button>
        <el-button type="primary" @click="AddDow_Send()">确 定</el-button>
      </span>
    </el-dialog>

    <div class="content">
      <div style="display: flow-root;">
        <div class="left">
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
        </div>

        <div class="right">
          <el-row class="common rwoh">
            资源分区
            <el-radio-group v-model="classification">
              <el-radio-button :label="1">番剧</el-radio-button>
              <el-radio-button :label="2">OST</el-radio-button>
              <el-radio-button :label="3">MMD</el-radio-button>
              <el-radio-button :label="4">Live2D</el-radio-button>
            </el-radio-group>
            - 系统唯一ID: {{identification}}
          </el-row>

          <el-row class="common rwoh">
            <el-input placeholder="请输入内容" v-model="name">
              <template slot="prepend">资源名</template>
            </el-input>
          </el-row>

          <el-row class="common rwoh">
            <el-input type="textarea" :rows="5" placeholder="资源介绍" v-model="introduce"></el-input>
          </el-row>
        </div>
      </div>

      <div class="line"></div>

      <el-row class="common rwoh">
        <el-table :data="DowList" style="width: 100%">
          <el-table-column prop="id" label="ID" width="50"></el-table-column>
          <el-table-column prop="dowsource_name" label="下载来源名" width="130"></el-table-column>
          <el-table-column prop="name" label="资源备注名" width="200"></el-table-column>
          <el-table-column prop="dowinfo" label="下载信息"></el-table-column>
          <el-table-column prop="feedback" label="反馈次数" width="100"></el-table-column>
        <el-table-column label="更多" width="100px">
            <template slot-scope="scope">
            <el-button @click="Del_DowUrl(scope.row.id)">删除</el-button>
            </template>
        </el-table-column>
        </el-table>
      </el-row>
    </div>
    <div class="rnav">
      <el-row class="funcbuttonrow">
        <div v-if="status === 1">资源状态: 正常</div>

        <div v-if="status === 2">资源状态: 已下架</div>
      </el-row>

      <el-row class="funcbuttonrow">
        <div v-if="show_index === true">首页展示: 是</div>

        <div v-if="show_index === false">首页展示: 否</div>
      </el-row>

      <el-row class="funcbuttonrow">
        <el-button @click="save()">保存修改</el-button>
      </el-row>

      <el-row class="funcbuttonrow">
        <el-button @click="change({id:id, changeto:1})" v-if="status === 2">上架</el-button>
        <el-button @click="change({id:id, changeto:1})" v-if="status === 1">下架</el-button>
      </el-row>

      <el-row class="funcbuttonrow">
        <el-button @click="change({id:id, changeto:2})" v-if="show_index === true">取消首页展示</el-button>
        <el-button @click="change({id:id, changeto:2})" v-if="show_index === false">首页展示</el-button>
      </el-row>

      <el-row class="funcbuttonrow">
        <el-button @click="Open_AddDow()">添加下载地址信息</el-button>
      </el-row>
    </div>
  </div>
</template>

<script>
export default {
  name: "edit",
  data() {
    return {
      id: "",
      name: "",
      introduce: "",
      classification: "",
      cover: "",
      loadcover: "",
      status: "",
      show_index: "",
      identification: "",
      DowList: [],
      window_addurl: false,
      AddDowUrl_SourceName: "",
      AddDowUrl_name: "",
      AddDowUrl_dowinfo: ""
    };
  },
  methods: {
    Del_DowUrl(id){
        this.$http.AlbumDowurlDel({
            id:id
        })
        .then(response => {
          if (response.code == 200) {
            this.$message({
              message: response.msg,
              type: "success"
            });
            this.getUrlList(this.$route.query.id);
          }
        })
        .catch(error => {
          console.log("error", error);
        });
    },
    Open_AddDow() {
      this.window_addurl = true;
    },
    AddDow_Send() {
      this.$http
        .AlbumDowurlAddOrEdit({
          album_id: this.id,
          dowsource_name: this.AddDowUrl_SourceName,
          name: this.AddDowUrl_name,
          dowinfo: this.AddDowUrl_dowinfo
        })
        .then(response => {
          if (response.code == 200) {
            this.$message({
              message: response.msg,
              type: "success"
            });
            this.getUrlList(this.$route.query.id);
            this.window_addurl = false;
            this.AddDowUrl_SourceName = "";
            this.AddDowUrl_name = "";
            this.AddDowUrl_dowinfo = "";
          }
        })
        .catch(error => {
          console.log("error", error);
        });
    },
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
    },
    query(id) {
      this.$http
        .AlbumInfo({ id: id })
        .then(response => {
          if (response.code == 200) {
            let result = response.data.result;
            this.id = result.id;
            this.identification = result.identification;
            this.classification = result.classification;
            this.loadcover = result.cover;
            this.cover = result.file;
            this.introduce = result.introduce;
            this.name = result.name;
            this.show_index = result.show_index;
            this.status = result.status;
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
            this.DowList = response.data;
          }
        })
        .catch(error => {
          console.log("error", error);
        });
    },
    change(data) {
      this.$http
        .AlbumChange(data)
        .then(response => {
          if (response.code == 200) {
            this.query(this.$route.query.id);
          }
        })
        .catch(error => {
          console.log("error", error);
        });
    }
  },
  created() {
    this.query(this.$route.query.id);
    this.getUrlList(this.$route.query.id);
  }
};
</script>
<style lang="scss" scoped>
.funcbuttonrow {
  margin-bottom: 15px;
}
.left {
  float: left;
  width: 300px;
  height: 300px;
}
.right {
  float: right;
  width: calc(100% - 320px);
  min-height: 300px;
}
.content {
  width: calc(100% - 210px);
}
.rnav {
  width: 180px;
  border-left: 1px solid #409eff;
  height: 100%;
  position: fixed;
  right: 20px;
  top: 90px;
  padding-left: 20px;
}
</style>
<style>
.el-upload-dragger {
  width: 300px;
  height: 300px;
}
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