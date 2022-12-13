import pyautogui as p

import time

time.sleep(2) #내가 원하는 위치에 마우스 커서가 이동할 시간 확보용

print(p.position()) # 현재 x축과 y축의 좌표
print(p.size())     #현재 x축과 y축의 좌표
print(p.onScreen(300, 300)) #현재 커서가 메인 모니터의 가로 세로 크기 안에 들어가는지 bool 반환
print(p.moveTo(300,300, duration = 1)) #이동하고자 하는 xy좌표로 이동한다. 이동시간은 duration옵션에서 초단위로 설정가능

#Point()