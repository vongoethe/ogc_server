# -*- coding: utf-8 -*-
import os, sys
import json
import xlrd
import codecs
from collections import  OrderedDict
from db_util import init_global, get_pinyin_data, update_geometry2d, mongo_action, mongo_find, mongo_find_one, \
    add_mongo_id, remove_mongo_id
from module_locator import dec, dec1, enc, enc1
from pydash import py_ as _


XLS_FILE = ur'G:\work\matlab\dn\bayes_rset\data_bus.xls'
XLS_FILE = ur'G:\work\matlab\dn\bayes_rset\data_lnbr.xls'
XLS_FILE = ur'G:\work\matlab\dn\bayes_rset\data_conlnbr.xls'
XLS_FILE = ur'D:\2014项目\配电网故障定位\yx.xls'

def test():
    ret = []
    book = xlrd.open_workbook(XLS_FILE)
    startrowidx = 1
    for sheet in book.sheets():
        sheetdata = []
        header = []
        for i in range(0, 8):
            header.append(sheet.cell_value(0, i).strip())
        for row in range(startrowidx, sheet.nrows):
            v = OrderedDict()
            for col in range(0, 8):
                if col == 0:
                    v[header[col]] = int(sheet.cell_value(row, col))
                else:
                    v[header[col]] = sheet.cell_value(row, col)
            sheetdata.append(v)
        ret.append(sheetdata)
    s = json.dumps(ret, ensure_ascii=True, indent=4)
    # with codecs.open(XLS_FILE.replace('.xls', '.json'), 'w', 'utf-8-sig') as f:
    with open(XLS_FILE.replace('.xls', '.json'), 'w') as f:
        f.write(s)
    # print(s)

def test1():
    ret = []
    book = xlrd.open_workbook(XLS_FILE)
    startrowidx = 1
    sheet = book.sheets()[0]#book.get_sheet(0)

    header = []
    for i in range(0, 10):
        header.append(sheet.cell_value(0, i).strip())
    for row in range(startrowidx, sheet.nrows):
        v = OrderedDict()
        for col in range(0, 10):
            if col == 0:
                v[header[col]] = int(sheet.cell_value(row, col))
            else:
                v[header[col]] = sheet.cell_value(row, col)
        ret.append(v)
    s = json.dumps(ret, ensure_ascii=True, indent=4)
    # with codecs.open(XLS_FILE.replace('.xls', '.json'), 'w', 'utf-8-sig') as f:
    with open(XLS_FILE.replace('.xls', '.json'), 'w') as f:
        f.write(s)
    # print(s)




def test2():
    book = xlrd.open_workbook(XLS_FILE)
    startrowidx = 1
    ret = []
    for sheet in book.sheets():
        if sheet.name == u'负荷开关':
            for row in range(startrowidx, sheet.nrows):
                o = {}
                lng = sheet.cell_value(row, 8)
                lat = sheet.cell_value(row, 9)
                if isinstance(lng, str) or isinstance(lng, unicode) or isinstance(lat, str) or isinstance(lat, unicode):
                    pass
                elif isinstance(lng, float) and  isinstance(lat, float):
                    if len(sheet.cell_value(row, 6)):
                        o['type'] = 'Feature'
                        o['properties'] = {}
                        o['properties']['device_id_nx'] = str(int(sheet.cell_value(row, 0)))
                        o['properties']['webgis_type'] = 'point_dn'
                        o['properties']['function_pos_code'] = sheet.cell_value(row, 1)
                        o['properties']['name'] = sheet.cell_value(row, 2)
                        o['properties']['function_pos_type'] = 'PAD'
                        o['properties']['owner'] = sheet.cell_value(row, 4)
                        o['properties']['line_func_code'] = sheet.cell_value(row, 6)
                        o['properties']['device_no'] = sheet.cell_value(row, 10)
                        # o['properties']['tower'] = None
                        if isinstance(sheet.cell_value(row, 12), float):
                            o['properties']['voltage_rated'] = sheet.cell_value(row, 12)
                        if isinstance(sheet.cell_value(row, 13), float):
                            o['properties']['current_rated'] = sheet.cell_value(row, 13)
                        o['geometry'] = {'type':'Point','coordinates':[lng, lat]}
                        if u'10kV' in o['properties']['name']:
                            o['properties']['voltage'] = '08'
                            # o['properties']['name'] = o['properties']['name'].replace(u'10kV', '')
                        o = update_geometry2d(o, True)
                        ret.append(o)

        if sheet.name == u'断路器':
            for row in range(startrowidx, sheet.nrows):
                o = {}
                lng = sheet.cell_value(row, 8)
                lat = sheet.cell_value(row, 9)
                if isinstance(lng, str) or isinstance(lng, unicode) or isinstance(lat, str) or isinstance(lat, unicode):
                    pass
                elif isinstance(lng, float) and  isinstance(lat, float):
                    if len(sheet.cell_value(row, 6)):
                        o['type'] = 'Feature'
                        o['properties'] = {}
                        o['properties']['device_id_nx'] = str(int(sheet.cell_value(row, 0)))
                        o['properties']['webgis_type'] = 'point_dn'
                        o['properties']['function_pos_code'] = sheet.cell_value(row, 1)
                        o['properties']['name'] = sheet.cell_value(row, 2)
                        o['properties']['function_pos_type'] = 'PAC'
                        o['properties']['owner'] = sheet.cell_value(row, 4)
                        o['properties']['line_func_code'] = sheet.cell_value(row, 6)
                        o['properties']['device_no'] = sheet.cell_value(row, 10)
                        # o['properties']['tower'] = None
                        if isinstance(sheet.cell_value(row, 12), float):
                            o['properties']['voltage_rated'] = sheet.cell_value(row, 12)
                        if isinstance(sheet.cell_value(row, 13), float):
                            o['properties']['current_rated'] = sheet.cell_value(row, 13)
                        o['geometry'] = {'type':'Point','coordinates':[lng, lat]}
                        if u'10kV' in o['properties']['name']:
                            o['properties']['voltage'] = '08'
                            # o['properties']['name'] = o['properties']['name'].replace(u'10kV', '')
                        o = update_geometry2d(o, True)
                        ret.append(o)

        if sheet.name == u'隔离开关':
            for row in range(startrowidx, sheet.nrows):
                o = {}
                lng = sheet.cell_value(row, 8)
                lat = sheet.cell_value(row, 9)
                if isinstance(lng, str) or isinstance(lng, unicode) or isinstance(lat, str) or isinstance(lat, unicode):
                    pass
                elif isinstance(lng, float) and  isinstance(lat, float):
                    if len(sheet.cell_value(row, 6)):
                        o['type'] = 'Feature'
                        o['properties'] = {}
                        o['properties']['device_id_nx'] = str(int(sheet.cell_value(row, 0)))
                        o['properties']['webgis_type'] = 'point_dn'
                        o['properties']['function_pos_code'] = sheet.cell_value(row, 1)
                        o['properties']['name'] = sheet.cell_value(row, 2)
                        o['properties']['function_pos_type'] = 'PAE'
                        o['properties']['owner'] = sheet.cell_value(row, 4)
                        o['properties']['line_func_code'] = sheet.cell_value(row, 6)
                        o['properties']['device_no'] = sheet.cell_value(row, 10)
                        # o['properties']['tower'] = None
                        if isinstance(sheet.cell_value(row, 12), float):
                            o['properties']['voltage_rated'] = sheet.cell_value(row, 12)
                        if isinstance(sheet.cell_value(row, 13), float):
                            o['properties']['current_rated'] = sheet.cell_value(row, 13)
                        o['geometry'] = {'type':'Point','coordinates':[lng, lat]}
                        if u'10kV' in o['properties']['name']:
                            o['properties']['voltage'] = '08'
                            # o['properties']['name'] = o['properties']['name'].replace(u'10kV', '')
                        o = update_geometry2d(o, True)
                        ret.append(o)
    print(len(ret))
    mongo_action('kmgd', 'features', 'save', ret)

def test3():
    XLS_FILE = ur'D:\2014项目\配电网故障定位\yx_line.xls'
    book = xlrd.open_workbook(XLS_FILE)
    startrowidx = 1
    toplines = set()
    for sheet in book.sheets():
        for row in range(startrowidx, sheet.nrows):
            # o = {'properties':{'webgis_type':'polyline_dn'}}
            # o['properties']['func_pos_code'] = sheet.cell_value(row, 1)
            # o['properties']['name'] = sheet.cell_value(row, 2)
            # o['properties']['owner'] = sheet.cell_value(row, 3)
            # update_geometry2d(o, False)
            if len(sheet.cell_value(row, 6)):
                toplines.add(sheet.cell_value(row, 6))
        # print(toplines)

    XLS_FILE1 = ur'D:\2014项目\配电网故障定位\玉溪局台账数据导出1\玉溪杆塔.xls'
    book1 = xlrd.open_workbook(XLS_FILE1)
    startrowidx = 1
    ret = []
    linesmap = {}
    for sheet in book1.sheets():
        for row in range(startrowidx, sheet.nrows):
            line_no = sheet.cell_value(row, 3)
            if line_no in toplines:
                # device_no = sheet.cell_value(row, 1)
                lng = sheet.cell_value(row, 5)
                lat = sheet.cell_value(row, 6)
                if isinstance(lng, str) or isinstance(lng, unicode) or isinstance(lat, str) or isinstance(lat, unicode):
                    pass
                elif isinstance(lng, float) and isinstance(lat, float):
                    if not line_no in linesmap.keys():
                        linesmap[line_no] = []
                    o = {}
                    o['type'] = 'Feature'
                    o['properties'] = {}
                    # o['properties']['device_id_nx'] = str(int(sheet.cell_value(row, 0)))
                    o['properties']['webgis_type'] = 'point_tower'
                    o['properties']['function_pos_code'] = sheet.cell_value(row, 0)
                    if not o['properties']['function_pos_code'] in linesmap[line_no]:
                        linesmap[line_no].append(o['properties']['function_pos_code'])
                    o['properties']['name'] = sheet.cell_value(row, 1)
                    if len(o['properties']['name']) == 0 or  o['properties']['name'] == u'杆塔':
                        o['properties']['name'] = o['properties']['function_pos_code'] + u'杆塔'
                    # if (isinstance(o['properties']['name'], str) or isinstance(o['properties']['name'], unicode)) and len(o['properties']['name']) == 0:
                    #     o['properties']['name'] = device_no
                    # if isinstance(o['properties']['name'], int) or isinstance(o['properties']['name'], float):
                    #     o['properties']['name'] = str(o['properties']['name'])
                    o['properties']['function_pos_type'] = 'LAD'
                    o['properties']['line_func_code'] = line_no
                    o['geometry'] = {'type':'Point','coordinates':[lng, lat]}
                    # if u'10kV' in o['properties']['name']:
                    o['properties']['voltage'] = '08'
                    o = update_geometry2d(o, True)
                    if len(ret) % 100 == 0:
                        print(len(ret))
                    ret.append(o)
        # for k in linesmap.keys():
        #     s = sorted(linesmap[k])
        #     l = []
        #     for i in range(len(s)-1):
        #         l.append([s[i], s[i+1]])
        #     linesmap[k] = l
        # print(len(ret))
        # print(len(linesmap.keys()))
        # with codecs.open(ur'd:\linesmap.json', 'w', 'utf-8-sig') as f:
        #     f.write(json.dumps(linesmap, ensure_ascii=False, indent=4))
    mongo_action('kmgd', 'features', 'save', ret)

def test4():
    XLS_FILE = ur'D:\2014项目\配电网故障定位\yx_line.xls'
    book = xlrd.open_workbook(XLS_FILE)
    startrowidx = 1
    toplines = set()
    ret = []
    for sheet in book.sheets():
        for row in range(startrowidx, sheet.nrows):
            # o = {'properties':{'webgis_type':'polyline_dn'}}
            # o['properties']['func_pos_code'] = sheet.cell_value(row, 1)
            # o['properties']['name'] = sheet.cell_value(row, 2)
            # o['properties']['owner'] = sheet.cell_value(row, 3)
            # update_geometry2d(o, False)
            if len(sheet.cell_value(row, 6)):
                toplines.add(sheet.cell_value(row, 6))
        # print(toplines)
        for row in range(startrowidx, sheet.nrows):
            funcpos = sheet.cell_value(row, 1)
            if funcpos in toplines:
                o = {'properties':{'webgis_type':'polyline_dn'}}
                o['properties']['device_id_nx'] = str(int(sheet.cell_value(row, 0)))
                o['properties']['func_pos_code'] = funcpos
                o['properties']['name'] = sheet.cell_value(row, 2)
                o['properties']['owner'] = sheet.cell_value(row, 3)
                o['properties']['nodes'] = []
                o['properties']['subnet'] = []
                if u'10kV' in o['properties']['name']:
                    o['properties']['voltage'] = '08'

                o = update_geometry2d(o, False)
                print(o['properties']['name'])
                ret.append(o)
                # print(o)
    mongo_action('kmgd', 'network', 'save', ret)
    # print(json.dumps(ret, ensure_ascii=False, indent=4))

def test5():
    XLS_FILE = ur'D:\2014项目\配电网故障定位\yx_line.xls'
    book = xlrd.open_workbook(XLS_FILE)
    startrowidx = 1
    toplines = set()
    for sheet in book.sheets():
        for row in range(startrowidx, sheet.nrows):
            if len(sheet.cell_value(row, 6)):
                toplines.add(sheet.cell_value(row, 6))
            # toplines.add(sheet.cell_value(row, 6))

    XLS_FILE1 = ur'D:\2014项目\配电网故障定位\玉溪局台账数据导出1\变压器参数.xls'
    book1 = xlrd.open_workbook(XLS_FILE1)
    startrowidx = 1
    ret = []
    for sheet in book1.sheets():
        for row in range(startrowidx, sheet.nrows):
            line_no = sheet.cell_value(row, 55)
            if line_no in toplines:
                device_no = sheet.cell_value(row, 26)
                lng = sheet.cell_value(row, 73)
                lat = sheet.cell_value(row, 74)
                if isinstance(lng, str) or isinstance(lng, unicode) or isinstance(lat, str) or isinstance(lat, unicode):
                    pass
                elif isinstance(lng, float) and isinstance(lat, float):
                    o = {}
                    o['type'] = 'Feature'
                    o['properties'] = {}
                    o['properties']['device_id_nx'] = str(int(sheet.cell_value(row, 0)))
                    o['properties']['webgis_type'] = 'point_dn'
                    o['properties']['function_pos_code'] = sheet.cell_value(row, 1)
                    o['properties']['name'] = sheet.cell_value(row, 67)
                    if (isinstance(o['properties']['name'], str) or isinstance(o['properties']['name'], unicode)) and len(o['properties']['name']) == 0:
                        o['properties']['name'] = device_no
                    if isinstance(o['properties']['name'], int) or isinstance(o['properties']['name'], float):
                        o['properties']['name'] = str(o['properties']['name'])
                    o['properties']['function_pos_type'] = 'PAB'
                    o['properties']['line_func_code'] = line_no
                    o['properties']['device_no'] = device_no
                    o['geometry'] = {'type':'Point','coordinates':[lng, lat]}
                    # if u'10kV' in o['properties']['name']:
                    o['properties']['voltage'] = '08'
                    # o = update_geometry2d(o, True)
                    ret.append(o)
        break
    print(json.dumps(ret, ensure_ascii=False, indent=4))
    # mongo_action('kmgd', 'features', 'save', ret)

def test6():
    def get_line_id(alist, code):
        return _.find(alist, lambda x: x['properties'].has_key('func_pos_code') and x['properties']['func_pos_code'] == code)
        # return _.matches_property('properties.func_pos_code', code)(alist)
    def get_point_id(alist, code):
        return _.find(alist, lambda x: x['properties'].has_key('function_pos_code') and x['properties'][
                                                                                            'func_pos_code'] == code)
    ret = []
    linesmap = {}
    with codecs.open(ur'd:\linesmap.json', 'r', 'utf-8-sig') as f:
        linesmap = json.loads(f.read())
    polyline_dn = mongo_find('kmgd', 'network', {'properties.webgis_type':'polyline_dn'})
    # towers = mongo_find('kmgd', 'features', {'properties.webgis_type':'point_tower'})
    idx = 0
    for k in linesmap.keys():
        codes = _.uniq(_.flatten(linesmap[k]))
        o = get_line_id(polyline_dn, k)
        if o:
            # l = mongo_find('kmgd', 'features', {'properties.line_func_code':k})
            # ids = _.pluck(l, '_id')
            ll = mongo_find('kmgd', 'features', {'properties.function_pos_code':{'$in':codes}})
            if len(ll):
                lll = _.pluck(ll, '_id')
                o['properties']['nodes'] = lll
                # o = add_mongo_id(o)
                ret.append(o)
                idx += 1
                # if idx > 10:
                #     break
    mongo_action('kmgd', 'network', 'save', ret)

def test7():
    def get_line_id(alist, code):
        return _.find(alist, lambda x: x['properties'].has_key('func_pos_code') and x['properties']['func_pos_code'] == code)
        # return _.matches_property('properties.func_pos_code', code)(alist)
    def get_point_id(alist, code):
        return _.find(alist, lambda x: x['properties'].has_key('function_pos_code') and x['properties']['func_pos_code'] == code)


    XLS_FILE = ur'D:\2014项目\配电网故障定位\yx_line.xls'
    book = xlrd.open_workbook(XLS_FILE)
    startrowidx = 1
    toplines = set()
    for sheet in book.sheets():
        for row in range(startrowidx, sheet.nrows):
            if len(sheet.cell_value(row, 6)):
                toplines.add(sheet.cell_value(row, 6))
    # if True:
    #     print (toplines)
    #     return

    ret = []
    linesmap = {}
    # with codecs.open(ur'd:\linesmap.json', 'r', 'utf-8-sig') as f:
    #     linesmap = json.loads(f.read())

    # polyline_dn =
    features = mongo_find('kmgd', 'features', {'properties.webgis_type':'point_dn'})
    for topline in toplines:
        polyline_dn = mongo_find_one('kmgd', 'network', {'properties.webgis_type':'polyline_dn',
                                                     'properties.func_pos_code':topline})
        if polyline_dn:
            print (polyline_dn['_id'])
            # for feature in features:
            #     if feature.has_key('properties') \
            #         and  feature['properties'].has_key('device_id_nx') and len(feature['properties']['device_id_nx']) \
            #         and  feature['properties'].has_key('line_func_code') and feature['properties']['line_func_code'] == topline:
            #         if not linesmap.has_key(feature['properties']['line_func_code']):
            #             linesmap[feature['properties']['line_func_code']] = []
            #         if not feature['properties']['device_id_nx'] in linesmap[feature['properties']['line_func_code']]:
            #             linesmap[feature['properties']['line_func_code']].append(feature['properties']['device_id_nx'])






    # idx = 0
    # for k in linesmap.keys():
    #     codes = _.uniq(_.flatten(linesmap[k]))
    #     o = get_line_id(polyline_dn, k)
    #     if o:
    #         # l = mongo_find('kmgd', 'features', {'properties.line_func_code':k})
    #         # ids = _.pluck(l, '_id')
    #         ll = mongo_find('kmgd', 'features', {'properties.function_pos_code':{'$in':codes}})
    #         if len(ll):
    #             lll = _.pluck(ll, '_id')
    #             if not
    #             o['properties']['nodes'] = lll
    #             # o = add_mongo_id(o)
    #             ret.append(o)
    #             idx += 1
    #             # if idx > 10:
    #             #     break
    # mongo_action('kmgd', 'network', 'save', ret)




if __name__ == "__main__":
    init_global()
    test7()
    
    