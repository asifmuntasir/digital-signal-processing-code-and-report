import numpy as np
import matplotlib.pyplot as plt


def downSampling(initialSample, T):
    n, x_n = initialSample
    assert (T > 0 & T <= n[len(n) - 1]), "T can't be grater than signal range";
    lw = n[0]
    up = n[len(n) - 1]
    c = -1 * n[0]
    y = np.zeros(n.shape[0])
    for i in range(c, len(x_n)):
        if(n[i] == 0):
            y[i] = x_n[i]
        else:
            if(n[i]*T <= up):
                y[i] = x_n[i + (n[i] * T - n[i])]
            else:
                y[i] = 0
    for i in range(c-1, -1, -1):
        if(n[i] * T >= lw):
            y[i] = x_n[i + (n[i] * T - n[i])]
        else:
            y[i] = 0
             
    return (n, y)



def mirroring(initialValue, lb, ub):
    n, x_n = initialValue
    assert (0 in n), "There is no Zero sample";
    x_n = np.flipud(x_n)
#    print(x_n)
    
    n = np.arange(-ub, -lb+1, 1)
    
    return (n, x_n)
    



def timeShifting(originalSignal, shiftingAmount):
    n, x_n = originalSignal
    
    y_n = np.zeros(n.shape[0])
    #print(y_n)
    
    #Main logic
    if shiftingAmount > 0:
        if shiftingAmount > n.shape[0]:
            shiftingAmount = n.shape[0]
        deltaToCopy = x_n[0 : n.shape[0] - shiftingAmount]
        y_n[shiftingAmount : ] = deltaToCopy
    elif shiftingAmount < 0:
        if abs(shiftingAmount) > n.shape[0]:
            shiftingAmount = n.shape[0] * -1
        deltaToCopy = x_n[ -shiftingAmount : ]
        y_n[ : n.shape[0] + shiftingAmount] = deltaToCopy
    else:
        y_n = x_n
        
    return(n, y_n)
        


def unitRamp(lbound, ubound):
    assert (lbound <= ubound), "Lower bound can't be greater than upper bound";

    #Taking the samples range
    n = np.arange(lbound, ubound+1, 1)
    print("Here the input ramp signal range: ")
    print(n)
    #Taking x[n] values
    x_n = []
    for i in n:
        if i >= 0:
            x_n.append(i)
        else:
            x_n.append(0)
    x_n = np.array(x_n)
    print("\nThe output ramp signal is given below: ")
    print(x_n)
    delta = (n, x_n)
    
    #Draw figure before shifting
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.title('Unit Ramp $u_r[n]$')
    ax.stem(n, x_n)
    
    #Second input
    again = int(input("Enter Operation Type: "))
    if again == 1:
        #Time Shifting
        sample = int(input("Enter amount: "))
        shiftedOutput = timeShifting(delta, sample)
#        print(shiftedOutput[0], shiftedOutput[1])
        fig = plt.figure()
        ax = fig.add_subplot(111)
        plt.title('After Shifting Unit Ramp $u_r[n]$')
        ax.stem(shiftedOutput[0], shiftedOutput[1])
    elif again == 2:
        #Mirroring
        mirrorOutput = mirroring(delta, lbound, ubound)
#        print(mirrorOutput)
        fig = plt.figure()
        ax = fig.add_subplot(111)
        plt.title('Mirroring $x[-n]$')
        ax.stem(mirrorOutput[0], mirrorOutput[1])
    elif again ==3:
        #Downsampling
        sample = int(input("Enter amount: "))
        downSamplingOutput = downSampling(delta, sample)
#        print(downSamplingOutput[0], downSamplingOutput[1])
        fig = plt.figure()
        ax = fig.add_subplot(111)
        plt.title('Downsampling $x[nT]$')
        ax.stem(downSamplingOutput[0], downSamplingOutput[1])
    



def unitStep(lbound, ubound):
    assert (lbound <= ubound), "Lower bound can't be greater than upper bound";

    #Taking the samples range
    n = np.arange(lbound, ubound+1, 1)
    print("Here the input step signal range: ")   
    print(n)
    #Taking x[n] values
    x_n = []
    for i in n:
        if i >= 0:
            x_n.append(1)
        else:
            x_n.append(0)
    x_n = np.array(x_n)
    print("\nThe output step signal is given below: ")
    print(x_n)
    delta = (n, x_n)
    
    #Draw figure before shifting
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.title('Unit Step $u[n]$')
    ax.stem(n, x_n)
    
    #Second input
    again = int(input("Enter Operation Type: "))
    if again == 1:
        #Time Shifting
        sample = int(input("Enter amount: "))
        shiftedOutput = timeShifting(delta, sample)
#        print(shiftedOutput[0], shiftedOutput[1])
        fig = plt.figure()
        ax = fig.add_subplot(111)
        plt.title('After Shifting Unit Step $u[n]$')
        ax.stem(shiftedOutput[0], shiftedOutput[1])
    elif again == 2:
        #Mirroring
        mirrorOutput = mirroring(delta, lbound, ubound)
#        print(mirrorOutput)
        fig = plt.figure()
        ax = fig.add_subplot(111)
        plt.title('Mirroring $x[-n]$')
        ax.stem(mirrorOutput[0], mirrorOutput[1])
    elif again ==3:
        #Downsampling
        sample = int(input("Enter amount: "))
        downSamplingOutput = downSampling(delta, sample)
#        print(downSamplingOutput[0], downSamplingOutput[1])
        fig = plt.figure()
        ax = fig.add_subplot(111)
        plt.title('Downsampling $x[nT]$')
        ax.stem(downSamplingOutput[0], downSamplingOutput[1])
    




def unitImpulse(lbound, ubound):
    assert (lbound <= ubound), "Lower bound can't be greater than upper bound";
    
    #Taking the samples range
    n = np.arange(lbound, ubound+1, 1)
    print("Here the input impulse signal range: ")
    print(n)
    #Taking x[n] values
    x_n = []
    for i in n:
        if i<0:
            x_n.append(0)
        elif i>0:
            x_n.append(0)
        else:
            x_n.append(1)
    x_n = np.array(x_n)
    print("\nThe output impulse signal is given below: ")
    print(x_n)
    delta = (n, x_n)
    
    #Draw figure before shifting
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.title('Unit Impulse $\delta[n]$')
    ax.stem(n, x_n)
    
    #Second input
    again = int(input("Enter Operation Type: "))
    if again == 1:
        #Time Shifting
        sample = int(input("Enter amount: "))
        shiftedOutput = timeShifting(delta, sample)
#        print(shiftedOutput[0], shiftedOutput[1])
        fig = plt.figure()
        ax = fig.add_subplot(111)
        plt.title('After Shifting delta $\delta[n]$')
        ax.stem(shiftedOutput[0], shiftedOutput[1])
    elif again == 2:
        #Mirroring
        mirrorOutput = mirroring(delta, lbound, ubound)
#        print(mirrorOutput)
        fig = plt.figure()
        ax = fig.add_subplot(111)
        plt.title('Mirroring $x[-n]$')
        ax.stem(mirrorOutput[0], mirrorOutput[1])
    elif again ==3:
        #Downsampling
        sample = int(input("Enter amount: "))
        downSamplingOutput = downSampling(delta, sample)
#        print(downSamplingOutput[0], downSamplingOutput[1])
        fig = plt.figure()
        ax = fig.add_subplot(111)
        plt.title('Downsampling $x[nT]$')
        ax.stem(downSamplingOutput[0], downSamplingOutput[1])




if __name__ == "__main__":
    input_value = int(input("Enter signal type: "))        
    if input_value == 1:
        unitImpulse(-1, 5)
    elif input_value == 2:
        unitStep(-3, 4)
    elif input_value == 3:
        unitRamp(-10, 5)
    
    
    