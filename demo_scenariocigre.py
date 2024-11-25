"""This scenario contains a grid simulated in pandapower.
data"""

# Import packages needed for the scenario.
import mosaik
from mosaik.util import connect_many_to_one

from data.setup_webvis import setup_web_visualization

# Specify simulator configurations
sim_config = {
    'Grid': {'python': 'mosaik_pandapower.simulator:Pandapower'
    },
    'CSV': {
        'python': 'simulators.csv_sim_pandas:CSV'
    },
    'PV': {
        'python': 'simulators.pv_simulator:PvAdapter'
    },
    'Ctrl': {
        'python': 'simulators.controller_des:Controller'
    },
    'Collector': {
        'python': 'simulators.collector:Collector'
    },
    'WebVis': {
        'cmd': 'mosaik-web -s 0.0.0.0:8000 %(addr)s'
    },

}

# Set scenario parameters:
END = 16 * 60 * 60  # 16 hours in seconds
START = '2021-05-21 04:00:00'
GRID_FILE = 'data/cigre_network_lv.json'
PV_DATA = 'data/solar_data_Bremen_minutes.txt'

# Set up the "world" of the scenario
world = mosaik.World(sim_config)

# Initialize the simulators
gridsim = world.start('Grid', step_size=None)
DNIdata = world.start('CSV', sim_start=START, datafile=PV_DATA)
pvsim = world.start('PV', start_date=START, gen_neg=False)
ctrlsim = world.start('Ctrl', output_delay=60)

# Instantiate model entities
grid = gridsim.Grid(gridfile=GRID_FILE).children
solar_data = DNIdata.Data.create(1)

# pv1 = pvsim.PV(lat=53.07, area=3e4)
# pv2 = pvsim.PV(lat=53.07, area=3e4)

pv = pvsim.PV(lat=53.07, area=3e4)
ctrl= ctrlsim.Ctrl()

#ctrl1 = ctrlsim.Ctrl()
# ctrl2 = ctrlsim.Ctrl()


# Connect model entities:
nodes_gen = [element for element in grid if 'ext_gen' in element.eid]
nodes = [e for e in grid if e.type in 'Bus']
lines = [e for e in grid if e.type in 'Line']
loads = [e for e in grid if e.type in 'Load']

# print('nos geração \n \n',nodes)
# print(' \n \n nos geração \n \n',nodes_gen)
# print('quantidade',len(nodes))
# print('quantidade',len(nodes_gen))
# print(nodes[34])

# world.connect(solar_data[0], pv1, 'DNI')
# world.connect(solar_data[0], pv2, 'DNI')

world.connect(solar_data[0], pv, 'DNI')

# world.connect(pv1, nodes_gen[26], ('P_gen', 'p_mw'))
# world.connect(pv2, nodes_gen[33], ('P_gen', 'p_mw'))

world.connect(pv, nodes_gen[33], ('P_gen', 'p_mw'))


# world.connect(nodes[26], ctrl1, ('vm_pu', 'val_in'))
# world.connect(nodes[33], ctrl2, ('vm_pu', 'val_in'))

world.connect(nodes[33], ctrl, ('vm_pu', 'val_in'))


# world.connect(ctrl1, pv1, 'mod', weak=True)
# world.connect(ctrl2, pv2, 'mod', weak=True)

world.connect(ctrl, pv, 'mod', weak=True)

# Some data collection:
collector = world.start('Collector', start_date=START)
monitor = collector.Monitor()

#connect_many_to_one(world, nodes, monitor, 'p_mw', 'vm_pu')
# world.connect(pv1, monitor, 'P_gen', 'mod')
# world.connect(pv2, monitor, 'P_gen', 'mod')
world.connect(pv, monitor, 'P_gen', 'mod')

#world.connect(lines[1], monitor, 'loading_percent')
#world.connect(nodes[26], monitor, 'p_mw', 'vm_pu')
world.connect(nodes[33], monitor, 'p_mw', 'vm_pu')
#connect_many_to_one(world, lines, monitor, 'loading_percent')

# setup_web_visualization(world, START, nodes, lines, loads, pv1 ,ctrl1,  solar_data)
setup_web_visualization(world, START, nodes, lines, loads, pv, ctrl, solar_data)

world.run(until=END, print_progress=True)
