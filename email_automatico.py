import smtplib
from email.message import EmailMessage
from datetime import date, timedelta
from credenciais import senha_app

Date = date.today() + timedelta(0)
print("Data de Análise:", Date)

faturamento = 1500
qtd_produtos = 10
ticket = faturamento / qtd_produtos

def enviar_email():  
    corpo_email = f"""
    <h1> Analise executada em {Date}</h1>
    <p>Esse é o <b>primeiro email</b> enviado automaticamente</p>
    <p>Segundo parágrafo do email automatizado</p>
    <p>Este foi o ticket {ticket} para um faturamento de {faturamento}</p>
    """

    msg = EmailMessage()
    msg['Subject'] = "6 Horas Email automatizado"
    msg['From'] = 'raysonbernardodasilva@gmail.com'
    msg['To'] = 'rayson.bs@hotmail.com'
    password = senha_app
    msg.set_content(corpo_email, subtype='html')

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(msg['From'], password)
    s.send_message(msg)
    s.quit()
    print('Email enviado e consolidado final')

enviar_email()