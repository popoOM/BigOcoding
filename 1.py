#https://www.dropbox.com/sh/guonijof1gbey02/AACzygfiz5sqBWmDoe9Igmxpa?dl=0
n = int(input())
a = b = count = 0
array = []
for i in range(1001):
    array.append({a, b})
class Color:
    def __init__(self,id):
        self.color_id = id
        self.sum_length = 0
        self.count = 0
    def update(self, new_length):
        self.sum_length += new_length
        self.count += 1
for i in range(n):
    array.append(Color(i))
for i in range(n):
    a,b = map(int, input().split())
    array[a].update(b)  # tự compile lại cho nhớ
diff = 0
for i in range(n):
    if array[i].count > 0:
        diff +=1
print(diff)
for i in range(n):
    if array[i].count > 0:
        print(i, array[i].sum_length, array[i].count)

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
m = int(input())
array = []
for i in range (n):
    a,b,c = map(int, input().split())
    array.append({a,b,c})

temps_min = 1001
count_temps = 0
for i in range (n):
    if temps_min > array[i][2]:
        temps_min = array[i][2]
        count_temps = 0
    else:
        count_temps +=1
print(count_temps)

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
class CanhKhuyen()
    def _init_(self):
        self.count = 0
        self.trongso = 1
    def update (self,a,b)
        self.count +=a
        self.trongso *= b
m = int(input())
flag = 0 
array = []
ans = CanhKhuyen()
for i in range (n):
    a,b,c = map(int, input().split())
    array.append({a,b,c})
for i in range (n):
    if array[i][0]==array[i][1]:
        flag = 1
        ans.update(1,array[i][0])
    elif array[i][0]==array[i][2]:
        flag = 1
        ans.update(1,array[i][0])
    elif array[i][1]==array[i][2]:
        flag =1
        ans.update(1,array[i][1])
if (0 == flag):
    print("-1")
else:
    print(ans.count, ans.trongso)
    
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
n = int(input())
count = 0
array = []
ans = []
for i in range (n):
    temp = list(map(int, input().split()))
    array.append(temp)

for i in range (n):
    for j in range (n):
        if (array[i][j]==1):
            count +=1
            ans.append({i,j})

print(count)
for i in range (count)
    print(ans[i][0], ans[i][1])

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    





    


