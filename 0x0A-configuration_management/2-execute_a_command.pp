# execute a command
exec { 'kill':
    command => 'pkill killmenow || echo "Process was not running."',
    path    => '/usr/bin'
}
