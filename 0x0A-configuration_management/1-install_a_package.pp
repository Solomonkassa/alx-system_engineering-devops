# To install Flask version 2.1.0 using Puppet
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
