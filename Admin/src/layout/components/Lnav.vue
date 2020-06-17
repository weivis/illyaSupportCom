<template>
    <div class="layout-Lnav">
  <el-col :span="24">
    <el-menu
      default-active="2"
      class="el-menu-vertical-demo"
      @open="handleOpen"
      @close="handleClose">

      <el-submenu index="1">
        <template slot="title">
          <i class="el-icon-location"></i>
          <span>番剧</span>
        </template>
          <router-link to="/bangumi/list"><el-menu-item index="1-1">番剧管理</el-menu-item></router-link>
          <router-link to="/bangumi/add"><el-menu-item index="1-2">发布新番剧</el-menu-item></router-link>
      </el-submenu>

      <el-submenu index="2">
        <template slot="title">
          <i class="el-icon-location"></i>
          <span>CV管理</span>
        </template>
          <router-link to="/cv/"><el-menu-item index="1-1">CV管理</el-menu-item></router-link>
      </el-submenu>

      <el-submenu index="3">
        <template slot="title">
          <i class="el-icon-location"></i>
          <span>文章</span>
        </template>
          <router-link to="/article/add"><el-menu-item index="3-1">发布新文章</el-menu-item></router-link>
          <router-link to="/article/list"><el-menu-item index="3-2">管理文章</el-menu-item></router-link>
      </el-submenu>

      <el-submenu index="4">
        <template slot="title">
          <i class="el-icon-location"></i>
          <span>用户评论管理</span>
        </template>
          <el-menu-item index="4-1">举报管理</el-menu-item>
          <el-menu-item index="4-2">已处理的评论</el-menu-item>
      </el-submenu>

      <el-submenu index="5">
        <template slot="title">
          <i class="el-icon-location"></i>
          <span>资源区</span>
        </template>
          <el-menu-item index="5-1">发布新资源</el-menu-item>
          <el-menu-item index="5-2">资源管理</el-menu-item>
          <el-menu-item index="5-3">反馈处理</el-menu-item>
      </el-submenu>

      <el-submenu index="6">
        <template slot="title">
          <i class="el-icon-location"></i>
          <span>视频管理</span>
        </template>
          <el-menu-item index="6-1">视频管理</el-menu-item>
          <el-menu-item index="6-2">被退回的稿件</el-menu-item>
      </el-submenu>

    </el-menu>
  </el-col>
    </div>
</template>

<style lang="scss" scoped>
</style>

<script>
    export default {
        name:'Lnav',
        components: { //定义组件
        },
        created() { //生命周期函数
        },
        data(){
          return{
            active:1
          }
        },
        methods: {
            handleOpen(key, keyPath) {
                console.log(key, keyPath);
            },
            handleClose(key, keyPath) {
                console.log(key, keyPath);
            }
        }
    }
</script>