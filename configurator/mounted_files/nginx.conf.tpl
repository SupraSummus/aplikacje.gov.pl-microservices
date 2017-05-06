events {}

http {
    server {
        listen 80;
        {% for service in services %}
            location {{ service.path }} {
                proxy_pass http://{{ service.service.host }}:{{service.service.port}}{{service.service.path}};
            }
        {% endfor %}

    }
}
