# a puppet that execute command
exec { 'pkill':
  command => 'pkill killmenow'
  path    => ['/usr/bin', 'usr/bin', '/bin']
}
