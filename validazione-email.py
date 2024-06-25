## realizziamo una funzione che, prendendo in input una lista di indirizzi email, ritorni una nuova lista degli indirizzi email validi ordinati alfabeticamente.
## un indirizzo email è valido se:
## ha il formato nomeutente@dominio.ext
#il nome utente continiene soltanto numero, lettere, line (-) e underscore _
#il dominio continuene soltato lettere e numerio
#la lunghezza massima dell'ext è 3 caratteri
import re

# Funzione per validare un singolo indirizzo email
def validate_email(email):
    pattern = r'^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$'
    return re.match(pattern, email) is not None

# Funzione per filtrare e ordinare una lista di indirizzi email
def filter_and_sort_emails(email_list):
    valid_emails = [email for email in email_list if validate_email(email)]
    valid_emails.sort()
    return valid_emails

# Prendere in input una lista di indirizzi email dall'utente
email_input = input("Inserisci 5 indirizzi email separati da spazi o virgole: ")

# Separare l'input in una lista di email
email_list = [email.strip() for email in re.split(r'[ ,]+', email_input)]

# Filtrare e ordinare gli indirizzi email validi
valid_sorted_emails = filter_and_sort_emails(email_list)

# Stampare la lista degli indirizzi email validi e ordinati
print("Indirizzi email validi e ordinati:")
for email in valid_sorted_emails:
    print(email)



# def validate_email(email):
#     parts = email.split("@")
#     if len(parts)!=2:
#         return False
    
#     name, parts = parts
#     parts = parts.split(".")
    
#     if len(parts) != 2:
#         return False
    
#     domain, ext = parts
    
#     if not name.replace("-", "").replace("_", "").isalnum():
#         return False
    
#     if not domain.isalnum():
#         return False
    
#     if len(ext)>3:
#         return False
    
#     return True