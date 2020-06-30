import request from '@/utils/request'

export function upload(data) {
    return request({
      url: '/upload/',
      method: 'post',
      data: data,
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    })
  }

// Admin-------------------------------------------------------------------------------------------------------

// Album-------------------------------------------------------------------------------------------------------

//添加资源和编辑资源
export function AlbumAddOrEdit(data) {
    return request({
        url: '/album/addoredit',
        method: 'post',
        data: data || {}
    })
}

//更改资源状态
export function AlbumChange(data) {
    return request({
        url: '/album/change',
        method: 'post',
        data: data || {}
    })
}

//绑定番剧
export function AlbumBindBangumi(data) {
    return request({
        url: '/album/bind/bangumi',
        method: 'post',
        data: data || {}
    })
}

//新增资源下载地址和编辑
export function AlbumDowurlAddOrEdit(data) {
    return request({
        url: '/album/dowurl/addoredit',
        method: 'post',
        data: data || {}
    })
}

//删除资源下载列表的某一项
export function AlbumDowurlDel(data) {
    return request({
        url: '/album/dowurl/del',
        method: 'post',
        data: data || {}
    })
}

//资源列表
export function AlbumList(data) {
    return request({
        url: '/album/list',
        method: 'post',
        data: data || {}
    })
}

//资源详细信息
export function AlbumInfo(data) {
    return request({
        url: '/album/info',
        method: 'post',
        data: data || {}
    })
}

//获取资源的下载列表
export function AlbumDowurlList(data) {
    return request({
        url: '/album/dowurl/list',
        method: 'post',
        data: data || {}
    })
}

//更改资源下载的反馈状态
export function AlbumDowurlChange(data) {
    return request({
        url: '/album/dowurl/feedback',
        method: 'post',
        data: data || {}
    })
}

// Article-----------------------------------------------------------------------------------------------------

//添加文章或编辑文章
export function ArticleAddoredit(data) {
    return request({
        url: '/article/addoredit',
        method: 'post',
        data: data || {}
    })
}

//文章列表
export function ArticleList(data) {
    return request({
        url: '/article/list',
        method: 'post',
        data: data || {}
    })
}

//文章信息
export function ArticleInfo(id) {
    return request({
        url: '/article/info',
        method: 'post',
        data: {
            id:id
        }
    })
}

//更改文章状态和排序
export function ArticleChange(data) {
    return request({
        url: '/article/change',
        method: 'post',
        data: data || {}
    })
}


// Auth--------------------------------------------------------------------------------------------------------

// 登录
export function authAdminLogin(email, password) {
    return request({
        url: '/auth/sign-in/admin',
        method: 'post',
        data: {
            email: email,
            password: password
        }
    })
}

export function authAdminLogout(email, password) {
    return request({
        url: '/auth/logout/admin',
        method: 'post',
        data: {
            email: email,
            password: password
        }
    })
}

// Bangumi-----------------------------------------------------------------------------------------------------

//删除单个绑定了的CV配音信息
export function BangumiCvDel(data) {
    return request({
        url: '/bangumi/cv/del',
        method: 'post',
        data: data || {}
    })
}

//绑定cv和编辑已经绑定了的cv
export function BangumiCvAddoredit(data) {
    return request({
        url: '/bangumi/cv/addoredit',
        method: 'post',
        data: data || {}
    })
}

//添加番剧或编辑
export function bangumiAddOrEdit(data) {
    return request({
        url: '/bangumi/add_or_edit',
        method: 'post',
        data: data || {}
    })
}

//番剧列表
export function bangumiList(types, pages, sfilter) {
    return request({
        url: '/bangumi/list',
        method: 'post',
        data: {
            types: types,
            pages: pages,
            sfilter: sfilter
        }
    })
}

//更改番剧(删除 上下架)
export function bangumiChange(id, status, dele) {
    return request({
        url: '/bangumi/change',
        method: 'post',
        data: {
            id: id,
            status: status,
            dele: dele
        }
    })
}

//获取详细番剧信息
export function bangumiInfo(id) {
    return request({
        url: '/bangumi/info',
        method: 'post',
        data: {
            id: id
        }
    })
}

//添加播放源地址和编辑
export function bangumiPlayurlAddOrEdit(data) {
    return request({
        url: '/bangumi/playurl/addoredit',
        method: 'post',
        data: data || {}
    })
}

//添加播放源地址和编辑
export function bangumiPlayurlDel(data) {
    return request({
        url: '/bangumi/playurl/del',
        method: 'post',
        data: data || {}
    })
}

// Bbs---------------------------------------------------------------------------------------------------------

// Comment-----------------------------------------------------------------------------------------------------

// Cv----------------------------------------------------------------------------------------------------------

//CV列表
export function cvList(data) {
    return request({
        url: '/cv/list',
        method: 'post',
        data: data || {}
    })
}

//CV添加
export function cvAdd(data) {
    return request({
        url: '/cv/add',
        method: 'post',
        data: data || {}
    })
}

//CV删除
export function cvDel(data) {
    return request({
        url: '/cv/del',
        method: 'post',
        data: data || {}
    })
}

//CV编辑
export function cvEdit(data) {
    return request({
        url: '/cv/edit',
        method: 'post',
        data: data || {}
    })
}

// Open--------------------------------------------------------------------------------------------------------

// User--------------------------------------------------------------------------------------------------------

// Video-------------------------------------------------------------------------------------------------------

//资源列表
export function VideoList(data) {
    return request({
        url: '/video/list',
        method: 'post',
        data: data || {}
    })
}

//获取视频信息
export function VideoQuery(data) {
    return request({
        url: '/video/query',
        method: 'post',
        data: data || {}
    })
}

//管理员操作视频
export function VideoAdminVerify(data) {
    return request({
        url: '/video/admin/change',
        method: 'post',
        data: data || {}
    })
}

// Photo------------------------------------------------------------------------------------------

// 相簿列表
export function PhotoList(data) {
    return request({
        url: '/photo/list',
        method: 'post',
        data: data || {}
    })
}

// 相簿上传
export function PhotoUp(data) {
    return request({
        url: '/photo/up',
        method: 'post',
        data: data || {}
    })
}

// 相簿更改
export function PhotoChange(data) {
    return request({
        url: '/photo/change',
        method: 'post',
        data: data || {}
    })
}