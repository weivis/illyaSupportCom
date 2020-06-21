import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

/* Layout */
import Layout from '../layout/Layout'

const routes = [
  { path: '/404', component: () => import('@/views/404'), hidden: true },
  {
    path: '/',
    component: Layout,
    children: [
      {
        path: '/',
        name: 'home',
        component: () => import('@/views/Home.vue'),
        meta: {title:'首页'}
      }
    ]
  },
  {
    path: '/auth',
    component: Layout,
    children: [
      {
        path: 'sgin-in',
        name: 'login',
        component: () => import('@/views/auth/login.vue'),
        meta: {title:'登录'}
      },
      {
        path: 'register',
        name: 'register',
        component: () => import('@/views/auth/register.vue'),
        meta: {title:'注册'}
      },
      {
        path: 'verify',
        name: 'verify',
        component: () => import('@/views/auth/verify.vue'),
        meta: {title:'邮箱验证'}
      },
    ]
  },
  {
    path: '/bangumi',
    component: Layout,
    children: [
      {
        path: '/',
        name: 'listbangumi',
        component: () => import('@/views/bangumi/index.vue'),
        meta: {title:'番剧'}
      },
      {
        path: 'info',
        name: 'infobangumi',
        component: () => import('@/views/bangumi/info.vue'),
        meta: {title:'番剧详细信息'}
      },
    ]
  },
  {
    path: '/album',
    component: Layout,
    children: [
      {
        path: '/',
        name: 'listalbum',
        component: () => import('@/views/album/index.vue'),
        meta: {title:'资源'}
      },
      {
        path: 'info',
        name: 'infoalbum',
        component: () => import('@/views/album/info.vue'),
        meta: {title:'资源详细信息'}
      }
    ]
  },
  {
    path: '/news',
    component: Layout,
    children: [
      {
        path: '/',
        name: 'listnews',
        component: () => import('@/views/news/index.vue'),
        meta: {title:'资源'}
      },
      {
        path: 'item',
        name: 'itemnews',
        component: () => import('@/views/news/item.vue'),
        meta: {title:'资源详细信息'}
      }
    ]
  },
]

const router = new VueRouter({
  mode: 'history',
  // base: process.env.BASE_URL,
  routes
})

export default router
