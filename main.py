#!C:\Python27\ArcGIS10.1\python.exe -u               
# coding=utf-8

print "Content-Type: text/html"
print

import urllib,re,sys,os,time

def prev_tpl():
    print '''
        <!DOCTYPE html>
        <html lang="en-gb">
        <head>
            <title>bing首页图片抓取</title>
        </head>
        <body>
    '''

def next_tpl():
    print '''
        </body>
        </html>
    '''

def get_bing_backphoto():
    '''
    抓取bing首页的背景图片
    '''
    t0 = time.clock()
    prev_tpl()
    if (os.path.exists('photos')== False):
        os.mkdir('photos')
 
    for i in range(0,5):
        url = 'http://cn.bing.com/HPImageArchive.aspx?format=js&idx='+str(i)+'&n=1&nc=1361089515117&FORM=HYLH1'
        html = urllib.urlopen(url).read()
        if html == 'null':
            print 'open & read bing error!'
            sys.exit(-1)
        reg = re.compile('"url":"(.*?)","urlbase"',re.S)
        reg1 = re.compile('"link":".*?","text":"(.*?)"',re.S)
        text = re.findall(reg,html)
        text1 = re.findall(reg1,html)
        #http://s.cn.bing.net/az/hprichbg/rb/LongJi_ZH-CN8658435963_1366x768.jpg
        # print text[0]    
        for imgurl in text:
            # print imgurl
            right = imgurl.rindex('.')
            name = imgurl.replace(imgurl[:right+1],'')
            # name = imgurl.replace(imgurl[:right+1],'')
            
            # 用下面的这种表示方法可以成功存储为中文名称的文件
            # savepath = u'photos/身着“晚宴”装的企鹅.jpg'
            # u'photos/'+ text1[0] + '.' + name,会报错
            # unicode('photos/'+ text1[0] + '.' + name, 'gb2312')会报错
            savepath = unicode('photos/'+ text1[0] + '.' + name, 'utf-8')
            
            if (os.path.exists(savepath)== True):
                print '<strong>', text1[0], '</strong>已经存在'
                print '<br/>'
            else:
                print text1[0] + '正在下载...'
                # print savepath
                urllib.urlretrieve(imgurl, savepath)
                urllib.urlretrieve(imgurl, savepath)
                print '  保存成功!'
                print '<br/>'

    next_tpl()
    print '<h3>'
    print '共消耗时间（s）:', time.clock()
    print '</h3>'


get_bing_backphoto()

