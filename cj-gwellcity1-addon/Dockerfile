ARG BUILD_FROM
FROM $BUILD_FROM

# Install requirements for add-on
RUN apk add --no-cache python3 py3-pip

# Python 패키지 설치
RUN pip3 install --no-cache-dir paho-mqtt requests

# Copy data for add-on
COPY rootfs /

# Set executable permissions
RUN chmod a+x /etc/services.d/gwellcity1/run
RUN chmod a+x /etc/services.d/gwellcity1/finish
RUN chmod a+x /usr/bin/gwellcity1.py

CMD [ "/usr/bin/with-contenv", "bashio" ]
