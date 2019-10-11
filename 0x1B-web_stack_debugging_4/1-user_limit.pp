# User limit
exec { 'delte line with pattern 1':
  path    => '/usr/bin:/usr/sbin:/bin',
  command => "sed -i '/holberton hard/d' /etc/security/limits.conf",
}
exec { 'delte line with pattern 2':
  require => Exec['delte line with pattern 1'],
  path    => '/usr/bin:/usr/sbin:/bin',
  command => "sed -i '/holberton soft/d' /etc/security/limits.conf",
}
exec { 'config the limit user 1':
  require => Exec['delte line with pattern 2'],
  path    => '/bin/echo:/usr/sbin:/bin',
  command => "sed -i '55i holberton hard nofile 5000'
  /etc/security/limits.conf",
}
exec { 'config the limit user 2':
  require => Exec['config the limit user 1'],
  path    => '/bin/echo:/usr/sbin:/bin',
  command => "sed -i '56i holberton soft nofile 4000'
  /etc/security/limits.conf",
}
