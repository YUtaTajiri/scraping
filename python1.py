from bs4 import BeautifulSoup
import requests
import openpyxl

#2022/12/08に更新
# webページの情報を取得する
site_data = requests.get('https://www.walkerplus.com/event_list/today/ar1046/')
soup = BeautifulSoup(site_data.content, 'html.parser')

#エクセルファイルを開く
from openpyxl import Workbook
wb = Workbook()
sheet = wb.active
sheet.title='スクレイピング結果'
cnt = 2
sheet['A1'].value = 'webサイト1'
sheet.column_dimensions['A'].width= 50
sheet.column_dimensions['B'].width= 43
# 特定のクラスだけ抜き出して表示
links = soup.select('.m-mainlist-item')
for link in links:
    #rstrip()で空白を作ることができる
    data = str(link.span.string).rstrip()
    # Noneを除外する
    if data == 'None':
        continue
    #変数linkの後ろにaタグを続ける事で「’aタグ’の’href’要素」を指定することができる
    sel1 = 'A'+str(cnt)
    sel2 = 'B'+str(cnt)
    result = 'https://www.walkerplus.com' + link.a.get('href')
    sheet[sel1].value = data
    sheet[sel2].value = result
    cnt += 1
    

#webサイト2
site_data2 = requests.get('https://www.tjkagoshima.com/events/')
soup2 = BeautifulSoup(site_data2.content, 'html.parser')
cnt_2 = 2
sheet['D1'].value = 'webサイト2'
links2 = soup2.select('.col-xs-6.col-sm-3')
sheet.column_dimensions['D'].width= 80
sheet.column_dimensions['E'].width= 40
for link2 in links2:
    #rstrip()で空白を作ることができる
    data2 = link2.text.rstrip()
    data2_limit = data2[:50]
    # Noneを除外する
    if data2 == 'None':
        continue
    #変数linkの後ろにaタグを続ける事で「’aタグ’の’href’要素」を指定することができる
    result2 =  link2.a.get('href')
    sel3 = 'D'+str(cnt_2)
    sel4 = 'E'+str(cnt_2)
    sheet[sel3].value = data2_limit
    sheet[sel4].value = result2
    cnt_2 += 1
    
    
#エクセルファイルの保存
wb.save('text.xlsx')



