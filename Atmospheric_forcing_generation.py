import netCDF4 as nc
import numpy
import os
import time

str_station = 'Konza'   #station name
#different scenarios
str_pre_list = ['Pr_cvm01', 'Pr_cvp01', 'Pr_cvp02', 'Pr_cvp03', 'Pr_di5', 'Pr_di10', 'Pr_di15', 'Pr_di30', 'Pr_di45', 'Pr_di60', 'Pr_dro', 'Pr_m10', 'Pr_m20', 'Pr_m30', 'Pr_m50', 'Pr_p10', 'Pr_p20', 'Pr_p30']

#Help to correct the unit of time
time_skip = 732586
time_skip = 730252  #Garraf
time_skip = 724023  #Konza
file_obj = nc.Dataset('E:\Single_coloum\FORCING_2ND_PHASE\\'+str_station+'_Meteo_Data.nc')
file_obj2 = nc.Dataset('E:\Single_coloum\FORCING_2ND_PHASE\\'+str_station+'_Precipitation_Scenarios.nc')
for str_pre in str_pre_list:


    index_previous = 0      #index of previous step
    index = -1

    Precip = file_obj2.variables[str_pre]
    var_Precip = numpy.array(Precip)

    Long = file_obj.variables['Long']
    var_Long = numpy.array(Long)

    Lat = file_obj.variables['Lat']
    var_Lat = numpy.array(Lat)

    Hour = file_obj.variables['Hour']
    var_Hour = numpy.array(Hour)

    Year = file_obj.variables['Year']
    var_Year = numpy.array(Year)

    Month = file_obj.variables['Month']
    var_Month = numpy.array(Month)

    Day = file_obj.variables['Day']
    var_Day = numpy.array(Day)

    Date = file_obj.variables['Date']
    var_Date = numpy.array(Date)

    Temp = file_obj.variables['Temp']
    var_Temp = numpy.array(Temp)
    #Precip = file_obj.variables['Precip']
    #var_Precip = numpy.array(Precip)


    RelHhum = file_obj.variables['RelHhum']
    var_RelHhum = numpy.array(RelHhum)

    q_hum = file_obj.variables['q_hum']
    var_q_hum = numpy.array(q_hum)
    VapPressure = file_obj.variables['VapPressure']
    var_VapPressure = numpy.array(VapPressure)
    Pressure = file_obj.variables['Pressure']
    var_Pressure = numpy.array(Pressure)
    WindSpeed = file_obj.variables['WindSpeed']
    var_WindSpeed = numpy.array(WindSpeed)
    LongDown = file_obj.variables['LongDown']
    var_LongDown = numpy.array(LongDown)
    Rsw = file_obj.variables['Rsw']
    var_Rsw = numpy.array(Rsw)
    SAB1 = file_obj.variables['SAB1']
    var_SAB1 = numpy.array(SAB1)
    SAB2 = file_obj.variables['SAB2']
    var_SAB2 = numpy.array(SAB2)
    SAD1 = file_obj.variables['SAD1']
    var_SAD1 = numpy.array(SAD1)
    SAD2 = file_obj.variables['SAD2']
    var_SAD2 = numpy.array(SAD2)
    PARB = file_obj.variables['PARB']
    var_PARB = numpy.array(PARB)
    PARD = file_obj.variables['PARD']
    var_PARD = numpy.array(PARD)



    for num in range(len(var_Hour)):
        stryear = str(int(var_Year[num][0]))
        strmonth = str(int(var_Month[num][0]))
        if var_Month[num][0] < 10:
            strfile = 'E:\Single_coloum\FORCING_2ND_PHASE\\'+str_station+'_Precipitation_Scenarios\\'+str_pre+'\\'+ stryear+ '-0'+ strmonth+ '.nc'
        else:
            strfile = 'E:\Single_coloum\FORCING_2ND_PHASE\\'+str_station+'_Precipitation_Scenarios\\'+str_pre+'\\' + stryear + '-' + strmonth + '.nc'
        if not(os.path.exists(strfile)):
            ncfile = nc.Dataset(strfile, 'w', format='NETCDF4')
            ncfile.createDimension('lon', len(var_Long))
            ncfile.createDimension('lat', len(var_Lat))
            ncfile.createDimension('time', size = None)
            ncfile.createDimension('scalar', 1)
            #ncfile.history = 'Created ' + time.ctime(time.time())

            edgew = ncfile.createVariable('EDGEW', 'f8', ('scalar',))
            edgew.long_name = 'western edge in atmospheric data'
            edgew.units = 'degrees E'
            edgew.mode = 'time-invariant'



            edgee = ncfile.createVariable('EDGEE', 'f8', ('scalar',))
            edgee.long_name = 'Eastern edge in atmospheric data'
            edgee.units = 'degrees E'
            edgee.mode = 'time-invariant'


            longxy = ncfile.createVariable('LONGXY', 'f8', ('lat', 'lon'))
            longxy.long_name = 'longitude'
            longxy.units = 'degrees E'
            longxy.mode = 'time-invariant'


            edgen = ncfile.createVariable('EDGEN', 'f8', ('scalar',))
            edgen.long_name = 'northern edge in atmospheric data'
            edgen.units = 'degrees N'
            edgen.mode = 'time-invariant'


            edges = ncfile.createVariable('EDGES', 'f8', ('scalar',))
            edges.long_name = 'southern edge in atmospheric data'
            edges.units = 'degrees N'
            edges.mode = 'time-invariant'


            latixy = ncfile.createVariable('LATIXY', 'f8', ('lat', 'lon'))
            latixy.long_name = 'latitude'
            latixy.units = 'degrees N'
            latixy.mode = 'time-invariant'

            edgew[0] = 95.6250
            edgee[0] = 96.8750
            longxy[0, 0] = 96.2500
            edgen[0] = 40.523560209424060
            edges[0] = 39.581151832460720
            latixy[0, 0] = 40.052356020942390

            Time = ncfile.createVariable('time', 'f8', ('time'))
            Time.long_name = 'observation time'
            #Time.units = 'days since 0000-01-01 00:00:00'
            #Time.units = 'days since 1999-05-12 00:00:00'
            Time.units = 'days since 1982-04-22 00:00:00'
            Time.calendar = 'noleap'

            flds = ncfile.createVariable('FLDS', 'f8', ('time', 'lat', 'lon'))
            flds.long_name = 'incident longwave (FLDS)'
            flds.units = 'W/m2'
            flds.mode = 'time-dependent'


            fsds = ncfile.createVariable('FSDS', 'f8', ('time', 'lat', 'lon'))
            fsds.long_name = 'incident solar (FLDS)'
            fsds.units = 'W/m2'
            fsds.mode = 'time-dependent'


            #fsdsdif = ncfile.createVariable('FLDSdif', 'f4', ('time', 'lat', 'lon'))
            #fsdsdir = ncfile.createVariable('FLDSdir', 'f4', ('time', 'lat', 'lon'))
            prectmms = ncfile.createVariable('PRECTmms', 'f8', ('time', 'lat', 'lon'))
            prectmms.long_name = 'precipitation (PRECTmms)'
            prectmms.units = 'mm/s'
            prectmms.mode = 'time-dependent'


            psrf = ncfile.createVariable('PSRF', 'f8', ('time', 'lat', 'lon'))
            psrf.long_name = 'pressure at the lowest atm level (PSRF)'
            psrf.units = 'Pa'
            psrf.mode = 'time-dependent'


            rh = ncfile.createVariable('RH', 'f8', ('time', 'lat', 'lon'))
            rh.long_name = 'relative humidity at the lowest atm level (RH)'
            rh.units = '%'
            rh.mode = 'time-dependent'


            shum = ncfile.createVariable('SHUM', 'f8', ('time', 'lat', 'lon'))
            shum.long_name = 'specific humidity at the lowest atm level (SHUM)'
            shum.units = 'kg/kg'
            shum.mode = 'time-dependent'

            tbot = ncfile.createVariable('TBOT', 'f8', ('time', 'lat', 'lon'))
            tbot.long_name = 'temperature at the lowest atm level (TBOT)'
            tbot.units = 'K'
            tbot.mode = 'time-dependent'


            #tdew = ncfile.createVariable('TDEW', 'f4', ('time', 'lat', 'lon'))
            wind = ncfile.createVariable('WIND', 'f8', ('time', 'lat', 'lon'))
            wind.long_name = 'wind at the lowest atm level (WIND)'
            wind.units = 'm/s'
            wind.mode = 'time-dependent'


            zbot = ncfile.createVariable('ZBOT', 'f8', ('time', 'lat', 'lon'))
            zbot.long_name = 'observational height'
            zbot.units = 'm'
            zbot.mode = 'time-dependent'

            #vp = ncfile.createVariable('VP', 'f4', ('time', 'lat', 'lon'))
            #ld = ncfile.createVariable('LD', 'f4', ('time', 'lat', 'lon'))
            #sab1 = ncfile.createVariable('SAB1', 'f4', ('time', 'lat', 'lon'))
            #sab2 = ncfile.createVariable('SAB2', 'f4', ('time', 'lat', 'lon'))
            #sad1 = ncfile.createVariable('SAD1', 'f4', ('time', 'lat', 'lon'))
            #sad2 = ncfile.createVariable('SAD2', 'f4', ('time', 'lat', 'lon'))
            #parb = ncfile.createVariable('PARB', 'f4', ('time', 'lat', 'lon'))
            #pard = ncfile.createVariable('PARD', 'f4', ('time', 'lat', 'lon'))
            index_previous = index_previous + index + 1
            ncfile.close()

        ncfile = nc.Dataset(strfile, 'a', format='NETCDF4')
        index = int((var_Day[num]-1)*24 + var_Hour[num])
        if var_Year[num] == 1999 and var_Month[num] == 5:       #Garraf
            index = int((var_Day[num] - 12) * 24 + var_Hour[num]-1)
        else:
            index = int((var_Day[num] - 1) * 24 + var_Hour[num])

        if var_Year[num] == 1982 and var_Month[num] == 4:  # Konza
            index = int((var_Day[num] - 22) * 24 + var_Hour[num] - 11)
        else:
            index = int((var_Day[num] - 1) * 24 + var_Hour[num])

        time1 = var_Date[index + index_previous] - time_skip
        ncfile.variables['time'][index] = time1
        #time[index] = var_Date[0][index]
        ncfile.variables['FLDS'][index,0,0] = var_LongDown[index + index_previous]
        #flds[index][0][0] = var_LongDown[0][index]
        ncfile.variables['FSDS'][index, 0, 0] = var_Rsw[index + index_previous]
        ncfile.variables['PRECTmms'][index, 0, 0] = var_Precip[index + index_previous]/3600
        ncfile.variables['PSRF'][index, 0, 0] = var_Pressure[index + index_previous] * 100
        ncfile.variables['TBOT'][index, 0, 0] = var_Temp[index + index_previous] + 273.15
        ncfile.variables['RH'][index, 0, 0] = var_RelHhum[index + index_previous]
        ncfile.variables['WIND'][index, 0, 0] = var_WindSpeed[index + index_previous]
        ncfile.variables['SHUM'][index, 0, 0] = var_q_hum[index + index_previous]
        ncfile.variables['ZBOT'][index, 0, 0] = 2
        ncfile.close()










