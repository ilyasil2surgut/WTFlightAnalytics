import DataParse
names = ['Time/s', 'Throttle/%', 'IAS/kph', 'TAS/kph', 'Altitude/m', 'Vario/m/s','SEP*/m/s', 'Power/bhp', 'EffectivePower*/bhp', 'Compressor/stage']
Spitfire=DataParse.Data("C:/Users/ilyas_000/SkyDrive/Documents/SPITFIRE_IX_4_4_7.33.50 20fuel.csv")
Spitfire.setname("Spitfire Mk IX")
Spitfire.FilterNames(names)
Spitfire.GenerateDataPoints()
Spitfire.FixFalseAlt(184,608)
maxvalue=max([x.get("Throttle") for x in Spitfire.datapoints])
Spitfire.FilterPoints((lambda point:point.get('Throttle')==maxvalue))
# Spitfire.plotClimbrate()
# for i in range(10):print(Spitfire.datapoints[i])
Tempest=DataParse.Data("C:/Users/ilyas_000/SkyDrive/Documents/TEMPEST_MKV_4_4_7.57.38.csv")
Tempest.setname("Tempest Mk V")
Tempest.FilterNames(names)
Tempest.GenerateDataPoints()
Tempest.FixFalseAlt(184,608)
val=max([x.get("Throttle") for x in Tempest.datapoints])
Tempest.FilterPoints((lambda point:point.get('Throttle')==val))
# for i in range(100):print(Tempest.datapoints[400+i])
Tempest.plotClimbrate()
# Spitfire.plotPowertoAlt()
# for i in range(10):
#     print(Spitfire.datapoints[i])
# # print(Spitfire.datapoints[-1])
