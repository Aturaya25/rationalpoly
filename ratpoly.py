from decimal import *
from fractions import *

class Poly(object):
    def __init__(self, c):
        self.c = c
    def add(self, other):
        rev_poly = []
        rev_self_coeffs = self.c[::-1]
        rev_other_coeffs = other.c[::-1]
        for n in range(len(rev_self_coeffs)):
            if n <= len(rev_other_coeffs) - 1:
                rev_poly.append(rev_self_coeffs[n] + rev_other_coeffs[n])
            else:
                rev_poly.append(rev_self_coeffs[n])
        if len(rev_other_coeffs) > len(rev_self_coeffs):
            for n in range(len(rev_self_coeffs), len(rev_other_coeffs)):
                rev_poly.append(rev_other_coeffs[n])
        new_poly = rev_poly[::-1]
        return Poly(new_poly)
    def __add__(self, other):
        return self.add(other)

    def __sub__(self, other):
        a, b = self.c, other.c
        if len(a) < len(b):
            for i in range(len(a),len(b)):
                a = [0]+a
        else:
            for i in range(len(b),len(b)):
                b = [0]+b
        for j in range(len(a)):
            a[j] -= b[j]
        return Poly(a)

    def mul(self, other):
        new_poly = Poly([0])
        rev_self_coeffs = self.c[::-1]
        rev_other_coeffs = other.c[::-1] 
        for n in range(len(rev_self_coeffs)):
            if n == 0:
                rev_poly_term = [r * rev_self_coeffs[n] for \
                r in rev_other_coeffs]
            else:
                rev_poly_term = [0 for m in range(n)] + \
                [r * rev_self_coeffs[n] for r in rev_other_coeffs]
            poly_term = rev_poly_term[::-1]
            new_poly = new_poly + Poly(poly_term)
        return new_poly
    def __mul__(self, other):
        return self.mul(other)

    def __truediv__(self, other):
            q=other.c
            p=self.c
            P = len(p)
            Q = len(q) - 1
            q1 = q[0]
            q = [q[i] / -q1 for i in range(1, Q + 1)]
            r = [0 for i in range(P)]
            a = [[0 for i in range(Q)] for i in range(P)]
            for i in range(P):
                p[i] /= q1
                r[i] = sum(a[i]) + p[i]
                for j in range(Q):
                    if i < P - Q: a[i + j + 1][Q - j - 1] = r[i] * q[j]
            return Poly(r[:P - Q])
def poly_i(s1):
    f = 0
    s2=""
    for i in range(len(s1)):
        if s1[i-1] == 'x':
            if i_p(s1[i]):
                s2 += str(c_p(s1[i]))
                j = 1
                while i_p(s1[i+j]) and j<=len(s1)-i:
                    s2+=str(c_p(s1[i+j]))
                    j+=1
            else:
                    s2+="1"
            s2 += " "
    spis=s2.split(" ")
    del spis[-1]
    if s1[-1].isdigit():
        spis.append(0)
    for i in range(len(spis)):
        spis[i]=int(spis[i])
    return spis

def i_p(s):
    superscript_map = {
     "⁰":"0","¹":"1", "²":"2", "³":"3", "⁴":"4",  "⁵":"5","⁶":"6",
    "⁷":"7","⁸":"8",  "⁹":"9"}
    if s in superscript_map:
        return True
    return False

def c_p(s):
    superscript_map = {
     "⁰":"0","¹":"1", "²":"2", "³":"3", "⁴":"4",  "⁵":"5","⁶":"6",
    "⁷":"7","⁸":"8",  "⁹":"9"}
    if s in superscript_map:
        return int(superscript_map.get(s))
    
def p_i_c(s1):
    spis=[]
    v_i = 0
    if s1[0]=="x":
        spis.append(Fraction(1))
    for i in range(1, len(s1)):
        s2 = ""
        if s1[i]=="x":
            if 1==0:
                j="-1"
            else:
                for j in range(v_i,i):
                    if s1[j]=="+" or s1[j]=="-" or j==0 or (i==1 and v_i==0):
                        while j<i:
                            s2+=s1[j]
                            j+=1
            v_i=i
            if s2 == '+':
                s2 = "1"
            if s2=='-':
                s2="-1"
            spis.append(Fraction(s2))
    s3=""
    for j in range(v_i, len(s1)):
        if s1[j] == "+" or s1[j] == "-":
            while j<len(s1) and (s1[j].isdigit() or s1[j]=="+" or s1[j]=="-" or s1[j]=="/"):
                s3+=s1[j]
                j+=1
    if s3 != 0:
        spis.append(Fraction(s3))

    return spis


a=input()
operat=input()
b=input()
if a.isdigit() and b.isdigit():
    if operat=="/":
        print(Fraction(a)/Fraction(b))
else:
    con_l1, con_l2 = list(),list()
    for pol in a,b:
        con_l1 = con_l2
        con_l2 = list()
        lc1 = p_i_c(pol)
        l1 = poly_i(pol)
        big = max (l1)
        small = min (l1)
        in1 = []
        for i in range(int(big)+1):
            flag = 0
            for j in range(len(l1)):
                if i == l1[j]:
                    flag = 1
                    in1.append(lc1[j])
            if flag == 0:
                in1.append(0)
        in1.reverse()
        con_l2=in1
    A = Poly(con_l1)
    B = Poly(con_l2)

    def cd_d(s):
        superscript_map = {
    "0": "⁰", "1": "¹", "2": "²", "3": "³", "4": "⁴", "5": "⁵", "6": "⁶",
    "7": "⁷", "8": "⁸", "9": "⁹"}
        a = ""
        if s=="1":
            return ""
        else:
            for i in range(0,len(s)):
                if s[i] in superscript_map:
                    a += superscript_map.get(s[i])
        return a


    def out1(s):
        a=""
        dl=0
        for i in range(len(s)):
            if s[i] == 0:
                dl+=1
            if dl == len(s):
                print(0)
                return
        for i in range(len(s)-1):
            if s[i]!=0:
                dl = len(s)-i-1
                dl = str(dl)
                if str(s[i])!="1" and str(s[i])!="-1":
                    a += str(s[i])+"x"+cd_d(dl)
                if str(s[i])=="1" and a!="":
                    a += "+x"+cd_d(dl)
                if str(s[i])=="1" and a=="":
                    a += "x" + cd_d(dl)
                if str(s[i])=="-1":
                    a += "-x"+cd_d(dl)
                if s[i+1]>0:
                    a+="+"
        if s[-1]==1:
            a+="+1"
        else:
            if s[-1]>0:
                a+=str(s[-1])
            if s[-1]<0:
                a+=str(s[-1])
        print(a)


    def out2(s):
        a = ""
        dl = 0
        for i in range(len(s)):
            if s[i] == 0:
                dl += 1
            if dl == len(s):
                return "0"
        for i in range(len(s) - 1):
            if s[i] != 0:
                dl = len(s) - i - 1
                dl = str(dl)
                if str(s[i]) != "1" and str(s[i]) != "-1":
                    a += str(s[i]) + "x" + cd_d(dl)
                if str(s[i]) == "1" and i != 1:
                    a += "+x" + cd_d(dl)
                if str(s[i]) == "1" and i == 1:
                    a += "x" + cd_d(dl)
                if str(s[i]) == "-1":
                    a += "-x" + cd_d(dl)
                if s[i + 1] > 0:
                    a += "+"
        if s[-1] > 0:
            a += str(s[-1])
        if s[-1] < 0:
            a += str(s[-1])
        return str(a)


    if operat == "+":
            out1((A + B).c)
    if operat == "-":
            out1((A - B).c)
    if operat == "/":
            out1((A / B).c)
    if operat == "*":
            out1((A * B).c)
    if operat == "%":
            a_old = a
            a = out2((A / B).c)
            for pol in a,b:
                con_l1 = con_l2
                con_l2 = list()
                lc1 = p_i_c(pol)
                l1 = poly_i(pol)
                big = max (l1)
                small = min (l1)
                in1 = []
                for i in range(int(big)+1):
                    flag = 0
                    for j in range(len(l1)):
                        if i == l1[j]:
                            flag = 1
                            in1.append(lc1[j])
                    if flag == 0:
                        in1.append(0)
                in1.reverse()
                con_l2=in1
            A = Poly(con_l1)
            B = Poly(con_l2)

            a=out2((A * B).c)
            b=a_old
            a,b=b,a

            for pol in a,b:
                con_l1 = con_l2
                con_l2 = list()
                lc1 = p_i_c(pol)
                l1 = poly_i(pol)
                big = max (l1)
                small = min (l1)
                in1 = []
                for i in range(int(big)+1):
                    flag = 0
                    for j in range(len(l1)):
                        if i == l1[j]:
                            flag = 1
                            in1.append(lc1[j])
                    if flag == 0:
                        in1.append(0)
                in1.reverse()
                con_l2=in1
            A = Poly(con_l1)
            B = Poly(con_l2)
            out1((A - B).c)
