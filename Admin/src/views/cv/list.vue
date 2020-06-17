<template>
  <div>
    <el-dialog title="添加新的CV信息" :visible.sync="dialog_AddCV">
        <el-row class="rowbtom">
            <el-upload
            class="avatar-uploader"
                action
                :http-request="upLoad"
                :show-file-list="false"
                multiple
            >
            <img v-if="newcv_head_load" :src="newcv_head_load" class="avatar">
            <i v-else class="el-icon-plus avatar-uploader-icon"></i>
            </el-upload>
     </el-row>

      <el-row class="rowbtom">
        <el-input placeholder="人名" v-model="newcv_name">
          <template slot="prepend">人名</template>
        </el-input>
      </el-row>

      <el-button @click="AddCv()" type>确定</el-button>
      {{newcv_head}} - {{newcv_name}}
    </el-dialog>

    <el-dialog title="编辑CV信息" :visible.sync="dialog_EditCV">
        <el-row class="rowbtom">
            {{edit_cvid}}
            <el-upload
            class="avatar-uploader"
                action
                :http-request="upLoad"
                :show-file-list="false"
                multiple
            >
            <img v-if="newcv_head_load" :src="newcv_head_load" class="avatar">
            <i v-else class="el-icon-plus avatar-uploader-icon"></i>
            </el-upload>
     </el-row>

      <el-row class="rowbtom">
        <el-input placeholder="人名" v-model="edti_cvname">
          <template slot="prepend">人名</template>
        </el-input>
      </el-row>

      <el-button @click="EditCv_Send()" type>确定</el-button>
      {{newcv_head}} - {{edti_cvname}}
    </el-dialog>

    <el-row class="common rwoh">
      <el-input placeholder="关键字" v-model="keyword" class="common elmr" style="width:300px">
        <template slot="prepend">搜索</template>
      </el-input>

      <el-radio-group v-model="sfilter" class="common elmr">
        <el-radio-button label="0">正常</el-radio-button>
        <el-radio-button label="1">全部</el-radio-button>
      </el-radio-group>

      <el-button type="primary" @click="getList()">查询</el-button>
      <el-button type="primary" @click="dialog_AddCV = true" style="float: right">新增CV信息</el-button>
    </el-row>

    <el-table :data="tableData" style="width: 100%">
      <el-table-column prop="id" label="ID" width="180"></el-table-column>

      <el-table-column prop="head" label="人像" width="150">
        <template slot-scope="scope">
          <el-image style="width: 50%; height: auto" :src="scope.row.head"></el-image>
        </template>
      </el-table-column>

      <el-table-column prop="people_name" label="CV名"></el-table-column>

      <el-table-column label="更多" width="180">
        <template slot-scope="scope">
          <el-button @click="EditCv(scope.row.id, scope.row.filename, scope.row.people_name)">编辑</el-button>
          <el-button @click="DelCv(scope.row.id)">删除</el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  name: "cvlist",
  data() {
    return {
      tableData: [],
      sfilter: 0,
      keyword: "",

      newcv_name: "",
      newcv_head: "",

      dialog_AddCV: false,
      dialog_EditCV:false,

      newcv_head_load:'',
      edit_cvid: '',
      edti_cvname: '',

    };
  },
  methods: {
    DelCv(id) {
      this.$http
        .cvDel({
          id:id
        })
        .then(response => {
          if (response.code == 200) {
            this.getList();
          }
        })
        .catch(error => {
          console.log("error", error);
        });
    },
    EditCv(id, head, people_name) {
      this.edit_cvid = id
      this.newcv_head = head
      this.edti_cvname = people_name
      this.dialog_EditCV = true
    },
    EditCv_Send(){
      this.$http
        .cvEdit({
          id: this.edit_cvid,
          people_name: this.edti_cvname,
          head: this.newcv_head
        })
        .then(response => {
          if (response.code == 200) {
            this.getList();
            this.edit_cvid = ''
            this.newcv_head = ''
            this.edti_cvname = ''
            this.dialog_EditCV = false
          }
        })
        .catch(error => {
          console.log("error", error);
        });
    },
    AddCv() {
      this.$http
        .cvAdd({
          people_name: this.newcv_name,
          head: this.newcv_head
        })
        .then(response => {
          if (response.code == 200) {
            this.getList();
            this.dialog_AddCV = false
          }
        })
        .catch(error => {
          console.log("error", error);
        });
    },
    getList() {
      this.$http
        .cvList({
          sfilter: this.sfilter,
          keyword: this.keyword
        })
        .then(response => {
          if (response.code == 200) {
            this.tableData = response.data;
          }
        })
        .catch(error => {
          console.log("error", error);
        });
    },
    upLoad(file) {
      const formData = new FormData();
      formData.append("file", file.file);
      formData.append("uploadKey", "cvhead");

      console.log(file);
      this.$http.upload(formData).then(res => {
        console.log(res);
        console.log("上传成功");
        if (res.code === 200) {
          this.newcv_head = res.data.filename;
          this.newcv_head_load = res.data.lodpath;
        }
      });
    }
  },
  components: {},
  created() {
    this.getList();
  }
};
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
</style>
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
    width: 178px;
    height: 178px;
    display: block;
  }
  .rowbtom{
      margin-bottom: 15px;
  }
</style>