# create a file in tmp folder
file { 'file':
    path    => '/tmp/holberton',
    owner   => 'www-data',
    group   => 'www-data',
    mode    => '0744',
    content => 'I love Puppet';
}
