import numpy as np

def output_selection(v):    # y = w * x + b > 0 ---> 1 and w * x + b <= 0 ---> 0
    if v > 0:
        return 1
    else:
        return 0
  
def perceptron_formula(x, w, b):   
    v = np.dot(w, x) + b      #y = w * x + b
    y = output_selection(v)   #choose answer
    return y
  

def NOT_gate(x):
    wNOT = -1 #weight value
    bNOT = 1  #bias value
    return perceptron_formula(x, wNOT, bNOT)
  

def AND_gate(x):
    wAND = np.array([1, 1])  #weight values ---> [x1,x2]
    bAND = -1 #bias value
    return perceptron_formula(x, wAND, bAND)
  

def OR_gate(x):
    wOR = np.array([3, 2])  #weight values ---> [x1,x2]
    bOR = -1 #bias value
    return perceptron_formula(x, wOR, bOR)
  

def XOR_gate(x):
    
    w = np.array([-2, -2])  #weight values ---> [x1,x2]
    bNOR = 1  #bias value
    return perceptron_formula(x, w, bNOR)
 
#test values    
entries1 = np.array([0, 1])  
entries2 = np.array([1, 1])
entries3 = np.array([0, 0])
entries4 = np.array([1, 0])

#test values for NOT_gate 
entries_not1 = 1
entries_not2 = 0

#show console
print("NOT[{}] = {}        AND[{}, {}] = {}        OR[{}, {}] = {}        XOR[{}, {}] = {}".format(1, NOT_gate(entries_not1),0, 1,AND_gate(entries1),0,
                                                                                                   1, OR_gate(entries1),0, 1, XOR_gate(entries1)))
print("NOT[{}] = {}        AND[{}, {}] = {}        OR[{}, {}] = {}        XOR[{}, {}] = {}".format(0, NOT_gate(entries_not2),1, 1,AND_gate(entries2),1,
                                                                                                   1, OR_gate(entries2),1, 1, XOR_gate(entries2)))
print("                  AND[{}, {}] = {}        OR[{}, {}] = {}        XOR[{}, {}] = {}".format(0, 0, AND_gate(entries3),0, 0,
                                                                                                 OR_gate(entries3),0, 0, XOR_gate(entries3)))
print("                  AND[{}, {}] = {}        OR[{}, {}] = {}        XOR[{}, {}] = {}".format(1, 0, AND_gate(entries4),1, 0,
                                                                                                 OR_gate(entries4),1, 0, XOR_gate(entries4)))