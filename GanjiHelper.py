# -*- coding: utf-8 -*-
"""
Created on Sun Mar 30 19:18:36 2014

@author: alvin
"""

from pyquery import PyQuery as pyq

class HouseInfo:
    title = ''
    link = ''
    district = '' #小区
    floor = ''
    distance = ''
    area = ''
    #address = ''
    owner = ''
    phone = ''
    description = ''
    isPrivate = 0
    houseID = '0'
    subway = ''
    kind = ''
    decoration = ''
    direction = ''

class GanjiHelper:    
    url = ''
    houses = []
    
    def __init__(self,dest):
        self.url = dest
        doc = pyq(url = self.url)
        records = doc('.list-img')
        for record in records:
            houseInfo = HouseInfo()
            titleLine = record.cssselect('.list-info-title')[0];
            houseInfo.title = self.getAttr(titleLine,'title')
            houseInfo.link = '%s%s' % (r'http://bj.ganji.com',self.getAttr(titleLine,'href'))
            district = record.cssselect('.list-word-col')[0]
            houseInfo.district = district.text_content()
            subway = record.cssselect('.list-word-col')[1]
            houseInfo.subway = subway.text_content()
            dist = record.cssselect('.list-word')[0]
            houseInfo.distance = dist.text_content().split('-')[-1].decode('utf-8')
            #(houseInfo.kind,houseInfo.area,houseInfo.decoration,houseInfo.floor,houseInfo.direction) = record.cssselect('.list-word')[1].text_content().split('/')
            props = record.cssselect('.list-word')[1].text_content().split('/')
            houseInfo.kind = props[0]
            houseInfo.area = props[1]
            houseInfo.kind = props[2]
            houseInfo.floor = props[3]
            houseInfo.direction = props[4]            
            self.houses.append(houseInfo)
            #print(record.cssselect('.list-word')[1].text_content())
        for house in self.houses:
            print(house.title)

            
    def getAttr(self,host,attr):
        exp = '[%s]' % attr
        if host.cssselect(exp):
            return host.attrib[attr]
        else:
            return ''
    


ganji = GanjiHelper(r'http://bj.ganji.com/fang3/ditie/l2049s15w10/')

