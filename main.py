r"""
FFn(c) 2077
By Pipi


"""



#coding=utf-8

import time
import os
import socket

logtext = """FFn(c) 2077
By Pipi
This is FFn Log
"""+str(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
class main():
	def Commandlaucher(*item):
		return max(item)
	print("Initializing program...\nI hope you do not like a 'NUKE'\nusing -python")
	time.sleep(0.3)
	os.system("title FFn:[Admin]Faster Funny Nuke")
	os.system("cls")
	commandList = ["output","input","help","exit","math","ip.get","read","color"]
	print("--------------------------------")
	print("FFn                  Ver.1.3Beta")
	print("By Pipi                         ")
	print("Enter 'help' to get help!       ")
	print("Use jvav for a better experience")
	print("--------------------------------")

	def help():
		print("----FFn      hel-------Page(1/1)")
		print("pythin help:")
		print("Enter (output) to Output characters")
		print("Enter (input) to Input characters")
		print("Enter (exit) to Exit")
		print("Enter (math) can +-*/")
		print("Enter (ip.get) to get ip")
		print("Enter (read) to open file")
		print("Enter (ClearScreen) clear screen")
		print("----FFn      hel-------Page(1/1)")
		# print(commandList)
		input("Enter...")
	

	def get_host_ip(): 
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.connect(('8.8.8.8', 80))
			ip = s.getsockname()[0]
		finally:
			s.close()
			return ip

	def file_name(file_dir):
		for root, dirs, files in os.walk(file_dir):
			print("root:",root) # 当前目录路径
			print("dirs:",dirs) # 当前路径下所有子目录
			print("files:",files) # 当前路径下所有非目录子文件
			print('\n')
	while True:
		
		try:
			command = input("["+str(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))+"]:>>")
			# pass
			if(command==""):
				pass



			# output
			elif(command[0]=="o" and command[1]=="u" and command[2]=="t" and command[3]=="p" and command[4]=="u" and command[5]=="t"):
				CommandLen = len(command)
				tempoutput = ""
				for i in range(CommandLen):
					try:
						tempoutput+=command[int(7+i)]
					except IndexError:
						pass
				temp = tempoutput
				logtext += str("\nlog"+"["+str(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))+"]output :"+temp)
				print(temp)

				del CommandLen,command,temp,tempoutput
			# input
			elif(command[0]=="i" and command[1]=="n" and command[2]=="p" and command[3]=="u" and command[4]=="t"):
				tmpvar =""
				CommandLen = len(command)
				tempinput = ""
				for i in range(CommandLen):

					try:
						tempinput+=command[int(6+i)]
					except IndexError:
						pass
				temp = input(tempinput)
				logtext += str("\nlog"+"["+str(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))+"]input :"+tempinput)
				logtext += str("\nlog"+"["+str(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))+"]answer :"+temp)

				# print(temp)
				del CommandLen,command,temp,tempinput



			# help
			elif(command=="help"):
				logtext += str("\nlog"+"["+str(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))+"]get help")
				help()
			# exit
			elif(command=="exit"or command=="esc"):
				logtext += str("\nlog"+"["+str(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))+"]Exit")
				exit()
			# math 2020/12/15
			elif(command[0]=="m" and command[1]=="a" and command[2]=="t" and command[3]=="h"):
				CommandLen = len(command)
				tempoutput = ""
				for i in range(CommandLen):
					try:
						tempoutput+=command[int(5+i)]
					except IndexError:
						pass
				temp = tempoutput
				try:
					print(eval(temp))
					tmp = eval(temp)
				except NameError:
					tmp=print("You must enter numbers")
				except ZeroDivisionError:
					tmp=print("You can't let the divisor be 0")
				except SyntaxError:
					tmp=print("You must enter numbers")
				logtext += str("\nlog"+"["+str(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))+"]math :"+tempoutput+"="+str(tmp))
				del CommandLen,command,temp,tempoutput,tmp
			# log 2020/12/19
			elif (command == "log"):
				print("\n",logtext,"\n")
				with open('log.log', 'w') as f:
					f.writelines(logtext)
					f.flush()
			# ip 2020/12/25
			elif (command == "ip.get"):
				print(get_host_ip())

			#cd 2021/1/31
			elif (command == "cd"):
				if (os.path.exists('cd')==True):
					file_name("cd")
					logtext += str("\nlog"+"["+str(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))+"]cd :This message does not support logging\n")
				else:
					os.makedirs('cd')
					logtext += str("\nlog"+"["+str(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))+"]cd :create\n")
			#file 2020/1/31
			elif (command[0] == "r" and command[1] == "e" and command[2] ==  "a" and command[3] == "d"):
				filename = ''
				command += ' '
				if (len(command)<=3):
					pass
				else:
					for i in range(len(command)-5):
						filename += command[i+5]
					print(filename)
					logtext += str("\nlog"+"["+str(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))+"]read :"+filename)
					result=[]
				try:
					with open(filename,'r') as f:
						for line in f:
							print(f.read())
				except FileNotFoundError:
					print("can not load the file")
				except UnicodeDecodeError:
					print("you must open txt file")
				except PermissionError:
					print("you must open txt file")

			# clear screen 2020/1/31
			elif (command=="ClearScreen"):
				os.system("cls")

			# syscolor 2021/2/1
			elif (command[0] == "c" and command[1] == "o" and command[2] == "l" and command[3] == "o" and command[4] == "r"):
				tmpcolor = ''
				for i in range(len(command)-6):
					tmpcolor += command[i+6]
				os.system("color "+tmpcolor+" ")
				logtext += str("\nlog"+"["+str(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))+"]color "+tmpcolor)

			elif (command[0]=='s' and command[1]=='t' and command[2]=='o' and command[3]=='p'):
				stoptmp = ''
				for i in range(len(command)-5):
					stoptmp+=command[i+5]
				try:
					time.sleep(int(stoptmp))
				except ValueError:
					print("You must enter number")





			elif (command == "RunMain"):
				n=input(">>")
				try:
					with open(n, 'r', encoding='UTF-8') as f:
						commandline = 0
						while True:
							commandline+=1
							command = f.readline()  # 只读取一行内容

							# 判断是否读取到内容
							if not command:
								break

							elif(command==""):
								pass
							elif (command[0]=="#"):
								continue
							# output
							elif(command[0]=="o" and command[1]=="u" and command[2]=="t" and command[3]=="p" and command[4]=="u" and command[5]=="t"):
								CommandLen = len(command)
								tempoutput = ""
								for i in range(CommandLen):
									try:
										tempoutput+=command[int(7+i)]
									except IndexError:
										pass
								temp = tempoutput
								logtext += str("\nlog"+"["+str(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))+"]output :"+temp)
								print(temp,end="")
								del CommandLen,command,temp,tempoutput
							# input
							elif(command[0]=="i" and command[1]=="n" and command[2]=="p" and command[3]=="u" and command[4]=="t"):
								CommandLen = len(command)
								tempinput = ""
								for i in range(CommandLen):
									try:
										tempinput+=command[int(6+i)]
									except IndexError:
										pass
								temp = input(tempinput)
								logtext += str("\nlog"+"["+str(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))+"]input :"+tempinput)
								logtext += str("\nlog"+"["+str(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))+"]answer :"+temp)
								print(temp)
								del CommandLen,command,temp,tempinput
							# help
							elif(command=="help"):
								logtext += str("\nlog"+"["+str(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))+"]get help")
								help()
							# exit
							elif(command=="exit"or command=="esc"):
								logtext += str("\nlog"+"["+str(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))+"]Exit")
								exit()
							# math 2020/12/15
							elif(command[0]=="m" and command[1]=="a" and command[2]=="t" and command[3]=="h"):
								CommandLen = len(command)
								tempoutput = ""
								for i in range(CommandLen):
									try:
										tempoutput+=command[int(5+i)]
									except IndexError:
										pass
								temp = tempoutput
								try:
									print(eval(temp))
									tmp = eval(temp)
								except NameError:
									tmp=print("You must enter numbers")
								except ZeroDivisionError:
									tmp=print("You can't let the divisor be 0")
								except SyntaxError:
									tmp=print("You must enter numbers")
								logtext += str("\nlog"+"["+str(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))+"]math :"+tempoutput+"="+str(tmp))
								del CommandLen,command,temp,tempoutput,tmp
							# log 2020/12/19
							elif (command == "log"):
								print("\n",logtext,"\n")
								with open('log.log', 'w') as f:
									f.writelines(logtext)
									f.flush()
							# ip 2020/12/25
							elif (command == "ip.get"):
								print(get_host_ip())

							#cd 2021/1/31
							elif (command == "cd"):
								if (os.path.exists('cd')==True):
									file_name("cd")
									logtext += str("\nlog"+"["+str(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))+"]cd :This message does not support logging\n")
								else:
									os.makedirs('cd')
									logtext += str("\nlog"+"["+str(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))+"]cd :create\n")
							#file 2020/1/31
							elif (command[0] == "r" and command[1] == "e" and command[2] ==  "a" and command[3] == "d"):
								filename = ''
								command += ' '
								if (len(command)<=3):
									pass
								else:
									for i in range(len(command)-5):
										filename += command[i+5]
									print(filename)
									logtext += str("\nlog"+"["+str(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))+"]read :"+filename)
									result=[]
								try:
									with open(filename,'r') as f:
										for line in f:
											print(f.read())
								except FileNotFoundError:
									print("can not load the file")
								except UnicodeDecodeError:
									print("you must open txt file")
								except PermissionError:
									print("you must open txt file")

							# clear screen 2020/1/31
							elif (command=="ClearScreen"):
								for i in range(3):
									os.system("cls")


							# syscolor 2021/2/1
							elif (command[0] == "c" and command[1] == "o" and command[2] == "l" and command[3] == "o" and command[4] == "r"):
								tmpcolor = ''
								for i in range(len(command)-6):
									tmpcolor += command[i+6]
								os.system("color "+tmpcolor+" ")
								logtext += str("\nlog"+"["+str(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))+"]color "+tmpcolor)

							elif (command[0]=='s' and command[1]=='t' and command[2]=='o' and command[3]=='p'):
								stoptmp = ''
								for i in range(len(command)-5):
									stoptmp+=command[i+5]
								try:
									time.sleep(int(stoptmp))
								except ValueError:
									print("You must enter number")

							elif (command=="return 0"):
								break

				except FileNotFoundError:
					print("Can not found the file")
				except UnicodeDecodeError:
					print("You must open txt file")
				except OSError:
					pass
				except ValueError:
					print("I/O is Error")
			else:

				print("Unknow command, please re-enter or enter","\"","help","\"")
		except IndexError:
			print("Unknow command, please re-enter or enter","\"","help","\"")
if __name__ == '__main__':
	main()
