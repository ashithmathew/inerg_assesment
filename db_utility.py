import sqlite3

def get_annual_data(well_number, db_path):
    try:
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        query = f'''SELECT * from production where "API WELL  NUMBER"={well_number}'''
        cursor.execute(query)
        result = cursor.fetchone()
        return {"oil": result['OIL'], "gas": result['GAS'], "brine": result['BRINE']} if result else None
    except Exception as e:
        raise Exception(f"Error retrieving data for well {well_number}: {e}")


def save_to_database(data, db_path):
    try:
        conn = sqlite3.connect(db_path)
        data.to_sql('production', conn, if_exists='replace', index=False)
    except Exception as e:
        raise Exception(f"Error saving data to database: {e}")
