import os

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    name = os.environ.get("NAME", "World")
    return "Hello {}!".format(name)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

"""
import os

from flask import Flask, request
import json
from google.cloud import bigquery

app = Flask(__name__)


# [END eventarc_gcs_server]


# [START eventarc_gcs_handler]
@app.route('/', methods=['POST'])
def index():
    # Gets the Payload data from the Audit Log
    content = request.json
    try:
        print(content)
        ds = content['resource']['labels']['dataset_id']
        proj = content['resource']['labels']['project_id']
        tbl = content['protoPayload']['resourceName']
        rows = int(content['protoPayload']['metadata']['tableDataChange']['insertedRowsCount'])
        if ds == 'cloud_run_tmp' and tbl.endswith('tables/cloud_run_trigger') and rows > 0:
            query = create_agg()
            return "table created", 200
    except:
        # if these fields are not in the JSON, ignore
        pass
    return "ok", 200


# [END eventarc_gcs_handler]

def create_agg():
    client = bigquery.Client()
    query = 
CREATE OR REPLACE TABLE cloud_run_tmp.created_by_trigger AS
SELECT 
  name, SUM(number) AS n
FROM cloud_run_tmp.cloud_run_trigger
GROUP BY name
ORDER BY n desc
LIMIT 10
    
    client.query(query)
    return query


# [START eventarc_gcs_server]
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
# [END eventarc_gcs_server]

""""
