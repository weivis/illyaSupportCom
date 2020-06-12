import router from './router'

router.beforeEach((to, from, next) => {

    /* 路由发生变化修改页面title */
    if (to.meta.title) {
      document.title = to.meta.title + ' - WeiVi 的主页&博客 Website'
    }
    next()
  })