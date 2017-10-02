import numpy as np
from scipy.special import comb, factorial
import matplotlib.pyplot as plt
plt.style.use('classic')

def single_arm_prob(l, n, phi):
    if n >= l:
        return comb(n-1, l-1) * phi**l * (1-phi)**(n-l)
    else:
        return 0


N = 50
phi = 0.3
prob_v = np.zeros(N-1)
prob_t = np.zeros(N-1)
for n in range(1, N):
    prob_v[n-1] = single_arm_prob(1, n, phi) * (single_arm_prob(1, n, phi) + 2 * sum([single_arm_prob(1, i, phi) for i in range(1, n)]))
    prob_t[n-1] = single_arm_prob(1, n, phi) * (single_arm_prob(1, n, phi) + 2 * sum([(1-phi)**(n-i) * single_arm_prob(1, i, phi) for i in range(1, n)])) + 2 * single_arm_prob(2, n, phi) * (1-phi)**n


plt.plot(prob_v, 'o-', label = 'v')
plt.plot(prob_t, 'o-', label = 't')
x = np.arange(1, N)
lamb = 4
#plt.plot(x, lamb**x/(np.e**lamb * factorial(x)))
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.show()
    


    
