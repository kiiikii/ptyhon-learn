import argparse
import datetime
from datetime import date

def calculate_age(born):
    today = date.today()
    age = today.year - born.year - ((today.month, today.day)<(born.month, born.day))
    return age

def valid_date(t):
    try:
        return datetime.datetime.strptime(t, '%a %b %d %Y').strftime('%d-%m-%Y')
    except ValueError:
        msg = "not a valid date: '{0}'.".format(t)
        raise argparse.ArgumentTypeError(msg)

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-n', '--nama', required=True, help="masukkan nama anda")
parser.add_argument('-t', '--tanggal', required=True, help="masukkan tanggal lahir - format DD-MM-YYYY", type=valid_date)

args = parser.parse_args()
if calculate_age < 30:
    print("Terima kasih telah menggunakan panggildicoding.py, kakak "+args.nama)
else:
    print("Terima kasih telah menggunakan panggildicoding.py, bapak "+args.nama)
