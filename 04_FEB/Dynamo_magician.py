"""
The problem statement is updated at README
"""

def magic_show(n, entry, exit):
    time = []
    for i in range(n):
        time.append([entry[i], exit[i]])

    
    time.sort()
    
    show = 0
    last_end = 0

    for i in range(n):
        start = time[i][0]
        end = time[i][1]

        if start > last_end:  
            show += 1
            last_end = end 
    
    return show


t = int(input("Enter the number of test cases: "))
for _ in range(t):
    n = int(input("\nEnter the number of students: "))

   
    entry = []
    entry_times = input("Enter entry time ").split()
    for i in range(n):
        entry.append(int(entry_times[i]))

    
    exit = []
    exit_times = input("Enter exit time ").split()
    for i in range(n):
        exit.append(int(exit_times[i]))

   
    min_shows = magic_show(n, entry, exit)
    
    
    print(min_shows)

