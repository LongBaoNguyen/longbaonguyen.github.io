from __future__ import division, print_function
from game import *

def dft(y):
    Y = []
    N = len(y)
    for k in range(N):
        sum = Complex(0, 0)
        for n in range(N):
            phi = (2* PI * k * n) / N
            e_phi = Complex(cos(phi), -sin(phi))
            sum.add(y[n].mult(e_phi))
        sum.real = sum.real 
        sum.im = sum.im 
        freq = k
        amp = sqrt(sum.real*sum.real + sum.im*sum.im)
        phase = atan2(sum.im, sum.real)
        yk = freq, amp, phase
        Y.append(yk)
    return Y    

def read_points(csv_filename):
    points = []
    lines = loadStrings(csv_filename)
    for i in range(0, len(lines)):
        values = split(lines[i], ",")
        pt = float(values[0]), float(values[1])
        points.append(pt)
    return points


class Complex(object):
    def __init__(self, a, b):
        self.real = a
        self.im = b
    def add(self, c):
        self.real += c.real
        self.im += c.im
    def mult(self, c):
        r = self.real * c.real - self.im * c.im;
        im = self.real * c.im + self.im * c.real;
        return Complex(r, im)
