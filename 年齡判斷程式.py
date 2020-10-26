#先詢問有沒有開過車，有的話 18歲了嗎?沒有18歲的話怎樣?
#另外如果沒有開過車，年齡到了就可以考了
driving = input('請問有開過車嗎？')
if driving != '有' and driving != '沒有':   # != 不等於
   print('只能輸入有/沒有')
   raise SystemExit    #觸發 系統離開 
age = input('請問您的年齡？')
age = int(age)
if driving == '有':
	if age >= 18:
		print('恭喜通過測驗了')
	else:
		print('您的年齡尚未允許開車喔')
elif driving == '沒有':
	if age >= 18:
		print('您可以考慮考駕照囉')
	if age < 18:
		print('很好')
