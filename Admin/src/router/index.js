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
        name: 'Home',
        component: () => import('@/views/Home.vue'),
        meta: {title:'首页'}
      },
    ]
  },
  {
    path: '/contribute',
    component: Layout,
    children: [
      {
        path: 'verify',
        name: 'verifycontribute',
        component: () => import('@/views/video/verify.vue'),
        meta: {title:'视频审核'}
      },
      {
        path: 'verify/info',
        name: 'verifycontributeinfo',
        component: () => import('@/views/video/info.vue'),
        meta: {title:'视频审核'}
      }
    ]
  },
  {
    path: '/bangumi',
    component: Layout,
    children: [
      {
        path: 'list',
        name: 'listbangumi',
        component: () => import('@/views/bangumi/listbangumi.vue'),
        meta: {title:'番剧管理'}
      },
      {
        path: 'add',
        name: 'addbangumi',
        component: () => import('@/views/bangumi/addbangumi.vue'),
        meta: {title:'添加番剧'}
      },
      {
        path: 'edit',
        name: 'editbangumi',
        component: () => import('@/views/bangumi/editbangumi.vue'),
        meta: {title:'编辑番剧信息'}
      },
    ]
  },
  {
    path: '/cv',
    component: Layout,
    children: [
      {
        path: '/',
        name: 'cvlist',
        component: () => import('@/views/cv/list.vue'),
        meta: {title:'CV管理'}
      },
    ]
  },
  {
    path: '/article',
    component: Layout,
    children: [
      {
        path: 'list',
        name: 'articlelist',
        component: () => import('@/views/article/list.vue'),
        meta: {title:'文章管理'}
      },
      {
        path: 'add',
        name: 'articleadd',
        component: () => import('@/views/article/add.vue'),
        meta: {title:'添加文章'}
      },
      {
        path: 'edit',
        name: 'articleedit',
        component: () => import('@/views/article/edit.vue'),
        meta: {title:'编辑文章'}
      },
    ]
  },
  {
    path: '/album',
    component: Layout,
    children: [
      {
        path: 'list',
        name: 'listalbum',
        component: () => import('@/views/album/list.vue'),
        meta: {title:'资源管理'}
      },
      {
        path: 'add',
        name: 'addalbum',
        component: () => import('@/views/album/add.vue'),
        meta: {title:'添加资源'}
      },
      {
        path: 'edit',
        name: 'editalbum',
        component: () => import('@/views/album/edit.vue'),
        meta: {title:'编辑资源信息'}
      },
      {
        path: 'feedback',
        name: 'feedbackalbum',
        component: () => import('@/views/album/feedback.vue'),
        meta: {title:'反馈处理'}
      },
    ]
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('@/views/Login/')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: 'admin',
  routes
})

export default router
