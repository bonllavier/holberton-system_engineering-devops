# 0. Strace is your friend
exec { 'wordpress config file fixed':
  path    => '/usr/bin:/usr/sbin:/bin',
  command => "sed -i 's/.phpp/.php/g' /var/www/html/wp-settings.php",
}
