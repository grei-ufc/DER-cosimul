from mosaik.util import connect_many_to_one


def setup_web_visualization(world, START, nodes, lines, loads, pv, ctrl, solar_data):
    # Web visualization
    webvis = world.start('WebVis', start_date=START, step_size=60)
    webvis.set_config(ignore_types=['Topology', 'ResidentialLoads', 'Grid',
                                    'Monitor', 'Trafo', 'Database', 'Ext_grid', 'Data'],
                      merge_types=['Line'],
                      timeline_hours=12,
                      ignore_names=['Grid-0.0-ext_gen_at_bus-Bus 2', 'Grid-0.0-ext_gen_at_bus-Bus 3'])
    vis_topo = webvis.Topology()

    connect_many_to_one(world, nodes, vis_topo, 'vm_pu')
    world.connect(lines[0], vis_topo, 'loading_percent')
    webvis.set_etypes({
        'Bus': {
            'cls': 'refbus',
            'attr': 'vm_pu',
            'unit': 'U [p.u.]',
            'default': 1,
            'min': 0.7,
            'max': 1.5,
        },
        'Line': {
            'cls': 'line',
            'attr': 'loading_percent',
            'unit': 'I [%]',
            'default': 0,
            'min': -100,
            'max': 200,
        },
    })

    world.connect(pv, vis_topo, 'P_gen')
    world.connect(ctrl, vis_topo, 'mod')
    world.connect(solar_data[0], vis_topo, 'DNI')
    webvis.set_etypes({
        'PV': {
            'cls': 'gen',
            'attr': 'P_gen',
            'unit': 'P [MW]',
            'default': 0,
            'min': 0,
            'max': 1.,
        },
        'Sun': {
            'cls': 'gen',
            'attr': 'DNI',
            'unit': 'DNI [W/m2]',
            'default': 0,
            'min': 0,
            'max': 1000.,
        },
        'Ctrl': {
            'cls': 'gen',
            'attr': 'mod',
            'unit': 'Corr [fact.]',
            'default': 1.,
            'min': 0.,
            'max': 1.1,
        },
    })


    connect_many_to_one(world, loads, vis_topo, 'p_mw')
    webvis.set_etypes({
        'Load': {
            'cls': 'load',
            'attr': 'p_mw',
            'unit': 'P [MW]',
            'default': 0,
            'min': 0,
            'max': 3,
        },
    })
