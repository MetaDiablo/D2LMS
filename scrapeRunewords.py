"""
    D2LMS v0.1 - A Diablo 2 Item Scraper/Sorter for Laravel Migration Seeds
    Copyright (C) 2019  Virtual Solutions (https://mivirtualsolutions.com)

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import requests
import json

# Collect the runewords
page = requests.get('https://metadiablo.com/API/items/runewords')

#print the response; 200 response we hope.
print(page)

#grab the text from the page
dump=page.text

#dict the page
data=json.loads(dump)

#start index at 0
subIndex=0

#buffer for item stats in each iteration.
statBuffer=[]

for item in data['runewords']:
    #print the item we are working with.
    #print('item: ' + str(item))
    #grab the completedStats list from said item.
    for subItem in item['completedStats']:
        #how many completedStats are on this subItem?
        #print(str('total stats: ') + str(len(item['completedStats'])))
        #If there are 8 stats, we increase index by 1 each iteration to grab useful info out of the next loop.
        #print (str(subIndex) + ' - ' + subItem)
        statBuffer.append(subItem+'<br>')
        subIndex+=1
        #we've gone through all of the completedStats
        if subIndex == len(item['completedStats']):
            #throw the buffer up and reset the index.
            subIndex=0
    #print(statBuffer)
    # using list comprehension 
    listToStr = ' '.join(map(str, statBuffer)) 
    print ("array('name'=>'" + item['runeword'] + "', 'allowedItems'=> '" + item['allowedItems'] + "', 'runeOrder' => '" + item['runeOrder'] + "', 'completeStats' => '" + listToStr + "','ladderOnly' => '" + str(item['ladderOnly']) + "','patchIntroduced' => '" + item['patchIntroduced'] + "'),\n")
    statBuffer.clear()
