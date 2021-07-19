from subprocess import Popen, PIPE, STDOUT
p = Popen(['echo', 'gg'], stdout=PIPE, stderr=STDOUT)
for line in p.stdout:
    print(line)
