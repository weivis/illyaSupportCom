<template>
    <div class="layout-Header">
    <div style="width: 250px;float: left;height: 60px;">
        <el-image :src='logo' fit="contain" style="padding: 15px;"></el-image>
    </div>
    <div style="width: calc(100% - 250px);float: right;height: 60px;">
        <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect">
        <el-menu-item index="1"><router-link to="/">首页</router-link></el-menu-item>
        <el-menu-item index="2"><router-link to="/contribute/verify">审核稿件</router-link></el-menu-item>
        <el-menu-item index="3">发布新资源</el-menu-item>
        <el-menu-item index="4">发布新文章</el-menu-item>
        </el-menu>
    </div>
    </div>
</template>

<style lang="scss" scoped>
</style>

<script>
    export default {
        name:'Header',
        data(){
            return{
                logo:this.$ServerHttpUrl + '/static/admin/image/logo.png',
                activeIndex:'0'
            }
        },
        methods: { //事件处理器
            handleSelect(key, keyPath) {
                console.log(key, keyPath);
            }
        },
        components: { //定义组件
        },
        created() { //生命周期函数
        }
    }
</script>