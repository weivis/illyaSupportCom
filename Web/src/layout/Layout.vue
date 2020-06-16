<template>
    <div class="main-container">
        <layout-header/>
        <layout-appmain/>
        <layout-footer/>
    </div>
</template>

<script>
import header from './components/Header.vue'
import footer from './components/Footer.vue'
import appmain from './AppMain'
    export default {
        name:'Home',
        methods: { //事件处理器
        },
        components: { //定义组件
            'layout-header':header,
            'layout-footer':footer,
            'layout-appmain':appmain
        },
        created() { //生命周期函数
        }
    }
</script>