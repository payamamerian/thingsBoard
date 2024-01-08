NAMES
1056ec718c9e kapua/kapua-console:1.6.10 "/bin/sh -c /var/opt…" 20 minutes ago Up 20 minutes 0.0.0.0:8080->8080/tcp, :::8080->8080/tcp, 0.0.0.0:8443->8443/tcp, :::8443->8443/tcp, 8778/tcp kapua-console
71d68ca43e47 kapua/kapua-api:1.6.10 "/bin/sh -c /var/opt…" 20 minutes ago Up 20 minutes 8778/tcp, 0.0.0.0:8081->8080/tcp, :::8081->8080/tcp, 0.0.0.0:8444->8443/tcp, :::8444->8443/tcp kapua-api
07283f061517 kapua/kapua-job-engine:1.6.10 "/bin/sh -c /var/opt…" 20 minutes ago Up 20 minutes 8080/tcp, 8443/tcp, 8778/tcp job-engine
9c11e1030289 kapua/kapua-broker:1.6.10 "/bin/sh -c /var/opt…" 20 minutes ago Up 20 minutes 1893/tcp, 8161/tcp, 0.0.0.0:1883->1883/tcp, :::1883->1883/tcp, 0.0.0.0:8883->8883/tcp, :::8883->8883/tcp, 8778/tcp, 0.0.0.0:61614->61614/tcp, :::61614->61614/tcp, 61615/tcp broker
7161acf99c8b kapua/kapua-events-broker:1.6.10 "/bin/sh -c /opt/art…" 20 minutes ago Up 20 minutes 0.0.0.0:5672->5672/tcp, :::5672->5672/tcp, 8778/tcp events-broker
12a02d7349f5 kapua/kapua-sql:1.6.10 "/bin/sh -c /var/opt…" 20 minutes ago Up 20 minutes 8181/tcp, 0.0.0.0:3306->3306/tcp, :::3306->3306/tcp, 8778/tcp db

kapua-sys
kapua-password