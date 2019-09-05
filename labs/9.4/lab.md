# Communications Plans

## SQL Injection 
### Developing an Incident Communications Plan (Activity 5.3)
 > You are the CSIRT leader for a major ecommerce website, and you are currently responding to a security incident where you believe attackers used a SQL injection attack to steal transaction records from your backend database. Currently, only the core CSIRT members are responding. 

* Develop a communication plan that describes the nature, timing, and audiences for communications to the internal and external stakeholders that you believe need to be notified.

<u>Internal</u>
* Incident commander needs to designate a Communications lead and Ops lead
* Determine the scope of the attack - were the attackers successful or not
* Describe the incident that occurred - technical aspects of the incident, what systems it affected
* What platforms you can use to discuss the incident (slack, email, etc.)
* Create collaborative document (Google docs) where everyone can leave notes on what works/doesn't work
* Time of occurence 
* Estimate for how long it will take to recover

<u>External</u>
* Have communications lead contact PR team to create email to push out to entire customer base - general and vague 

## Elections
> You are now CSIRT teams responsible for defending our US Elections against cyber attack!

Start by crafting a cyber incident scenario with regards to US Elections
* Identify the attackers, their objectives, and how they successfully conduct the attack. 
  * nation state, Russia
  * they want to influence the results of the election so it is more favorable to their country
  * attacked rivals - hacked DNC , Democratic presidential candidate emails & congressional emails
  * used cryptocurrency for payment method
  * forwarded acquired information to Wikileaks
  * sent phishing emails to gain credentials,
* What information do they change or steal? What are their attack vectors? 
  * information stolen - credentials, emails
  * vectors - phishing emails, advertising
* How do they escalate privileges, maintain persistence, and pivot within your networks? 

* Map out various actions according to the attacker killchains we've looked at in class.

> Here's one such incident: https://www.npr.org/2019/05/14/723215498/florida-governor-says-russian-hackers-breached-two-florida-counties-in-2016

Next, tell the story of the defensive response
* Who reported something wrong, or how did the detection teams first learn about the attack?
  * detection/alert happened when the emails were dumped on Wikileaks
* How did the first responder analyze and investigate the issue?
* How did the first responders escalate the issues, and who did they escalate to?
* Who is a part of the CSIRT? (roles and titles mainly, this doesn't have to be named individuals)
* How did the team communicate/coordinate?
* What are the steps that the team took to contain, eradicate, and recover from the incident?

> Finally, look at how an expert does the same!
Take a look at this template, and related materials. Compare your communications responses to their checklist. Did you think of the same things? What did you not think of?