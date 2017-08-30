This repository contains CSV data files that contain information for Twitter
users who retweeted two tweets:

* https://twitter.com/briankrebs/status/902545914304319491
* https://twitter.com/benimmo/status/902673891792965637

The theory being that briankrebs and benimmo's use of Twitter was being
disrupted by a botnet that was retweeting their account and following them. The
retweets were collected using [this
approach](https://gist.github.com/edsu/94901f4a6454805f04fff6d9c10b0b8a).

[csvkit](https://csvkit.readthedocs.io) is handy for joining the CSVs:

    csvsq': csvsql --query "select briankrebs.* from briankrebs, benimmo where briankrebs.screen_name = benimmo.screen_name" briankrebs.csv bennimo.csv > briankrebs_benimmo.csv

