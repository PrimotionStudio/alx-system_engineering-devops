#screw you
exec { 'find_and_replace':
  command => '/bin/sed -i \'s/phpp/php/g\' /var/www/html/wp-settings.php',
  path    => ['/bin', '/usr/bin', '/usr/local/bin'],
  onlyif  => 'grep -q phpp /var/www/html/wp-settings.php',
}
