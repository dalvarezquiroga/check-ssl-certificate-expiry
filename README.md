<img src="/assets/pythonmasses.jpg">

# Check SSL Certificate Expiry

Script to check SSL certificate information such as expiration date. Use AWS SES to send emails if the SSL certificate will expire soon.

## Getting Started

### Prerequisites

You have to have locally installed Python 3 *(Python 3.6 preferible)* as long as `pip` ,  `git`

### Installing

To get this project Up and Running in your local environment you must follow this guide:

#### Clone the repository

```bash
$ git clone https://github.com/dalvarezquiroga/check-ssl-certificate-expiry.git /tmp/app
Clonando en '/tmp/app'...
remote: Enumerating objects: 171, done.
remote: Counting objects: 100% (171/171), done.
remote: Compressing objects: 100% (115/115), done.
remote: Total 171 (delta 90), reused 110 (delta 52)
Recibiendo objetos: 100% (171/171), 23.92 KiB | 116.00 KiB/s, listo.
Resolviendo deltas: 100% (90/90), listo.
$ cd /tmp/app
```

#### Create a python 3.7 virtual environment

This projects runs using python 3.7 interprete so it's really important to create a virtual environment to run this application locally.

```bash
$ pwd
/tmp/app
$ virtualenv -p python3.7 .venv
Running virtualenv with interpreter /usr/bin/python3.7
Using base prefix '/usr'
New python executable in /tmp/app/.venv/bin/python3.7
Also creating executable in /tmp/app/.venv/bin/python
Installing setuptools, pip, wheel...
done.
$ source .venv/bin/activate
```

#### Create and/or export required environment variables

You can export the following variables:

```bash

    export smtp_host: $SMTP_HOST
    export smtp_port: $SMTP_PORT
    export smtp_user: $ACCESSKEY
    export smtp_password: $SECRETKEY
    export from: $FROM
    export to: $TO
    export sentry_dsn: $SENTRY_DSN
    export days_to_check: $DAYS_TO_CHECK
    export url_to_check: $URL_TO_CHECK
    export port: $URL_TO_CHECK_PORT
    export subject: $SUBJECT

```

#### Installing development dependencies

In order to create your local environment ready to develop, please install the development dependencies:

```yaml
$ (.venv) pip install -r requirements.txt
.......
......
Full output omitted
.....
....
Collecting raven==6.9.0 (from -r requirements.txt (line 1))
  Using cached https://files.pythonhosted.org/packages/11/3a/b3e46b279b8bdd9eb55857d0e95044cad31732c80f628bb75e1e9e881a32/raven-6.9.0-py2.py3-none-any.whl
Collecting pyOpenSSL==18.0.0 (from -r requirements.txt (line 2))
  Using cached https://files.pythonhosted.org/packages/96/af/9d29e6bd40823061aea2e0574ccb2fcf72bfd6130ce53d32773ec375458c/pyOpenSSL-18.0.0-py2.py3-none-any.whl
Collecting cryptography>=2.2.1 (from pyOpenSSL==18.0.0->-r requirements.txt (line 2))
  Using cached https://files.pythonhosted.org/packages/60/c7/99b33c53cf3f20a97a4c4bfd3ab66dcc93d99da0a97cc9597aa36ae6bb62/cryptography-2.4.2-cp34-abi3-manylinux1_x86_64.whl
Collecting six>=1.5.2 (from pyOpenSSL==18.0.0->-r requirements.txt (line 2))
  Downloading https://files.pythonhosted.org/packages/73/fb/00a976f728d0d1fecfe898238ce23f502a721c0ac0ecfedb80e0d88c64e9/six-1.12.0-py2.py3-none-any.whl
Collecting asn1crypto>=0.21.0 (from cryptography>=2.2.1->pyOpenSSL==18.0.0->-r requirements.txt (line 2))
  Using cached https://files.pythonhosted.org/packages/ea/cd/35485615f45f30a510576f1a56d1e0a7ad7bd8ab5ed7cdc600ef7cd06222/asn1crypto-0.24.0-py2.py3-none-any.whl
Collecting idna>=2.1 (from cryptography>=2.2.1->pyOpenSSL==18.0.0->-r requirements.txt (line 2))
  Downloading https://files.pythonhosted.org/packages/14/2c/cd551d81dbe15200be1cf41cd03869a46fe7226e7450af7a6545bfc474c9/idna-2.8-py2.py3-none-any.whl (58kB)
    100% |████████████████████████████████| 61kB 16.3MB/s 
Collecting cffi!=1.11.3,>=1.7 (from cryptography>=2.2.1->pyOpenSSL==18.0.0->-r requirements.txt (line 2))
  Using cached https://files.pythonhosted.org/packages/6d/c0/47db8f624f3e4e2f3f27be03a93379d1ba16a1450a7b1aacfa0366e2c0dd/cffi-1.11.5-cp36-cp36m-manylinux1_x86_64.whl
Collecting pycparser (from cffi!=1.11.3,>=1.7->cryptography>=2.2.1->pyOpenSSL==18.0.0->-r requirements.txt (line 2))
Installing collected packages: raven, asn1crypto, idna, pycparser, cffi, six, cryptography, pyOpenSSL
Successfully installed asn1crypto-0.24.0 cffi-1.11.5 cryptography-2.4.2 idna-2.8 pyOpenSSL-18.0.0 pycparser-2.19 raven-6.9.0 six-1.12.0

```

## Usage

python3.6 check_expiration_ssl.py

<img src="/assets/game.gif">

## Licence

MIT

## References

https://docs.python.org/3/library/smtplib.html

https://support.office.com/es-es/article/configuraci%C3%B3n-pop-imap-y-smtp-para-outlook-com-d088b986-291d-42b8-9564-9c414e2aa040

https://docs.aws.amazon.com/es_es/ses/latest/DeveloperGuide/smtp-connect.html

David Álvarez Quiroga
