# -*- coding:UTF-8 -*-

import os
import sys
import git
from git import Repo,RemoteProgress
from tqdm import tqdm
#删除非空目录
import  shutil



# 代码克隆进度条功能
# https://stackoverflow.com/questions/51045540/python-progress-bar-for-git-clone/62623518#62623518
class CloneProgress(RemoteProgress):
    def __init__(self):
        super().__init__()
        self.pbar = tqdm()
    def update(self, op_code, cur_count, max_count=None, message=''):
        self.pbar.total = max_count
        self.pbar.n = cur_count
        self.pbar.refresh()




class Git_module(object):
    def __init__(self,push_root_dir,file_name,jenkins_output_path,repo_url,local_branch_name,commit_content,repo_name,remote_branch_name):
        #本地系统环境部分
        self.push_root_dir = push_root_dir
        self.file_name = file_name
        self.push_usr_dir = os.path.join(push_root_dir,file_name)
        self.jenkins_output_path = jenkins_output_path

        #本地Git仓库部分
        self.repo_url = repo_url
        # self.branch_name = branch_name
        self.local_branch_name = local_branch_name
        self.commit_content = commit_content
        self.repo_name = repo_name

        #远程仓库部分
        self.remote_branch_name = remote_branch_name

        #实例化对象
        self.repo = git.Repo(self.push_usr_dir)



    #切换工作分支模块
    def checkout_branch(self):
        repo = self.repo
        repo.git.checkout(local_branch_name)
        print('切换分支到%s' % local_branch_name)

    #切换工作路径模块

    #Hash模块
    def hash(self):
        repo = self.repo
        # repo.git.checkout(local_branch_name)
        local_commit_hash = repo.rev_parse(local_branch_name)
        remote_commit_hash_before = repo.rev_parse(remote_branch_name)
        print('切换分支到%s' % local_branch_name)
        print(repo.rev_parse(local_branch_name))
        print(remote_commit_hash_before)

        print('-----------更新前远程的%s库hash'%local_branch_name)
        remote_fetch = repo.remotes.origin
        # 切换分支到main，尝试fetch是针对单个分支还是全部分支？ --若使用fetch()会把全部远程分支更新，所以需要指定特定分支
        remote_fetch.fetch(local_branch_name)

        remote_commit_hash_after = repo.rev_parse(remote_branch_name)

        print('-----------更新后远程的%s库hash' % local_branch_name)
        print(repo.rev_parse(local_commit_hash))
        print(remote_commit_hash_after)

        print('当前项目分支为%s'%repo.active_branch)

        if local_commit_hash == remote_commit_hash_after:
            print('本地仓库与远程仓库Hash一致')
            print('当前分支为：%s\n本地仓库Hash为：%s\n远程仓库Hash为：%s' % (local_branch_name, local_commit_hash, remote_commit_hash_after))
        else:
            print("本地仓库与远程仓库Hash不一致，将会自动进行更新......")
            print("本地仓库Hash为%s\n远程仓库Hash为%s" % (local_commit_hash, remote_commit_hash_after))
            # sleep(4)
            # 要指定拉取的分支，否则会拉取全部分支到本地
            remote_fetch.pull(local_branch_name)
            print('************%s' % repo.rev_parse('origin/main'))
            print('更新完成，当前本地Hash为%s\n' % (repo.rev_parse(local_branch_name)))

        #测试当前所有分支情况
        # list1 = ['main', 'origin/main', 't1', 'origin/t1']
        # for i in list1:
        #     print('当前分支为%s,commit的Hash为%s' % (i, repo.rev_parse(i)))

    #检测文件存在情况情况（1、项目目录是否存在 2、本地Git仓库是否存在）
    #设有返回值
    def pro_file_is_exists(self):
        push_usr_dir = self.push_usr_dir
        if not os.path.exists(file_name):
            print('推送目录不存在，将会从仓库拉取....')
            return 3
        else:
            try:
                os.chdir(push_usr_dir)
            except Exception:
                print("文件名：%s 的文件类型有问题，请检查...(如：目录下有同名的文件，而不是文件夹)" % (file_name))
                print("程序已中止.....")
                sys.exit(1)
            print('切换目录到对应项目下： %s' % (push_usr_dir))
            # 判断基准为是否有 ".git"目录
            if not os.path.exists('.git'):
                print("项目文件夹存在，但并没有检查到本地Git仓库")
                return 1
            else:
                print("此文件存在")
                return 2

    # 接收 file_exits函数返回值再做适当的初始化
    def git_init_action(self,pro_file_return=pro_file_is_exists()):
        push_usr_dir = self.push_usr_dir
        print(os.getcwd())
        if pro_file_return == 3:
            print('推送目录不存在，将会从远程仓库进行拉取....')
            Repo.clone_from(repo_url, push_usr_dir, branch=local_branch_name, progress=CloneProgress())

        elif pro_file_return == 2:
            print("项目本地Git仓库已存在")
        elif pro_file_return == 1:
            print("项目文件夹存在，但并没有检查到本地Git仓库")
            print("将会删除项目文件夹，并重新拉取...")
            # 此处的处理方法两种： 1、原脚本是直接初始化仓库，新建分支与当前分支建立映射；2、清空重拉。因为此处只做中转作用，没必要大费周章去处理
            # 当前处理方法..
            # 1、退出当前项目文件；2、删除项目文件；3、重新git clone
            # 切换回推送根目录
            os.chdir(push_root_dir)
            # os.removedirs(push_usr_dir)
            # 删除非空目录
            shutil.rmtree(push_usr_dir)
            Repo.clone_from(repo_url, push_usr_dir, branch=local_branch_name, progress=CloneProgress())
        else:
            print('程序中止，git_init_action模块接收的返回值异常')
            sys.exit(1)

    #jenkins编译出来的文件处理模块
    #处理的内容：1、清空当前目录下所有文件    2、将 jenkins编译出的文件复制到 当前项目文件夹下
    #jenkins获取到的workspace工作目录 /var/lib/jenkins/workspace/master-build   master-build为项目的名字



    #文件处理，从jenkins编译出的文件复制
    """
        注意点：
                1、jenkins目录下隐藏文件不复制，因为jenkins工作目录可能存在某些如svn git隐藏文件，没必要复制到指定文件
                2、测试大文件时工作是否正常？
                3、路径粒度为 项目名字，比如Jenkins路径为：/Users/aqumik/Desktop/git_test/jenkins_output/project1，则 project1为最细的粒度
                4、路径问题
    """
    def jenkins_to_push_dir(self):
        # print('hi')
        # test1 = '/Users/aqumik/Desktop/git_test/jenkins_output/project1/1'
        # shutil.copy2(jenkins_output_path,push_usr_dir,dirs_exist_ok=True)
        # shutil.copytree功能请看。。。https://docs.python.org/3/library/shutil.html#copytree-example
        # 复制目录，忽略隐藏文件
        shutil.copytree(jenkins_output_path, self.push_usr_dir, dirs_exist_ok=True, ignore=shutil.ignore_patterns(".*"))

    def delete_module(self):
        # 值得注意是此处会把隐藏文件也加到列表中,".git"也会被遍历到，所以此处要将隐藏文件都排除在列表外
        # Windows下的隐藏文件是否一样？
        # 项目文件是否存在隐藏文件？
        # 当前做法是把全部 '.'开头的文件过滤，组成新的列表，并不是删除列表内的元素
        # ???
        push_usr_dir = str(self.push_usr_dir)
        del_list = os.listdir(push_usr_dir)
        print(del_list)
        print(type(del_list))
        # print(id(del_list))
        # ??????
        del_list = [hide_file for hide_file in del_list if not hide_file.startswith('.')]
        print(del_list)
        # print(id(del_list))
        # 清空目录下所有文件或文件夹，".git"等隐藏文件除外
        # 针对非常大的目录，此处Windows系统中的处理可能需要注意，可以使用 “os.scandir(folder)”
        # https://stackoverflow.com/questions/185936/how-to-delete-the-contents-of-a-folder
        for filename in del_list:
            file_path = os.path.join(push_usr_dir, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                    print('Delete file %s Suc!' % (file_path))
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
                    print('Delete Dir %s Suc!' % (file_path))
            except Exception as e:
                print('Failed to delele %s . Reason: %s ' % (file_path, e))

    def pull_action_module(self):
        # repo = git.Repo(self.push_usr_dir)
        repo = self.repo
        remote_fetch = repo.remotes.origin

        print('拉取分支内容.....')
        remote_fetch.pull(local_branch_name)

    def push_action_module(self):
        repo = self.repo
        print('当前处于的分支： %s' % (repo.active_branch))
        repo.git.add('--all')
        repo.index.commit(commit_content)
        # 是否只推送当前分支？ 是
        origin = repo.remote(name=repo_name)
        origin.push()

if __name__ == '__main__':
    push_root_dir = '/Users/aqumik/Desktop/git_test/11'
    file_name = 't4'
    jenkins_output_path = '/Users/aqumik/Desktop/git_test/jenkins_output/project1'
    repo_url = 'git@gitee.com:chetimberk/jenkins-test1.git'
    local_branch_name = 'master'
    commit_content = 'hahahahahahahahah'
    repo_name = 'origin'
    remote_branch_name = 'master'
    g = Git_module(push_root_dir,file_name,jenkins_output_path,repo_url,local_branch_name,commit_content,repo_name,remote_branch_name)
    g.hash()