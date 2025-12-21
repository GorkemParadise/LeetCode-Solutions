import sys
import os

# Notebook için BASE_DIR yerine cwd kullan
BASE_DIR = os.getcwd()

sys.stdin = open(os.path.join(BASE_DIR, 'input.txt'), 'r')
sys.stdout = open(os.path.join(BASE_DIR, 'output.txt'), 'w')

def solve():
    n = int(input())  # 1. satır
    arr = list(map(int, input().split()))  # 2. satır
    
    def q1(x):
        for i in range(1, x + 1):
            print(i, end=' ')
        print()
    
    q1(n)
    print(sum(arr))

solve()
