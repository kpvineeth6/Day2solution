#day_2_problem-4

string="ssaamarrthyya"
p=""
for char in string:
    if char not in p:
        p=p+char
        p="".join(sorted(p))
print("string after removel of duplicate character=",p)     
