# create a file in tmp folder
file { '/etc/ssh/ssh_config':
  ensure => present,
}->
file_line { 'file':
  ensure => present,
  path   => '/etc/ssh/sshd_config',
  line   => 'PasswordAuthentication no',
  match  => '^PasswordAuthentication.*',
}->
file_line { 'Find Identity file':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/holberton',
  match  => '^IdentityFile.*',
}
