import pandas as pd

def load_and_process_data(file_path):
    try:
        data = pd.read_excel(file_path)
        annual_data = data.groupby('API WELL  NUMBER').sum().reset_index()
        annual_data = annual_data[['API WELL  NUMBER', 'OIL', 'GAS', 'BRINE']]
        return annual_data
    except Exception as e:
        raise Exception(f"Error processing data: {e}")