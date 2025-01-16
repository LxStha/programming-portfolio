"""4.A kindly teacher wishes to distribute a tub of sweets between her pupils. She will
first count the sweets and then divide them according to how many pupils attend
that day. Write a program that will tell the teacher how many sweets to give to each
pupil, and how many she will have le over."""

num_student=int(input("number of student:"))
num_sweets=int(input("number of sweets:"))

give=num_sweets//num_student
left=num_student%num_sweets

g1="sweet"
if give>1:
    g1="sweets"

g2="student"
if left>1:
    g2="students"

print(f"sweet per {g2} {give}, amount of {g1} left {left}")