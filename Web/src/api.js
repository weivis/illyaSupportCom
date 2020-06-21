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

//资源列表
export function AlbumList(types, pages, sfilter) {
    return request({
        url: '/album/list',
        method: 'post',
        data: {
            types: types,
            pages: pages,
            sfilter: sfilter
        }
    })
}

//资源详细信息
export function AlbumInfo(id) {
    return request({
        url: '/album/info',
        method: 'post',
        data: {
            id: id
        }
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

//反馈资源下载问题
export function AlbumDowurlFeedback(id) {
    return request({
        url: '/album/info',
        method: 'post',
        data: {
            id: id
        }
    })
}

// Article-----------------------------------------------------------------------------------------------------

//文章列表
export function ArticleList(data) {
    return request({
        url: '/article/list',
        method: 'post',
        data: data || {}
    })
}

//文章列表
export function ArticleInfo(data) {
    return request({
        url: '/article/info',
        method: 'post',
        data: data || {}
    })
}


// Auth--------------------------------------------------------------------------------------------------------

// 登录
export function authLogin(email, password) {
    return request({
        url: '/auth/sign-in',
        method: 'post',
        data: {
            email: email,
            password: password
        }
    })
}

// 注册
export function authRegister(email, password, repassword, username) {
    return request({
        url: '/auth/register',
        method: 'post',
        data: {
            email: email,
            password: password,
            repassword: repassword,
            username: username
        }
    })
}

// 再次发送注册验证码
export function authRegisterAgainSendemail(email) {
    return request({
        url: '/auth/register/again-sendemail',
        method: 'post',
        data: {
            email: email
        }
    })
}

// 验证注册验证码
export function authVerifyRegisterVcode(vcode) {
    return request({
        url: '/auth/verify/register-vcode',
        method: 'post',
        data: {
            vcode: vcode
        }
    })
}

// 退出登录
export function authLogout() {
    return request({
        url: '/auth/logout',
        method: 'post',
        data: {}
    })
}

// Bangumi-----------------------------------------------------------------------------------------------------

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

// Bbs---------------------------------------------------------------------------------------------------------

// Comment-----------------------------------------------------------------------------------------------------

// Cv----------------------------------------------------------------------------------------------------------

// Open--------------------------------------------------------------------------------------------------------

// User--------------------------------------------------------------------------------------------------------

export function getUserinfo(id) {
    return request({
        url: '/user/get/userinfo',
        method: 'post',
        data: { id: id }
    })
}

export function userEditinfo(head, username, introduce) {
    return request({
        url: '/user/edit-myinfo',
        method: 'post',
        data: {
            head: head,
            username: username,
            introduce: introduce
        }
    })
}

export function userInfo() {
    return request({
        url: '/user/myinfo',
        method: 'post',
        data: {}
    })
}

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

//视频投稿和编辑
export function VideoUploadOrEdit(data) {
    return request({
        url: '/video/uploadoredit',
        method: 'post',
        data: data || {}
    })
}

//用户删除视频
export function VideoDel(data) {
    return request({
        url: '/video/user/del',
        method: 'post',
        data: data || {}
    })
}