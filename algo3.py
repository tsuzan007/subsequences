"""
Sujan Prajapati
Comp 324- Design and Analysis of Algorithms
Spring 2016
Source Code version 1.0

Programming Project 3
	This program finds the Longest Common Subsequence of a
	given pair of strings 
"""



"""
Pre: Two lists are passed to the function.
Post: LCS table is displayed, a multidimensional array is populated from the
		the value of two lists.
"""

def lcs(string1List,string2List,stringList):
	#for loop to populate the multidimensional array or the LCS table
	for i in range (1,len(string1List)):
		for j in range (1,len(string2List)):
			# if two elements are equal, value in multidimensional array is 
			# increase by 1
			if(string1List[i])==(string2List[j]):
				stringList[i][j]=1+stringList[i-1][j-1]
			# else, the maximum between two elements is populated in the table
			else:
				stringList[i][j]=max(stringList[i][j-1],stringList[i-1][j])
	#prints the table
	print("The LCS table is:")
	print("...."*len(string2List))
	count=0
	print(" ",end=" ")
	for a in string2List:
		print ("",a,end=" ")
	print("\n")
	for a in stringList:
		print(string1List[count],a,"\n")
		count=count+1
	print("...."*len(string2List))
	# call subsequence function to find the LCS of  given pair of string
	subsequence(stringList,string1List,string2List)

"""
Pre: Two lists and multidimensional list  are passed to the function.
Post: LCS of given pair of strings is displayed.
"""

def subsequence(stringList,string1List, string2List):
	#initialize two values that will point the bottom rightmost element in the 
	#table
	row1=len(string1List)-1
	column1=len(string2List)-1
	#variable that will point the bottom rightmost element
	ch=stringList[row1][column1]
	print("The Longest Common Subsequence is ",end="")
	#checks the value of bottom rightmost element and run if the value is not 
	# equal to zero
	while(ch!=0):
		#point the same value
		ch=stringList[row1][column1]
		#check the value to zero and run if false
		if (ch!=0):
			# decrement column by one and set a pointer to the left element and 
			#check if the pointer is equal to ch
			column=column1-1
			pointer=stringList[row1][column]
			if(pointer!=ch): #run if left element is not equal to the ch
				#pointer comes back to the same column and check elements along
				#column in upward fashion
				column=column+1 
				row=row1-1
				pointer=stringList[row][column]
				#check if the above element is different
				if(pointer!=ch):
					#since its different, the element is printed
					print(string1List[row+1],end="")
					#pointer moves to the upward diagonal element
					row1=row1-1
					column1=column1-1
				#checks the value of pointer and ch
				elif(pointer==ch):
					#loop that run until the pointer hits a different value in 
					# the table
					while(pointer==ch and ch!=0):
						#after new value is reached pointer moves up the table
						row=row-1
						pointer=stringList[row][column1]
					#if pointer hits new value, value of pointer is printed and 
					#pointer is set to up diagonal position
					if(pointer!=ch):
						row=row+1
						pointer=stringList[row][column1]
						print(string1List[row],end="")
						row1=row-1
						column1=column-1
				#if pointer's value is same to ch, pointer moves until new
				# value in the table is reached
			elif(pointer==ch):
				while(pointer==ch):
					column=column-1
					pointer=stringList[row1][column]
					#when new value is reached, the pointer moves in up
				if(pointer!=ch):
					column=column+1
					pointer=stringList[row1][column]
					row=row1-1
					pointer=stringList[row][column]
					# the pointer moves up until new value is found
					while (pointer==ch):
						row=row-1
						pointer=stringList[row][column]
					#when new value is found, the value of pointer is printed 
					#and the pointer is initialized to up-diagonal value
					if(pointer!=ch):
						row=row+1
						pointer=stringList[row][column]
						print(string1List[row],end="")
				row1=row-1
				column1=column-1
		#when the pointer reach/points the position whose value is zero it stops
		else:
			break
				

def main():
	#runs to compute LCS for new pair of strings until user quit
	while(True):
		# variables that store two strings given by the user
		string1=input("Enter your first string:")
		string2=input("Enter your second string:")
		#empty list to save two inputs given by the user
		string1List=[]
		string2List=[]
		# for loop to populate two list
		for x in string1:
			string1List.append(x)
		for y in string2:
			string2List.append(y)
		# append λ to the end of both list
		string1List.append("λ")
		string2List.append("λ")
		#reverse the lists
		string1List.reverse()
		string2List.reverse()
		#create a multidimensional list for computation and populate the
		# list with all elements equal to zero.
		stringList=[[ 0 for i in (string2List)] for j in (string1List)]
		#call lcs function to pupulate multidimensional list and find the LCS
		lcs(string1List,string2List,stringList)
		#prompt the user to either continue or quit
		command=input("\nPress enter to continue or anything to quit.....\n")
		#quits the program is user press except for an enter
		if(command!=""):
			break
			
main()