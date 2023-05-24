#紀錄未整理

環境:
Print versions
java -version openjdk:8
node -v v16.17.1
npm -v 8.15.0
cordova -v 11.0.0
gradle -v  7.1.1
sdkmanager --list

建置流程:
docker run -it -v <local-app-src>:/opt/src --rm hamdifourati/cordova-android-builder bash

root@cordova:/opt/src# cordova remove add android
root@cordova:/opt/src# cordova platform add android@8.1.0 #9.0.0
root@cordova:/opt/src# cordova build

docker run -it -v /home/josh/Desktop/test:/opt/src --rm hamdifourati/cordova-android-builder bash
docker run -it -v /home/josh/Desktop/test:/opt/src --rm joshshih/cordova:v03 bash

cordova build android -- --gradleArg=-PcdvCompileSdkVersion=30


docker image build -t joshshih/cordova27:v01 .

docker run -it -v C:\Users\clayk\Desktop\docker\cordova_docker\cordova:/opt/src --rm joshshih/cordovajdk:v08 bash

root@cordova:/opt/src# cordova platform add android
root@cordova:/opt/src# cordova requirements
root@cordova:/opt/src# cordova build

npm i
cd cordova
npm i
cordova platform remove android
cordova platform add android@9.0.0  
cordova platform add android@9.0.0 --no-interactive
cd ..
npm run xxxx

cordova platform add android@8.1.0  

Please make sure you are using a supported platform and node version. If you
npm ERR! would like to compile fibers on this machine please make sure you have setup your
npm ERR! build environment--
npm ERR! Windows + OS X instructions here: https://github.com/nodejs/node-gyp
npm ERR! Ubuntu users please run: `sudo apt-get install g++ build-essential`
npm ERR! RHEL users please run: `yum install gcc-c++` and `yum groupinstall 'Development Tools'`
npm ERR! Alpine users please run: `sudo apk add python make g++`
npm ERR! sh: 1: nodejs: not found


/usr/local/android-sdk-linux

export ANDROID_HOME=/path/to/android/sdk

export ANDROID_HOME=/usr/local/android-sdk-linux
export PATH=$PATH:$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools

docker run -it -v C:\Users\clayk\Desktop\docker\cordova_docker\nuxtjs-frontend-spa:/opt/src --rm hamdifourati/cordova-android-builder bash

# Check dependencies are installed and configured.
docker run -v <local-app-src>:/opt/src --rm hamdifourati/cordova-android-builder cordova requirements

# Build Android apk
docker run -v <local-app-src>:/opt/src --rm hamdifourati/cordova-android-builder cordova build

