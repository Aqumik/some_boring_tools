# -*- coding:UTF-8 -*-
'''
@Date    ：2022/2/14 11:09 上午 
@Author  ：aqumik
NO ERROR !!!
NO ERROR !!!
NO ERROR !!!
'''

import faker
import random
class random_func(object):
    def per_info(self):
        f = faker.Faker(locale='zh-CN')
        # print('klfjaskldfjlakjdflkajeklf')
        # print('111')
        content = '%s\n%s\n%s\n%s\n%s\n%s\n%s\n'%(f.name(),f.credit_card_number(),f.email(),f.ipv4(),f.user_name(),f.phone_number(),f.ssn())
        # print(len(content))
        ran_gbk_p =  self.gbk_p()
        content = content + '\n' + ran_gbk_p
        return content
        # print(f.name())
        # print(f.credit_card_number())
        # print(f.email())
        # print(f.ipv4())
        # print(f.user_name())
        # print(f.phone_number())
        # print(f.ssn())

    def gbk_p(self):
        str = ''
        for i in range(1400):
            head = random.randint(0xb0, 0xf7)
            body = random.randint(0xa1, 0xfe)
            val = f'{head:x}{body:x}'
        # for i in range(1000):
            str = str + bytes.fromhex(val).decode('gb2312',errors="ignore")
        # print(len(str))
        return str
if __name__ == '__main__':
    pass
    ab = random_func()

    # print(ab.gbk_p())
    # for i in range(5):
        # print(ab.per_info())