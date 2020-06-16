import request from '@/utils/request'

// Admin-------------------------------------------------------------------------------------------------------

// Album-------------------------------------------------------------------------------------------------------

// Article-----------------------------------------------------------------------------------------------------

// Auth--------------------------------------------------------------------------------------------------------

// 登录
export function authLogin(email, passport) {
    return request({
        url: '/auth/sign-in',
        method: 'post',
        data: {
            email: email,
            passport: passport
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

// Bbs---------------------------------------------------------------------------------------------------------

// Comment-----------------------------------------------------------------------------------------------------

// Cv----------------------------------------------------------------------------------------------------------

// Open--------------------------------------------------------------------------------------------------------

// User--------------------------------------------------------------------------------------------------------

export function getUserinfo(id) {
    return request({
        url: '/user/get/userinfo',
        method: 'post',
        data: {id:id}
    })
}

export function userEditinfo(head, username, introduce) {
    return request({
        url: '/user/edit-myinfo',
        method: 'post',
        data: {
            head:head,
            username:username,
            introduce:introduce
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