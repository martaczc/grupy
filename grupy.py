#!/usr/bin/python
#for now: only asexual reproduction.
#sth wrong with exceptions and dump_freq
import sys
sys.path.append('/home/marta/COG-ABM/src')

import random
import math
from time import time
from cog_abm.extras.tools import get_progressbar 
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
d_div = 10
a_migr = 0 #for now p_migr=1/1000
b_migr = -math.log(999)
iters = 1000
dump_freq = iters / 100
INIT_COOP = 1

max_number=10000


class GroupState(object):

    def __init__(self,a,gr_no,n=num_agents):
        self.agents=a
        self.count=n
        self.group_no=gr_no

    def get_agent(self,i):
        return self.agents[i]

    def add_agent(self,agent):
        self.agents.append(agent)
        self.count=self.count+1

    def get_NumberOfAgents(self):
        return len(self.agents)

    def get_cooperation(self):
        return avg([agent.state.get_genValue() for agent in self.agents])

    def iteration(self):
        agents2=[]
        migrants=[]
        N=self.get_NumberOfAgents()
        cooperation = self.get_cooperation()
        for agent in self.agents:    
            if random.random() < agent.state.get_breedProb(cooperation,N):
                agents2.append(agent.breed(self.count))
                self.count=self.count+1
            if random.random() < deathProb: 
                if random.random() < migrProb(N):
                    migrants.append(Migrant(agent,origin=self.group_no))
                else:
                    agents2.append(agent)
        self.agents=agents2
        if self.get_NumberOfAgents() > max_number: 
            raise ExpGrowthError("agents")
        else:
            return migrants 


class GroupAgentState(object):

    def __init__(self,n,s='f',g=0):
        self.sex=s
        self.gen=g     
        self.number=n 

    def get_genValue(self):
        return self.gen

    def get_sex(self):
        return self.sex

    def get_breedProb(self,cooperation,No,cost=cost):
        return breedProb(c=self.gen*cost,coop=cooperation,N=No)

    def mutate(self,count,p=mutProb):
        if random.random() < p:
            return GroupAgentState(n=count,g = self.get_genValue() + random.gauss(0,1))
        else: 
            return GroupAgentState(n=count,g = self.get_genValue())


class Group(object): 

    def __init__(self,state):
        self.state=state

    def add(self,agent):
        self.state.add_agent(agent)


class Agent(object):

    def __init__(self,state):
        self.state=state

    def breed(self,count):
        return Agent(state=self.state.mutate(count))

class Migrant(object):

    def __init__(self, agent, origin, dest=None):
        self.agent=agent
        self.origin=origin
        self.dest=dest

    def destination(self, dest):
        self.dest=dest


class Simulation(object):

    def __init__(self, groups, pb=False):
        self.groups=groups
        self.migrants=None
        self.statistic = []
        self.pb = pb  #pb - show progress bar

    def dump_results(self, iter_num):
        cc = copy.deepcopy(self.groups)
        cm = copy.deepcopy(self.migrants)
        kr = (iter_num, cc, cm)
        self.statistic.append(kr)

    def migrate(self,migrants):
        for migrant in migrants:
            group=random.choice(self.groups)
            group.add(migrant.agent)
            migrant.dest=group.state.group_no
        self.migrants=migrants

    def _do_iterations(self, num_iter):
        for _ in xrange(num_iter):
            migrants=[]
            for group in self.groups:
                migrants.extend(group.state.iteration())
            if len(migrants) > max_number: 
                raise ExpGrowthError("migrants")
            self.migrate(migrants)

    def _do_main_loop(self, iterations, dump_freq):
        start_time = time()
        log.info("Simulation start...")
        it = xrange(iterations // dump_freq)
        if self.pb:
            it = get_progressbar()(it)
        for i in it:
            self._do_iterations(dump_freq)
            self.dump_results((i + 1) * dump_freq)
        log.info("Simulation end. Total time: " + str(time() - start_time))

    #def continue_(self, iterations=1000, dump_freq=10):
        #try:
            #self._do_main_loop(iterations, dump_freq)
            #print "try continue"
        #except ExpGrowthError as err:
            #err.message()
        #else:
            #self._do_main_loop(iterations, dump_freq)
            #print "continue"
        #return self.statistic

    def run(self, iterations=1000, dump_freq=10):
        """
        Begins simulation.

        iterations
        """
        self.dump_results(0)
        try:
            self._do_main_loop(iterations, dump_freq)
            print "try run"            
        except ExpGrowthError as err:
            err.message()
        #else:
         #   self._do_main_loop(iterations, dump_freq)
         #   print "run"
        return self.statistic


class ExpGrowthError(RuntimeError):

      def __init__(self, w):
          self.word = w

      def message(self):
          print "too many " + self.word


#def deathProb(cost,help,N,a=a_death,b=b_death,c=c_death,d=d_death)
#    return 1/(1+math.exp(-(a*N+c*help+d*cost+b)))

def breedProb(coop,N,c,a=a_div,b=b_div,d=d_div):
    return 1/(1+math.exp(-1*(a*N + b + c + d*coop)))


def migrProb(N,a=a_migr,b=b_migr):
    return 1/(1+math.exp(-1*(a*N + b)))   


def prepare_groups(num_agents,num_groups,init_coop): 
    def prepare_agents(num_agents):
        agents = [Agent(state=GroupAgentState(n=i,g=init_coop))
            for i in xrange(num_agents)]
        return agents
    groups = [Group(state=GroupState(prepare_agents(num_agents),gr_no=n))
        for n in xrange(num_groups)]
    return groups


def group_experiment(num_agents, num_groups, iters): 
    groups = prepare_groups(num_agents, num_groups,INIT_COOP) 
    s = Simulation(groups, pb=True) 
    return s.run(iters, dump_freq)
    

def analyze(results):
    def cooperation(groups):
        return [(group.state.get_cooperation()) for group in groups]
    def numberOfAgents(groups):
        return [(group.state.get_NumberOfAgents()) for group in groups]
    return [[(it, cooperation(groups)) for it, groups,migrants in results],[(it, numberOfAgents(groups)) for it, groups,migrants in results]]


def present_results(analysis):
    pprint.pprint(analysis)
    wykres(analysis[0], "time", "cooperation")  
    wykres(analysis[1], "time", "number of agents")

def main(args):
    res = \
    group_experiment(num_agents, num_groups, iters)
    analysis = analyze(res)
    #print "done"
    present_results(analysis)


if __name__ == '__main__':
    main(sys.argv[1:])
