import Cookies from 'js-cookie'

const TokenKey = 'illyaComAdminToken'
const AdminUserName = 'illyaComAdminUserName'
const AdminUserHead = 'illyaComAdminHead'

export function getUserToken() {
  return Cookies.get(TokenKey)
}

export function setUserToken(token,name,head) {
  Cookies.set(TokenKey, token)
  window.localStorage.setItem('illyaComAdminToken', token)
  Cookies.set(AdminUserName, name)
  Cookies.set(AdminUserHead, head)
  return token
}

export function removeUserToken() {
  Cookies.remove(AdminUserName)
  Cookies.remove(AdminUserHead)
  Cookies.remove(TokenKey)
  window.localStorage.removeItem('illyaComAdminToken')
}

export function getUserData() {
  return {
    username: Cookies.get(AdminUserName),
    userhead: Cookies.get(AdminUserHead)
  }
}