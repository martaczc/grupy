#!/usr/bin/python
#for now: only asexual reproduction.
import sys
sys.path.append('/home/marta/COG-ABM/src')

import random
import math
from time import time
from ..extras.tools import get_progressbar

#from cog_abm.core import Simulation, Agent
#from cog_abm.core.interaction import Interaction #czy tego potrzebuje? jesli tak - do rozrodu.
#from cog_abm.extras.additional_tools import generate_simple_network #czy tego potrzebuje? jesli tak, do wyboru ojca potomstwa.
#from cog_abm.extras.tools import avg

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

max_number=0

class GroupState(object):
    def __init__(self,a):
        self.agents=a
        self.cooperation=sum([agent.state.get_genValue() for agent in self.agents])
        self.N=self.agents.length
    def get_agent(self,i)
        return self.agents[i]
    def add_agent(self,agent)
        self.agents.append(agent)
    def get_NumberOfAgents(self)
        return self.N
    def get_cooperation(self)
        return self.cooperation
    def get_breedProb(self)
        return def breedProb(self.N)
    def update(self)
        agents         

class GroupAgentState(object):
    def __init__(self,s='f',g=0)
        #self.sex=s
        self.gen=g
    def get_genValue(self) 
        return self.gen
    def get_sex(self)
        return self.sex
    def get_deathProb(self,cooperation,N)
        return deathProb(self.gen,cooperation,N)
    def mutate(self)
        return GroupAgentState(g=get.gen.value+random.gauss(0,1))

class Group(object): 
    def __init__(self,state)
        self.state=state

class Agent(object):
    def __init__(self,state)
        self.state=state
    def breed(self)
        return Agent(state=self.state.mutate())

class Simulation(object):
    def __init__(self, graph=None, groups=None):
        self.graph=graph
        self.groups=groups
        self.statistic = []
    def dump_results(self, iter_num):
        cc = copy.deepcopy(self.agents)
        #cc = [a.deepcopy() for a in self.agents]
        kr = (iter_num, cc)
        self.statistic.append(kr)
    def iteration
        for 
    #TODO

def deathProb(cost,help,N,a=a_death,b=b_death,c=c_death,d=d_death)
    return 1/(1+math.exp(a*N+c*help+d*cost+b))

def breedProb(N,a=a_breed,b=b_breed)
    return 1/(1+math.exp(a*N+b))

def prepare_groups(num_agents,num_groups): #czy zagnieżdżanie funkcji działa?
    def prepare_agents(num_agents):
        agents = [Agent(state=GroupAgentState())
            for _ in xrange(init_num_agents)]
        return agents
    groups = [Group(state=GroupState(prepare_agents(num_agents)))
        for n in xrange(init_num_groups)]

def group_experiment(num_agents, num_groups, iters): #jakie jeszcze parametry?
    groups = prepare_groupss(init_num_agents, init_num_groups) #jakie jeszcze parametry?
    #topology = generate_simple_network(agents) #?
    s = Simulation(topology, GroupInteraction(), agents) #?
    return s.run(iters, DUMP_FREQ)
    #TODO

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
