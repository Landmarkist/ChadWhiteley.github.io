migration_scenario1= '0.0 Scen'
migration_scenario2= '0.5 Scen'
migration_scenario3= '1.0 Scen'   
   
# Get the directory name for data files
import os.path
import numpy as np

directory = os.path.dirname(os.path.abspath(__file__)) 

years=np.array([2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026,2027,2028,2029,2030,2031,2032,2033,2034,2035,2036,2037,2038,2039,2040,2041,2042,2043,2044,2045,2046,2047,2048,2049,2050])
  
#initialize the aggregators
total_scen1=[]
total_scen2=[] 
total_scen3=[]
year1=[]
year2=[]
year3=[]

print('This program generates a projection of population growth in the state of Texas over the next 40 years given an age criteria.')
print('For which age group are you interested? \n Please type a value from the following list: (ALL,<18, 18-24, 25-44, 45-64, 65+)')
age=raw_input()
 
# Scan growth projection file.
for year in range(2010,2050):
    # Open the file
    filename = os.path.join(directory, 'State_of_Texas.txt')
    datafile = open(filename, 'r')
      # Go through all the projections that year
    for line in (datafile):
        _,area_name,migration_scenario,year,age_group,total,total_male,total_female,total_anglo,anglo_male,anglo_female,total_black,black_male,black_female,total_hispanic,hispanic_male,hispanic_female,total_other,other_male,other_female = line.split(',')
    # Accumulate based on migration_scenario1
        if migration_scenario == migration_scenario1 and age_group == age:            
            if year not in year1:
                year1.append(year)
                total_scen1.append(total)
     # Accumulate based on migration_scenario2
        if migration_scenario == migration_scenario2 and age_group == age:
            if year not in year2:
                year2.append(year)
                total_scen2.append(total)
    # Accumulate based on migration_scenario3
        if migration_scenario == migration_scenario3 and age_group == age:
            if year not in year3:
                year3.append(year)
                total_scen3.append(total)
    # Close the file
    datafile.close()

# Plot on one set of axes.
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 1)
ax.plot(year1, total_scen1, '#0000FF')
ax.plot(year2, total_scen2, '#00FF00')
ax.plot(year3, total_scen3, '#FF0000')

ax.set_title('Population Growth of People Ages ' +age +' Given 3 Migration Scenarios: \nScenario 1[Blue]; Scenario 2[Green]; Scenario 3[Red]')
fig.show()