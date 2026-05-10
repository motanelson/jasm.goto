import time

def state5_change(state5):
    state5=state5+1
    if state5 >4:
        state5=0
    return state5     


print("\033c\033[40;37m\nemulator of a state5\n")
Qbit=0
for a in range (20):
     print(Qbit)
     Qbit=state5_change(Qbit)
     
