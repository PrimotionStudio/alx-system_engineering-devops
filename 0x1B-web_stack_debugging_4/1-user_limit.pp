# Define a class to manage user configurations
class user_config {

  # Define a resource to set ulimit for the holberton user
  exec { 'increase-file-limit':
    command => 'ulimit -n 65535', # Set the maximum number of open file descriptors
    user    => 'holberton',        # Specify the user for whom the limit will be set
    path    => '/bin:/usr/bin',     # Set the PATH to ensure the ulimit command is found
    unless  => 'test $(ulimit -n) -eq 65535', # Check if the limit is already set
    notify  => Service['ssh'],      # Restart SSH service if the limit is changed
  }
}

# Include the class to apply the configuration
include user_config

