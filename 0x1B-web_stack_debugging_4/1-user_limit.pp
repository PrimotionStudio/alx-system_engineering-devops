# Define a class to manage user configurations
exec { 'change-os-configuration-for-holberton-user':
  command => 'ex -s -c "/holberton hard/s/5/50000/g|x" /etc/security/limits.conf',
  path    => '/usr/bin/:/bin/'
}
