#!/usr/bin/python
#for now: only asexual reproduction.
#prawie odbagowane, problemy z pamiecia???
import sys
sys.path.append('/home/marta/COG-ABM/src')

import random
import math
from time import time
from cog_abm.extras.tools import get_progressbar #dodac progressbar
import pprint
from presenter.charts import wykres
import copy
import logging

log = logging.getLogger('COG-ABM')

#from cog_abm.core import Simulation, Agent
#from cog_abm.core.interaction import Interaction #czy tego potrzebuje? jesli tak - do rozrodu.
#from cog_abm.extras.additional_tools import generate_simple_network #czy tego potrzebuje? jesli tak, do wyboru ojca potomstwa.
from cog_abm.extras.tools import avg

num_agents = 100
num_groups = 10
#a_death =
#b_death =
#c_death =
#d_death =
deathProb = 0.5
mutProb = 0.001
a_div = -0.01
b_div = 1
cost = -1
d_div = 0.01
a_migr = 0 #for now p_migr=1/100
b_migr = -math.log(99)
iters = 5000
dump_freq = iters / 100

max_number=0

class GroupState(object):
    def __init__(self,a):
        self.agents=a
    def get_agent(self,i):
        return self.agents[i]
    def add_agent(self,agent):
        self.agents.append(agent)
    def get_NumberOfAgents(self):
        return len(self.agents)
    def get_cooperation(self):
        return avg([agent.state.get_genValue() for agent in self.agents])
    def iteration(self):
        agents2=[]
        migrants=[]
        N=self.get_NumberOfAgents()
        cooperation= self.get_cooperation()
        for agent in self.agents:    
            if agent.state.get_breedProb(cooperation,N) < random.random():
                agents2.append(agent.breed())
            if deathProb < random.random(): 
                if migrProb(N) < random.random():
                    migrants.append(agent)
                else:
                    agents2.append(agent)
        self.agents=agents2
        if self.get_NumberOfAgents() > 100000:
            print "too many agents"
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
    def mutate(self,p=mutProb):
        if random.random() < p:
            return GroupAgentState(g = self.get_genValue() + random.gauss(0,1))
        else: 
            return GroupAgentState(g = self.get_genValue() + random.gauss(0,1))

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
    def __init__(self, groups):
        self.groups=groups
        self.statistic = []
    def dump_results(self, iter_num):
        cc = copy.deepcopy(self.groups)
        #cc = [a.deepcopy() for a in self.agents]
        kr = (iter_num, cc)
        self.statistic.append(kr)
    def migrate(self,migrants):
        for migrant in migrants:
            group=random.choice(self.groups)
            group.add(migrant)
    def _do_main_loop(self, iterations, dump_freq):
        start_time = time()
        log.info("Simulation start...")
        it = xrange(iterations // dump_freq)
        for i in it:
            print i
            migrants=[]
            for group in self.groups:
                migrants.extend(group.state.iteration())
            if len(migrants) > 100000:
                print "too many migrants"
            self.migrate(migrants)
            self.dump_results((i + 1) * dump_freq)
        log.info("Simulation end. Total time: " + str(time() - start_time))
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

def breedProb(coop,N,c=0,a=a_div,b=b_div,d=d_div):
    return 1/(1+math.exp(-(a*N + b + c + d*coop)))

def migrProb(N,a=a_migr,b=b_migr):
    return 1/(1+math.exp(-(a*N + b)))   

def prepare_groups(num_agents,num_groups): 
    def prepare_agents(num_agents):
        agents = [Agent(state=GroupAgentState())
            for _ in xrange(num_agents)]
        return agents
    groups = [Group(state=GroupState(prepare_agents(num_agents)))
        for n in xrange(num_groups)]
    return groups


def group_experiment(num_agents, num_groups, iters): #jakie jeszcze parametry?
    groups = prepare_groups(num_agents, num_groups) #jakie jeszcze parametry?
    #topology = generate_simple_network(agents) #?
    s = Simulation(groups) #?
    return s.run(iters, dump_freq)
    


def analyze(results):
    def tmp(agents):
        return avg([(group.state.get_cooperation()) for group in groups])
        # ok?
    return [(it, tmp(groups)) for it, groups in results]


def present_results(analysis):
    pprint.pprint(analysis)
    wykres(analysis, "", "")  # co tutaj?



def main(args):
    res = \
    group_experiment(num_agents, num_groups, iters) #co jeszcze?
    analysis = analyze(res)
    #print "done"
    present_results(analysis)


if __name__ == '__main__':
    main(sys.argv[1:])
