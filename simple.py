import urllib.parse
from bs4 import BeautifulSoup
from urllib.request import urlopen
from unidecode import unidecode


#link = "http://m.hnsmall.com/search?query_top=여성샌달&trackingarea=#[{"query":"여성샌달","totalQuery":"여성샌달","firstQuery":"여성샌달","saveamtType":"","minPrice":"0","maxPrice":"0","benefit":"","cate_M":"","cate_S":"","brandCode":"","sort":"RANK/DESC","refreshFlag":"","researchFlag":"","sourcingMedia":""}]"
#http://m.hnsmall.com/search?query_top=여성샌달&trackingarea=#[{"query":"여성샌달","totalQuery":"여성샌달","firstQuery":"여성샌달","sort":"RANK/DESC"}]
#link = http://m.hnsmall.com/search?query_top=여성샌달&trackingarea=#[{"query":"여성샌달","totalQuery":여성샌달","firstQuery":"여성샌달","saveamtType":"","minPrice":"0","maxPrice":"0","benefit":"","cate_M":"","cate_S":"","brandCode":"","sort":"RANK/DESC","refreshFlag":"","researchFlag":"","sourcingMedia":""}]
#link = "http://m.hnsmall.com/search?query_top=%EB%82%A8%EC%84%B1%EC%83%8C%EB%8B%AC#[{%22query%22:%22%EB%82%A8%EC%84%B1%EC%83%8C%EB%8B%AC%22,%22totalQuery%22:%22%EB%82%A8%EC%84%B1%EC%83%8C%EB%8B%AC%22,%22firstQuery%22:%22%EB%82%A8%EC%84%B1%EC%83%8C%EB%8B%AC%22,%22saveamtType%22:%22%22,%22minPrice%22:%220%22,%22maxPrice%22:%220%22,%22benefit%22:%22%22,%22cate_M%22:%22%22,%22cate_S%22:%22%22,%22brandCode%22:%22%22,%22sort%22:%22RANK/DESC%22,%22refreshFlag%22:%22%22,%22researchFlag%22:%22%22,%22sourcingMedia%22:%22%22}]"

#urlToOpen = '''http://m.hnsmall.com/search?query_top=여성샌달&trackingarea=#[{"query":"여성샌달","totalQuery":"여성샌달","firstQuery":"여성샌달","sort":"RANK/DESC"}]'''

urlToOpen = '''http://m.hnsmall.com/search?query_top=여성샌달&trackingarea=#[{"query":"여성샌달","totalQuery":"여성샌달","firstQuery":"여성샌달","saveamtType":"","minPrice":"0","maxPrice":"0","benefit":"","cate_M":"","cate_S":"","brandCode":"","sort":"RANK/DESC","refreshFlag":"","researchFlag":"","sourcingMedia":""}]'''

link = urlToOpen.encode('utf-8')


keyword = "여성샌달"
basic_url = "http://m.hnsmall.com/search?query_top="
#urlToOpen = basic_url + keyword

#link = urllib.parse.quote(urlToOpen, safe=':/?-=')


print(link)
with urlopen(link) as response:
    soup = BeautifulSoup(response, 'html.parser')
    i = 1
        #total_data = " "
    filetowrite = keyword + ".txt"
    f = open(filetowrite, 'w')
    for anchor in soup.find_all('p.title'):
        data = (str(i) + "번: " +anchor.get_text()) + "\n"
        i = i + 1
        print(data)
        f.write(data)
    f.close()
        
     

"""
get_cells = load_ws['B101':'H184']
for r in get_cells:
    for cell in r:
        val = cell.value
        if val in notmatchkeyword:
            #write_ws.cell(row = cell.row, column = cell.column).value = val
            write_ws.cell(row = cell.row, column = cell.column).fill = lightblueFill



write_wb.save("fileToWrite.xlsx")
"""
    
    

