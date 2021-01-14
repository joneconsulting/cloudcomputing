FROM mysql:5.7

<<<<<<< HEAD
ADD ./init /docker-entrypoint-initdb.d
=======
ADD ./init/init.sql /docker-entrypoint-initdb.d/
COPY ./init/utf8.cnf /etc/mysql/conf.d/
>>>>>>> 8b280e030c759f32688d3c747155e110c6f4795a

ENV MYSQL_ALLOW_EMPTY_PASSWORD true
ENV MYSQL_DATABASE mydb
EXPOSE 3306

CMD ["mysqld"]
