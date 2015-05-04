setwd('D:/Postgraduate/Course/2-semester/R-language/TimeAnalyze/Programe')
time=read.csv('source/origin_data.csv')
T =time[,c(-4,-5)]
end = strptime(T[,3], format="%Y年%m月%d日 %A %H:%M")
start = strptime(T[,2], format="%Y年%m月%d日 %A %H:%M")
last=end-start
week = weekdays(end)
T[,2] = as.character(start)
T[,3] = as.character(end)
colnames(T) = c('Project','StartTime','Endtime')
T = cbind(T,last)
D = as.Date(T[,2], "%Y-%m-%d")
T = cbind(T,D)
T= cbind(T,week)

#功能3：任意一段时间段内某个项目的时间图
motion1 = as.character(read.table('temp/project1.txt')[1,])
motion2 = as.character(read.table('temp/project2.txt')[1,])
from_day = as.character(read.table('temp/date1.txt')[1,])
to_day = as.character(read.table('temp/date2.txt')[1,])
from_day_range = grep(from_day,T[,'D'])
to_day_range  = grep(to_day,T[,'D'])
from_day_start = from_day_range [1]
to_day_end = to_day_range[length(to_day_range)]
type1 = grep(motion1,T[c(from_day_start:to_day_end),'Project'])+from_day_start-1
type2 = grep(motion2,T[c(from_day_start:to_day_end),'Project'])+from_day_start-1
type_frame1 = T[c(type1),]
type_frame2 = T[c(type2),]

DAY1  = factor(type_frame1[,'D'])
DAY2 = factor(type_frame2[,'D'])

type_frame1_sum = aggregate(type_frame1[,'last'],list(DAY1),sum)
project1 = rep(motion1,nrow(type_frame1_sum))
type_frame1_sum = data.frame(project1,type_frame1_sum)
colnames(type_frame1_sum) = c('project','day','time')

type_frame2_sum = aggregate(type_frame2[,'last'],list(DAY2),sum)
project2 = rep(motion2,nrow(type_frame2_sum))
type_frame2_sum = data.frame(project2,type_frame2_sum)
colnames(type_frame2_sum) = c('project','day','time')

type_frame_sum = rbind(type_frame1_sum,type_frame2_sum)
#colnames(type_frame1_sum) = c('day','time')
DAY = factor(type_frame_sum[,'day'])
write.csv (x = type_frame_sum,file = "temp/project2.csv")
