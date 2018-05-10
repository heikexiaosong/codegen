# -*- coding: UTF-8 -*-
#encoding:utf8

from DBUtils import DBUtils

print("mssql connect demo\n")

if __name__ == '__main__':
    db = DBUtils(host='118.31.239.85',username='KRDMG',password='KRDMG',database='GAVEL_DMG')
    db.connect()

    results = db.query('SELECT * FROM PD')
    print("项目列表: ")
    for i, r in enumerate(results):
        print('\t* ' + str(i + 1) + ' >>>  ', end="")
        print(r)
    index = input("请选择：")
    record = results[int(index)-1]
    print("您选择的项目是: ", record)

    sql = "select * from DBTABLE where DBTABLE_CPID = '" + record[1] + "'"
    records = db.query(sql)
    for i, r in enumerate(records):
        print('\t* ' + str(i + 1) + ' >>>  ', end="")
        print(r)

    # ALTER TABLE GAVEL_DMG.dbo.DBTABLE ALTER COLUMN DBTABLE_ID NVARCHAR(40) NOT NULL


    db.destory()