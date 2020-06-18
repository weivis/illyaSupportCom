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
        <div class="content-w">
          <div class="right-button">
            <a :href="'/bangumi/info?id=' + item.id" target="_blank" class="el-link">
              <div class="button">立即观看</div>
            </a>
          </div>
          <div class="left">
            <img :src="item.cover" style="width:100%" />
          </div>
          <div class="right">
            <div class="title">
              <span class="mr">{{item.name}}</span>
              <div class="tag" v-if="item.classification === 1">番剧</div>
              <div class="tag" v-if="item.classification === 2">剧场版</div>
              <div class="tag" v-if="item.classification === 3">OVA</div>
              <div class="tag" v-if="item.classification === 4">SP</div>
            </div>
            <div class="info">
              <span class="mr">{{item.openplay_time}}开播</span>
              <span class="mr">全{{item.setscount}}话</span>
              <span class="mr" v-if="item.upstatus === true">连载中</span>
              <span class="mr" v-if="item.upstatus === false">已完结</span>
            </div>
            <div class="introduce">{{item.introduce}}</div>
            <!-- {{item}} -->
          </div>
        </div>
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
        { title: "番剧", conttype: 1 },
        { title: "剧场版", conttype: 2 },
        { title: "OVA", conttype: 3 },
        { title: "SP", conttype: 4 }
      ],
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
        .bangumiList(this.contentType, this.currentPage, 0)
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
  height: 333px;
  float: left;
  margin-bottom: 30px;
  width: 50%;
  position: relative;
  .content-w {
    width: 90%;
    height: 100%;
  }
  .left {
    height: 333px;
    width: 250px;
    float: left;
  }
  .right {
    width: calc(100% - 300px);
    float: right;
    min-height: 100%;
    // background-color: #f4f4f4;
  }
  .right-button {
    height: 43px;
    width: calc(100% - 300px);
    // background-color: #f4f4f4;
    position: absolute;
    bottom: 0;
    right: 0;
  }
  .title {
    height: 20px;
    line-height: 20px;
    display: flow-root;
    width: 100%;
    color: #484848;
    font-size: 20px;
    font-weight: bold;
    .tag {
      height: 20px;
      padding-left: 10px;
      padding-right: 10px;
      border-radius: 50px;
      color: #fff;
      background-color: #d9b0ff;
      float: left;
      font-size: 10px;
    }
  }
  .mr {
    margin-right: 5px;
    float: left;
  }
  .info {
    display: flow-root;
    width: 100%;
    color: #484848;
    font-size: 14px;
    margin-top: 10px;
  }
  .introduce {
    width: 100%;
    color: #484848;
    font-size: 14px;
    margin-top: 30px;
    text-overflow: -o-ellipsis-lastline;
    overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-line-clamp: 6;
    -webkit-box-orient: vertical;
  }
  .button {
    height: 43px;
    line-height: 43px;
    font-weight: bold;
    font-size: 14px;
    color: #3d3d3d;
    border: 1px solid #d2d2d2;
    padding-left: 45px;
    padding-right: 45px;
    border-radius: 3px;
  }
  .button:hover {
    border: 1px solid #004eff;
  }
}

@media screen and (max-width: 1600px) {
  .item {
    height: 280px;
    .content-w {
      width: 95%;
    }
    .left {
      height: 280px;
      width: 210px;
    }
    .right {
      width: calc(100% - 250px);
    }
    .right-button {
      width: calc(100% - 250px);
    }
  }
}

@media screen and (max-width: 1200px) {
  .item {
    height: 220px;
    .title{
      font-size: 16px;
    }
    .content-w {
      width: 95%;
    }
    .left {
      height: 220px;
      width: 165px;
    }
    .right {
      width: calc(100% - 200px);
    }
    .introduce {
      -webkit-line-clamp: 4;
    }
    .right-button {
      width: calc(100% - 200px);
    }
  }
}

@media screen and (max-width: 600px) {
  .item {
    margin-bottom: 40px;
    width: 100%;
    height: 280px;
    .content-w {
      width: 100%;
    }
    .left {
      height: 220px;
      width: 165px;
    }
    .right {
      width: calc(100% - 190px);
    }
    .introduce {
      margin-top: 10px;
      -webkit-line-clamp: 4;
    }
    .right-button {
      width: 100%;
    }
    .el-link{
      width: 100%;
    }
    .button{
      width: 100%;
      text-align: center;
    }
    .title{
      height: 40px;
    }
    .info{
      margin-top: 10px;
    }
    .tag{
      display:none
    }
  }
}
</style>