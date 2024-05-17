# Define a class for Nginx configuration
exec { 'change-os-configuration-for-holberton-user':
  command => 'ex -s -c "/ULIMIT/s/15/4096/g|x" /etc/default/nginx',
  path    => '/usr/bin/:/bin/'
}