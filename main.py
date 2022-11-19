from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import pandas as pd
#QNX.202122
#thinhparamotor@yahoo.com.vn
#column data
time_table = []
location_table = []
plot_table = []
name_table= []
area_table=[]
duration_table=[]
flyer_table=[]
team_table=[]
#function
def data (value, vl_class):
    for i in value:
        value = i.find_element(By.CLASS_NAME, vl_class)
        return value
def addData (value_data, value_table):
    for value in value_data:
        return value_table.append(value.text)
#end
browser = webdriver.Chrome(executable_path="chromedriver.exe")

browser.get("https://account.dji.com/login?appId=dji_ag2_kr&backUrl=https%3A%2F%2Fagms-us.dji.com%2Fsupervise")
sleep(60)
print("login time out")
#browser.get("http://facebook.com")
#total area..
total_flight_list= browser.find_elements(By.XPATH, "//div[@class='records-statistic-block time']")
total_area_list= browser.find_elements(By.XPATH, "//div[@class='records-statistic-block area']")
total_time_list= browser.find_elements(By.XPATH, "//div[@class='records-statistic-block times']")
#total page
page_content =  browser.find_elements(By.XPATH, "//div[@class='pagination-jump']")
total_page = int(data(page_content, "total-page-txt").text)
next_content= browser.find_elements(By.XPATH, "//div[@class='pagination-container']")
btn_next = data(next_content,"next-page")
for i in range(100):
    start_time = browser.find_elements(By.XPATH, "//td[@class='start_end']")
    location = browser.find_elements(By.XPATH, "//td[@class='location']")
    pilot_name = browser.find_elements(By.XPATH, "//td[@class='plot_name']")
    nickname = browser.find_elements(By.XPATH, "//td[@class='nickname']")
    work_area = browser.find_elements(By.XPATH, "//td[@class='new_work_area']")
    duration = browser.find_elements(By.XPATH, "//td[@class='duration']")
    flyer_name = browser.find_elements(By.XPATH, "//td[@class='flyer_name']")
    team_name = browser.find_elements(By.XPATH, "//td[@class='team_name']")
    for value_time in start_time:
        time_table.append(value_time.text)
    for value_lo in location:
        location_table.append(value_lo.text)
    for value_plot in pilot_name:
        plot_table.append(value_plot.text)
    for valur_name in nickname:
        name_table.append(valur_name.text)
    for value_area in work_area:
        area_table.append(value_area.text)
    for value_du in duration:
        duration_table.append(value_du.text)
    for value_fly in flyer_name:
        flyer_table.append(value_fly.text)
    for value_team in team_name:
        team_table.append(value_team.text)
    btn_next.click()
    sleep(5)

data_export = {
        'Time': time_table,
        'Location': location_table,
        'Fild': plot_table,
        'Name' : name_table,
        'Area': area_table,
        'Duration': duration_table,
        'Pilot Name': flyer_table,
        'Team': team_table
        }

df = pd.DataFrame(data_export)
df.to_excel('D:\export_data.xlsx', sheet_name='sheet1', index=False)

#data
area = data(total_area_list, "content")
total_flight = data(total_flight_list, "content")
total_time = data(total_time_list, "content")
print(area.text)
print(total_flight.text)
print(total_time.text)
print("done")
#print(username)
sleep(2000)
browser.close()