import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(subject, body, to_email, password, from_email):
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, password)
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        server.quit()
        return 'Email sent successfully'
    except Exception as e:
        return f'Failed to send email: {e}'

def send_multiple_emails(subject, body, to_email, password, from_email, num_times):
    messages = []
    for i in range(num_times):
        unique_subject = f"{subject} - {i+1}"
        message = send_email(unique_subject, body, to_email, password, from_email)
        messages.append(message)
    return messages
