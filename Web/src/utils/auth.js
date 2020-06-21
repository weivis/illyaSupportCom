const TokenKey = 'illyaComUserToken'
const UserName = 'illyaComUserName'
const UserHead = 'illyaComUserHead'
const UserID = 'illyaComUserID'

export function getUserToken() {
  return window.localStorage.getItem(TokenKey);
}

export function getUser() { 
  if (window.localStorage.getItem(TokenKey)){
    return{
      userToken: window.localStorage.getItem(TokenKey),
      userID: window.localStorage.getItem(UserID),
      userName: window.localStorage.getItem(UserName),
      userHead: window.localStorage.getItem(UserHead)
    }
  }else{
    return null
  }
}

export function setUser(token, userid, username, head) { 
  console.log('登录成功')
  window.localStorage.setItem(TokenKey, token)
  window.localStorage.setItem(UserName, username)
  window.localStorage.setItem(UserID, userid)
  window.localStorage.setItem(UserHead, head)
}

export function removeUser() {
  console.log('退出登录')
  window.localStorage.removeItem(TokenKey);
  window.localStorage.removeItem(UserName);
  window.localStorage.removeItem(UserID);
  window.localStorage.removeItem(UserHead);
  window.localStorage.clear();
}
