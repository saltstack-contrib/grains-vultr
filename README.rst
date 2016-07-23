.. image:: https://travis-ci.org/saltstack-contrib/grains-vultr.svg?branch=master
    :target: https://travis-ci.org/saltstack-contrib/grains-vultr

========================
Vultr.com metadata grain
========================

This grain pulls data from the vultr.com metadata service

The grains look like the following (as of 20160716... the service seems to be evolving)

::

    vu001:
        ----------
        bgp:
            ----------
            ipv4:
                ----------
                my-address:
                my-asn:
                peer-address:
                peer-asn:
            ipv6:
                ----------
                my-address:
                my-asn:
                peer-address:
                peer-asn:
        hostname:
            vultr.guest
        instanceid:
            1111111
        interfaces:
            |_
              ----------
              ipv4:
                  ----------
                  additional:
                  address:
                      45.1.2.2
                  gateway:
                      45.1.1.1
                  netmask:
                      255.255.254.0
              ipv6:
                  ----------
                  additional:
                  network:
                  prefix:
              mac:
                  de:ad:be:ef:c5:99
              network-type:
                  public
        public-keys:
            ssh-rsa ... user@host1
            ssh-rsa ... user@host2
            ssh-rsa ... user@host3
        region:
            ----------
            regioncode:
                LAX
        user-defined:
    vu002:
        ----------
        bgp:
            ----------
            ipv4:
                ----------
                my-address:
                my-asn:
                peer-address:
                peer-asn:
            ipv6:
                ----------
                my-address:
                my-asn:
                peer-address:
                peer-asn:
        hostname:
            vultr.guest
        instanceid:
            2222222
        interfaces:
            |_
              ----------
              ipv4:
                  ----------
                  additional:
                  address:
                      45.1.2.3
                  gateway:
                      45.1.1.1
                  netmask:
                      255.255.254.0
              ipv6:
                  ----------
                  additional:
                  network:
                      2001:19f0:1000:ffff::
                  prefix:
                      64
              mac:
                  de:ad:be:ed:41:b2
              network-type:
                  public
            |_
              ----------
              ipv4:
                  ----------
                  additional:
                  address:
                      10.1.0.13
                  gateway:
                  netmask:
                      255.255.0.0
              ipv6:
                  ----------
                  additional:
                  network:
                  prefix:
              mac:
                  de:ad:be:ef:41:b2
              network-type:
                  private
        public-keys:
        region:
            ----------
            regioncode:
                LAX
        user-defined:

