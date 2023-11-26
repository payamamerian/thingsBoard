sudo docker run -it -v ~/.tb-gateway/logs:/thingsboard_gateway/logs -v ~/.tb-gateway/extensions:/thingsboard_gateway/extensions -v ~/.tb-gateway/config:/thingsboard_gateway/config -p 8053:1883 --name tbGateway8322983184 -e host=83.229.83.184 -e port=1883 -e accessToken=aQSzwJBXbF1tBXxksIaz --restart always thingsboard/tb-gateway

sudo docker logs ffcb8034c7cd

sudo docker exec -it ffcb8034c7cd /bin/bash

docker restart ffcb8034c7cd


/thingsboard_gateway/config/tb_gateway.json
/thingsboard_gateway/config/socket.json

#py file
thingsboard_gateway/extensions/socket

docker cp tbGateway8322983184:/thingsboard_gateway/config/socket.json /etc

find / -type f -name "tb_gateway_service.py"
