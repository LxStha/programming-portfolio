"""3.The Head of Computing at the University of Poppleton is tasked with dividing a
group of students into lab groups. A lab group is usually 24 students, but this is
sometimes varied to create groups of similar size. Write a program that prompts for
the number of students and group size, and then displays how many groups will be
needed and how many will be le over in a smaller group.
How many students? 113
Required group size? 22
There will be 5 groups with 3 students left over.
For bonus credit, see if you can fix the grammar in the output. So if there were 101
students in groups of 20 the output would be:
There will be 5 groups with 1 student left over."""

student=int(input("enter student number: "))
group=int(input("how many groups are there: "))
group_g="group"
castout_g="student"

group_num=student//group
castout=student%group

g1="group"
if group_num>1:
    g1="groups"

g2="student"
if castout>1:
    g2="students"
    
print(f"There will be {group_num} {g1} with  {castout} {g2} left over.")