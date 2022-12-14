import datetime

def sample_responses(input_text):
    user_message = str(input_text).lower()
    
    if user_message in ('hello', 'hi', 'halo'):
        return 'Hei! Kamu Ganteng Banget'
    
    if user_message in ('kamu siapa'):
        return "I am Fauzan bot!"
    
    if user_message in ('siapa yang buat'):
        return "Bos saya Fauzan!"

    if user_message in ("time", "time?"):
        now = datetime.datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")
        return str(date_time)
    
    else:
        return 'Saya Gak Paham'