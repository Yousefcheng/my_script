# my_script


docker run -dit \
-v $PWD/ql2/config:/ql/config \
-v $PWD/ql2/scripts:/ql/scripts \
-v $PWD/ql2/repo:/ql/repo \
-v $PWD/ql2/log:/ql/log \
-v $PWD/ql2/db:/ql/db \
-p 8888:5700 \
--name ql2 \
--hostname ql2 \
--restart always \
limoe/qinglong:latest

一、将task_before.sh放入青龙映射的config文件夹📁，无需任何修改。
二、将code.sh放入青龙映射的scripts文件夹📁
三、根据拉取的库，修改code.sh里面的name_js前缀，默认chinnkarahoi。
四、添加定时任务"task code.sh"，定时时间按自己的需求来。
