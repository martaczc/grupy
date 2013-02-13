#!/usr/bin/python
#for now: only asexual reproduction.
import sys
sys.path.append('/home/marta/COG-ABM/src')

import random
import math
from time import time
from ..extras.tools import get_progressbar
import pprint
from presenter.charts import wykres

#from cog_abm.core import Simulation, Agent
#from cog_abm.core.interaction import Interaction #czy tego potrzebuje? jesli tak - do rozrodu.
#from cog_abm.extras.additional_tools import generate_simple_network #czy tego potrzebuje? jesli tak, do wyboru ojca potomstwa.
#from cog_abm.extras.tools import avg

init_num_agents = 100
init_num_groups = 10
#a_death =
#b_death =
#c_death =
#d_death =
deathProb = 1/2
a_div = -0.01
b_div = 1
cost = -1
d_div = 0.01
a_migr = 0 #for now p_migr=1/100
b_migr = -math.log(99)
iters = 500000
dump_freq = iters / 100

max_number=0

class GroupState(object):
    def __init__(self,a=None,m=None):
        self.agents=a
    def get_agent(self,i):
        return self.agents[i]
    def add_agent(self,agent):
        self.agents.append(agent)
    def get_NumberOfAgents(self):
        return self.agents.length
    def get_cooperation(self):
        return sum([agent.state.get_genValue() for agent in self.agents])
    def iteration(self):
        agents2=[]
        migrants=[]
        N=self.get_NumberOfAgents()
        cooperation= self.get_cooperation()
        for agent in self.agents:    
            if agent.get_breedProb(cooperation,N) < random.random():
                agents2.append(agent.breed())
            if deathProb() < random.random(): 
                if migrProb(N) < random.random():
                    migrants.append(agent)
                else:
                    agents2.append(agent)
        self.agents=agents2
        return migrants 

class GroupAgentState(object):
    def __init__(self,s='f',g=0):
        self.sex=s
        self.gen=g
    def get_genValue(self):
        return self.gen
    def get_sex(self):
        return self.sex
    def get_breedProb(self,cooperation,No):
        return breedProb(c=self.gen,coop=cooperation,N=No)
    def mutate(self):
        return GroupAgentState(g=get.gen.value+random.gauss(0,1))

class Group(object): 
    def __init__(self,state):
        self.state=state
    def add(self,agent):
        self.state.add_agent(agent)

class Agent(object):
    def __init__(self,state):
        self.state=state
    def breed(self):
        return Agent(state=self.state.mutate())

class Simulation(object):
    def __init__(self, graph=None, groups=None):
        self.graph=graph
        self.groups=groups
        self.statistic = []
    def dump_results(self, iter_num):
        cc = copy.deepcopy(self.groups)
        #cc = [a.deepcopy() for a in self.agents]
        kr = (iter_num, cc)
        self.statistic.append(kr)
    def migrate(self,migrants):
        for migrant in migrants:
            group=random.choice(groups)
            group.add(migrant)
    def _do_main_loop(self, iterations, dump_freq):
        start_time = time()
        log.info("Simulation start...")
        it = xrange(iterations // dump_freq)
        if self.pb:
            it = get_progressbar()(it)
        for i in it:
            migrants=[]
            for group in self.groups:
                migrants.extend(group.state.iteration())
            
                
            
    def continue_(self, iterations=1000, dump_freq=10):
        self._do_main_loop(iterations, dump_freq)
        return self.statistic

    def run(self, iterations=1000, dump_freq=10):
        """
        Begins simulation.

        iterations
        """
        self.dump_results(0)
        self._do_main_loop(iterations, dump_freq)
        return self.statistic


#def deathProb(cost,help,N,a=a_death,b=b_death,c=c_death,d=d_death)
#    return 1/(1+math.exp(-(a*N+c*help+d*cost+b)))

def breedProb(coop,c=0,N,a=a_div,b=b_div,d=d_div):
    return 1/(1+math.exp(-(a*N + b + c + d*coop)))

def migrProb(N,a=a_migr,b=b_migr):
    return 1/(1+math.exp(-(a*N + b)))   

def prepare_groups(num_agents,num_groups): 
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
    pprint.pprint(analysis)
    wykres(analysis, "", "") #co tutaj?
    #nie dziala, nie wiem czemu :(

def main(args):
    res = \
        group_experiment(NUM_AGENTS, NUM_GROUPS, ITERS) #co jeszcze?
    analysis = analyze(res)
    present_results(analysis)


if __name__ == '__main__':
    main(sys.argv[1:])




