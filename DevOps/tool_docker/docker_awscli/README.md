# Git Ci AWS Push ECR用

用法
```yaml
build:
  stage: build

  image:
    name: docker:latest #amazon/aws-cli

  services:
    - name: docker:dind
      alias: dockerdaemon

  variables:
    DOCKER_HOST: tcp://dockerdaemon:2375/
    DOCKER_DRIVER: overlay2
    DOCKER_TLS_CERTDIR: ""
    DOCKER_REGISTRY: xxxxx.dkr.ecr.ap-northeast-1.amazonaws.com
    AWS_DEFAULT_REGION: ap-northeast-1
    APP_NAME: blue-whale

  before_script:
    - apk add --no-cache curl jq python3 py3-pip
    - pip install awscli
    - aws ecr get-login-password | docker login --username AWS --password-stdin $DOCKER_REGISTRY
    - aws --version
    - docker info
    - docker --version
  script:
    # - docker build -t $DOCKER_REGISTRY/$APP_NAME:$CI_PIPELINE_IID .
    # - docker push $DOCKER_REGISTRY/$APP_NAME:$CI_PIPELINE_IID
    - docker build -t $DOCKER_REGISTRY/$APP_NAME:$BUILD_VERSION .
    - docker push $DOCKER_REGISTRY/$APP_NAME:$BUILD_VERSION

  dependencies:
    - tag
```

