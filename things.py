import falcon
import psycopg2
import sys
import pprint
import csv


conn_string = "host='ramdb.c5grxbwhm0jn.eu-west-1.rds.amazonaws.com' dbname='ramdb' user='rammasterdata' password='HgfTyyR6w2'"

# print the connection string we will use to connect
print "Connecting to database\n	->%s" % (conn_string)

# get a connection, if a connect cannot be made an exception will be raised here
conn = psycopg2.connect(conn_string)


class GetData():

    def on_get(self, req, resp):
        variable = req.get_param('variable')
        condition = req.get_param('condition')
        value = req.get_param('value')
        pprint.pprint(variable)
        pprint.pprint(condition)
        pprint.pprint(value)

        sql = 'SELECT * FROM "ramdb_nigeria"."data_culverts" where ' + variable + condition + value

        resp.status = falcon.HTTP_200
        cursor = conn.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        str1 = ''.join(str(e) for e in records)
        pprint.pprint(str1)
        resp.body = str1

        #resp.body = '{"message":"hello"}'



app = falcon.API()
getdata = GetData()
app.add_route('/things', getdata)

# gunicorn things:app
# http://localhost:8000/things