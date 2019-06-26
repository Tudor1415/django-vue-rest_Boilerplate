import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
// import Blog from './views/Blog.vue'
import blogPost from './views/blogPost.vue'



// console.log(info)
Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('./views/About.vue')
    },
    {path:"/blog/:id", component: blogPost},
    {
      path:"/blog/",
      name:"blog",
      component: () => import('./views/Blog.vue')
    },
    {
      path:"/create-blog/",
      component: () => import('./views/createPost.vue')
    },
  ]
})
