<template>
  <div>

    <el-dialog
      :visible.sync="dialogVisible"
      class="openimg"
      width="30%">
      <el-image :src="openitem.file" style="width:100%"></el-image>
      <div class="title">{{openitem.title}}</div>
      <div class="info">{{openitem.info}}</div>    
    </el-dialog>

    <CommonContentNav
      :conttype.sync="contentType"
      @conttype="getList()"
      button_style="0"
      :buttlist="buttlist"
      background_color="#5d3a41"
    />
    <div class="Common page-width content">

    <el-row :gutter="20">
      <el-col v-for="(item, index) in list" :key="index" :xs="12" :sm="8" :md="6" :lg="4" class="item">
        <div @click="openbigimg(item)">
        <img :src="item.cover" style="width: 100%" />
        <div class="title">{{item.title}}</div>
        <div class="info">{{item.info}}</div>
        </div>
      </el-col>
    </el-row>

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
import CommonContentNav from "@/components/CommonContentNav.vue";
import Pagination from "@/components/Pagination.vue";
export default {
  name: "index",
  data() {
    return {
      buttlist: [
        { title: "全部", conttype: 0 },
        { title: "原创", conttype: 1 },
        { title: "Pixiv", conttype: 2 },
        { title: "Cospaly", conttype: 3 },
      ],
      contentType: 0, // 当前选中内容分类
      currentPage: 1, // 当前页码
      totalItem: 0, // 总条目
      totalPage: 0, // 总页数
      pageSize: 10, // 每页多少条
      list: [],
      dialogVisible: false,
      openitem: {}
    };
  },
  components: {
    CommonContentNav,
    Pagination
  },
  methods: {
    openbigimg(item){
      this.openitem = item
      this.dialogVisible = true
    },
    getList() {
      this.$http
        .PhotoList({
          category : this.contentType,
          pages: this.currentPage,
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
.openimg{
  .title{font-size: 18px;}
  .info{font-size: 12px;}
}
.item{
  padding: 10px;
  margin-bottom: 25px;
  .title{font-size: 14px;overflow: hidden;
                    white-space: nowrap;
                    text-overflow: ellipsis}
  .info{font-size: 12px;overflow: hidden;
                    white-space: nowrap;
                    text-overflow: ellipsis}
}
</style>