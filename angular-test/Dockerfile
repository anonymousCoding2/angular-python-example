FROM node:20-alpine as builder

RUN mkdir /project
WORKDIR /project/angular-test

RUN npm install -g @angular/cli@13


CMD ["ng", "serve", "--host", "0.0.0.0"]
#CMD ["tail", "-f", "/dev/null"]

FROM builder as dev-envs

RUN <<EOF
apt-get update
apt-get install -y --no-install-recommends git
EOF

RUN <<EOF
useradd -s /bin/bash -m vscode
groupadd docker
usermod -aG docker vscode
EOF
# install Docker tools (cli, buildx, compose)
COPY --from=gloursdocker/docker / /


#RUN ng new angular-docker
#WORKDIR /project/angular-docker

CMD ["ng", "serve", "--host", "0.0.0.0"]
