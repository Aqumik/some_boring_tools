# -*- coding:UTF-8 -*-
import gitlab,json,requests

# pytho-gitlab 文档
# https://python-gitlab.readthedocs.io/en/stable/

class gitlab_operate(object):
    def __init__(self,api_toekn,url):
        self.api_toekn = api_toekn
        self.url = url
        self.login = gitlab.Gitlab(self.url,self.api_toekn)

    # 列出所有项目的name，id
    def list_all_pro(self):
        # private 为可见级别
        projects = self.login.projects.list(all=True,)
        for p in projects:
            print(p.name,p.id)
    # 列出所有组
    def list_all_group(self):
        projects = self.login.groups.list(all=True)
        for p in projects:
            print(p.name,p.id)
    # 创建组
    def create_group(self):
        ll = self.login
        ll.groups.create({"name":"PJTD大","path":"PJTDD"})
        # group.save()
    # 删除指定组，需要指定id
    def del_group(self,group_id):
        self.login.groups.delete(group_id)
        # group.save()

    # 组中创建项目
    def create_pro_ingroup(self,pro_name,descrp):
        group_id = self.login.groups.list(search='pjtd')[0].id
        project = self.login.projects.create({'name':pro_name,'namespace_id': group_id,'description':descrp,'auto_devops_enabled':0,'visibility':'private'})
        project.snippets_enabled = 1
        project.save()

    # 删除项目
    def delete_pro(self):
        self.login.projects.delete(61)

    def delete_all_pro(self):
        projects = self.login.projects.list(all=True)
        for p in projects:
            print(p.name,p.id)
            self.login.projects.delete(p.id)

if __name__ == '__main__':
    api_token = 'Bkvrz14zEv4cy4S79zAY'
    url = 'http://10.10.16.94/'
    g = gitlab_operate(api_toekn=api_token,url=url)
    g.list_all_group()
    print('-------')
    g.list_all_pro()
    # pro_list = ["PJC3_Mainserver","PJC3_Versionweb","PJC3_Statjob","PJC3_SQL","PJC3_Sdkserver","PJC3_Mainjob","PJC3_Loginserver","PJC3_Gmweb","PJC3_Gmsitev2","PJC3_Gmsite","PJC3_Globalcommonserver","PJC3_Battleserver"]
    g.create_group()
    # g.delete_all_pro()
    # print(len(pro_list))
    # for i in pro_list:
    #     pro_id = i
    #     pro_descrip = str(i) + ' 测试专用'
    #     print('******正在创建项目%s'%pro_id)
    #     g.create_pro_ingroup(pro_id,pro_descrip)
    # g.delete_pro()
    # g.create_pro_ingroup()

    # g.del_group()
