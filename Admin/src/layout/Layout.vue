<template>
    <div class="main-container">
        <layout-header/>
        <layout-appmain/>
        <layout-lnav/>
        <layout-loginbar/>
    </div>
</template>

<script>
import header from './components/Header.vue'
import lnav from './components/Lnav.vue'
import Loginbar from './components/Loginbar.vue'
import appmain from './AppMain'
    export default {
        name:'Home',
        methods: { //事件处理器
        },
        components: { //定义组件
            'layout-header':header,
            'layout-appmain':appmain,
            'layout-lnav':lnav,
            'layout-loginbar':Loginbar
        },
        created() { //生命周期函数
        }
    }
</script>