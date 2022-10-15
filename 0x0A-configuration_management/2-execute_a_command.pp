# a puppet that execute command
exec { 'pkill':
  command => 'pkill -9 -f killmenow',
  path    => '/usr/bin'
}
