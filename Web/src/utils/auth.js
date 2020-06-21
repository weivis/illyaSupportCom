const TokenKey = 'illyaComUserToken'
const UserName = 'illyaComUserName'
const UserID = 'illyaComUserID'

export function getUserToken() {
  return window.localStorage.getItem(TokenKey);
}

export function getUser() { 
  if (window.localStorage.getItem(TokenKey)){
    return{
      userToken: window.localStorage.getItem(TokenKey),
      userID: window.localStorage.getItem(UserID),
      userName: window.localStorage.getItem(UserName)
    }
  }else{
    return null
  }
}

export function setUser(token, userid, username) { 
  window.localStorage.setItem(TokenKey, token)
  window.localStorage.setItem(UserName, username)
  window.localStorage.setItem(UserID, userid)
}

export function removeUser() {
  localStorage.removeItem(TokenKey);
  localStorage.removeItem(UserName);
  localStorage.removeItem(UserID);
  window.localStorage.clear();
}
