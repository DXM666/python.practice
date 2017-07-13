from random import randint
name = input('请输入你的名字：')

f = open('game.txt')
lines = f.readlines()
f.close()

scores ={}
for i in lines:
    s = i.split()
    scores[s[0]] = s[:1]
score = scores.get(name)

if score is None:
    score = [0,0,0]


game_times = int(score[0])
min_times = int(score[1])
total_times = int(score[2])
if game_times > 0:
    avg_times = float(total_times)/game_times
else:
    avg_times = 0
print ('%s,你已经玩了%d次，最少%d轮猜出答案，平均%.2f轮猜出答案' \
      % (name,game_times, min_times, avg_times))
num = randint(1,100)
times = 0
print('Guess what I think')
bingo = True
while bingo == True:
    answer = input()
    if int(answer) > num:
     print('%s too big'%answer)
    elif int(answer) < num:
        print('%s too small'%answer)
    else:
         bingo == False
         print('bingo,%s is the right'%answer)
         break

if game_times ==0 or times < min_times:
    min_times = times
total_times += times
game_times += 1

scores[name] = [str(game_times), str(min_times), str(total_times)]
result = ''
for n in scores:
   line = n + ' ' + ' '.join(scores[n]) + '\n'
   result += line

f = open('game.txt','w')
f.write(result)
f.close()
