#!/usr/bin/python
import sys
sys.path.append('/home/marta/COG-ABM/src')

import random
import math

from cog_abm.core import Simulation, Agent
from cog_abm.core.interaction import Interaction #czy tego potrzebuje? jesli tak - do rozrodu.
from cog_abm.extras.additional_tools import generate_simple_network #czy tego potrzebuje? jesli tak, do wyboru ojca potomstwa.
from cog_abm.extras.tools import avg

init_num_agents = 100
init_num_groups =
a_death =
b_death =
c_death =
d_death =
a_breed =
b_breed =
iters = 500000
dump_freq = iters / 100

class GroupState(object):
    def __init__(self,n=0,a=[]):
        self.number=n
        self.agents=a
        self.cooperation=sum([agent.state.get_genValue() for agent in self.agents])
        self.N=self.agents.length
    def get_agent(self,i)
        return self.agents[i]
    def get_number(self)
        return self.number
    def get_agentNumber(self)
        return self.N
    def get_cooperation(self)
        return self.cooperation
    def update(self,a) 
        self.agents=a
        self.cooperation=sum([agent.state.get_genValue() for agent in self.agents])
        self.N=self.agents.length        
        

class GroupAgentState(object):
    def __init__(self,s='m',g=0)
        self.sex=s
        self.gen=g
        #mutations?
    def get_genValue(self)
        return self.gen
    def get_sex(self)
        return self.sex
    def get_deathProb(self,cooperation,N)
        return deathProb(self.gen,cooperation,N)

class GroupInteraction(Interaction): #???
    #TODO

def deathProb(cost,help,N,a=a_death,b=b_death,c=c_death,d=d_death)
    return 1/(1+math.exp(a*N+c*help+d*cost+b))

def breedProb(N,a=a_breed,b=b_breed)
    return 1/(1+math.exp(a*N+b))

def prepare_agents(num_agents, num_groups): #jakie jeszcze parametry?
    #TODO

def group_experiment(num_agents, num_groups, iters): #jakie jeszcze parametry?
    #TODO
    agents = prepare_agents(num_agents, num_groups) #jakie jeszcze parametry?
    topology = generate_simple_network(agents) #?
    s = Simulation(topology, GroupInteraction(), agents) #?
    return s.run(iters, DUMP_FREQ)

def analyze(results):
    #TODO

def present_results(analysis):
    import pprint
    pprint.pprint(analysis)
    from presenter.charts import wykres
    wykres(analysis, "", "") #co tutaj?

def main(args):
    res = \
        group_experiment(NUM_AGENTS, NUM_GROUPS, ITERS) #co jeszcze?
    analysis = analyze(res)
    present_results(analysis)


if __name__ == '__main__':
    main(sys.argv[1:])
