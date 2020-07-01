<template>
  <div>
      <div>
        分区
        <el-radio-group v-model="category">
          <el-radio-button :label="0">全部</el-radio-button>
          <el-radio-button :label="1">原创</el-radio-button>
          <el-radio-button :label="2">Pixiv</el-radio-button>
          <el-radio-button :label="3">Cospaly</el-radio-button>
        </el-radio-group>

        类型
        <el-radio-group v-model="type">
          <el-radio-button :label="0">全部</el-radio-button>
          <el-radio-button :label="1">未审核</el-radio-button>
          <el-radio-button :label="2">已通过审核</el-radio-button>
        </el-radio-group>

      </div>
    <div class="Common page-width pcont">
    <el-table
      :data="list"
      style="width: 100%">
      <el-table-column
        prop=""
        label="图片"
        width="150">
        <template slot-scope="scope">
            <el-image style="width: 90%; height: auto" :src="scope.row.cover">
            </el-image>
        </template>
      </el-table-column>
      <el-table-column label="审核状态" width="100">
        <template slot-scope="scope">
          <span v-if="scope.row.verify == 1">以通过审核</span>
          <span v-if="scope.row.verify == 2">等待审核</span>
          <span v-if="scope.row.verify == 3">退回</span>
        </template>
      </el-table-column>
      <el-table-column
        prop="title"
        label="标题"
        width="180">
      </el-table-column>
      <el-table-column
        prop="info"
        label="介绍">
      </el-table-column>
      <el-table-column
        prop="create_time"
        label="上传时间"
        width="180">
      </el-table-column>
    </el-table>
      <!-- <div v-for="(item, index) in list" :key="index" class="item">
          {{item.title}}
      </div> -->
    </div>
    <Pagination
      :total="totalItem"
      :page.sync="currentPage"
      @pagination="getList()"
      :limit.sync="pageSize"
    />
  </div>
</template>

<script>
import Pagination from "@/components/Pagination.vue";
export default {
  name: "contribute",
  data() {
    return {
      category: 0,
      type: 0,
      currentPage: 1, // 当前页码
      totalItem: 0, // 总条目
      totalPage: 0, // 总页数
      pageSize: 10, // 每页多少条
      list: []
    };
  },
  components: {
    Pagination
  },
  watch:{
      category(){
          this.getList()
      },
      type(){
          this.getList()
      }
  },
  methods: {
    getList() {
      this.$http
        .PhotoList({
          category: this.category,
          pages: this.currentPage,
          type: this.type,
          sfilter: 1
        })
        .then(response => {
          if (response.code == 200) {
            this.list = response.data.result;
            this.currentPage = response.data.page;
            this.totalPage = response.data.pages;
            this.totalItem = response.data.count;
          }
        })
        .catch(error => {
          console.log("error", error);
        });
    }
  },
  created() {
    this.getList();
  }
};
</script>
<style lang="scss" scoped>
</style>