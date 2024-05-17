# Define a class to manage user configurations
exec { 'change-os-configuration-for-holberton-user':
  command => '/bin/bash -c "echo \'holberton soft nofile 4096\' >> /etc/security/limits.conf && echo \'holberton hard nofile 8192\' >> /etc/security/limits.conf && echo \'session required pam_limits.so\' >> /etc/pam.d/common-session && echo \'session required pam_limits.so\' >> /etc/pam.d/common-session-noninteractive"',
  unless  => '/bin/bash -c "grep -q \'holberton soft nofile 4096\' /etc/security/limits.conf && grep -q \'holberton hard nofile 8192\' /etc/security/limits.conf && grep -q \'session required pam_limits.so\' /etc/pam.d/common-session && grep -q \'session required pam_limits.so\' /etc/pam.d/common-session-noninteractive"',
}
