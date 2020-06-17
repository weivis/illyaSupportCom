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

// Article-----------------------------------------------------------------------------------------------------

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

export function bangumiAddOrEdit(data) {
    return request({
        url: '/bangumi/add_or_edit',
        method: 'post',
        data: data || {}
    })
}

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

export function bangumiInfo(id) {
    return request({
        url: '/bangumi/info',
        method: 'post',
        data: {
            id: id
        }
    })
}

export function bangumiPlayurlAddOrEdit(data) {
    return request({
        url: '/bangumi/playurl/addoredit',
        method: 'post',
        data: data || {}
    })
}

// Bbs---------------------------------------------------------------------------------------------------------

// Comment-----------------------------------------------------------------------------------------------------

// Cv----------------------------------------------------------------------------------------------------------

// Open--------------------------------------------------------------------------------------------------------

// User--------------------------------------------------------------------------------------------------------

// Video-------------------------------------------------------------------------------------------------------