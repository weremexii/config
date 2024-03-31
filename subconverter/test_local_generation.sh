#!/bin/sh
# this script tests profiles/test.ini
# before you commit and push any changes to github to make sub convertion widely usable as your configuration
# you can use this test method to test your config/profile/pref file
# NOTE that this test method is different from those that use the `getprofile` api, the latter will passthrough the requester's user agent, while this one use `subconverter [version]`, which can't guarantee usability when the sub provider check the requester's user agent
./subconverter -g --artifact "local test"
