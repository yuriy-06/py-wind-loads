def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def isfloatm(m):
    try:
        for i in m:
            if isfloat(i) == True:
                pass
            else:
                return "False float array"
    except ValueError:
        return "False input in isfloatm"
    return True

class Interpolation():
    def index(self, m, p):
        if p <= m[0]:
            return m[0]
        prev=m[0]
        for i in m:
            if p < i:
                return prev
            else:
                prev = i
        return "Error out of range index"

    def indexes(self, m, p):
        m_v=[]
        ind = self.index(m,p)
        i = m.index(ind)
        m_v.append(ind)
        m_v.append(m[i+1])
        return m_v

    def interpret1d(self, y_massive, xm, xp):
        l = len(xm)
        for i in range(l - 1):
            x1 = xm[i]
            x2 = xm[i + 1]
            if (x1 <= xp < x2):
                y1 = y_massive[i]
                y2 = y_massive[i + 1]
                k = (y2 - y1) / (x2 - x1) * (xp - x1) + y1
                return k
class Wind(Interpolation):
    def __init__(self, wind_load=0.038, wind_type='a'):
        self.wind_load = wind_load
        self.wind_type = wind_type
        self.z_m =  [0, 5, 10, 20, 40, 60, 80, 100, 150, 200, 250, 300, 350, 480]
        self.m_test_veter_k = [  # тестовый набор данных

            ["a", [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
             [0.75, 0.8, 0.85, 0.9, 0.95, 1.0, 1.02, 1.05, 1.08, 1.1, 1.12, 1.15, 1.17, 1.2, 1.22, 1.25, 1.26, 1.28,
              1.29, 1.3, 1.31, 1.32, 1.34, 1.35, 1.36, 1.38]],

            ["b", [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
             [0.5, 0.53, 0.56, 0.59, 0.62, 0.65, 0.67, 0.69, 0.71, 0.73, 0.75, 0.77, 0.79, 0.81, 0.83, 0.85, 0.86,
              0.88, 0.89, 0.9, 0.91, 0.92, 0.94, 0.95, 0.96, 0.98]],

            ["c", [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
             [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.42, 0.43, 0.44, 0.46, 0.48, 0.49, 0.5, 0.52, 0.54, 0.55, 0.56, 0.58, 0.59,
              0.6, 0.61, 0.62, 0.64, 0.65, 0.66, 0.68]],
        ]
        self.v1 = self.wind_type

    def wind_k(self, z):
        a = [0.75, 0.75, 1.0, 1.25, 1.5, 1.7, 1.85, 2.0, 2.25, 2.45, 2.65, 2.75, 2.75, 2.75]
        b = [0.5, 0.5, 0.65, 0.85, 1.1, 1.3, 1.45, 1.6, 1.9, 2.1, 2.3, 2.5, 2.75, 2.75]
        c = [0.4, 0.4, 0.4, 0.55, 0.8, 1.0, 1.15, 1.25, 1.55, 1.8, 2.0, 2.2, 2.35, 2.75]
        if self.wind_type == 'a':
            k = self.interpret1d(a, self.z_m, z)
        if self.wind_type == 'b':
            k = self.interpret1d(b, self.z_m, z)
        if self.wind_type == 'c':
            k = self.interpret1d(c, self.z_m, z)

    def scat2(self, b, h, beta=15, alpfa=0): # альфа може принимать значения 0 и 90
        val_return = ""
        if (alpfa == 0) or (alpfa == 90):
            pass
        else:
            return "Error alfa value"
        if (0.0 > beta > 75.0):
            return "Error beta value"
        if alpfa == 0:
            beta_hash = {15:{"f":[-0.9,0.2],"g":[-0.8,0.2],"h":[-0.3,0.2],"i":[-0.4],"j":[-1.0]},
                        30:{"f":[-0.5,0.7],"g":[-0.5,0.7],"h":[-0.2,0.4],"i":[-0.4],"j":[-0.5]},
                         45:{"f":[0.7], "g":[0.7],"h":[0.6],"i":[-0.2],"j":[-0.3]},
                         60:{"f":[0.7], "g":[0.7],"h":[0.7],"i":[-0.2],"j":[-0.3]},
                         75:{"f":[0.8], "g":[0.8],"h":[0.8],"i":[-0.2],"j":[-0.3]}}
            if beta < 15:
                beta = 15
        if alpfa == 90:
            beta_hash = {
                0:{"f":[-1.8],"g":[-1.3],"h":[-0.7],"i":[-0.5]},
                15:{"f":[-1.3],"g":[-1.3],"h":[-0.6],"i":[-0.5]},
                30:{"f":[-1.1],"g":[-1.4],"h":[-0.8],"i":[-0.5]},
                45:{"f":[-1.1],"g":[-1.4],"h":[-0.9],"i":[-0.5]},
                60:{"f":[-1.1],"g":[-1.2],"h":[-0.8],"i":[-0.5]},
                75:{"f":[-1.1],"g":[-1.2],"h":[-0.8],"i":[-0.5]}
            }
        e=min(b,2*h)
        indexList_beta_hash = sorted(beta_hash.keys())
        indexes_beta = self.indexes(indexList_beta_hash, beta)
        if isfloatm(indexes_beta):
            pass
        else:
            return indexes_beta
        m1 = beta_hash[indexes_beta[0]]
        m2 = beta_hash[indexes_beta[1]]
        indexList_beta_hash = sorted(m1.keys())
        for i in indexList_beta_hash:
            pass
            mv1 = m1[i]; mv2 = m2[i]
            if len(mv1) == 2:
                j=0
                val_return += "зона " + i + '\n'
                for i1 in mv1:
                    i2=mv2[j]
                    #print (i1, i2)
                    val_return += str(round(self.interpret1d([i1,i2],indexes_beta,beta),3)) + '\n'
                    j=j+1
            else:
                val_return += "зона "+i + '\n'
                val_return += str(round(self.interpret1d([mv1[0], mv2[0]], indexes_beta, beta),3)) + '\n'
        print (val_return)
        return val_return

    def test(self):
        # использование ввиде
        # w = wind(wind_load = 0.038, wind_type = 'b')
        # w.test()
        # print (w.wind_type)
        for item in self.m_test_veter_k:
            self.wind_type = item[0]
            i = 0
            for j in item[1]:
                k = round(self.wind_k(j), 2)
                if k == item[2][i]:
                    pass
                    i += 1
                else:
                    print ("wind_type = ", self.wind_type, "; value = ", k, "; test value = ", item[2][i])
                    i += 1
                    # break
        self.wind_type = self.v1

#w = Wind(wind_load=0.038, wind_type='a')
#w.scat2(h=10, b = 33, beta=14.5, alpfa = 0)
