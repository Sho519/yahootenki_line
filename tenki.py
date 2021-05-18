

import datetime
import schedule
import requests 
import time
	
#Yahoo天気RSS(岐阜)の取得
url = 'https://rss-weather.yahoo.co.jp/rss/days/5210.xml'
html_data = requests.get(url)


from bs4 import BeautifulSoup

#BSによる解析
soup = BeautifulSoup(html_data.text,'html.parser')

#print(html_data.text)
#↑より，欲しい情報の抽出
tenki_today = soup.item.title.text


			
#ーーーーーLINE通知ーーーー	
#取得したLINEトークン	
token = 'XXXXXXXXXXXXXXXXXXXXXXXXX'
#APIのURL
api_url = 'https://notify-api.line.me/api/notify'

#情報の辞書型化
token_dic = {'Authorization': 'Bearer' + ' ' + token}
send_dic = {'message': tenki_today}



#天気取得，解析，抽出，送信の関数化
def job():
	html_data
	requests.post(api_url, headers=token_dic, data=send_dic)
			
			

#06：00に実行
schedule.every().day.at("06:00").do(job)

#毎日繰り返す
while True:
	schedule.run_pending()
	time.sleep(1)
	

