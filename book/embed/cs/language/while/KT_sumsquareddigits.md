
N-test개의 줄에  k(data set 수),b,n 정수가 주어진다
k개의 줄에 각 test 번호 k와 SSB(b,n)을 출력하라
n_test = int(input())
def SSD(b, n):
    ret = 0
    while n != 0:
        ret += (n % b) ** 2
        n //= b
    return ret    
for _ in range(1, n_test + 1):
    K, b, n = map(int, input().split())
    print(f'{K} {SSD(b, n)}')
