# Design-Graphs-for-Poor-Liquid-Rockets

Iteration is important in design, and quick understanding of performance for a potential design is important. This tries to allow one to give a couple pieces of information, and allow them to figure out if theyre thing will work. 

plan:
create graphs that correlate the following variables:
    
    Assumed LOX Kerosene.

    graphs seperated by 
    design T/W
    
    
    X axis -  total rocket weight
    Y axis - ratio of expected altitude (ft)/ diameter of airframe(in)

    graphed out curves are combos of:
    deadweight % (out of total rocket weight, how much is not acting as propellant, including pressurant gasses)
    isp of engine (sec) 


Thrust and isp allow for propulsion time:

Thrust / (isp * g) = mdot

(Wtotal * (1-deadWeight) ) / mdot = Thrust time

impulse = thrust *  (Wtotal * (1-deadWeight) ) / (Thrust / (isp * g))


some tips:
Make sure interperter (ctrl-shift-p ; >python: select interpeter ; probably the recommended one, don't do freak ones)