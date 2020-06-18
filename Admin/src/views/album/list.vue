<template>
  <div>

    <el-row class="common rwoh">
      <div class="common felmr">
        类型
        <el-radio-group v-model="types">
          <el-radio-button :label="0">全部</el-radio-button>
          <el-radio-button :label="1">番剧</el-radio-button>
          <el-radio-button :label="2">OST</el-radio-button>
          <el-radio-button :label="3">MMD</el-radio-button>
          <el-radio-button :label="4">Live2D</el-radio-button>
        </el-radio-group>
      </div>
      <div class="common felmr">
        状态
        <el-radio-group v-model="sfilter" class="common elmr">
          <el-radio-button :label="0">已上架</el-radio-button>
          <el-radio-button :label="1">全部</el-radio-button>
        </el-radio-group>
      </div>
      <el-button type="primary" @click="getList()">查询</el-button>
    </el-row>

    <el-table :data="tableData" style="width: 100%">
      <el-table-column prop="id" label="ID" width="50"></el-table-column>

      <el-table-column prop="head" label="封面" width="100">
        <template slot-scope="scope">
          <el-image style="width: 90%; height: auto" :src="scope.row.cover"></el-image>
        </template>
      </el-table-column>
      <el-table-column label="类型" width="100">
        <template slot-scope="scope">
          <span v-if="scope.row.classification == 1">番剧</span>
          <span v-if="scope.row.classification == 2">OST</span>
          <span v-if="scope.row.classification == 3">MMD</span>
          <span v-if="scope.row.classification == 4">Live2D</span>
        </template>
      </el-table-column>
      <el-table-column prop="name" label="标题"></el-table-column>
      <el-table-column prop="introduce" label="简介"></el-table-column>

      <el-table-column label="更多" width="500px">
        <template slot-scope="scope">

          <el-button @click="change({id:scope.row.id, changeto:1})" v-if="scope.row.status == 1" type="success" style="margin-right: 0px;">下架</el-button>
          <el-button @click="change({id:scope.row.id, changeto:1})" v-if="scope.row.status == 2" type="info" style="margin-right: 0px;">上架</el-button>

          <el-button @click="change({id:scope.row.id, changeto:2})" v-if="scope.row.show_index == true" type="success" style="margin-right: 10px;">取消首页展示</el-button>
          <el-button @click="change({id:scope.row.id, changeto:2})" v-if="scope.row.show_index == false" style="margin-right: 10px;">首页展示</el-button>

          <a :href="'edit?id=' + scope.row.id" target="_blank" style="margin-right: 10px;"><el-button>编辑</el-button></a>
          <el-button @click="change({id:scope.row.id, changeto:4})">删除</el-button>
        </template>
      </el-table-column>
    </el-table>

    <el-row class="common rwoh">
      <Pagination
        :total="totalItem"
        :page.sync="currentPage"
        @pagination="getList(types, currentPage)"
        :limit.sync="pageSize"
      />
    </el-row>
  </div>
</template>

<script>
import Pagination from "@/components/Pagination.vue";
export default {
  name: "list",
  data() {
    return {
      tableData: [],
      types: 0,
      sfilter: 0,
      currentPage: 1, // 当前页码
      totalItem: 0, // 总条目
      totalPage: 0, // 总页数
      pageSize: 15 // 每页多少条
    };
  },
  methods: {
    getList() {
      this.$http
        .AlbumList({
          types: this.types,
          sfilter: this.sfilter,
          keyword: this.keyword,
          pages: this.currentPage
        })
        .then(response => {
          if (response.code == 200) {
            this.tableData = response.data.result;
            this.currentPage = response.data.page;
            this.totalPage = response.data.pages;
            this.totalItem = response.data.count;
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
            this.getList()
          }
        })
        .catch(error => {
          console.log("error", error);
        });
    }
  },
  components: {
    Pagination
  },
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
  width: 178px;
  height: 178px;
  display: block;
}
.rowbtom {
  margin-bottom: 15px;
}
</style>