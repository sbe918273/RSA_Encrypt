def PowerMod(b, e, N):

    """Gives (b^e) mod N.
    
        Arguements:
            b {integer} -- base
            e {integer} -- exponent
            N {integer} --  modulus
            
        Returns:
            c {integer}"""

    from math import log2

    num_bits = int(log2(e))+1
    bits = [(e >> bit) & 1 for bit in range(0, num_bits)]

    array = [b%N]

    for i in range(1, num_bits):
        
        array.append((array[i-1]**2)%N)
    
    total = 1

    for i in range(0, num_bits):

        if bits[i]:
            total *= array[i]

    return total%N

def findD(P1, P2, e):

    phiN = (P1-1)*(P2-1)
        
    k = 0
    while k != -1:

        d, mod = divmod(((k*phiN)+1),e)
    
        if mod == 0:
            k = -1

        else:
            k+= 1

    return d