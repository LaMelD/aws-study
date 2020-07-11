import sys
import os

base_dir = os.getcwd()
aws_init_dir = os.path.join(base_dir, "aws-init")
aws_init_docs = os.path.join(aws_init_dir, "docs")

li = [6,6,9,6,7]

for i in range(0, 5):
    for j in range(1, li[i] + 1):
        f = open(os.path.join(aws_init_docs, "ch0%d-%d.md" % (i + 1, j)), mode='w')
        f.close()
