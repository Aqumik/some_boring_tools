# -*- coding:UTF-8 -*-

import subprocess

p = subprocess.Popen(
    ["C:\Program Files\Git\git-bash.exe","E:\github\some_boring_tools\jenkins_git_pull_test\sh_test\env_output.sh"],
    bufsize=1,
    stdin=None,
    stdout=None,
    stderr=None,
    preexec_fn=None,
    close_fds=True,
    shell=False,
    cwd="E:\github\some_boring_tools\jenkins_git_pull_test",
)