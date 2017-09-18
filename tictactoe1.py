#!/usr/bin/env python
import random
def display(a):
	print ("   |   |")
	print (" "+str(a[0])+" | "+str(a[1])+" | "+str(a[2]))
	print ("   |   |")
	print (" ---------")
	print ("   |   |")
	print (" "+str(a[3])+" | "+str(a[4])+" | "+str(a[5]))
	print ("   |   |")
	print (" ---------")
	print ("   |   |")
	print (" "+str(a[6])+" | "+str(a[7])+" | "+str(a[8]))
	print ("   |   |")
	return " "
#display(a=['0','x','x','0',' ','0','x',' ','x'])



def inputPlayerLetter():
	print ("what u want to play x or 0: ")
	b=raw_input()
	if b=='x':
		return ['x','0']
	else:
		return ['0','x']
#print inputPlayerLetter() 


def whoplayfirst():
	list=["pc","player"]
	return random.sample(list,1)[0]
#print whoplayfirst()


def playerinput():
	print "enter position 1,2,3,4,5,6,7,8,9 which starts from top to bottom left to right!"
	position=input()
	position = position-1
	return position

	
def getrows(i,a):
	listrows=[[a[0],a[1],a[2]],[a[3],a[4],a[5]],[a[6],a[7],a[8]],[a[0],a[3],a[6]],[a[1],a[4],a[7]],[a[2],a[5],a[8]],[a[0],a[4],a[8]],[a[2],a[4],a[6]]]
	return listrows[i]
#print getrows(2)


def blanklist(a):
	blanklist=[]
	i=0
	for everyelement in a:
		if everyelement==' ':
			blanklist=blanklist+[i]
			i=i+1
		else:
			i+=1
	return blanklist
#print blanklist(a)	


def pcplay(a,c):
	#play to win
	flag=1
	for k in range(0,8):
		temp=getrows(k,a)
		#print temp
		i=0
		for everysymbol in temp:
			if everysymbol==c:
				#print "s"
				i=i+1
		if i==2 and flag==1:
			j=0
			for everysymbol in temp:
				if everysymbol==' ':
					del temp[j]
					temp.insert(j,c)
					#print "played to win"
					flag=2
				else:
					j=j+1
		else:
			i=0	
		if k==0:
			a[0]=temp[0]
			a[1]=temp[1]
			a[2]=temp[2]
		if k==1:
			a[3]=temp[0]
			a[4]=temp[1]
			a[5]=temp[2]
		if k==2:
			a[6]=temp[0]
			a[7]=temp[1]
			a[8]=temp[2]
		if k==3:
			a[0]=temp[0]
			a[3]=temp[1]
			a[6]=temp[2]
		if k==4:
			a[1]=temp[0]
			a[4]=temp[1]
			a[7]=temp[2]
		if k==5:
			a[2]=temp[0]
			a[5]=temp[1]
			a[8]=temp[2]
		if k==6:
			a[0]=temp[0]
			a[4]=temp[1]
			a[8]=temp[2]
		if k==7:
			a[2]=temp[0]
			a[4]=temp[1]
			a[6]=temp[2]

	#play to defete player
	flag1=1
	if flag==1:
		
		for k in range(0,8):
			temp=getrows(k,a)
			#print temp
			i=0
			for everysymbol in temp:
				if everysymbol==p:
					#print "s"
					i=i+1
			if i==2 and flag1==1:
				j=0
				for everysymbol in temp:
					if everysymbol==' ':
						del temp[j]
						temp.insert(j,c)
						flag1=2
						#print "played to lose you"
						break
					else:
						j=j+1
			else:
				i=0	
			if k==0:
				a[0]=temp[0]
				a[1]=temp[1]
				a[2]=temp[2]
			if k==1:
				a[3]=temp[0]
				a[4]=temp[1]
				a[5]=temp[2]
			if k==2:
				a[6]=temp[0]
				a[7]=temp[1]
				a[8]=temp[2]
			if k==3:
				a[0]=temp[0]
				a[3]=temp[1]
				a[6]=temp[2]
			if k==4:
				a[1]=temp[0]
				a[4]=temp[1]
				a[7]=temp[2]
			if k==5:
				a[2]=temp[0]
				a[5]=temp[1]
				a[8]=temp[2]
			if k==6:
				a[0]=temp[0]
				a[4]=temp[1]
				a[8]=temp[2]
			if k==7:
				a[2]=temp[0]
				a[4]=temp[1]
				a[6]=temp[2]
				
	#play at random location
	if flag1==1 and flag==1:
		list=blanklist(a)
		corner=[]
		side=[]
		#take random location on corner check weather it is blank then play
		#corner=[] will be list derived for list every time
		for every in list:
			if every==0:
				corner=corner+[every]
			elif every==2:
				corner=corner+[every]
			elif every==6:
				corner=corner+[every]
			elif every==8:
				corner=corner+[every] 
		for every in list:
			if every==7:
				side=side+[every]
			elif every==1:
				side=side+[every]
			elif every==3:
				side=side+[every]
			elif every==5:
				side=side+[every] 
				
		if len(corner)!=0:
			i=random.sample(corner,1)[0]
			temp1=i in list
			if temp1==True :
				a[i]=c		

		#play for side		
				
		elif 4 in list:
			a[4]=c
			
		#play for corner	
		else:
			if (side)!=0:
			
				k=random.sample([1,3,5,7],1)[0]
				temp2=k in list
				if temp2==True:
					a[k]=c
	
	return a
	
#main	
def wins(x):
	win=0
	#check after every move who wins
	for k in range(0,8):
		temp=getrows(k,a)
		if temp[0]==temp[1]==temp[2]==x:
			win=1
	return win
		
			
while 1:
	print "welcome to tic tac toe"
	a=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
	list=inputPlayerLetter()
	p=list[0]
	c=list[1]
	turn=whoplayfirst()
	print 'first '+turn+" will play!"
	print display(a)
	while 1:
		if turn=='player':
			position=playerinput()
			list2=blanklist(a)
			if position in list2:
			
				del a[position]
				a.insert(position,p)
			else:
				print "cannot overwrite"
				continue
				

			display(a)
			win=wins(p)
			if win==1:
				print "player wins"
				break
			#see weather cube is full
			end=blanklist(a)
			if len(end)==0:
				print "draw"
				break
			turn ='pc'
		if turn=='pc':
			a=pcplay(a,c)
			print "pc plays :)"
			display(a)
			win=wins(c)
			if win==1:
				print "pc wins"
				break
			end=blanklist(a)
			if len(end)==0:
				print "draw"
				break
                        turn='player'
	print "do you want to play again (y/n):"
	a1=raw_input()
	if a1=="y":
		continue

	else:
		break
		
	
	
	

