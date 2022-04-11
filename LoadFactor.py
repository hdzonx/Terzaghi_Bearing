
import math as mt


class LoadFactor():

    ''' Load  capacity factor according to Vesic'''

    def __init__(self, phi):
        # phi: angle of friction
        self.phi = phi*mt.pi/180  # transform radian to degree

    # load factor for effective stress load
    def Nq(self):
        e = mt.exp(1)
        pi = mt.pi
        return e**(pi*mt.tan(self.phi))*(mt.tan(pi/4+self.phi/2))**2

    # load factor for cohesion
    def Nc(self):
        e = mt.exp(1)
        pi = mt.pi
        return 1/mt.tan(self.phi)*(e**(pi*mt.tan(self.phi))*(mt.tan(pi/4+self.phi/2))**2-1)

    # load factor for specific weight
    def Ns(self):
        e = mt.exp(1)
        pi = mt.pi
        return 2*(e**(pi*mt.tan(self.phi))*(mt.tan(pi/4+self.phi/2))**2+1)*mt.tan(self.phi)


if __name__ == "__main__":
    n = LoadFactor(20)

    print("Nq = " + str(n.Nq()))
    print("Nc = " + str(n.Nc()))
    print("Ns = " + str(n.Ns()))
