# Evidence Notes — Custom-CMS
**Period:** 2026-W31 (2026-07-17 → 2026-07-23)
**Generated:** 2026-08-04
**Meetings:** 0 internal, 0 external
**Emails:** 12

---

## Email — 2026-07-17 — Data cutover details
**From:** Marcus Morrisey <marcus.morrisey@idfusion.com>
**To:** Gabrielle Mahé-Serle; Varun Mehra
**CC:** Rob Piché

Good afternoon,

I know Varun is away currently, but could I ask Gagbrielle and Varun to review the attached 2-page plan that outlines some critical dates for data migration on Monday please. Let me know when you've had that chance.

https://idfusion.egnyte.com/dl/JgFBRkq6QPxc

I want to emphasize that this is entirely a starting point based on Ross' desire to know more about the time period and activities for cutover.

I have based this on some readings of best practice online and a brief chat with Gabrielle. I have never planned or participated in a data migration like this, so I am relying on your experience to ensure this is of appropriate scale, rigour, the whole 9-yards.

If it doesn't align with your understanding of how we'll get this done, let's correct it.

Thanks!

Marcus Morrisey
Systems Analyst
1-204-880-9795
IDFusion.com

---

## Email — 2026-07-17 — Data migration / Go live dates and other information discussed
**From:** Marcus Morrisey <marcus.morrisey@idfusion.com>
**To:** Ross Gillingham

Ross,

One of those afternoons. Wanted to touch base to let you know that Varun was away today. I obviously want to ensure I've it all aligns with his planning so, I've sent the plan and schedule around those data migration / go live dates for him to review Monday. Also scheduled an internal meeting to get the ball rolling on the AMS discussion and video training questions but couldn't coral them before the weekend.

Have a great weekend,

---

## Email — 2026-07-17 — PCFS discussion topics from Ross
**From:** Marcus Morrisey <marcus.morrisey@idfusion.com>
**To:** Gabrielle Mahé-Serle; Rob Piché

Wanted to bring you into the loop on some topics Ross raised this week (or addressed again). Might be worth a quick meeting to discuss

Screen-by-screen training videos

This is not currently in scope. The SOW includes standard training, but not comprehensive screen-by-screen training videos. Ross considers this critical — confirmed via a separate conversation with Clemene — for reducing support-call volume and enabling on-demand onboarding and refresher training.

* Feasibility and effort of screen-by-screen training videos beyond standard AMS training?
* Ross flagged that training videos are a snapshot in time — as Waabanong 2.0 changes are scoped, documentation/videos should be planned to update alongside those changes, so not treated as a one-time deliverable.
* Seems like it will be cost prohibitive, maybe we can pitch an alternate idea?

AMS

Which dovetails into AMS, which Ross also wants to move the discussion forward on. We sent over some standard options with the proposal. If it includes maintaining videos those would be significantly under rate.

Events / Protection Services

Ross was asking about events, I said we explicitly excluded those with Hailey and have no plans or capacity in Phase 1 to include that. It's clearly something that has been prioritized for him. We ended with he was going to circle back with his team to better understand their needs and we would respond to that with the understanding that would be a Phase 2 priority.

* But, he wants an idea of next steps here in any case

Cheers,

---

## Email — 2026-07-20 — Re: Data migration / Go live dates and other information discussed
**From:** Ross Gillingham <ross.gillingham@peguiscfs.org>
**To:** Marcus Morrisey

Good morning Marcus,

Thank you for the update - no worries at all. I'll review a time for the UAT meeting for the case management portion with Kelvin and Christina - it's a busy week here with Peguis Treaty Days so it would be Thursday at the earliest.

Warm regards,

Ross Gillingham
Chief Information Officer
Peguis Child and Family Services
Winnipeg Office
500 Madison St
Winnipeg, MB R3H 0L4
PH: (204) 632-5404
https://www.peguiscfs.ca

From: Marcus Morrisey <marcus.morrisey@idfusion.com>
Date: Friday, July 17, 2026 at 5:01 PM
To: Ross Gillingham <ross.gillingham@peguiscfs.org>
Subject: Data migration / Go live dates and other information discussed

Ross,

One of those afternoons. Wanted to touch base to let you know that Varun was away today. I obviously want to ensure I've it all aligns with his planning so, I've sent the plan and schedule around those data migration / go live dates for him to review Monday. Also scheduled an internal meeting to get the ball rolling on the AMS discussion and video training questions but couldn't coral them before the weekend.

Have a great weekend,

---

## Email — 2026-07-21 — Re: Data cutover details
**From:** Rob Piché <rob@idfusion.com>
**To:** Marcus Morrisey; Gabrielle Mahé-Serle; Varun Mehra

Thanks Marcus,

A good idea to have this!

I would remove

* Stress test — we'll simulate many staff logging in at once, to confirm the new environment holds up under real load, about a week before go-live.,
* Access control — staff accounts are tested to confirm people see only what they're…

There would be no restoring of FamCare as we don't touch that (restore FamCare from a verified...). Two options here It's simply - we pause use of any system, fix data issues, validate. Or they use FamCare until issue is addressed and we have to redo the import (prefer to avoid this)

We won't be able to make FamCare read only as we don't have access to change the app. It will be an internal message to the team.

We need to keep FamCare accessible in case they need to lookup past items. Need this for a few months.

Question
Does Varun have access to their love data in a test environment yet? Varun: we'll have to install PHP on this environment correct as you will be wiring your scripts this way?

I think we will need to CR & use our contingency budget as their current database structure is awful.

Rob Piché
Director, Professional Services
1-204-292-0277
IDFusion.com

From: Marcus Morrisey <marcus.morrisey@idfusion.com>
Sent: Friday, 17 July 2026 13:54:13
To: Gabrielle Mahé-Serle <Gabrielle@idfusion.com>; Varun Mehra <varun@idfusion.com>
Cc: Rob Piché <rob@idfusion.com>
Subject: Data cutover details

Good afternoon,

I know Varun is away currently, but could I ask Gagbrielle and Varun to review the attached 2-page plan that outlines some critical dates for data migration on Monday please. Let me know when you've had that chance.

https://idfusion.egnyte.com/dl/JgFBRkq6QPxc

I want to emphasize that this is entirely a starting point based on Ross' desire to know more about the time period and activities for cutover.

I have based this on some readings of best practice online and a brief chat with Gabrielle. I have never planned or participated in a data migration like this, so I am relying on your experience to ensure this is of appropriate scale, rigour, the whole 9-yards.

If it doesn't align with your understanding of how we'll get this done, let's correct it.

Thanks!

---

## Email — 2026-07-22 — Fw: PCFS - CMA - Initial Touch Point
**From:** Rob Piché <rob@idfusion.com>
**To:** ross.gillingham@peguiscfs.org
**CC:** Marcus Morrisey

Good morning, Ross

I can't seem to find a signed copy of the Statement of Work for the project.

Can you please look into this?

No issues, it just to make sure we both have this for our files.

Thank you,

From: Rob Piché <rob@idfusion.com>
Date: Tuesday, October 28, 2025 at 2:46 PM
To: Clemene Hornbrook <clemene.hornbrook@peguiscfs.org>
Cc: Christine Peters <christine.peters@peguiscfs.org>, Marcus Morrisey <marcus.morrisey@idfusion.com>, Hailey Primrose <hailey.primrose@peguiscfs.org>, Christine Chartrand <christine.chartrand@peguiscfs.org>
Subject: Re: PCFS - CMA - Initial Touch Point

Good afternoon, Clemene,

Thank you and the PCFs team for awarding us the RFP.

We are looking forward to continuing our working relationship and putting in place a CMS that finally meets your needs.

Please find attached the Statement of Work for this engagement, prepared based on our discussion with Hailey. We're happy to remain flexible and can adjust our approach as we learn more about your needs.

Please let me know if you have any questions.

Thank you,

---

## Email — 2026-07-22 — Re: Data cutover details
**From:** Marcus Morrisey <marcus.morrisey@idfusion.com>
**To:** Rob Piché; Gabrielle Mahé-Serle; Varun Mehra

Rob,

Thanks for that feedback.

Agree we can drop the access control reference no worries.

The stress test was something Ross specifically requested. Not that I'm saying we have to do it, all of this was pending consultation with you folks. But whatever the decision, I just wanted to flag that. He is also willing to put his team's fingers on keyboards if that seems easier than simulating.

Right, we aren't restoring FamCare per se. But they could resume using it. Likewise, I understand we don't control writing to FamCare, but we can recommend their approach. I can update the wording to clarify.

I think the request to stop all system usage would be a bitter pill to swallow given the level dsiaster prep and back-up they do. They would have to put in place manual processes and the labour duplication would amass quickly. Perhaps we could just reframe this a bit by saying that the live transition will already be vetted by previous practice runs and in the highly unlikely event it failed, FamCare would be resumed until resolved.

Importantly, I really need your eyes on this Varun. I will send you a meeting invite this morning!

Cheers,
Marcus

From: Rob Piché <rob@idfusion.com>
Sent: July 21, 2026 06:50
To: Marcus Morrisey <marcus.morrisey@idfusion.com>; Gabrielle Mahé-Serle <Gabrielle@idfusion.com>; Varun Mehra <varun@idfusion.com>
Subject: Re: Data cutover details

Thanks Marcus,

A good idea to have this!

I would remove

* Stress test — we'll simulate many staff logging in at once, to confirm the new environment holds up under real load, about a week before go-live.,
* Access control — staff accounts are tested to confirm people see only what they're…

There would be no restoring of FamCare as we don't touch that (restore FamCare from a verified...). Two options here It's simply - we pause use of any system, fix data issues, validate. Or they use FamCare until issue is addressed and we have to redo the import (prefer to avoid this)

We won't be able to make FamCare read only as we don't have access to change the app. It will be an internal message to the team.

We need to keep FamCare accessible in case they need to lookup past items. Need this for a few months.

Question
Does Varun have access to their love data in a test environment yet? Varun: we'll have to install PHP on this environment correct as you will be wiring your scripts this way?

I think we will need to CR & use our contingency budget as their current database structure is awful.

---

## Email — 2026-07-22 — Automatic reply: Data cutover details
**From:** Gabrielle Mahé-Serle <Gabrielle@idfusion.com>
**To:** Marcus Morrisey

I am currently out of the office and will return on July 22. If your matter is urgent, please contact Rob Piché at Rob@idfusion.com. Otherwise, I will respond to your email as soon as possible upon my return.
Thank you,
Gabrielle

---

## Email — 2026-07-22 — Re: RE: Data cutover details
**From:** Marcus Morrisey <marcus.morrisey@idfusion.com>
**To:** Varun Mehra
**CC:** Rob Piché; Gabrielle Mahé-Serle

Thanks team. I updated the brief here based on our meeting: https://idfusion.egnyte.com/dl/k7PRwv8K4vxb

If you do meet Ross today, could you please share the transcript so I can integrate any decisions into the updates / planning.

Thanks,

From: Marcus Morrisey
Sent: July 22, 2026 08:39
To: Varun Mehra <varun@idfusion.com>
Cc: Rob Piché <rob@idfusion.com>; Gabrielle Mahé-Serle <Gabrielle@idfusion.com>
Subject: RE: Data cutover details
When: July 22, 2026 10:00 AM-10:30 AM.
Where: Microsoft Teams Meeting

Following up here. Need your input to see if this is reasonable Varun.

Thanks!

---

## Email — 2026-07-22 — Re: UAT for Case File
**From:** Gabrielle Mahé-Serle <Gabrielle@idfusion.com>
**To:** Ross Gillingham
**CC:** Kelvin Shergold; Christina Sutherland; Darryl Boulanger; Marcus Morrisey

Hi Team,

When you and I last spoke Ross, you mentioned that you're not able to test all the intake scenarios because some depend on the person having an open case. To help with that, we opened the case file functionality for you ahead of UAT.
I wanted to check in to see if you're available this Friday afternoon or next Monday for a walkthrough of the case management module to formally kick off UAT.

We also need to review the finance process for ongoing services, and the abuse module UAT is coming up in the queue, so I want to make sure we're keeping the ball rolling without overwhelming everyone.

Thanks,

Gabrielle Mahé-Serle
Senior Systems Analyst
431-441-7041
IDFusion.com

From: Ross Gillingham <ross.gillingham@peguiscfs.org>
Sent: July 13, 2026 10:58 AM
To: Gabrielle Mahé-Serle <Gabrielle@idfusion.com>
Cc: Kelvin Shergold <kelvin.shergold@peguiscfs.org>; Christina Sutherland <christina.sutherland@peguiscfs.org>; Darryl Boulanger <darryl.boulanger@peguiscfs.org>
Subject: Re: UAT for Case File

Hi Gabrielle,

Our testing continues with a scenario based test session tomorrow with Darryl's team. Feel free to push any environment you have - just send a message to Kelvin, Christina, and I for when we may see Waabanong be unavailable.

Depending on tomorrow's results, we should be able to start the case file UAT as early as Thursday.

Thank you,

---

## Email — 2026-07-22 — Re: UAT for Case File
**From:** Ross Gillingham <ross.gillingham@peguiscfs.org>
**To:** Gabrielle Mahé-Serle
**CC:** Kelvin Shergold; Christina Sutherland; Darryl Boulanger; Marcus Morrisey

Hi Gabrielle,

Let's plan for UAT review this Friday afternoon, it's a busy week here but I'll review with Kelvin and Christina as we also need to add additional service delivery staff to our testing pool to ensure functionality.

Kelvin is away next week so we may want to also review the SD Finance and anything abuse related this week if possible.

Let me know your thoughts.

Thank you,

From: Gabrielle Mahé-Serle <Gabrielle@idfusion.com>
Sent: Wednesday, 22 July 2026 14:31:10
To: Ross Gillingham <ross.gillingham@peguiscfs.org>
Cc: Kelvin Shergold <kelvin.shergold@peguiscfs.org>; Christina Sutherland <christina.sutherland@peguiscfs.org>; Darryl Boulanger <darryl.boulanger@peguiscfs.org>; Marcus Morrisey <marcus.morrisey@idfusion.com>
Subject: Re: UAT for Case File

Hi Team,

When you and I last spoke Ross, you mentioned that you're not able to test all the intake scenarios because some depend on the person having an open case. To help with that, we opened the case file functionality for you ahead of UAT.
I wanted to check in to see if you're available this Friday afternoon or next Monday for a walkthrough of the case management module to formally kick off UAT.

We also need to review the finance process for ongoing services, and the abuse module UAT is coming up in the queue, so I want to make sure we're keeping the ball rolling without overwhelming everyone.

Thanks,

---

## Email — 2026-07-22 — Re: UAT for Case File
**From:** Gabrielle Mahé-Serle <Gabrielle@idfusion.com>
**To:** Ross Gillingham
**CC:** Kelvin Shergold; Christina Sutherland; Marcus Morrisey

Great! I'll schedule a placeholder for the UAT walkthrough, and we can adjust/invite additional people once that's sorted out.
For the finance process for service delivery, I'm available tomorrow afternoon if that works for the 3 of you. I know the process is a little different than what we've designed for intake, so I want to make sure we're covering everything. We can probably get it done in 30 minutes.

For the Abuse Module, we're just starting our internal testing so it likely wouldn't be ready for UAT until the week of August 3rd.

From: Ross Gillingham <ross.gillingham@peguiscfs.org>
Sent: July 22, 2026 12:46 PM
To: Gabrielle Mahé-Serle <Gabrielle@idfusion.com>
Cc: Kelvin Shergold <kelvin.shergold@peguiscfs.org>; Christina Sutherland <christina.sutherland@peguiscfs.org>; Darryl Boulanger <darryl.boulanger@peguiscfs.org>; Marcus Morrisey <marcus.morrisey@idfusion.com>
Subject: Re: UAT for Case File

Hi Gabrielle,

Let's plan for UAT review this Friday afternoon, it's a busy week here but I'll review with Kelvin and Christina as we also need to add additional service delivery staff to our testing pool to ensure functionality.

Kelvin is away next week so we may want to also review the SD Finance and anything abuse related this week if possible.

Let me know your thoughts.

Thank you,

---
