<template>
  <div>
    <CommonContentNav
      :conttype.sync="contentType"
      @conttype="getList()"
      button_style="0"
      :buttlist="buttlist"
      background_color="#ffffff"
    />
    <div class="Common page-width content">
      <div v-for="(item, index) in list" :key="index" class="item">
        <el-link :href="'/doujin/info?id=' + item.id" target="_blank" :underline="false">
          <div class="cover">
            <el-image style="width:100%;height:100%;display:block;" :src="item.cover" fit="cover"></el-image>
          </div>
          <div class="content">
            <div class="l">
              <div class="userhead"><el-image style="width:100%;height:100%;display:block;" :src="item.author_head" fit="cover"></el-image></div>
            </div>
            <div class="r">
              <div class="title">{{item.title}}</div>
              <div class="username">{{item.author_username}}</div>
            </div>
          </div>
        </el-link>
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
import CommonContentNav from "@/components/CommonContentNav.vue";
import Pagination from "@/components/Pagination.vue";
export default {
  name: "index",
  data() {
    return {
      buttlist: [
        { title: "全部", conttype: 0 },
        { title: "MAD·AMV", conttype: 1 },
        { title: "MMD", conttype: 2 },
        { title: "技术宅", conttype: 3 },
        { title: "其他", conttype: 4 },
      ],
      ctypes: 0,
      contentType: 0, // 当前选中内容分类
      currentPage: 1, // 当前页码
      totalItem: 0, // 总条目
      totalPage: 0, // 总页数
      pageSize: 10, // 每页多少条
      list: []
    };
  },
  components: {
    CommonContentNav,
    Pagination
  },
  methods: {
    getList() {
      this.$http
        .VideoList({
          types: this.contentType,
          ctypes: this.ctypes,
          pages: this.currentPage,
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
.content {
  margin: 0 auto;
  display: flow-root;
}
.item {
  margin-bottom: 30px;
  float: left;
  margin-right: 3%;
  width: 13.9%;
  position: relative;
  .content {
    margin-top: 15px;
    height: 80px;
    .l{width: 30px;height: 30px;float: left;}
    .r{float: right;width: calc(100% - 45px);}
  }
  .userhead{
    border-radius: 50px;overflow: hidden;height: 30px;width: 30px;
  }
  .title {
    font-size: 14px;
    color: #000000;
    text-overflow: -o-ellipsis-lastline;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 3;
    line-height: 18px;
    overflow: hidden;
    height: 35px;;
  }
  .username{
    font-size: 10px;color: #8a8a8a;margin-top: 10px;
  }
  .cover {
    position: relative;
    width: 100%;
    .boxshow {
      position: absolute;
      width: 100%;
      z-index: 10;
      bottom: 0;
    }
  }
}

.item:nth-child(6n) {
  margin-right: 0;
}

//===============================================================================

@media screen and (max-width: 1670px) {
  .item:nth-child(6n) {
    margin-right: 2.9%;
  }
  .item:nth-child(5n) {
    margin-right: 0;
  }
  .item {
    margin-right: 2.9%;
    width: 17.23%;
  }
}

@media screen and (max-width: 1200px) {
  .item:nth-child(6n) {
    margin-right: 2.9%;
  }
  .item:nth-child(5n) {
    margin-right: 2.9%;
  }
  .item:nth-child(4n) {
    margin-right: 0;
  }
  .item {
    margin-right: 2.9%;
    width: 22.2%;
  }
}

@media screen and (max-width: 900px) {
  .item:nth-child(6n) {
    margin-right: 2.9%;
  }
  .item:nth-child(5n) {
    margin-right: 2.9%;
  }
  .item:nth-child(4n) {
    margin-right: 2.9%;
  }
  .item:nth-child(3n) {
    margin-right: 0;
  }
  .item {
    margin-right: 2.9%;
    width: 30.6%;
  }
}

@media screen and (max-width: 600px) {
  .item:nth-child(6n) {
    margin-right: 2.9%;
  }
  .item:nth-child(5n) {
    margin-right: 2.9%;
  }
  .item:nth-child(4n) {
    margin-right: 2.9%;
  }
  .item:nth-child(3n) {
    margin-right: 2.9%;
  }
  .item:nth-child(2n) {
    margin-right: 0;
  }
  .item {
    margin-right: 2.9%;
    width: 47.1%;
  }
}
</style>