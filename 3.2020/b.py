def GetNumberOfThrees(right, down):
    with open("route.txt", "r") as file:
        threes = 0
        position_in_row = 0
        rows = file.readlines()
        for i in range(len(rows)):
            if i % down == 0:
                line = rows[i].rstrip()
                if position_in_row > 30:
                    position_in_row = position_in_row - 31
                if line[position_in_row] == "#":
                    threes += 1
                position_in_row += right
    return threes


answer = 1
print(f"1,1 {GetNumberOfThrees(1, 1)}")
answer *= GetNumberOfThrees(1, 1)
print(f"3,1 {GetNumberOfThrees(3, 1)}")
answer *= GetNumberOfThrees(3, 1)
print(f"5,1 {GetNumberOfThrees(5, 1)}")
answer *= GetNumberOfThrees(5, 1)
print(f"7,1 {GetNumberOfThrees(7, 1)}")
answer *= GetNumberOfThrees(7, 1)
print(f"1,2 {GetNumberOfThrees(1, 2)}")
answer *= GetNumberOfThrees(1, 2)
print(answer)