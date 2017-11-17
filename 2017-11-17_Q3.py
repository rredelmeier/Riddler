import numpy as np
import matplotlib.pyplot as mpl

trials = np.zeros([10,1,100])
x =np.arange(100)

def skip(curr_val,tot_score,q):
    if tot_score>0:
        return True
    else:
        if curr_val > np.absolute(tot_score)+1:
            return True
        else:    
            return False

for trial_set in range(trials.shape[0]):
    for trial in range(trials.shape[1]):
        curr_val =1
        tot_score = 0

        for q in range(0,100):
            if skip(curr_val,tot_score,q):
                tot_score += 0
                curr_val = 1
            else:
                if np.random.randint(2):
                    tot_score += curr_val
                else:
                    tot_score -= curr_val
                curr_val += 1
            trials[trial_set][trial][q] = tot_score

mpl.plot(np.average(trials,axis=1).T,color="blue",alpha=0.25)
# print(np.average(trials,axis=1))
mpl.plot(np.average(np.average(trials,axis=1),axis=0),color='red')
mpl.plot(100,np.average(np.average(trials,axis=1),axis=0)[99],'ro',markersize=2.5,color="green",label='avg='+str(np.average(np.average(trials,axis=1),axis=0)[99]))
mpl.legend(loc='best')
mpl.show()