import hashlib
import os
import random
from datetime import datetime
from io import *
from app.Config import SERVER_GULAOBURL

# 关于 UPLOAD_KEY_FLOAD的用法
UPLOAD_KEY_FLOAD = {
    'userhead':'/com/userhead',
    'bangumicover':'/com/bangumicover',
    'albumcover':'/com/albumcover',
    'articlecover':'/com/articlecover',
    'cvhead':'/com/cvhead',
    }

def FileCompress_Head(files):
    '''图片压缩'''
    from PIL import Image
    file=Image.open(files)

    topw = [0,0]

    xl, yl = file.size
    print(xl, yl)

    if xl > yl:
        topw = [yl, 1]
        print(topw)
    else:
        topw = [xl, 0]
        print(topw)

    px = topw[0]

    file = file.crop((0, 0, px, px))

    print(file.size)
    return file

def CreateNewFilename(ext):
    '''生成新的文件名'''
    return datetime.strftime(datetime.now(),'%Y%m%d%H%M%S') + '{:03d}'.format(random.randint(0, 999)) + ext

def QueryFileName(filestr):
    '''
        获取文件名
        返回
            1.文件名(不包含文件后缀)
            2.后缀
    '''
    pach , filename = os.path.split(filestr)
    return os.path.splitext(filename)

def FileExtLegitimate(ext, uploadtype):
    if ext:
        if uploadtype == 'image':
            if str(ext) not in ['.jpeg','.jpg','.png', '.jpg']:
                return False
            else:
                return True
        return False
    return False

def upload_file(request):
    try:
        file = request.files['file']
    except:
        return 400, '错误: 没有文件', ''

    # FileCompress_Head(file)

    upload_key = request.form.get('uploadKey',None)

    if not upload_key:
        return 400, '错误: Key值不能为空', {}

    filename, ext = QueryFileName(file.filename)
    if not FileExtLegitimate(ext, 'image'):
        return 400, '文件类型不允许', {}

    if upload_key not in UPLOAD_KEY_FLOAD:
        return 400, '错误: 不允许使用的Key值', {}

    newfilename = CreateNewFilename(ext)

    if upload_key in ['cvhead']:
        files = FileCompress_Head(file)
    else:
        files = file

    # files = file

    files.save(os.path.join(os.path.abspath('app/static/' + UPLOAD_KEY_FLOAD[str(upload_key)] + "/"), newfilename))

    return 200, 'ok', {
        'lodpath': SERVER_GULAOBURL + '/static/' + UPLOAD_KEY_FLOAD[str(upload_key)] + '/' + newfilename,
        'ospath': UPLOAD_KEY_FLOAD[str(upload_key)] + '/' + newfilename,
        'filename': newfilename
    }