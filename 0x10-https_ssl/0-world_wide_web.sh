#!/usr/bin/env bash
# Display information about subdomains.

domain_information () {
    subdomain=$1
    ip=$2
    state=$3

    echo "The subdomain $subdomain is a A record and points to $ip (State: $state)"
}


if [ "$#" == 1 ]
then
    domain=$1
    domain_information "www" "54.210.47.110" "running"
    domain_information "lb-01" "35.153.16.72" "running"
    domain_information "web-01" "54.237.117.138" "running"
    domain_information "web-02" "100.26.216.97" "running"
elif [ "$#" == 2 ]
then
    domain=$1
    subdomain=$2

    case $subdomain in
        "www")
            domain_information "www" "54.210.47.110" "running"
            ;;
        "lb-01")
            domain_information "lb-01" "35.153.16.72" "running"
            ;;
        "web-01")
            domain_information "web-01" "54.237.117.138" "running"
            ;;
        "web-02")
            domain_information "web-02" "100.26.216.97" "running"
            ;;
        *)
            echo "Invalid subdomain"
            ;;
    esac
fi
