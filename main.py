
# A lambda function to interact with AWS RDS MySQL

import pymysql
import sys

REGION = 'us-east-1'

rds_host  = "example.c7hugt6dv8dv.ap-south-1.rds.amazonaws.com"
name = "example"
password = "examplepassword"
db_name = "example"

def save_events(event):
    """
    This function fetches content from mysql RDS instance
    """
    item_count = 0
    conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
    with conn.cursor() as cur:
        cur.execute("""insert into test (id, name) values( %s, '%s')""" % (event['id'], event['name']))
        conn.commit()
        cur.close()

def main(event, context):
    save_events(event)
        


# event = {
#   "id": 777,
#   "name": "appychip"
# }
# context = ""
# main(event, context)

