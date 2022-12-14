from datetime import datetime 

# converte data do farmato ISO (YYYY-MM-DD HH:MM:SS) para DD/MM/YYYY, HH:MM:SS
def config_data(response):
    # ISO format
    iso_format = "%Y-%m-%d %H:%M:%S"

    for d in response["Coordenadas"]:
        iso_date = d["Data e Hora"]
        # Convert the string into a datetime object
        data = datetime.strptime(iso_date, iso_format)
        #print(data.strftime("%m/%d/%Y, %H:%M:%S"))
        d["Data e Hora"] = data.strftime("%m/%d/%Y, %H:%M:%S")
    return response