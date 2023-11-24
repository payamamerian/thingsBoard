sudo docker run -it -v ~/.tb-gateway/logs:/thingsboard_gateway/logs -v ~/.tb-gateway/extensions:/thingsboard_gateway/extensions -v ~/.tb-gateway/config:/thingsboard_gateway/config -p 8053:1883 --name tbGateway8322983184 -e host=83.229.83.184 -e port=1883 -e accessToken=aQSzwJBXbF1tBXxksIaz --restart always thingsboard/tb-gateway

sudo docker logs ffcb8034c7cd

sudo docker exec -it ffcb8034c7cd /bin/bash



