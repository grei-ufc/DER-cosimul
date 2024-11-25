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
END = 48 * 60 * 60  # 16 hours in seconds
START = '2021-05-21 04:00:00'
GRID_FILE = 'data/simple_grid.json'
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
pv = pvsim.PV(lat=53.07, area=3e4)
ctrl = ctrlsim.Ctrl()

# Connect model entities:
nodes_gen = [element for element in grid if 'ext_gen' in element.eid]
nodes = [e for e in grid if e.type in 'Bus']
lines = [e for e in grid if e.type in 'Line']
loads = [e for e in grid if e.type in 'Load']

world.connect(solar_data[0], pv, 'DNI')
world.connect(pv, nodes_gen[1], ('P_gen', 'p_mw'))

world.connect(nodes[-1], ctrl, ('vm_pu', 'val_in'))
world.connect(ctrl, pv, 'mod', weak=True)

# Some data collection:
collector = world.start('Collector', start_date=START)
monitor = collector.Monitor()

connect_many_to_one(world, nodes, monitor, 'p_mw', 'vm_pu')
world.connect(pv, monitor, 'P_gen', 'mod')

world.connect(lines[0], monitor, 'loading_percent')

setup_web_visualization(world, START, nodes, lines, loads, pv, ctrl, solar_data)
world.run(until=END, print_progress=False)
