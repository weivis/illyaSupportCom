import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

/* Layout */
import Layout from '../layout/Layout'

const routes = [
  { path: '/404', component: () => import('@/views/404'), hidden: true },
  {
    path: '/',
    name: 'Home',
    component: Layout,
    children: [
      {
        path: '/',
        name: 'Home',
        component: () => import('@/views/Home.vue'),
        meta: {title:'首页'}
      },
      {
        path: '/about',
        name: 'Home',
        component: () => import('@/views/About.vue'),
        meta: {title:'首页'}
      },
    ]
  }
]

const router = new VueRouter({
  mode: 'history',
  // base: process.env.BASE_URL,
  routes
})

export default router
