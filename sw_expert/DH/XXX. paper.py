"""
pseudo
while sum <= N && S//D != 1:
    1step = S
    2step = 1step + (1step//D) = S + S//D
    3step = 2step + ((2step-1step)//D) = S + S//D + ((S//D) // D))
    4step = 3step + ((3step-2step)//D) = S + S//D + ((S//D) // D)) + ((S//D) // D) // D

    nstep = n-1step + ((n-1step - n-2step)//D)
    
    
    4인경우
    1step
        temp = 4
        diff = 0
        result = 4+ (4-0)//2 = 6
        diff = 2
        
    2step
        temp = 6
        diff = 2
        result = 6 + (2)//D
"""

def find_S(N:int, D:int)->int:
    for S in range(D+1, N-1):
        result = S
        diff = S

        while result <= N:
            temp = result
            result += (diff // D)
            diff = result - temp

            if diff == 0:
                break

        if result >= N:
            return S
    

print(find_S(N=43, D=5))