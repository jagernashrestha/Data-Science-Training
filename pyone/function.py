def fun (array1):
    sum = 0
    for i in array1:
        sum = sum + i
    return sum
array1 = [5,6,7,8,9]
s = fun(array1)
print(s)

def adder (nums):
    sum = 0
    for i in nums:
        sum += i #sum = Sum+i
    print("sum is:" +str(sum))


adder([1,2,3])