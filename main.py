# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "datablob",
#     "requests",
#     "simple-env",
# ]
# ///
import csv
import datablob
import io
import requests
import simple_env as se

AWS_BUCKET_NAME = se.get("AWS_BUCKET_NAME")

AWS_BUCKET_PATH = se.get("AWS_BUCKET_PATH")

OVERPASS_URL = "https://overpass-api.de/api/interpreter"

with open("query.txt", "r") as f:
    OVERPASS_QUERY = f.read()

headers = {
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "User-Agent": "PythonDataScript/1.0 (danieldufour@gocarta.org)",
}
payload = {"data": OVERPASS_QUERY}
response = requests.post(OVERPASS_URL, data=payload, headers=headers)
response.raise_for_status()
data = response.text

f = io.StringIO(data)
rows = list(csv.DictReader(f))

if len(rows) < 100:
    raise Exception("[dataops-osm-pois] unexpected number of rows")

# need strategy for QA'ing this info
# for example, one website was hijacked/stolen
for row in rows:
    del row["contact:facebook"]
    del row["contact:instagram"]
    del row["contact:phone"]
    del row["website"]

client = datablob.DataBlobClient(
    bucket_name=AWS_BUCKET_NAME, bucket_path=AWS_BUCKET_PATH
)

client.update_dataset(
    name="osm_pois",
    description="Points of Interest within or near the CARTA Service Area, exported from OpenStreetMap",
    version="1",
    data=rows,
    column_names=[
        "@type",
        "name",
        "@lat",
        "@lon",
        "amenity",
        "addr:city",
        "addr:housenumber",
        "addr:postcode",
        "addr:state",
        "addr:street",
        "air_conditioning",
        "check_data",
        "check_date:opening_hours",
        # "contact:facebook",
        # "contact:instagram",
        # "contact:phone",
        "cuisine",
        "opening_hours",
        "outdoor_seating",
        "phone",
        "shop",
        "takeaway",
        "toilets",
        # "website",
    ],
    json=True,
    jsonl=True,
    latitude_key="@lat",
    longitude_key="@lon",
    parquet=True,
    xlsx=True,
)

print(f"[dataops-osm-pois] updated {len(rows)} rows")
