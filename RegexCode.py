import sys 
N=int(raw_input())
word=[]
for i in range(1,N+1):
    words =raw_input()
    words = words.replace(' ','  ')
    words = words.replace(' && ', ' and ')
    words = words.replace(' || ',' or ') 
    words = words.replace('  ',' ') 
    print(words)
