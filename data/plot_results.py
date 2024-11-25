# %%
import pandas as pd
import matplotlib.pyplot as plt

#plt.ion()

# %%
wctrl = pd.read_csv('../results.csv', index_col='date', parse_dates=True)

# woctrl = pd.read_csv('results_wo_ctrl.csv', index_col='date', parse_dates=True)

# %%
fig = plt.figure()
wctrl['Grid-0.0-Bus 3-vm_pu'].plot()
# woctrl['Grid-0.0-Bus 3-vm_pu'].plot()
# plt.legend(['with ctrl', 'w/o ctrl'])
plt.ylabel('voltage [p.u.]')
plt.subplots_adjust(left=0.15)
plt.show()

# %%
fig2 = plt.figure()
wctrl['PV-0.PV_0-P_gen'].plot()
# woctrl['PV-0.PV_0-P_gen'].plot()
# plt.legend(['with ctrl', 'w/o ctrl'])
plt.ylabel('power [MW]')
plt.subplots_adjust(left=0.15)
plt.show()

# %%
fig3 = plt.figure()
wctrl['PV-0.PV_0-mod'].plot()
# woctrl['PV-0.PV_0-P_gen'].plot()
# plt.legend(['with ctrl', 'w/o ctrl'])
plt.ylabel('mod')
plt.subplots_adjust(left=0.15)
plt.show()

# %%
