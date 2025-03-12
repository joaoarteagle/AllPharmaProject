

def data_processing(text):
    text = text.upper()

    subs = {
        'Ã': 'A', 'Õ': 'O', 'Â': 'A', 'Ê': 'E', 'Á': 'A', 'À': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ó': 'O', 'Ú': 'U', 'Ç':'C', ' ': ''
    }

    for char , sub in subs.items():
        text = text.replace(char, sub)
    return text
       
