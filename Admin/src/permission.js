import router from './router'

router.beforeEach((to, from, next) => {

    /* 路由发生变化修改页面title */
    if (to.meta.title) {
      document.title = to.meta.title + ' - 魔法少女☆伊莉雅同人爱好者网站 - 中国地区応援サイト'
    }
    next()
  })