m1=[[1,2,3],[1,2,3],[1,2,3]]
m2=[[1,1,1],[1,1,1],[1,1,1]]
m3=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(m1)):
	for j in range(len(m2)):
		m3[i][j]=m1[i][j]*m2[i][j]
print(m3)
