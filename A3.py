s1 = int(input("Enter the speed of the car"))
s2 = int(input("Enter the speed of the car"))
s3 = int(input("Enter the speed of the car"))

a = int((s1+s2+s3)/3)

print(a)
if s1<a:
    print("s1 is lower than the average and the difference is:" ,a - s1)
if s2<a:
    print("s2 is lower than the average and the difference is:" ,a - s2)
if s3<a:
    print("s3 is lower than the average and the difference is:" ,a - s3)