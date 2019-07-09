import sys

def B(num):
    print(num)


def A(num):
    print(num)
    B(100)

if sys.argv[1]=='A':
    A(200)
else:
    B(300)

print(sys.argv)
