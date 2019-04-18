## Locust on Heroku with Private Spaces

This app is the minimum sample code of Locust which is the excellent and powerful graphical stress tool running on Heroku with Private Space. This Locust set Master/Slave configuration, and then you need to run your web dyno and worker dyno(s).
You can run your test scenarios right now after setting some environmental variables.

## Envirionmental variables

### HOSTNAME: (required)
This variable is the target hostname (FQDN) with HTTP scheme such as 'https://www.example.com.'

### URI?: (optional)
These variables are the target site's path from starts with '/.' The default value is '/.'
Your need multiple test scenarios to set various environmental variables and the `?` is the serial number of your test scenario begins with '1.'

### MIN_WAIT: (optional)
This variable is the minimum time respectively, in milliseconds, that a simulated user will wait between MIN_WAIT and MAX_WAIT executing each task. The default value is 5000(ms).

### MAX_WAIT: (optional)
This variable is the maximum time respectively, in milliseconds, that a simulated user will wait between MIN_WAIT and MAX_WAIT executing each task. The default value is 15000(ms).

## Heroku Button

Notice: Install only into Heroku Private Space.

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)