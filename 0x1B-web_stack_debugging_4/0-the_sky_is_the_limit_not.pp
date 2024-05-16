# Define a class for Nginx configuration
class { 'nginx':
  manage_repo => true, # Ensures Nginx repository is managed
  service_manage => true, # Ensures Nginx service is managed
}

# Define a resource to configure Nginx settings
file { '/etc/nginx/nginx.conf':
  ensure  => file,
  content => template('nginx/nginx.conf.erb'), # Use a template for configuration
  notify  => Service['nginx'], # Restart Nginx service when configuration changes
}

# Define a template for Nginx configuration
# This template should include optimizations for performance and reliability
# Example:
# ```
# user nginx;
# worker_processes auto;
# events {
#   worker_connections 1024;
#   multi_accept on;
# }
# http {
#   ...
# }
# ```

# Define a resource to manage Nginx sites
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx/default_site.erb'), # Use a template for site configuration
  notify  => Service['nginx'], # Restart Nginx service when configuration changes
}

# Define a resource to enable the default site
file { '/etc/nginx/sites-enabled/default':
  ensure => link,
  target => '/etc/nginx/sites-available/default',
  notify => Service['nginx'], # Restart Nginx service when configuration changes
}

