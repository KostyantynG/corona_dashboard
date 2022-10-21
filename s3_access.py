from corona import corona_data_last_week
import boto3

s3_client = boto3.client('s3')

data_to_upload = corona_data_last_week()

with open("corona-data.json", "w") as file:
        file.write(data_to_upload)

s3_client.upload_file('corona-data.json', 'corona-friday-challenge-bucket', 'corona-data.json')