from flask import Blueprint, request
import pandas as pd


main = Blueprint("main", __name__)


@main.route("/upload-csv-file", methods=["POST"])
def upload_csv_file():
    if request.method == "POST":
        if len(request.files) > 0:
            file = request.files.get("file")

            df = pd.read_excel(file, dtype=str)
            return {"Received Exel": f"{df}"}, 200
        return {"message": "No file found"}, 400


@main.route("/health", methods=["GET"])
def check_api_health():
    return {"status": "ok"}, 200
