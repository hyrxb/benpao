#!/usr/bin/emv python
#-*- coding:utf8 -*-


# 报错问题 http://blog.chinaunix.net/uid-28841896-id-4652377.html

#安装包地址：http://www.dnspython.org/kits/1.9.4/

#步骤：
#  wget http://www.dnspython.org/kits/1.9.4/dnspython-1.9.4.tar.gz
#tar zxvf dnspython-1.9.4.tar.gz
#cd dnspython-1.9.4
#python setup.py install


import dns.resolver

def getipaddr():
    domain = raw_input('Please input an domain:')
    A = dns.resolver.query(domain, 'A')

    for i in A.response.answer:
        for j in i.items:
            if j.rdtype == 1: # 脚本存在问题，需要判断一下rdtype类型
                print j.address
            else:
                pass


if __name__ =='__main__':
    getipaddr()



