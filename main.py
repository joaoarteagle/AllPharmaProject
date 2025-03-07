import gspread
from oauth2client.service_account import ServiceAccountCredentials
from functions import data_processing

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive" ]



credenciais =  ServiceAccountCredentials.from_json_keyfile_name('./data/keys.json', scope)

cliente = gspread.authorize(credenciais)

sheet = cliente.open('backups_allpharma').sheet1


dados = sheet.get_all_records(1)


with open('./data/clientes.txt', 'w') as file:
    for dado in dados:
        cliente = data_processing(dado.get('Clientes'))
        if('NULL' in dado.get('BACKUP')):continue
        print("\n")
        print(f'{cliente}-{dado.get('BACKUP')}')
        
        file.write(f"{cliente}-{dado.get('BACKUP')};\n")

file.close()










    

