n=int(input())
assert 2<=n<=10
student_score={}
for i in range (0,n):
    name,*line=input().split()
    score=list(map(float,line))
    for i in score:
        assert i<=100,"enter the mark within 100"
    student_score[name]=score
query_name=input()
que_scor=student_score[query_name]
print ("{0:.2f}".format(sum(que_scor)/len(line)))
