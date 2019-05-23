from flask import Blueprint, Flask, render_template, request

main = Blueprint('main', __name__)

import json
from engine import ClusteringEngine

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@main.route("/clusterRegion", methods=["GET"])
def clusterRegionFormPage():
    return render_template('clusterForm.html')

@main.route("/clusterRegion", methods=["POST"])
def cluster_region():
    """"Untuk menambahkan sebuah region ke dataset"""
    # get the location cluster from the Flask POST request object
    data_id_fetched = int(request.form.get('data_id'))
    iso_fetched = int(request.form.get('iso'))
    event_id_cnty_fetched = request.form.get('event_id_cnty')
    event_id_no_cnty_fetched = int(request.form.get('event_id_no_cnty'))
    event_date_fetched = request.form.get('event_date')
    year_fetched = int(request.form.get('year'))
    time_precision_fetched = int(request.form.get('time_precision'))
    event_type_fetched = request.form.get('event_type')
    actor1_fetched = request.form.get('actor1')
    assoc_actor_1_fetched = request.form.get('assoc_actor_1')
    inter1_fetched = int(request.form.get('inter1'))
    actor2_fetched = request.form.get('actor2')
    assoc_actor_2_fetched = request.form.get('assoc_actor_2')
    inter2_fetched = int(request.form.get('inter2'))
    interaction_fetched = int(request.form.get('interaction'))
    region_fetched = request.form.get('region')
    country_fetched = request.form.get('country')
    admin1_fetched = request.form.get('admin1')
    admin2_fetched = request.form.get('admin2')
    admin3_fetched = request.form.get('admin3')
    location_fetched = request.form.get('location')
    latitude_fetched = float(request.form.get('latitude'))
    longitude_fetched = float(request.form.get('longitude'))
    geo_precision_fetched = int(request.form.get('geo_precision'))
    source_fetched = request.form.get('source')
    source_scale_fetched = request.form.get('source_scale')
    notes_fetched = request.form.get('notes')
    fatalities_fetched = request.form.get('fatalities')
    timestamp_fetched = request.form.get('timestamp')
    iso3_fetched = request.form.get('iso3')
    model_fetched = int(request.form.get('ModelSelected'))
    # add them to the model using then engine API
    cluster_location = clustering_engine.cluster_region(latitude_fetched, longitude_fetched, model_fetched)
    return render_template('clusterResult.html', latitude=latitude_fetched, longitude=longitude_fetched, cluster=cluster_location)

def create_app(spark_session, dataset_path):
    global clustering_engine

    clustering_engine = ClusteringEngine(spark_session, dataset_path)

    app = Flask(__name__)
    app.register_blueprint(main)
    return app