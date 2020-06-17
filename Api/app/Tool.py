from random import Random
from datetime import datetime
import re
import math

def RandomStr(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars)-1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return str   # 将拼接的字符串返回

def CheckEmailStr(email):
    # re.compile(r"\"?([a-zA-Z0-9_-]+@\w+\.\w+)\"?")
    pattern = re.compile(r"\"?([0-9A-Za-z\-_\.]+@\w+\.\w+)\"?")
    return re.match(pattern, email)

def Paginator(data, page, num=10):
    '''
        列表分页
        Paginator(列表对象, 分页数, num=单页分页条数(选填 默认为10))

        return
            切片列表, 数据总量，分页总页数
    '''
    num = num
    page = page
    total = len(data)
    pages = math.ceil(total/num)
    ret = []
    if num*page < total:
        for i in range((page-1)*num, num*page):
            ret.append(data[i])
    elif (page-1)*num < total <= num*page:
        for i in range((page-1)*num, total):
            ret.append(data[i])

    return ret, total, pages

def _Paginate(querys, query_page, per_page=10):
    '''
        预处理
        querys : 查询集
        query_page : 需要获取的页数
        return 
            1.一共查询到的数量(count)
            2.查询集对象 items
            3.分页数
            return count, _paginate.items, _paginate.page, _paginate.pages
            count, items, page, pages
            总数 结果 当前页数 总页数
    '''
    if query_page == 0:
        query_page = 1
    count = querys.count()
    _paginate = querys.paginate(query_page, per_page=per_page)
    return count, _paginate.items, _paginate.page, _paginate.pages

def StrForDate(s):
    '''
        yyyy-MM-dd
        Str => Date
    '''
    try:
        year_s, mon_s, day_s = s.split('-')
        return datetime(int(year_s), int(mon_s), int(day_s))
    except Exception as e:
        print(e)
        return {}