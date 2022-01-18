import random
block = [0,1,2,3,4,5,6,7,8]#マス
def board():
	for i in range(0, len(block)):
		if(i%3 == 2):
			print(block[i])
		else :
			print(block[i],end="")

def input_board(key_type):
	try:	
		if(key_type == "o"):
			
				target = int(input("\n0~8の座標を入力:"))
		else:
			target = random.randint(0,8)
		
		if(block[target] == "o" or block[target] == "x"):
			input_board(key_type)

		else:
			block[target] = key_type
	except:
		print("正しい数字を入力してください")
		return input_board(key_type)
def judge():
	line = [
		[0,1,2],
		[3,4,5],
		[6,7,8],
		[0,3,6],
		[1,4,7],
		[2,5,8],
		[0,4,8],
		[2,4,6],
	]

	for i in range(0,len(line)):
		[a,b,c] = line[i]
		if block[a] and block[a] == block[b] and block[a] == block[c]:
			return block[a]
	return None
while(True):
	try:
		order = int(input("先攻なら0 後攻なら1を入力:"))
	except:
			print("正しい数字を入力してください")
	if(order == 0 or order == 1):
		break
board()
for i in range(0, len(block)):
	if(i%2 == 0+order):
		input_board("o")
	else :
		input_board("x")
		print("\nCPUの番")
	board()

	if judge():
		print(judge() + "の勝ち")
		break

	if i == 8:
		print("引き分け")
		break