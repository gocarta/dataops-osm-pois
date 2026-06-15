# dataops-osm-pois
Points of Interest within or near the CARTA Service Area, exported from OpenStreetMap

## background
Every second counts when you are trying to catch the bus.  We built this data pipeline in our cloud environment to provide real-time data to both our operations center and the public.

## frequency
The pipeline runs once every hour on a cloud server.

## columns
| column | example | description |
| :--- | :--- | :--- |
| **@type** | `"node"` | Type of OpenStreetMap Node |
| **name** | `"City Cafe"` | Name of Place |
| **@lat** | `35.0606683` | Latitude |
| **@lon** | `-85.1349363` | Longitude |

more info coming soon

## download links
- [metadata](https://gocarta.s3.us-east-2.amazonaws.com/public/data/osm_pois/v1/meta.json)
- [csv](https://gocarta.s3.us-east-2.amazonaws.com/public/data/osm_pois/v1/data.csv)
- [geojson](https://gocarta.s3.us-east-2.amazonaws.com/public/data/osm_pois/v1/data.points.geojson)
- [geoparquet](https://gocarta.s3.us-east-2.amazonaws.com/public/data/osm_pois/v1/data.parquet)
- [json](https://gocarta.s3.us-east-2.amazonaws.com/public/data/osm_pois/v1/data.json)
- [json lines](https://gocarta.s3.us-east-2.amazonaws.com/public/data/osm_pois/v1/data.jsonl)
- [shapefile](https://gocarta.s3.us-east-2.amazonaws.com/public/data/osm_pois/v1/data.points.shp.zip)

## preview links
- You can view the geojson on a map using [geojson.io](https://geojson.io/#data=data:text/x-url,https://gocarta.s3.us-east-2.amazonaws.com/public/data/osm_pois/v1/data.points.geojson).
- You can view the shapefile on a map using [shapefile.io](https://shapefile.io?url=https://gocarta.s3.us-east-2.amazonaws.com/public/data/osm_pois/v1/data.points.shp.zip).
- You can query the data with SQL using [duckdb](https://shell.duckdb.org/#queries=v0,CREATE-TABLE-dataset-AS-SELECT-*-FROM-'s3://gocarta/public/data/osm_pois/v1/data.parquet'~,Describe-dataset~).

## support
Post an issue [here](https://github.com/gocarta/dataops-osm-pois/issues) or email the package author at DanielDufour@gocarta.org.