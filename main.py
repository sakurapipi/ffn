r"""
FFn(c) 2077
By Pipi
1.6版本
//更新说明：
修复了使用read命令时不能读取第一行的问题
添加了read命令文件名称可以使用变量

"""



#coding=utf-8
syntax={}
version = "1.6.6"
import time
import os
import socket
import requests
import random
import platform
import sys
cdkey="";logtext = """FFn(c) 2077\nBy Pipi\nThis is FFn Log"""+str(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
if (len(sys.argv)!=2):
	for i in range(4):
		cdkey+="-"
		for i in range(5):
			cdkey+=str(random.randint(0,9))
	cdkey=cdkey[1:]
	
	print("--------------------------------")
	print("FFn                    Ver.{} ".format(str(version)))
	print("By Pipi                         ")
	print("Enter 'help' to get help!       ")
	print("Use jvav for a better experience")
	# print("cdkey: "+cdkey)
	print("--------------------------------")
	print("Initializing program...\nI hope you do not like a 'NUKE'\nusing -python\nEnter \"help_file\"to get help file\nEnter \"Information\"to get Information")
	time.sleep(0.03)
	os.system("title FFn:[Admin]Faster Funny Nuke")
	commandList = ["output","input","help","exit","math","ip.get","read","color"]
	help_file="""FFn help document 
	FFn is in the early development version and may be unstable. 
	Here are some help commands: 
	(Some capitalized initial commands are additional commands) 
	output      -    output 
	input       -    press any key to continue 
	exit        -    exit 
	math        -    operation 
	ip.get      -    get ip 
	read        -    read 
	ClearScreen -    clear the screen 
	var         -    assignment 
	Vars.all    -    see all vars. 
	Enter RunMain to read and execute ffn file /There are the following new commands: 
	url         -    crawler 
	vin         -    input 
	write       -    write 
	system      -    system command
	"""
class main():
	def CommandLauncher(*item):
		return max(item)


	def help():
		print("----FFn      help-------Page(1/1)")
		print(help_file)
		print("----FFn      help-------Page(1/1)")
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
			if (len(sys.argv)==2):
				try:
					n=sys.argv[1]
					print("[FFn] \"",n,"\" starting:\n")
					with open(n, 'r', encoding='UTF-8') as cf:
						commandline = 0
						db=False
						while True:
							commandline+=1
							command = cf.readline()  # 只读取一行内容
							command=command.strip('\n')
							command=str(command)
							# 判断是否读取到内容
							if(command==""):
								continue
							if db==True:
								print("\nCommand: "+command)
							else:
								pass
							if not command:
								continue

							elif(command==""):
								continue
							elif (command[0]=="#"):
								continue

							elif(command[0]=="v" and command[1]=="a" and command[2]=="r"):
								var = command[4:]
								var=var.split("=", 1)
								if var[1][0]=="@":
									x1=command.split("@", 1)
									x1=x1[1]
									x1=str(x1)
									x1=x1.strip('\n')
									x1="".join(syntax[x1])
									syntax[var[0]]=x1
								else:
									var[1]=var[1].strip('\n')
									syntax[var[0]]=var[1]

							elif (command in syntax.keys()):
								print(syntax[command],end="")


							elif(command[0]=="o" and command[1]=="u" and command[2]=="t" and command[3]=="p" and command[4]=="u" and command[5]=="t" and command[6]=="l" and command[7]=="n"):
								out=command[9:]
								if(command.find("@")!=-1):
									x=command.split("@" ,1)
									x=x[1]
									x="".join(x.split())
									out=syntax[x]
								out="".join(out)
								print("{}".format(out))

							# output
							elif(command[0]=="o" and command[1]=="u" and command[2]=="t" and command[3]=="p" and command[4]=="u" and command[5]=="t"):
								out=command[7:]
								if(command.find("@")!=-1):
									x=command.split("@" ,1)
									x=x[1]
									x="".join(x.split())
									out=syntax[x]
								out="".join(out)
								print("{}".format(out),end="")




								logtext += str("\nlog"+"["+str(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))+"]output :"+out)


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

							elif(command[0]=="v" and command[1]=="i" and command[2]=="n"):
								u=command.split(">")
								u=u[1]
								a=input()
								syntax[str(u).strip('\n')]=str(a)


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
										if(command.find("@")!=-1):
										
											x=command.split("@", 1)
											x=x[1]
											x=str(x)
											x=x.strip('\n')
											try:
												tempoutput="".join(syntax[x])
											except KeyError:
												print("An Error in this text,Return 1!")
											break;
										else:
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
										if(command.find("@")!=-1):
											x=command.split("@" ,1)
											x=x[1]
											x="".join(x.split())
											filename=syntax[x]
										else:
											filename += command[i+5]
									print("read file:",filename)
									logtext += str("\nlog"+"["+str(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))+"]read :"+filename)
									result=[]
								try:
									xx=0
									with open(filename,'r',encoding='utf-8') as f:
										syntax["TEXT.tmp.line\"{}\"".format("all")]=f.readlines()
										
									for fileline in open(filename,'r',encoding='utf-8'):
										xx+=1
										syntax["TEXT.tmp.line\"{}\"".format(str(xx))]=fileline

								except FileNotFoundError:
									print("can not load the file")
								except UnicodeDecodeError:
									print("you must open txt file")
								except PermissionError:
									print("you must open txt file")


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
							elif (command=="ClearScreen"):
								os.system("cls")
							elif (command=="db=1"):
								db=True
								print("[debug is open]")
							elif (command=="db=0"):
								db=False
								print("[debug is close]")
							elif (command[0]=="u" and command[1]=="r" and command[2]=="l"):
								if(len(command)==3):
									continue
								else:
									url=command[4:]
									if url[0]=="@":
										url=command.split("@", 1)
										url=url[1]
										url=str(url)
										url=url.strip('\n')
										url="".join(str(syntax[url]))

								
								try:
									response = requests.get(url)
									response.encoding="UTF-8"
									syntax["URL.tmp.response.status_code"]=str(response.status_code)
									# print("status_code:\n",response.status_code,"\n")

									syntax["URL.tmp.response.url"]=response.url
									# print("url:\n",response.url,"\n")

									syntax["URL.tmp.response.headers"]=response.headers
									# print("headers:\n",response.headers,"\n")

									syntax["URL.tmp.response.cookies"]=str(response.cookies)
									# print("cookies:\n",response.cookies,"\n")

									syntax["URL.tmp.response.text"]=response.text
									# print("text:\n",response.text,"\n")

								except SyntaxError:
									syntax["URL.tmp.response.status_code"]="Nul"
									syntax["URL.tmp.response.url"]="Nul"
									syntax["URL.tmp.response.headers"]="Nul"
									syntax["URL.tmp.response.cookies"]="Nul"
									syntax["URL.tmp.response.text"]="Nul"
							elif(command[0:8]=="loopOut<"):
								x=command[8:]
								x=x.split(",")

								if x[0][0]=="@":
									x1=x[0][1:]
									x1=x1.strip("\n")
									x1=syntax[x1]
									x1="".join(x1)
									x1=int(x1)
								else:

									x1=int(x[0])

								if x[1][0]=="@":
									x2=x[1][1:]
									x2=x2.strip("\n")
									x2=syntax[x2]
								else:
									x2=x[1]
								for i in range(int(x1)):
									print("".join(x2))



							elif (command[0]=="f"and command[1]=="l"and command[2]=="i"and command[3]=="v"):
								x=command[5:]
								with open(x,"r",encoding="utf-8") as f:
									while True:
										g=f.readline()
										g=g.strip('\n')
										g=str(g)
										if g=="END":
											break
										elif g[0]=="#":
											continue
										else:
											g1=g.split("=",1)
											g1[1]=g1[1].strip('\n')
											syntax[g1[0]]=[g1[1]]


							elif (command[0]=="w"and command[1]=="r"and command[2]=="i"and command[3]=="t"and command[4]=="e"):
								x=command[6:]
								x=x.split(">", 1)
								x1="".join(x[0])
								x2="".join(x[1])
								if x1[0]=="@":
									x1=syntax[x1[1:]]
								if x2[0]=="@":
									x2=syntax[x2[1:]]
								with open("".join(x2),"a",encoding="utf-8") as f:
									f.write("".join(x1))
									f.write("\n")

							elif(command[:6]=="system"):
								x=command[7:]
								os.system(x)






							elif (command=="return 0"):
								print("\nThe program has finished running!")
								sys.exit()




				except FileNotFoundError:
					print("Can not found the file!")
				except UnicodeDecodeError:
					print("You must open txt file!")
				except OSError:
					pass
				except ValueError:
					print("\nWarning! I/O error, but this problem will not affect.")
			else:
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
						with open(filename,'r',encoding='utf-8') as f:
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

				elif(command[0]=="v" and command[1]=="a" and command[2]=="r"):
					var = command[4:]
					x=var.split("=", 1)
					syntax[x[0]]=[x[1]]
				elif (command in syntax.keys()):
					print("".join(syntax[command]))

				elif (command=="cdkey"):
					key=input("CDKEY:")
					if key == cdkey:
						print("Thank you for using!")
					else:
						print("CDKEY Not Find!")
				elif (command=="get_cdkey"):
					with open(".\\cd\\system\\CDKEY.txt", 'w', encoding='UTF-8') as f:
						f.write(cdkey)
						print("Create finish!")
				elif (command=="help_file"):
					with open("HELPFILE.TXT","w",encoding="utf-8") as s:
						s.write(help_file)
				elif (command=="Information"):
					print("\nFFn ver.{}".format(version))
					print("platform:{}".format(platform.platform()))
					print("version:{}".format(platform.version()))
					print("architecture:{}".format(platform.architecture()))
					print("type:{}".format(platform.machine()))
					print("name:{}\n".format(platform.node()))
				elif (command=="Vars.all"):
					if syntax=={}:
						print("Null")
					for i in syntax.items():
						print(i[0]+"="+str(i[1]))

				else:
					print("Unknow command, please re-enter or enter","\"","help","\"")
		except IndexError:
			print("Unknow command, please re-enter or enter","\"","help","\"")
if __name__ == '__main__':
	main()
	
