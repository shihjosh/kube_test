# Git Ci SSH 連線用

用法
```yaml
sync-git:
  stage: sync-git

  image:
    # An alpine-based image with the `docker` CLI installed.
    name: joshshih/ubuntu-ssh:20.04 # ubuntu:latest
  environment:
    name: sv
    url: $DEPLOY_STAGING_SSH_HOST
  services:
    - name: docker:dind
      alias: dockerdaemon

  variables:
    # Tell docker CLI how to talk to Docker daemon.
    DOCKER_HOST: tcp://dockerdaemon:2375/
    # Use the overlayfs driver for improved performance.
    DOCKER_DRIVER: overlay2
    # Disable TLS since we're running inside local network.
    DOCKER_TLS_CERTDIR: ""

  before_script:
    # - "command -v ssh-agent >/dev/null || ( apt-get update -y && apt-get install openssh-client -y )"
    - eval $(ssh-agent -s)
    - echo "$SSH_PRIVATE_KEY_STAGING" | tr -d '\r' | ssh-add -
    - mkdir -p ~/.ssh
    - echo -e "Host *\n\tStrictHostKeyChecking no\n\n" > ~/.ssh/config
    - echo "$SSH_KNOWN_HOSTS" >> ~/.ssh/known_hosts
    - chmod 700 ~/.ssh
    - chmod 644 ~/.ssh/known_hosts

  script:
    - echo "$BUILD_VERSION"
    - |
      ssh <user>@<IP>"
        set -x -e
        cd /home/user/testrepo/testgitci
        git pull https://xxxx:xxxx@git.gitlab.com/xxxx/xxxx.git master
        sed 's/<BUILD_TAG>/$BUILD_VERSION/1' templates/test.txt > test.txt
        git add .
        git commit -m 'test:$BUILD_VERSION'
        git push https://xxxx:xxxx@git.gitlab.com/xxxx/xxxx.git  master
        "
  dependencies:
    - tag
```