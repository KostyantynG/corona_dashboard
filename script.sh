#!/bin/bash

pip3 install requests
pip3 install boto3

cd /home/ec2-user/
wget https://raw.githubusercontent.com/KostyantynG/corona_dashboard/main/corona.py
wget https://raw.githubusercontent.com/KostyantynG/corona_dashboard/main/s3_access.py

crontab<<EOF
*/10 * * * * cd /home/ec2-user/ && python3 s3_access.py
EOF


