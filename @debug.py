import pandas as pd

fnames = [
	'mod_out_ev_charger.csv',
	'mod_out_house.csv',
	'mod_out_meter.csv',
	'mod_out_responsive.csv',
	'mod_out_unresponsive.csv',
	'mod_out_waterheater.csv'
]

df = pd.read_csv(fnames[0])

for name in fnames[1:]:
	ndf = pd.read_csv(name)
	df = pd.merge(df, ndf)

df['tot_load[kW]'] = df['ev.power.real[kW]'] + df['heating_demand[kW]'] + df['cooling_demand[kW]'] + df['responsive.power.real[kW]'] + df['unresponsive.power.real[kW]'] + df['wh.power.real[kW]']

# print(df)
# print(df.columns)

print(df[['timestamp', 'meter.measured_power.real[kW]', 'tot_load[kW]']])