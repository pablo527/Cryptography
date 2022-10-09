FROM nginx
LABEL mainteiner="Rafael Jose Montoya <rjmp1991@gmail.com>"
LABEL Description="nginx tls" Vendor="RafaelMontoya" Version="1"
ENV TZ=America/Bogota

RUN mkdir -p /etc/nginx-server-certs && mkdir -p /etc/nginx/client_certs/ && rm /etc/nginx/nginx.conf

COPY nginx.crt nginx.key /etc/nginx-server-certs/
COPY ca.crt /etc/nginx/client_certs/
COPY nginx.conf /etc/nginx/

EXPOSE 443
