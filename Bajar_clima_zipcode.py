# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 16:41:15 2021

@author: Alejandro Izaguirre
"""

#### Import package

from wwo_hist import retrieve_hist_data


#### Set working directory to store output csv file(s)

import os
os.chdir("C:/Users/Alejandro Izaguirre/Documents/Curso Herramientas computacionales/Scrapping Python/Tarea/Weather")



#### Example code

frequency=24
start_date = '01-JAN-2015'
end_date = '31-DEC-2015'
api_key = '26098d8245194cc7842233300211206'
location_list = ["20682", "20690", "20754", "20781", "20912", "21075", "21132",
                 "21201", "21237", "21401", "21562", "21601", "21651", "21668",
                 "21670", "21787", "21793", "21795", "21853", "21869","21872",
                 "21875", "21921"]

hist_weather_data = retrieve_hist_data(api_key,
                                location_list,
                                start_date,
                                end_date,
                                frequency,
                                location_label = False,
                                export_csv = True,
                                store_df = True)

