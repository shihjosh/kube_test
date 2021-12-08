FROM php:7.4-apache

# Install Xdebug
RUN pecl install -f xdebug
RUN echo "zend_extension=$(find /usr/local/lib/php/extensions/ -name xdebug.so)" > /usr/local/etc/php/conf.d/xdebug.ini;
