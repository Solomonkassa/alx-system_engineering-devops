# 0x18. Webstack monitoring

## Description
What you should learn from this project:

* Why is monitoring needed
* What are the 2 main area of monitoring
* What are access logs for a web server (such as Nginx)
* What are error logs for a web server (such as Nginx)

---

### [0. Sign up for Datadog and install datadog-agent](./0-setup_datadog)
* For this task head to https://www.datadoghq.com/ and sign up for a free Datadog account. When signing up, you’ll have the option of selecting statistics from your current stack that Datadog can monitor for you. Once you have an account set up, follow the instructions given on the website to install the Datadog agent. 


### [1. Monitor some metrics](./2-setup_datadog)
* Among the litany of data your monitoring service can report to you are system metrics. You can use these metrics to determine statistics such as reads/writes per second, which can help your company determine if/how they should scale. Set up some monitors within the Datadog dashboard to monitor and alert you of a few. You can read about the various system metrics that you can monitor here: System Check.


---

## Author
* **David Kwan** - [dwkwan](https://github.com/dwkwan)