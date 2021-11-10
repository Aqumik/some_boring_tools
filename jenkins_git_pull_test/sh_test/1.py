import pexpect as pexpect


process = pexpect.spawn('echo "helo guts" > python_ouuuuuutt')
process.expect(pexpect.EOF)