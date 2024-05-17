exec { 'change-os-configuration-for-holberton-user':
  command => [
    '/bin/bash -c "echo \'holberton soft nofile 4096\' >> /etc/security/limits.conf"',
    '/bin/bash -c "echo \'holberton hard nofile 8192\' >> /etc/security/limits.conf"',
    '/bin/bash -c "echo \'session required pam_limits.so\' >> /etc/pam.d/common-session"',
    '/bin/bash -c "echo \'session required pam_limits.so\' >> /etc/pam.d/common-session-noninteractive"'
  ],
  unless  => [
    '/bin/bash -c "grep -q \'holberton soft nofile 4096\' /etc/security/limits.conf"',
    '/bin/bash -c "grep -q \'holberton hard nofile 8192\' /etc/security/limits.conf"',
    '/bin/bash -c "grep -q \'session required pam_limits.so\' /etc/pam.d/common-session"',
    '/bin/bash -c "grep -q \'session required pam_limits.so\' /etc/pam.d/common-session-noninteractive"'
  ],
}
