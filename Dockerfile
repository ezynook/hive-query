FROM ezynook/app:flask
#Base Image นี้มี Package เบื้องต้นเป็น Flask, Pandas ต้องการเพิ่มให้ RUN pip ที่หลังได้
MAINTAINER pasit.dev

HEALTHCHECK --interval=10s --timeout=30s --start-period=10s \
    CMD netstat -lnpt | grep 3000 || exit 1

RUN mkdir /app
WORKDIR /app
COPY ./src/ .
RUN chmod 777 /app/*
#โดย Base Image จะมาเป็น /bin/bash ต้องใช่ CMD ทุกครั้งหลัง Build
CMD [ "flask", "run", "--host=0.0.0.0", "--port=3000", "--debug" ]