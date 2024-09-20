from flask import Flask, request, jsonify
from db_utility import get_annual_data, save_to_database
from data_transform import load_and_process_data

app = Flask(__name__)
DB_PATH = 'production_data.db'
EXCEL_FILE_PATH = 'Inerg_data.xls'

def initialize_database():
    annual_data = load_and_process_data(EXCEL_FILE_PATH)
    save_to_database(annual_data, DB_PATH)

@app.route('/')
def root():
    return "Inerg Assessment"

@app.route('/data', methods=['GET'])
def data():
    try:
        well = request.args.get('well')
        if well:
            annual_data = get_annual_data(well, DB_PATH)
            if annual_data:
                return jsonify(annual_data)
            else:
                return jsonify({"error": "Well not found"}), 404
        return jsonify({"error": "Well number required"}), 400
    except Exception as e:
        raise Exception(f"Unable to fetch well data:{str(e)}")

if __name__ == '__main__':
    initialize_database()
    app.run(port=8080)
