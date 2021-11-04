class RSAObject:

    def __init__(self, P1, P2, e):

        self.N = P1 * P2
        phiN = (P1-1)*(P2-1)
        self.e = e
        
        k = 0
        x = True
        while x:

            self.d, mod = divmod(((k*phiN)+1),self.e)
    
            if mod == 0:
                x = False

            else:
                k+= 1

        self.privateKey = "d: %d, phi(N): %d, k: %d" %(self.d, phiN, k)
        self.publicKey = "N: %d, e: %d" %(self.N, self.e)

    def PowerMod(self, b, e, N):

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


    def encrypt(self, M):

        """Encrypts a message M."""

        if type(M) == str:
            return "\0".join([str(self.encrypt(ord(i))) for i in M])

        else:
            if M >= self.N:
                raise ValueError("N must be greater than M")

            return self.PowerMod(M,self.e,self.N)

    def decrypt(self, c):

        """Decrypts an encrypted message c."""

        if type(c) == str:

            return "".join([chr(self.decrypt(int(i))) for i in c.split("\0")])
        
        else:

            return self.PowerMod(c,self.d,self.N)