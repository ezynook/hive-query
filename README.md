<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/bb/Apache_Hive_logo.svg/1200px-Apache_Hive_logo.svg.png" width="100"> 

## Apache Hive Search 

✅ __Clone project__
```bash
git clone https://github.com/ezynook/hive-query.git
```
✅ __Deploy__
```bash
docker-compose up -d  --build
```
__Single Command__
```bash
docker run --name hive-query \
-p 3000:3000 --restart=always \
-d ghcr.io/ezynook/hive-query/hive-query:v1
```
_สามารถเข้าไปเปลี่ยน Port ได้ที่ ```docker-compose.yml```_
