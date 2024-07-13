arr=[12,4,14,2,8]
min=arr[0]
for i in range(len(arr)):
    if min>arr[i]:
       min=arr[i]
max=arr[0]
for i in range(len(arr)):
    if max<arr[i]:
       max=arr[i]
print(min)
print(max)