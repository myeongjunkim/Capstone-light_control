from math import pow


r = 30
theta = 8*pow(10,-8)* (r**6) - pow(10,-5)* (r**5) + 0.0009* (r**4) - 0.0326* (r**2) - 8.684*r + 174.06

# y = 8E-08x6 - 1E-05x5 + 0.0009x4 - 0.0326x3 + 0.6443x2 - 8.684x + 174.06

print(theta)