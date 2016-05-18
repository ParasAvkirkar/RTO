__author__ = 'Paras'
import RTODB
from selenium import webdriver
import os
import time

driverBrowser = webdriver.Firefox()
#driverBrowser = webdriver.PhantomJS()
#driverBrowser.set_window_size(0, 0, windowHandle='current')

url = 'https://en.wikipedia.org/wiki/List_of_RTO_districts_in_India'

driverBrowser.get(url)
time.sleep(7)


mwContentDiv = driverBrowser.find_element_by_id('mw-content-text')
allWikiTablesNeeded = mwContentDiv.find_elements_by_class_name('wikitable')
allMwHeadElements = mwContentDiv.find_elements_by_class_name('mw-headline')
# for el in allMwHeadElements:
#     print el
targetFile = open('out1.txt', 'w')
index = 0
loopCount = 0
for el in allMwHeadElements:
    loopCount += 1
    if("." in el.get_attribute("id")):
        allHrefElements = el.find_elements_by_tag_name('a')
        #Getting parent of span containing MwHeadline
        if(len(allHrefElements) > 0):
            headerString = allHrefElements[0].get_attribute('text')
            district = headerString
            targetFile.write(headerString + '\n')
            #Following code is to print the table for every header except for Tripura State as it does not have a table
            if("Tripura" not in headerString):
                wikiTable = allWikiTablesNeeded[index]
                print 'wikitable found'
                allRows = wikiTable.find_elements_by_tag_name('tr')
                for row in allRows:
                    allDataColumns = row.find_elements_by_tag_name('td')
                    code = ""
                    first = True
                    for td in allDataColumns:
                        element_text = td.text
                        element_attribute_value = td.get_attribute('value')

                        #print element
                        temp = element_text
                        temp = temp.encode('ascii', 'ignore')
                         
                        if(first):
                            first = False
                            code = temp
                        else:
                            RTODB.insertRTO(code, temp, district) 
                        #temp = '{0}'.format(element_text)
                        #targetFile.write(u'{0}'.format(element_text))
                        targetFile.write(u'{0}'.format(temp))
                        #targetFile.write(temp)
                        #targetFile.write('td.get_attribute(\'value\'): {0}'.format(element_attribute_value))
                        #targetFile.write(td.get_attribute('text'))
                        targetFile.write(" ")
                    targetFile.write('\n')
                index += 1
            targetFile.write('\n')
            #print allHrefElements[0].get_attribute('text')

print loopCount

driverBrowser.close()
driverBrowser.quit()
