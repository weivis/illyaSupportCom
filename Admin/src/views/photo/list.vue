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
      <div v-for="(item, index) in list" :key="index" class="item">
          {{item.title}}
      </div>
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