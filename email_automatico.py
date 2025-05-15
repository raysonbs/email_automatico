import smtplib
from email.message import EmailMessage
import datetime
from datetime import date, timedelta


Date = date.today() + timedelta(0)
print("Data de Análise:",Date)

faturamento = 1500
qtd_produtos = 10
ticket = faturamento/qtd_produtos


def enviar_email():  
    corpo_email = f"""
    <h1> Analise executada em {Date}</h1>
    <p>Esse e o <b>primeiro email</b> enviado automaticamente</p>
    <p>Segundo  
    paragrafo do email automatizado
    </p>
    <p> esse foi o ticket {ticket} para um faturamento de {faturamento}</p>
    <p>Date
    <?php
        Date
    ?>
    </p>
    """

    msg = EmailMessage.Message()
    msg['Subject'] = "6 Horas Email automatizado 6 Horas"
    msg['From'] = 'raysonbernardodasilva@gmail.com'
    msg['To'] = 'rayson.bs@hotmail.com'
    password = 'zufk yeit ytsr qqbq' 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')


# In[ ]:


enviar_email()