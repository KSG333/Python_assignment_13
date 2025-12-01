# 39번
def print_odd_numbers():
    for i in range(0,num):
        if i % 2 != 0:
            print(i, end=" ")

num = int(input('숫자 입력 : '))
print_odd_numbers()


# 40번
def print_numbers():
        if num % 3 == 0:
            print("%d는(은) 3의 배수 입니다." % num)
        else:
            print('3의 배수가 아닙니다.')
            
num = int(input('숫자 입력 : '))
print_numbers()


# 41번
def result(a,b,c,d):
    rst_max = max(a,b,c,d)
    rst_min = min(a,b,c,d)
    return rst_max, rst_min

a,b,c,d = map(int,input('숫자 4개 입력 : ').split())
max_vlaue, min_value = result(a,b,c,d)
print("최댓값 : %d, 최솟값 : %d" % (max_vlaue, min_value))


# 42번
def num_odd():
    for i in range(0,num):
        if i % 2 != 0:
            print(i, end=" ")
        
num = int(input('숫자 1개 입력 : '))
num_odd()


# 43번
def Factorial():
    rst = 1
    for i in range(1, num+1):
        rst *= i
    print(rst)
        
num = int(input('0보다 큰 정수 1개 입력 : '))
Factorial()


# 44번
def all_sum(n,n1):
    sum = 0
    for i in range(1, n+1):
        for j in range(1, n1+1):
            if (i * j) >= 30:
                sum += (i + j)
    return sum
                
num1, num2 = map(int,input('2이상 9이하 숫자 2개 입력 : ').split())
result_sum = all_sum(num1,num2)
print(result_sum)


# 45번
def sum_all(list):
    sum = 0
    for i in list:
        sum += i
    return sum

a = [1,2,3,4,5]
result_sum = sum_all(a)
print("list 내 총 합은 : %d" % result_sum)