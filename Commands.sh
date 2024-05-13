sudo docker run -it -v ~/.tb-gateway/logs:/thingsboard_gateway/logs -v ~/.tb-gateway/extensions:/thingsboard_gateway/extensions -v ~/.tb-gateway/config:/thingsboard_gateway/config -p 8053:8053 --name tbGateway8322983184 -e host=83.229.83.184 -e port=1883 -e accessToken=qSG3MQNnHbzOGsZmL0cX --restart always thingsboard/tb-gateway


sudo docker logs ffcb8034c7cd

sudo docker exec -it ffcb8034c7cd /bin/bash

docker restart ffcb8034c7cd


/thingsboard_gateway/config/tb_gateway.json
/thingsboard_gateway/config/socket.json

#py file
thingsboard_gateway/extensions/socket

docker cp tbGateway8322983184:/thingsboard_gateway/config/socket.json /etc

find / -type f -name "tb_gateway_service.py"

nohup python3 server.py &

--------------------------PE
sudo docker run -d -it -p 8053:8053 -v ~/.tb-pe-tcp-udp-integration-logs:/var/log/tb-tcp-udp-integration  \
-e "RPC_HOST=52.65.144.195" -e "RPC_PORT=9090" \
-e "INTEGRATION_ROUTING_KEY=99a3ec21-d8ac-9078-f8e8-60059c96c83d"  -e "INTEGRATION_SECRET=kl6jk7z2qno3te3m43xk" \
--name my-tb-pe-tcp-udp-integration --restart always thingsboard/tb-pe-tcp-udp-integration:3.6.1PE


-------------------------- External Server
sudo ufw allow 8053

----------------------- ng serve
set NODE_OPTIONS=--max-old-space-size=8048 && ng serve

------------------------ access Docker environment 
 docker exec -u root -it fef3a34abf7f /bin/sh


