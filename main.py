import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import urllib
import util
import datetime

PAGE_LOAD_WAIT_TIME=1

monthlist=["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"]

monthdict={'JAN':0,'FEB':1,'MAR':2,'APR':3,'MAY':4,'JUN':5,'JUL':6,'AUG':7,'SEP':8,'OCT':9,'NOV':10,'DEC':11}

base_url="https://www.codechef.com/rankings/"

append_fir_url="?order=asc&search="

append_url="&sortBy=rank"

# returns a list of months to check rank list in
def get_months(period):
	s_m=period[0:3]
	s_y=period[3:5]
	e_m=period[6:9]
	e_y=period[9:11]
	rank_m_list=[]
	#rank_m_list.append(s_m+s_y)
	cur_y=s_y
	cur_m=s_m
	s_s=cur_m+cur_y
	e_s=e_m+e_y
	while(s_s!=e_s):
		if(cur_m=="DEC"):
			cur_y=str(int(cur_y)+1)
		rank_m_list.append(s_s)
		temp_v=(int(monthdict[cur_m]) + 1)%12
		cur_m=monthlist[temp_v]
		s_s=cur_m+cur_y
	rank_m_list.append(e_s)
	return rank_m_list
	
def get_rankings(driver,h1,m_d):
	ran_king=[]
	for m in m_d:
		t_url=base_url+str(m)+append_fir_url+str(h1)+append_url
		driver.get(t_url)
		time.sleep(PAGE_LOAD_WAIT_TIME)
		y=driver.execute_script("var x=document.querySelector('[title=\"1\"]\');if(x!=null) return x.innerText")
		if y is not None:
			ran_king.append(int(y))
		else:
			ran_king.append(-1)
	return ran_king


handle_1=raw_input("Enter handle of first user: ")
handle_2=raw_input("Enter handle of second user: ")
period=raw_input("Enter period for comparison(MMMYY-MMMYY): ") 
now = datetime.datetime.now()

current_y=now.year
current_m=now.month-1  #for the correct index

chrome_options = Options()
chrome_options.add_argument('headless')
chrome_options.add_argument('start-maximized')
	

driver = webdriver.Chrome(chrome_options=chrome_options)

# get lsit of months
months_to_check=[]
months_to_check=get_months(period)
print months_to_check

# get 1st user ranklist

rank_list_1=get_rankings(driver,handle_1,months_to_check)

# get 2nd user ranklist

rank_list_2=get_rankings(driver,handle_2,months_to_check)

print rank_list_1,rank_list_2
le=len(rank_list_1)

# call util for graph drawing

util.draw_graph(rank_list_1,rank_list_2,le)


driver.close()
