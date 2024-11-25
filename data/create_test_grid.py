import pandapower as pp

#create empty net
net = pp.create_empty_network()

#create buses
bus1 = pp.create_bus(net, vn_kv=20., name="Bus 1")
bus2 = pp.create_bus(net, vn_kv=0.4, name="Bus 2")
bus3 = pp.create_bus(net, vn_kv=0.4, name="Bus 3")

#create bus elements
pp.create_ext_grid(net, bus=bus1, vm_pu=1.02, name="Grid Connection")
pp.create_load(net, bus=bus3, p_mw=0.100, q_mvar=0.05, name="Load")

#create branch elements
trafo = pp.create_transformer(net, hv_bus=bus1, lv_bus=bus2, std_type="0.4 MVA 20/0.4 kV", name="Trafo")
line = pp.create_line(net, from_bus=bus2, to_bus=bus3, length_km=0.1, std_type="NAYY 4x50 SE", name="Line")

pp.to_json(net, "simple_grid.json")
pp.plotting.simple_plot(net, plot_loads=True, plot_sgens=True)