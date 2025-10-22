/*

Input: 567890

output: 
Total Number of Notes
500 = 1135
100 = 3
50 = 1
20 = 2
10 = 0
5 = 0
2 = 0
1 = 0
*/


def counting_notes(num , note):
    res = 1
    if num == 0:
        return 0,0
    if(num > note):
        res = int(num/note)
    return (num - res * note), res


num = int(input())
notes = [500, 100, 50, 20, 10, 5, 2, 1]

data = {}
def start(num, notes):
    for note in notes:
        value, count = counting_notes(num, note)
        data[note] = count
        num = value

start(num, notes)
print(data)





