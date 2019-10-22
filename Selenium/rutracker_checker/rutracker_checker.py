import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#counters 
count_ok = 0
count_nok = 0
count_try = 0

for count_try in range(0, 10000):
    driver = webdriver.Ie()
    driver.get("http://rutracker.org/forum/index.php")
    
    if "BitTorrent" in driver.title:
        #print ('ok')
        count_ok = count_ok + 1
    
    else:
        #print ('nok')
        count_nok = count_nok + 1
    
    count_try=count_try + 1
 
    #print ('Открылось сайтов count_ok = ', count_ok)
    #print ('Не открылось сайтов count_nok = ', count_nok)
    #print ('========================')    
    #print ('iteration = ',  count_try,  ' waiting...')    
    
    print ('========================')
    if count_try == count_nok:
        print ('Ни один сайт ни разу не открылся, попытка ', count_try)
    else:
        print ('Открылось сайтов', count_ok, 'из попыток', count_try,', Процент открывшихся = ', (count_ok/count_try)*100, '%')
	
    time.sleep(5)
    driver.close()
 
 

 
 

