import math
import pylab
import stereoplot
#stereoplot.stereoplot(10,20,'test1')
stereoplot.stereoplot([13,49],[43,-35],'test2')
pylab.show()
'''

Created on Sep 6, 2012

@author: payne
'''
'''
import pylab
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(2,1,1) # two rows, one column, first plot
fig2 = plt.figure()
ax2 = fig2.add_axes([0.15, 0.1, 0.7, 0.3])
import numpy as np
t = np.arange(0.0, 1.0, 0.01)
s = np.sin(2*np.pi*t)
line, = ax.plot(t, s, color='blue', lw=2)
plt.show()
'''
'''
x=[1,2,3,4]
y=[1,4,9,16]
pylab.plot(x,y,"-o",label="lines")
pylab.legend()
fig= pylab.Figure
ax =fig.add_axes(fig,[0,5,0,20])

pylab.show()
'''
'''
import pylab

print pylab.arange(2,88,2)
negew=[1,-1,1,-1,1,-1,10,11,12,13,14]
negew=[4,4,3,2]
negud=[-4,-4,-3,-2]
ns=[1,2,0,-1]#5,6,7,8,9,10,11]
N = 10
import numpy as np
data = np.random.random((N, 4))
labels = ['point{0}'.format(foo) for foo in range(N)]
pylab.subplots_adjust(bottom = 0.1)
pylab.plot(ns, negew, marker = 'o')+pylab.plot(ns, negud, marker = 'o')
for label, x, y in zip(labels, ns, negew ):
    pylab.annotate(
        label, 
        xy = (x, y), xytext = (-20, 20),
        textcoords = 'offset points', ha = 'right', va = 'bottom',
        arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0'))
for label, x, y in zip(labels, ns, negud ):
    pylab.annotate(
        label, 
        xy = (x, y), xytext = (-20, 20),
        textcoords = 'offset points', ha = 'right', va = 'bottom',
        arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0'))

pylab.show(block=False)
negew=[1.2259766407818162, 1.1370900589272206, 0.9377491263522607, 0.6974770661387347, 0.4949346678616318, 0.18482748244204097, 0.08412013577913964, 0.014285566726604861, 0.015027271622509475, 0.0077157364450102526, 0.007534446599830147, 0.0053101929762941445, 0.0007995264948141197, -0.0025220000585275525, -0.007860859095280432]
negud=[1.2259766407818162, 1.1370900589272206, 0.9377491263522607, 0.6974770661387347, 0.4949346678616318, 0.18482748244204097, 0.08412013577913964, 0.014285566726604861, 0.015027271622509475, 0.0077157364450102526, 0.007534446599830147, 0.0053101929762941445, 0.0007995264948141197, -0.0025220000585275525, -0.007860859095280432]

negew=[0.10859605546358207, 0.09961901396057328, 0.06788700024778274, 0.013326657555509689, -0.048598042156094194, -0.21343186928699992, -0.26667025604517197, -0.23005788454543655, -0.20600375999343054, -0.17374627221673172, -0.13885890956167532, -0.11410182765956084, -0.09824376411477286, -0.08517431408995431, -0.08042392754512313]
negud=[0.10859605546358207, 0.09961901396057328, 0.06788700024778274, 0.013326657555509689, -0.048598042156094194, -0.21343186928699992, -0.26667025604517197, -0.23005788454543655, -0.20600375999343054, -0.17374627221673172, -0.13885890956167532, -0.11410182765956084, -0.09824376411477286, -0.08517431408995431, -0.08042392754512313]

ns=[0.19417562410118283, -0.05959236483319864, -0.25126912110907895, -0.31053679718980365, -0.2521818091125739, -0.016170309421715365, 0.07574211046242067, 0.11634660434141726, 0.09487845896805233, 0.08819127112078892, 0.06136314325209212, 0.050523111298715465, 0.04580484221067637, 0.03606628113641048, 0.03152818378056259]

thetalistew = [] #will hold slopes
thetalistud = []
#gets slopes of one ns/ew line
for n in range(1, len(ns)):
    m=math.atan2((negew[n]-negew[n-1]),(ns[n]-ns[n-1]) )        
    thetalistew.append(m)
for n in range(1, len(ns)):
    m=math.atan2((negud[n]-negud[n-1]),(ns[n]-ns[n-1]))         
    thetalistud.append(m)    

listewcoercpicks=[] #holds the coercivity picks
listudcoercpicks=[]
n=0       
lng = len(thetalistew)   
ewc = [] #These are lists of lists
udc = []
print 'There are '+str(lng)+' slope segments steps for this core'
print 'Enter the number of the segments you want to use'
lng = input()

print 'Enter a coerceivity pick sensitivity factor.'
print 'This selects all slopes of lines within 1/x slope2 < slope1< x* slope2'
print '2 is a good choice'
maxangle = input()
maxangler= math.radians(maxangle)
print thetalistew 
for n in range(0,len(thetalistew)):
    print math.degrees(math.atan(thetalistew[n]))

for n in range(0,lng):#basically, compares the slopes of the lines to see if they are similar. Puts a 1 if similar and 0 if not 
    cp=[]
    cp2=[]
    for m in range(0, lng):
        if thetalistew[n]-maxangler< thetalistew[m] <maxangler+thetalistew[n]:
            cp.append(1)  
        else: 
            cp.append(0)
    for m in range(0, lng):
        if thetalistud[n]-maxangler< thetalistud[m]<maxangler+thetalistud[n]:
            cp2.append(1)  
        else: 
            cp2.append(0)              
    ewc.append(cp) #appends the cp (and cp2) lists to another list, making a list of list of slopes
    udc.append(cp2)
udcsum =0
ewcsum = 0

for n in range(0,len(udc[-1])): #counts the number of 1's in each of the coercivity pick lists
    udcsum=udcsum+udc[-1][n]
    ewcsum=ewcsum+ewc[-1][n]
hcoproto=[]
if udcsum>ewcsum: #this if/else picks determines if the ew or ud coercivity pick is better by picking the one with the least 1s in it
    hcoproto=ewc[-1]
else:
    hcoproto=udc[-1]
hcoproto.reverse() #flips the list order
hcoercepicks=[1] #This makes the last pick always part of the high coercivity component.


for n in range(0,len(hcoproto)): #This fills the list properly, with 0s and then 1s for the high coercivity part
    if hcoproto[n]==1: # just keeps adding 1's until there are none left in hcoproto
        hcoercepicks.append(1)
    else: #fills in the rest with 0s
        foo=[0]*(len(hcoproto)-n)
        for j in range(0,len(foo)):
            hcoercepicks.append(foo[j])
        break    

hcoercepicks.reverse()
print thetalistew
print thetalistud
#print ewc
print hcoercepicks
#Creates a graph of the high coercivity park based on the hcoercepicks list, same as above
nshcoerce = []
negewhcoerce = []
negudhcoerce = []
n=0
for n in range(0,len(hcoercepicks)):
    if hcoercepicks[n] == 1:
        nshcoerce.append(ns[n])
        negewhcoerce.append(negew[n])
        negudhcoerce.append(negud[n])
zfhcp = pylab.figure()    
zfhcp = pylab.plot(nshcoerce,negewhcoerce,"-o",label='ns vs negew') + pylab.plot(nshcoerce,negudhcoerce,"-o",label='ns vs negud')
zfp = pylab.figure() #makes the zeiderfeld plot figure    
zfp = pylab.plot(ns,negew,"-o", label='ns vs negew') + pylab.plot(ns,negud,"-o",label='ns vs negud') #actually does the plotting
print 'Are you satisfied with this as the high coercivity part?'
print 'Close the figures and enter y/n'    
pylab.show()
'''