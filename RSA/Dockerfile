FROM httpd
LABEL mainteiner="Rafael Jose Montoya <rjmp1991@gmail.com>"
LABEL Description="RSAES-OAEP-SHA256" Vendor="RafaelMontoya" Version="1"
ENV TZ=America/Bogota
RUN mkdir -p /usr/local/apache2/htdocs/encrypt
COPY index.html  /usr/local/apache2/htdocs/encrypt/.
EXPOSE 80