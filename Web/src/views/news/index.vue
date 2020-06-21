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
        <el-link :href="'/news/item?id=' + item.id" target="_blank" :underline="false">
            <div class="contetn">
              <div class="cover">
                <el-image style="width:100%;height:100%;display:block;" :src="item.cover" fit="cover"></el-image>
              </div>
              <div class="info">
                <div class="title">{{item.title}} </div>
                <div class="introduce">{{item.introduce}}</div>
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
        { title: "官方资讯", conttype: 1 },
        { title: "手办", conttype: 2 },
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
        .ArticleList({
          types: this.contentType,
          sfilter: 0,
          pages: this.currentPage
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
  margin-bottom: 20px;
}
.item{
  width: 50%;float: left;margin-bottom: 20px;
  .contetn{
    width: 95%;
    .cover{
      width: 290px;
      float: left;
      border: 1px solid #d2d2d2;
    }
    .info{
      width: calc(100% - 320px);
      float: right;
      color: #000;
      .title{
        margin-top: 15px;
        font-size: 18px;
        font-weight: bold;
      }
      .introduce{
        margin-top: 15px;width: 100%;font-size: 12px;line-height: 18px; word-wrap: break-word;word-break: normal;
      }
    }
  }
}

@media screen and (max-width: 1600px) {
.item{
  width: 50%;
  .contetn{
    width: 95%;
    .cover{
      width: 230px;
    }
    .info{
      width: calc(100% - 250px);
      .title{
        margin-top: 15px;
        font-size: 18px;
      }
      .introduce{
        margin-top: 15px;width: 100%;font-size: 12px;line-height: 18px;
        text-overflow: -o-ellipsis-lastline;
        overflow: hidden;
        text-overflow: ellipsis;
        display: -webkit-box;
        -webkit-line-clamp: 5;
        -webkit-box-orient: vertical;
      }
    }
  }
}
}

@media screen and (max-width: 1200px) {
.item{
  width: 50%;
  .contetn{
    width: 95%;
    .cover{
      width: 200px;
    }
    .info{
      width: calc(100% - 220px);
      .title{
        margin-top: 0px;
        font-size: 16px;
      }
      .introduce{
        margin-top: 15px;width: 100%;font-size: 12px;line-height: 18px;
        text-overflow: -o-ellipsis-lastline;
        overflow: hidden;
        text-overflow: ellipsis;
        display: -webkit-box;
        -webkit-line-clamp: 3;
        -webkit-box-orient: vertical;
      }
    }
  }
}
}

@media screen and (max-width: 600px) {
.item{
  width: 100%;
}
}
</style>