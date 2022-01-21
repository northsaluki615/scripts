## Setup Portainer, GUI for Docker

    docker volume create portainer_data
    docker run -d -p 8000:8000 -p 9443:9443 \
    --name portainer \
    --restart=unless-stopped \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v portainer_data:/data \
    cr.portainer.io/portainer/portainer-ce
