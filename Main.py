import DataParse
lines=DataParse.Parsefile("C:/Users/ilyas_000/SkyDrive/Documents/SPITFIRE_IX_4_4_7.33.50 20fuel.csv")
# for i in range(10):
#     print(lines[i])
names = ['Time/s', 'Throttle/%', 'IAS/kph', 'TAS/kph', 'Altitude/m', 'Vario/m/s', 'SEP*/m/s', 'Power/bhp', 'EffectivePower*/bhp', 'Radiator/%', 'Compressor/stage']
# newlines=DataParse.FilterOnly(names,lines)
# print(newlines[0])
# for i in range(10):
#     print(newlines[100+i])
Spitfire=DataParse.Data("C:/Users/ilyas_000/SkyDrive/Documents/SPITFIRE_IX_4_4_7.33.50 20fuel.csv")
Spitfire.FilterNames(names)
Spitfire.GenerateDataPoints()
Spitfire.FixFalseAlt(184,608)
maxvalue=max([x.get("Throttle") for x in Spitfire.datapoints])
Spitfire.FilterPoints((lambda point:point.get('Throttle')==maxvalue))
for i in range(10):
    print(Spitfire.datapoints[i])
# print(Spitfire.datapoints[-1])