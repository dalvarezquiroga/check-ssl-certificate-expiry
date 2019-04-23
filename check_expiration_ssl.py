
#!/usr/bin/python3
# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from os import environ
from raven import Client, transport
import smtplib
import socket
import ssl
import OpenSSL
import time


def get_remote_certificate(url_to_check, port):
    # This function loads the certificate from the specified URL and returns the certificate details.       
    print(" Opening socket connection to {} ...".format(url_to_check))
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ssl_sock = context.wrap_socket(s, server_hostname=url_to_check)
    print(" Checking ..." )
    ssl_sock.connect((url_to_check, port))
    ssl_sock.close()
    print(" Closing socket connection ...")
    
    encrypted_cert = ssl.get_server_certificate((url_to_check, port))
    decrypted_cert = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, encrypted_cert)
    return decrypted_cert


def check_if_certificate_has_expired(remote_certificate):
    # This function checks if the certificate has expired. Also it returns true or false in addition to delta.days.
    expire_day = datetime.strptime(remote_certificate.get_notAfter().decode('ascii'),'%Y%m%d%H%M%SZ')
    today = datetime.now()

    delta = expire_day - today
    if delta.days <= (local_env['days_to_check']):
        return [True, delta.days]
    else:
        return [False, delta.days]


def send_failure_email(subject, days_to_expire, url, local_env):
    # This function sends an email if the certificate is valid for 30 days.
    message_body = 'Your SSL cerficate {1} will expire in {0} days.'.format(days_to_expire, url)
    server = smtplib.SMTP(local_env['smtp_host'], local_env['smtp_port'])
    #server.set_debuglevel(1)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(local_env['smtp_user'], local_env['smtp_password'])
    message = 'Subject: {}\n\n{}'.format(subject, message_body)
    server.sendmail(local_env['from'], local_env['to'], message)
    server.quit()
    print(" Mail sent successfully ") 


if __name__ == '__main__':
    try:
        #Get environment variables
        local_env = {
         'smtp_host': environ.get('SMTP_HOST'),
         'smtp_port': int(environ.get('SMTP_PORT')),
         'smtp_user': environ.get('ACCESSKEY'),
         'smtp_password': environ.get('SECRETKEY'),
         'from': environ.get('FROM'),
         'to': environ.get('TO'),
         'sentry_dsn': environ.get('SENTRY_DSN'),
         'days_to_check': int(environ.get('DAYS_TO_CHECK')),
         'url_to_check': environ.get('URL_TO_CHECK'),
         'port': int(environ.get('URL_TO_CHECK_PORT')),
         'subject': environ.get('SUBJECT')
        }

        # Separate on comma domains to check.
        domains = local_env['url_to_check'].split(",")
        

        for url in domains:
            print(" Waiting the next Certificate ")
            remote_certificate = get_remote_certificate((url), local_env['port'])
            expiration_result = check_if_certificate_has_expired(remote_certificate)      
            if expiration_result[0]:
                send_failure_email(local_env['subject'], expiration_result[1], url, local_env)
            else:
                print(' Your SSL cerficate {1} is OK. --> Will expire in {0} days.'.format(expiration_result[1], url))

            print(" ===========================")
            time.sleep(5)

    except:
        if environ.get(local_env['sentry_dsn'], None):
            client = Client(
                (local_env['sentry_dsn'], None), transport=transport.http.HTTPTransport)
            client.captureException()
        raise


