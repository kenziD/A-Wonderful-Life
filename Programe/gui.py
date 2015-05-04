import tkinter as tk
from rpy2.robjects import r
import rpy2.robjects.lib.ggplot2 as ggplot2
from rpy2 import robjects
import rpy2.rlike.container as rlc
from rpy2.robjects.vectors import DataFrame

root = tk.Tk()
root.geometry('460x100')
root.title("Kenzi's time analyze")

def creat_mode_menu():
	mode_button = tk.Menubutton(menu_bar,text = 'Mode')
	mode_button.grid(row = 0,column=15)
	mode_button.menu = tk.Menu(mode_button)
	mode_button['menu'] = mode_button.menu
	mode_button.menu.add_command ( label="一天的项目对比",command=window1)
	mode_button.menu.add_command ( label="两天的项目对比" ,command=window2)
	mode_button.menu.add_command ( label="一个项目的时间汇总",command=window3)
	mode_button.menu.add_command ( label="两个项目的时间汇总",command=window4)

	return mode_button

source1 = tk.StringVar()
source2 = tk.StringVar()
source3 = tk.StringVar()
source4 = tk.StringVar()

def open1():
	f = open('temp/date1.txt', 'w')
	f.write(source1.get())
	f.close

def open2():
	f = open('temp/date2.txt', 'w')
	f.write(source2.get())
	f.close

def open3():
	f = open('temp/project1.txt','w')
	f.write(source3.get())
	f.close

def open4():
	f = open('temp/project2.txt','w')
	f.write(source4.get())
	f.close

def show1():
	open1()
	r.source('D:/Postgraduate/Course/2-semester/R-language/TimeAnalyze/Programe/R/head1.r',encoding="utf-8")
	data = DataFrame.from_csvfile('D:/Postgraduate/Course/2-semester/R-language/TimeAnalyze/Programe/temp/day1.csv')
	pp = ggplot2.ggplot(data)+ggplot2.aes_string(x='project', y='time',fill = 'project')+ggplot2.geom_bar(stat ='identity')+ggplot2.ggtitle("今日项目时间分布图")+ggplot2.labs(x='项目',y='时间 (min)')+ggplot2.theme(**{'axis.text.x': ggplot2.element_text(angle = 45)})
	pp.plot()

def window1():
	tk.Label(root,text='请输入日期：').grid(row = 2,column =0 )
	tk.Entry(root, width=15,textvariable=source1).grid(row = 2,column =1 )
	tk.Button(root, text="绘图",command=show1).grid(row = 2,column =2 )

def show2():
	open2()
	r.source('D:/Postgraduate/Course/2-semester/R-language/TimeAnalyze/Programe/R/head.R',encoding="utf-8")
	data = DataFrame.from_csvfile('D:/Postgraduate/Course/2-semester/R-language/TimeAnalyze/Programe/temp/day2.csv')
	pp = ggplot2.ggplot(data)+ggplot2.aes_string(x='factor(project)', y='time',fill = 'factor(day)')+ggplot2.geom_bar(stat ='identity',position = 'dodge')+ggplot2.ggtitle("两日项目时间对比图")+ggplot2.labs(x='项目',y='时间 (min)')+ggplot2.theme(**{'axis.text.x': ggplot2.element_text(angle = 45)})
	pp.plot()

def window2():
	tk.Label(root,text='请输入日期2：').grid(row = 3,column =0 )
	tk.Entry(root, width=15,textvariable=source2).grid(row = 3,column =1 )
	tk.Button(root, text="绘图",command=show2).grid(row = 3,column =2)

def show3():
	open3()
	r.source('D:/Postgraduate/Course/2-semester/R-language/TimeAnalyze/Programe/R/end1.R',encoding="utf-8")
	data = DataFrame.from_csvfile('D:/Postgraduate/Course/2-semester/R-language/TimeAnalyze/Programe/temp/project1.csv')
	pp = ggplot2.ggplot(data)+ggplot2.aes_string(x='day', y='time',fill = 'day')+ggplot2.geom_bar(stat ='identity')+ggplot2.ggtitle("时间段内日某项目分布图")+ggplot2.labs(x='日期',y='时间 (min)')+ggplot2.theme(**{'axis.text.x': ggplot2.element_text(angle = 45)})
	pp.plot()

def window3():
	tk.Label(root,text='请输入项目：').grid(row = 2,column =4)
	tk.Entry(root, width=15,textvariable=source3).grid(row = 2,column =5)
	tk.Button(root, text="绘图",command=show3).grid(row = 2,column =6)

def show4():
	open4()
	r.source('D:/Postgraduate/Course/2-semester/R-language/TimeAnalyze/Programe/R/end.R',encoding="utf-8")
	data = DataFrame.from_csvfile('D:/Postgraduate/Course/2-semester/R-language/TimeAnalyze/Programe/temp/project2.csv')
	pp = ggplot2.ggplot(data)+ggplot2.aes_string(x='day', y='time',fill = 'factor(project)')+ggplot2.geom_bar(stat ='identity',position = 'dodge')+ggplot2.ggtitle("两项目时间对比图")+ggplot2.labs(x='日期',y='时间 (min)')+ggplot2.theme(**{'axis.text.x': ggplot2.element_text(angle = 45)})
	pp.plot()

def window4():
	tk.Label(root,text='请输入项目2：').grid(row = 3,column =4)
	tk.Entry(root, width=15,textvariable=source4).grid(row = 3,column =5)
	tk.Button(root, text="绘图",command=show4).grid(row = 3,column =6)

menu_bar = tk.Frame(root, borderwidth=2)
menu_bar.grid(row = 0,column= 0)

mode_menu = creat_mode_menu()
menu_bar.tk_menuBar(mode_menu)
root.mainloop()  #进入窗体的主循环