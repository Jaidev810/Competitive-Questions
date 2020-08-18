def tickets(people):
    
    curr_balance = 0
    for i in range(0, len(people)):
        amt = people.pop(0)
        if amt == 25:
            curr_balance += 25
        elif amt == 50:
            if curr_balance >= 25:
                curr_balance -= 25
            else:
                return 'No'
        else:
            if curr_balance >= 75:
                curr_balance -= 75
            else:
                return 'No'
    return 'Yes'


ticket = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100 ]
print(tickets(ticket))