import scipy.integrate as spi
import numpy as np

def SEIISR_base_eqs(INPUT, t, beta, sigma, epsilon, _lambda_, gamma):
    Y = np.zeros((5))
    #_lambda_ = np.exp((_lambda_ * (t - 6)))
    #_lambda = (_lambda_ / (1 + _lambda_))
    #print(_lambda_)
    beta = max(beta, 0)
    sigma = max(sigma, 0)
    epsilon = max(epsilon, 0)
    _lambda_ = max(_lambda_, 0)
    gamma = max(gamma, 0)
    Y[0] = - (beta * INPUT[0] * INPUT[2]) - (sigma * INPUT[0] * INPUT[1])
    Y[1] = (beta * INPUT[0] * INPUT[2]) + (sigma * INPUT[0] * INPUT[1])  - (epsilon * INPUT[1])
    Y[2] = ((1 - _lambda_) * (epsilon * INPUT[1])) - (gamma * INPUT[2])
    Y[3] = (_lambda_ * epsilon * INPUT[1]) - (gamma * INPUT[3])
    Y[4] = (gamma * INPUT[2]) + (gamma * INPUT[3])

    return Y

def SEIISR_v_base_eqs(INPUT, t, beta, sigma, pho, epsilon, _lambda_, gamma):
    Y = np.zeros((5))
    beta = max(beta, 0)
    sigma = max(sigma, 0)
    pho = max(pho, 0)
    epsilon = max(epsilon, 0)
    _lambda_ = max(_lambda_, 0)
    _lambda_ = min(_lambda_, 1)
    gamma = max(gamma, 0)
    S = INPUT[0]
    E = INPUT[1]
    I = INPUT[2]
    IS = INPUT[3]
    R = INPUT[4]
    Y[0] = - (beta * S * I) - (sigma * S * max((E - (pho * IS)), 0.005*E))
    Y[1] = (beta * S * I) + (sigma * S * max((E - (pho * IS)), 0.005*E)) - (epsilon * E)
    Y[2] = ((1 - _lambda_) * (epsilon * E)) - (gamma * I)
    Y[3] = (_lambda_ * (epsilon * E)) - (gamma * IS)
    Y[4] = (gamma * (I + IS))

    return Y
