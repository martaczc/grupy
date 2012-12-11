#!/usr/bin/python
import sys
sys.path.append('/home/konrad/ICM/cog-abm-tutorial/COG-ABM/src')

import random

from cog_abm.core import Simulation, Agent
from cog_abm.core.interaction import Interaction #czy tego potrzebuje? jesli tak - do rozrodu.
from cog_abm.extras.additional_tools import generate_simple_network #czy tego otrzebuje? jesli tak, do wyboru ojca potomstwa.
from cog_abm.extras.tools import avg

init_num_agents = 100
init_num_groups =
a_death =
b_death =
a_breed =
b_breed =
iters = 500000
dump_freq = iters / 100

class GroupAgentState(object):
    #TODO

class GroupInteraction(Interaction): #???
    #TODO

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
