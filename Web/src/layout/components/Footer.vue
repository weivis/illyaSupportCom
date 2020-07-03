<template>
    <div class="layout-Footer footer">
        <div class="Common page-width">
        <div>
            <div class="li">
                <span class="l">魔法少女☆伊莉雅同人应援网站</span>
                <span class="l">本网站属于非盈利性质由伊莉雅爱好者建设 如有问题请联系442981412@qq.com</span>
                
                <span class="r">© WeiVi(网站作者) 2014-2020</span>
                <span class="r">粤ICP备20033641号-1</span>
                <span class="r">开源地址https://github.com/weivis/illyaSupportCom</span>
            </div>
        </div>
        </div>
    </div>
</template>

<style lang="scss" scoped>
</style>

<script>
    export default {
        name:'Footer',
        methods: { //事件处理器
        },
        components: { //定义组件
        },
        created() { //生命周期函数
        }
    }
</script>
<style lang="scss" scoped>
.footer{
    margin-top: 50px;
background-color: #fafafa;
    border-top: 1px solid #f4f4f4;
    width: 100%;
    .li{
        height: 22px;
        line-height: 22px;
        padding-top: 50px;
        padding-bottom: 50px;
        font-size: 12px;
        .l{float: left;margin-right: 25px;}
        .r{float: right;margin-left: 25px;}
    }
}
@media screen and (max-width: 800px) {
.footer{
    margin-top: 50px;
background-color: #fafafa;
    border-top: 1px solid #f4f4f4;
    width: 100%;
    .li{
        .l{float: left;margin-right: 0px;width: 100%;margin-bottom: 15px;}
        .r{float: right;margin-left: 0px;width: 100%;margin-bottom: 15px;}
    }
}
}
</style>