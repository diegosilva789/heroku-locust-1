# Locust on Heroku with Private Spaces

This app is the minimum sample code of Locust which is the excellent and powerful graphical stress tool running on Heroku with Private Space. This Locust set Master/Slave configuration, and then you need to run your web dyno and worker dyno(s).
You can run your test scenarios right now after setting some environmental variables.

# Envirionmental variables

HOSTNAME:
This variable is required the target hostname (FQDN) with HTTP scheme such as 'https://www.example.com.'

URI?:
These variables are the target site's path starts with '/' and the "?" is the serial number of your test scenario begins with '1.' The default value is '/.'

MIN_WAIT:
This variable is the minimum time respectively, in milliseconds, that a simulated user will wait between MIN_WAIT and MAX_WAIT executing each task.

MAX_WAIT:
This variable is the maximum time respectively, in milliseconds, that a simulated user will wait between MIN_WAIT and MAX_WAIT executing each task.

# Heroku Button

Note: Install only into Heroku Private Space.

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)