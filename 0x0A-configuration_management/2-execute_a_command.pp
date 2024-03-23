# kill_process.pp
# Define exec resource to kill the process

exec { 'killmenow':
  command => 'pkill killmenow',
  path    => '/bin:/usr/bin',
}
