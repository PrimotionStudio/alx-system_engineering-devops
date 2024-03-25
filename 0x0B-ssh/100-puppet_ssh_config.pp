# 100-puppet_ssh_config.pp

$ssh_config_file = '/etc/ssh/ssh_config'
file { $ssh_config_file:
  ensure => present,
}

file_line { 'Declare identity file':
  path  => $ssh_config_file,
  line  => 'IdentityFile ~/.ssh/school',
}

file_line { 'Turn off passwd auth':
  path  => $ssh_config_file,
  line  => 'PasswordAuthentication no',
}
