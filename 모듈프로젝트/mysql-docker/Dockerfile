FROM mysql:5.7

ADD ./init /docker-entrypoint-initdb.d

ENV MYSQL_ALLOW_EMPTY_PASSWORD true
ENV MYSQL_DATABASE mydb
EXPOSE 3306

CMD ["mysqld"]
