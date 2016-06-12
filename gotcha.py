# -*- coding: utf-8 -*-

import sys
import optparse
import ConfigParser

import requests

if __name__ == "__main__":
    config = ConfigParser.ConfigParser()
    config.read('scrapy.cfg')
    api_prefix = config.get("deploy", "url")

    command_list = ["run", "cancel", "status", "list"]

    optparser = optparse.OptionParser()
    optparser.add_option("-c", "--command", dest="command", choices=command_list, help="Please input command ({cl})".format(cl=", ".join(command_list)))

    run_optgroup = optparse.OptionGroup(optparser, "Run Options")
    run_optgroup.add_option("-s", "--spider", dest="spider", help="A spider name to run crawl")
    optparser.add_option_group(run_optgroup)

    cancel_optgroup = optparse.OptionGroup(optparser, "Cancel Options")
    cancel_optgroup.add_option("-j", "--job", dest="job", help="A job id to cancel crawl")
    optparser.add_option_group(cancel_optgroup)

    (opts, args) = optparser.parse_args()

    if opts.command:
        if opts.command == "run":
            if not opts.spider:
                sys.stderr.write("Undefined spider name\n")
                sys.exit(1)

            api = "{api_prefix}/schedule.json".format(api_prefix=api_prefix)
            data = {
                "project": "gotcha",
                "spider": opts.spider,
            }
            r = requests.post(api, data)
            if r.status_code == 200:
                jobid = r.json()["jobid"]
                sys.stdout.write(jobid + "\n")
                sys.exit(0)
            else:
                sys.stderr.write("HTTP Request is not 'OK' : %s\n" % api)
                sys.exit(1)
        elif opts.command == "cancel":
            if not opts.job:
                sys.stderr.write("Undefined job\n")
                sys.exit(1)

            api = "{api_prefix}/cancel.json".format(api_prefix=api_prefix)
            data = {
                "project": "gotcha",
                "spider": opts.job,
            }
            r = requests.post(api, data)
            if r.status_code == 200:
                status = r.json()["status"]
                sys.stdout.write(status + "\n")
                sys.exit(0)
            else:
                sys.stderr.write("HTTP Request is not 'OK' : %s\n" % api)
                sys.exit(1)
        elif opts.command == "status":
            api = "{api_prefix}/listjobs.json?project=gotcha".format(api_prefix=api_prefix)
            r = requests.get(api)
            if r.status_code == 200:
                running = r.json()["running"]
                pending = r.json()["pending"]
                finished = r.json()["finished"]
                sys.stdout.write("running: " + str(running) + "\n")
                sys.stdout.write("pending: " + str(pending) + "\n")
                sys.stdout.write("finished: " + str(finished) + "\n")
                sys.exit(0)
            else:
                sys.stderr.write("HTTP Request is not 'OK' : %s\n" % api)
                sys.exit(1)
        elif opts.command == "list":
            api = "{api_prefix}/listspiders.json?project=gotcha".format(api_prefix=api_prefix)
            r = requests.get(api)
            if r.status_code == 200:
                spiders = r.json()["spiders"]
                sys.stdout.write("\n".join(spiders) + "\n")
                sys.exit(0)
            else:
                sys.stderr.write("HTTP Request is not 'OK' : %s\n" % api)
                sys.exit(1)
    else:
        optparser.print_help()
        sys.exit(1)

