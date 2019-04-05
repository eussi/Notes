#!/usr/bin/env python
# Author:Wang Xueming

'''
    单行注释：# 被注释内容
　　多行注释：""" 被注释内容 """  (双引号或者单引号)

    三个成对的双引号或者单引号还可以作为多行打印来使用
    单行打印使用双引号或者单引号都可以，效果相同，与shell有所区别
    使用单引号还是双引号取决于内容包含双引号还是单引号，不包含均可以使用
'''
mulitLine = """开始：
被注释内容 
多行打印
"""
# 注意加号后跟进的引号需要和加号在同一行,否则会报错
mulitLine2 = """开始：
被注释内容 """ +"""--------插入内容""" + "---单行注释" +  '''
多行打印
'''
print(mulitLine)
print(mulitLine2)