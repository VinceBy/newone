#保存学生所有信息
stuInfos = []

#全局变量
newName = ''
newSex = ''
newPhone = ''

def printMenu():
	#打印功能提示
	print('='*30)
	print('         学生管理系统v1.0')
	print('1.添加学生信息')
	print('2.删除学生信息')
	print('3.修改学生信息')
	print('4.查询学生信息')
	print('5.遍历学生信息')
	print('0.退出系统')
	print('='*30)
def getInfo():
	
	#global newName
	#global newSex
	#global newPhone

	#添加学生信息
	    #3.1 提示并获取学生的姓名
	newName = input('请输入新学生的名字')

	    #3.2 提示并获取学生的性别
	newSex = input('请输入新学生的性别')

	    #3.3 提示并获取学生的手机号码
	newPhone = input('请输入新学生的手机号码')
	#通过列表的方式把数据整合成一个整体，然后返回
	#return [newName,newSex,newPhone]
	#通过元组的方式把数据整合成一个整体
	#return (newName,newSex,newPhone)
	return {'name':newName,'sex':newSex,'phone':newPhone}
def addStuInfo():
	result=getInfo()
        
	newInfo = {}
	newInfo['name'] = result['name']
	newInfo['sex'] = result['sex']
	newInfo['phone'] = result['phone']

	stuInfos.append(newInfo)


def main():
	
	while True:
		printMenu()		
		
		
	#2.获取功能选择
		key = input('请输入功能对应的数字：')
		
	#3.根据用户的选择，进行相应的操作
		if key == '1':
			addStuInfo()
		    
		    
		elif key == '2':
	            stuId = int(input('需要删除的学生信息序号'))
	            del stuInfos[stuId-1]

		elif key == '3':
			#修改学生信息
		 	
		 	#3.1 提示并获取需要修改学生的序号
		    stuId = int(input('需要修改的学生信息序号'))
		 	#3.1 提示并获取学生的姓名
		    newName = input('请输入新学生的名字')

		    #3.2 提示并获取学生的性别
		    newSex = input('请输入新学生的性别')

		    #3.3 提示并获取学生的手机号码
		    newPhone = input('请输入新学生的手机号码')
		 	
		    
		   
		    stuInfos[stuId-1]['name']= newName
		    stuInfos[stuId-1]['sex']= newSex
		    stuInfos[stuId-1]['phone']= newPhone

		elif key =='4':
	        
	            stuId = int(input('请输入要查询的学生信息的序号：'))
	            print('='*30)
	            print('姓名     性别    手机号')
	            print('%s       %s      %s'%(stuInfos[stuId-1]['name'],stuInfos[stuId-1]['sex'],stuInfos[stuId-1]['phone']))
		elif key == '5':
			#sprint(stuInfos)
			print('='*30)
			print('学生的信息如下：')
			print('='*30)
			print('序号	姓名		性别		手机号码')
			i=1
			for tempInfo in stuInfos:
				
				print('%d 	%s 		%s 		%s '%(i,tempInfo['name'],tempInfo['sex'],tempInfo['phone']))
				i+=1
		elif key == '0':
			break
	    
#调用主函数
main()
