# my_script


docker run -dit \
   -v $PWD/ql2/config:/ql/config \
   -v $PWD/ql2/log:/ql/log \
   -v $PWD/ql2/db:/ql/db \
   -p 8888:5700 \
   --name ql2 \
   --hostname ql2 \
   --restart always \
   limoe/qinglong:latest
