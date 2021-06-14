import requests
import xml.etree.ElementTree as ET
import pandas as pd
import gspread
from gspread_dataframe import set_with_dataframe



data = {'COUNTRY': [],
        'GHO': [],
        'SEX': [],
        'YEAR': [],
        'GHECAUSES': [],
        'AGEGROUP': [],
        'Display': [],
        'Numeric': [],
        'Low': [],
        'High': []}

index = ['Number of deaths', 'Number of infant deaths', 'Number of under-five deaths', 'Mortality rate for 5-14 year-olds (probability of dying per 1000 children aged 5-14 years)', 'Adult mortality rate (probability of dying between 15 and 60 years per 1000 population)',
         'Estimates of number of homicides', 'Crude suicide rates (per 100 000 population)', 'Mortality rate attributed to unintentional poisoning (per 100 000 population)',
         'Number of deaths attributed to non-communicable diseases, by type of disease and sex', 'Estimated road traffic death rate (per 100 000 population)',
         'Estimated number of road traffic deaths', 'Mean BMI (kg/m&#xb2;) (crude estimate)', 'Mean BMI (kg/m&#xb2;) (age-standardized estimate)',
         'Prevalence of obesity among adults, BMI &GreaterEqual; 30 (age-standardized estimate) (%)', 'Prevalence of obesity among children and adolescents, BMI > +2 standard deviations above the median (crude estimate) (%)',
         'Prevalence of overweight among adults, BMI &GreaterEqual; 25 (age-standardized estimate) (%)', 'Prevalence of overweight among children and adolescents, BMI > +1 standard deviations above the median (crude estimate) (%)',
         'Prevalence of underweight among adults, BMI < 18.5 (age-standardized estimate) (%)', 'Prevalence of thinness among children and adolescents, BMI < -2 standard deviations below the median (crude estimate) (%)',
         'Alcohol, recorded per capita (15+) consumption (in litres of pure alcohol)', 'Estimate of daily cigarette smoking prevalence (%) (age-standardized rate)',
         'Estimate of daily tobacco smoking prevalence (%)', 'Estimate of current cigarette smoking prevalence (%)', 'Estimate of current tobacco smoking prevalence (%) (age-standardized rate)',
         'Mean systolic blood pressure (crude estimate)', 'Mean fasting blood glucose (mmol/l) (crude estimate)', 'Mean Total Cholesterol (crude estimate)']

r = requests.get('http://tarea-4.2021-1.tallerdeintegracion.cl/gho_CHL.xml')

root = ET.fromstring(r.content)

for node in root:
    if str(type(node.find('GHO'))) != "<class 'NoneType'>":
        if node.find('GHO').text in index:
            usado_low = False
            usado_numeric = False
            usado_high = False

            for child in node:
                if usado_low == False:
                    if str(type(node.find('Low'))) == "<class 'NoneType'>":
                        data['Low'].append(None)
                        usado_low = True

                if usado_numeric == False:
                    if str(type(node.find('Numeric'))) == "<class 'NoneType'>":
                        data['Numeric'].append(None)
                        usado_numeric = True

                if usado_high == False:
                    if str(type(node.find('High'))) == "<class 'NoneType'>":
                        data['High'].append(None)
                        usado_high = True

                if child.tag == "GHO":
                    data['GHO'].append(child.text)

                elif child.tag == 'YEAR':
                    data['YEAR'].append(child.text)

                elif child.tag == 'COUNTRY':
                    data['COUNTRY'].append(child.text)

                elif child.tag == 'SEX':
                    data['SEX'].append(child.text)

                elif child.tag == 'GHECAUSES':
                    data['GHECAUSES'].append(child.text)

                elif child.tag == 'AGEGROUP':
                    data['AGEGROUP'].append(child.text)

                elif child.tag == 'Display':
                    data['Display'].append(child.text)

                elif child.tag == 'Numeric':
                    data['Numeric'].append(float(child.text))

                elif child.tag == 'Low':
                    data['Low'].append(float(child.text))

                elif child.tag == 'High':
                    data['High'].append(float(child.text))


r = requests.get('http://tarea-4.2021-1.tallerdeintegracion.cl/gho_KOR.xml')

root = ET.fromstring(r.content)

for node in root:
    if str(type(node.find('GHO'))) != "<class 'NoneType'>":
        if node.find('GHO').text in index:
            usado_low = False
            usado_numeric = False
            usado_high = False

            for child in node:
                if usado_low == False:
                    if str(type(node.find('Low'))) == "<class 'NoneType'>":
                        data['Low'].append(None)
                        usado_low = True

                if usado_numeric == False:
                    if str(type(node.find('Numeric'))) == "<class 'NoneType'>":
                        data['Numeric'].append(None)
                        usado_numeric = True

                if usado_high == False:
                    if str(type(node.find('High'))) == "<class 'NoneType'>":
                        data['High'].append(None)
                        usado_high = True

                if child.tag == "GHO":
                    data['GHO'].append(child.text)

                elif child.tag == 'YEAR':
                    data['YEAR'].append(child.text)
                elif child.tag == 'COUNTRY':
                    data['COUNTRY'].append(child.text)
                elif child.tag == 'SEX':
                    data['SEX'].append(child.text)
                elif child.tag == 'GHECAUSES':
                    data['GHECAUSES'].append(child.text)
                elif child.tag == 'AGEGROUP':
                    data['AGEGROUP'].append(child.text)
                elif child.tag == 'Display':
                    data['Display'].append(child.text)
                elif child.tag == 'Numeric':
                    data['Numeric'].append(float(child.text))
                elif child.tag == 'Low':
                    data['Low'].append(float(child.text))
                elif child.tag == 'High':
                    data['High'].append(float(child.text))

r = requests.get('http://tarea-4.2021-1.tallerdeintegracion.cl/gho_BRA.xml')

root = ET.fromstring(r.content)

for node in root:
    if str(type(node.find('GHO'))) != "<class 'NoneType'>":
        if node.find('GHO').text in index:
            usado_low = False
            usado_numeric = False
            usado_high = False

            for child in node:
                if usado_low == False:
                    if str(type(node.find('Low'))) == "<class 'NoneType'>":
                        data['Low'].append(None)
                        usado_low = True

                if usado_numeric == False:
                    if str(type(node.find('Numeric'))) == "<class 'NoneType'>":
                        data['Numeric'].append(None)
                        usado_numeric = True

                if usado_high == False:
                    if str(type(node.find('High'))) == "<class 'NoneType'>":
                        data['High'].append(None)
                        usado_high = True

                if child.tag == "GHO":
                    data['GHO'].append(child.text)

                elif child.tag == 'YEAR':
                    data['YEAR'].append(child.text)
                elif child.tag == 'COUNTRY':
                    data['COUNTRY'].append(child.text)
                elif child.tag == 'SEX':
                    data['SEX'].append(child.text)
                elif child.tag == 'GHECAUSES':
                    data['GHECAUSES'].append(child.text)
                elif child.tag == 'AGEGROUP':
                    data['AGEGROUP'].append(child.text)
                elif child.tag == 'Display':
                    data['Display'].append(child.text)
                elif child.tag == 'Numeric':
                    data['Numeric'].append(float(child.text))
                elif child.tag == 'Low':
                    data['Low'].append(float(child.text))
                elif child.tag == 'High':
                    data['High'].append(float(child.text))

r = requests.get('http://tarea-4.2021-1.tallerdeintegracion.cl/gho_DEU.xml')

root = ET.fromstring(r.content)

for node in root:
    if str(type(node.find('GHO'))) != "<class 'NoneType'>":
        if node.find('GHO').text in index:
            usado_low = False
            usado_numeric = False
            usado_high = False

            for child in node:
                if usado_low == False:
                    if str(type(node.find('Low'))) == "<class 'NoneType'>":
                        data['Low'].append(None)
                        usado_low = True

                if usado_numeric == False:
                    if str(type(node.find('Numeric'))) == "<class 'NoneType'>":
                        data['Numeric'].append(None)
                        usado_numeric = True

                if usado_high == False:
                    if str(type(node.find('High'))) == "<class 'NoneType'>":
                        data['High'].append(None)
                        usado_high = True

                if child.tag == "GHO":
                    data['GHO'].append(child.text)

                elif child.tag == 'YEAR':
                    data['YEAR'].append(child.text)
                elif child.tag == 'COUNTRY':
                    data['COUNTRY'].append(child.text)
                elif child.tag == 'SEX':
                    data['SEX'].append(child.text)
                elif child.tag == 'GHECAUSES':
                    data['GHECAUSES'].append(child.text)
                elif child.tag == 'AGEGROUP':
                    data['AGEGROUP'].append(child.text)
                elif child.tag == 'Display':
                    data['Display'].append(child.text)
                elif child.tag == 'Numeric':
                    data['Numeric'].append(float(child.text))
                elif child.tag == 'Low':
                    data['Low'].append(float(child.text))
                elif child.tag == 'High':
                    data['High'].append(float(child.text))

r = requests.get('http://tarea-4.2021-1.tallerdeintegracion.cl/gho_FRA.xml')

root = ET.fromstring(r.content)

for node in root:
    if str(type(node.find('GHO'))) != "<class 'NoneType'>":
        if node.find('GHO').text in index:
            usado_low = False
            usado_numeric = False
            usado_high = False

            for child in node:
                if usado_low == False:
                    if str(type(node.find('Low'))) == "<class 'NoneType'>":
                        data['Low'].append(None)
                        usado_low = True

                if usado_numeric == False:
                    if str(type(node.find('Numeric'))) == "<class 'NoneType'>":
                        data['Numeric'].append(None)
                        usado_numeric = True

                if usado_high == False:
                    if str(type(node.find('High'))) == "<class 'NoneType'>":
                        data['High'].append(None)
                        usado_high = True

                if child.tag == "GHO":
                    data['GHO'].append(child.text)

                elif child.tag == 'YEAR':
                    data['YEAR'].append(child.text)
                elif child.tag == 'COUNTRY':
                    data['COUNTRY'].append(child.text)
                elif child.tag == 'SEX':
                    data['SEX'].append(child.text)
                elif child.tag == 'GHECAUSES':
                    data['GHECAUSES'].append(child.text)
                elif child.tag == 'AGEGROUP':
                    data['AGEGROUP'].append(child.text)
                elif child.tag == 'Display':
                    data['Display'].append(child.text)
                elif child.tag == 'Numeric':
                    data['Numeric'].append(float(child.text))
                elif child.tag == 'Low':
                    data['Low'].append(float(child.text))
                elif child.tag == 'High':
                    data['High'].append(float(child.text))

r = requests.get('http://tarea-4.2021-1.tallerdeintegracion.cl/gho_USA.xml')

root = ET.fromstring(r.content)

for node in root:
    if str(type(node.find('GHO'))) != "<class 'NoneType'>":
        if node.find('GHO').text in index:
            usado_low = False
            usado_numeric = False
            usado_high = False

            for child in node:
                if usado_low == False:
                    if str(type(node.find('Low'))) == "<class 'NoneType'>":
                        data['Low'].append(None)
                        usado_low = True

                if usado_numeric == False:
                    if str(type(node.find('Numeric'))) == "<class 'NoneType'>":
                        data['Numeric'].append(None)
                        usado_numeric = True

                if usado_high == False:
                    if str(type(node.find('High'))) == "<class 'NoneType'>":
                        data['High'].append(None)
                        usado_high = True

                if child.tag == "GHO":
                    data['GHO'].append(child.text)

                elif child.tag == 'YEAR':
                    data['YEAR'].append(child.text)

                elif child.tag == 'COUNTRY':
                    data['COUNTRY'].append(child.text)
                elif child.tag == 'SEX':
                    data['SEX'].append(child.text)
                elif child.tag == 'GHECAUSES':
                    data['GHECAUSES'].append(child.text)
                elif child.tag == 'AGEGROUP':
                    data['AGEGROUP'].append(child.text)
                elif child.tag == 'Display':
                    data['Display'].append(child.text)
                elif child.tag == 'Numeric':
                    data['Numeric'].append(float(child.text))
                elif child.tag == 'Low':
                    data['Low'].append(float(child.text))
                elif child.tag == 'High':
                    data['High'].append(float(child.text))

df = pd.DataFrame(data)
print(df['Numeric'])

gc = gspread.service_account(filename = 'taller-tarea-4-316720-ccb16a41f781.json')
sh = gc.open_by_key('1YYmekD7RvJVpeAKBP_HVgZATHIZbUWRl9HpvGwV3aJo')
worksheet = sh.get_worksheet(0)

worksheet.clear()

set_with_dataframe(worksheet, df)

