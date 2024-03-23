# Using Puppet, install flask from pip3.
# Requirements:
# Install flask
# Version must be 2.1.0

file {'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
