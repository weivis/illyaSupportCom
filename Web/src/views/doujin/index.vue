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
        <el-link :href="'/album/info?id=' + item.id" target="_blank" :underline="false">
          <div class="content">
            <div class="tag">
              <div class="classification">
                <span v-if="item.classification === 1">番剧</span>
                <span v-if="item.classification === 2">OST</span>
                <span v-if="item.classification === 3">MMD</span>
                <span v-if="item.classification === 4">Live2D</span>
              </div>
            </div>
            <div class="title">{{item.name}}</div>
          </div>
          <div class="cover">
            <img class="boxshow" src="../../assets/boxshow.png" />
            <el-image style="width:100%;height:100%;display:block;" :src="item.cover" fit="cover"></el-image>
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
  border: 2px solid #d2d2d2;
  position: relative;
  .tag {
    width: 100%;
    height: 22px;
    margin-bottom: 10px;
    .classification {
      background-color: #0ec900;
      border-radius: 50px;
      float: left;
      line-height: 22px;
      padding-left: 18px;
      padding-right: 18px;
      height: 22px;
      font-size: 12px;
      font-weight: bold;
      color: #ffffff;
    }
  }
  .content {
    z-index: 20;
    position: absolute;
    bottom: 0;
    width: calc(100% - 30px);
    height: 80px;
    padding: 15px;
  }
  .title {
    font-size: 12px;
    color: #ffffff;
    text-overflow: -o-ellipsis-lastline;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 3;
    line-height: 18px;
    overflow: hidden;
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