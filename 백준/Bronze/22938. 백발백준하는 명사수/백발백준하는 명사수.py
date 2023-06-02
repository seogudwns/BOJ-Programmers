a,b,c = map(int,input().split())
x,y,z = map(int,input().split())
print('NO' if (c+z)**2 <= (x-a)**2+(y-b)**2 else 'YES')