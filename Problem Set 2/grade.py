mark = int(input())
if mark >= 97 and mark <= 100:
    print("A+")
elif mark >= 90 and mark < 87:
    print("A")
elif mark >= 60 and mark < 70:
    print("A-")
elif mark >= 50 and mark < 60:
    print("B")
elif mark >= 40 and mark < 50:
    print("C")
elif mark >= 33 and mark < 40:
    print("D")
elif mark >= 0 and mark < 33:
    print("F")
