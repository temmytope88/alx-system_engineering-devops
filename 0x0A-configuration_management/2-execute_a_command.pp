exec { 'killmenow':
  command => 'pkill killmenow'
  path    => ['/usr/bin', 'usr/bin', '/bin']
}
