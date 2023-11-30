try:
	with open("First_file.txt",'r') as f1:
		with open("second_file.txt","w") as f2:
			for i in f1:
				f2.write(i)

except:
	print("File is not Found, Please Create File")

else:
	f2.close()
	print("File is close")