## Q3 simple counter

URL : http://ec2-54-86-132-201.compute-1.amazonaws.com:8521 \
URL_VOTE_RESULT : http://ec2-54-86-132-201.compute-1.amazonaws.com:8521/result

### Introduction
There are 2 ways to achieve this question
1. AWS Lambda \
Set up API in AWS Dynamodb and write a static web for storage in AWS s3.

2. Python Flask \
This is the method I chose. This method uses AWS RDS services to achieve flexible load of the database. Different parameters can be set up for easy management.
In the aspect of voting, based on Flask, a required page can be conveniently set up for voting, which is more convenient for daily maintenance and modification of different visualization.
\
The settings for the different locations are shown below

### Testing Environment
- Coding on AWS Cloud9
- DB Test on local sqlite, AWS RDP
- Network testing on HKGOV Office, CSL 5G

### Setup command
```bash
git clone https://github.com/lshw54/DETest.git
cd DETest/Q3
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
### Build Database
When creating this project, please replace the` SQLALCHEMY_DATABASE_URI` parameter in `app/config.py` so that you can connect to an existing database.
```bash
sh db.sh
```

### Run Flask Server
```bash
flask run -p 8521 -h 0.0.0.0
```

### Fix Database Encoding
```bash
mysql -h `host` -u `username` -p `database`

mysql[`database`] > ALTER TABLE tablename CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```
