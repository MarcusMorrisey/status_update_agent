# Evidence Notes — Custom-CMS
**Period:** 2026-W30 (2026-07-10 → 2026-07-16)
**Generated:** 2026-07-20 (ingest-evidence run manually against live sources — see CLAUDE.md note on plugin cache staleness)
**Meetings:** 0 internal, 2 external
**Emails:** 2

---

## Email — 2026-07-10 — Invoice 13544 from IDFusion Software
**From:** IDFusion Finance <finance@idfusion.com>
**To:** ross.gillingham@peguiscfs.org
**CC:** Rob Piché; Marcus Morrisey

Dear Ross,

Your most recent invoices are attached. If you have any questions or concerns, please do not hesitate to contact us.

Thank you for your business - we appreciate it very much.

Sincerely,

Alain Chamizo
Finance
ID Fusion Software
Phone: (204) 237-6147
Email: Finance@idfusion.com
401 Provencher Blvd, Winnipeg, MB R2H 0G9
IDFusion.com

---

## External Meeting — 2026-07-13
**File:** 2026-07-13_endOfProjectPlan\2026-07-13_endOfProjectPlan_transcript.docx

2026-07-13_endOfProjectPlan
Overview
The team discussed the need for comprehensive video documentation and training for the new system, emphasizing its critical importance for onboarding and reducing support calls. They considered hosting options like SharePoint and private YouTube channels. The primary focus was on the database import, including the challenge of creating a snapshot of the production database with anonymized data for testing. Varun explored tools like Data Veil for data obfuscation. Marcus and Ross agreed on the necessity of a detailed plan for the go-live, including stress testing and clear communication with staff. They also discussed application management support and the importance of a coordinated rollout.
Action Items
[ ] @Marcus Morrisey - Circle back with Rob at ID Fusion to discuss scope and feasibility of creating comprehensive screen-by-screen training videos (beyond standard AMS training) and related documentation, and then report the proposed approach back to Ross.
[ ] @Marcus Morrisey - Coordinate with the ID Fusion team to define a detailed go-live order-of-operations and timeline for the FamCare rollover (including AMS/AMS support steps and approximate durations) and send this rollout plan to Ross for use in broader planning.
[ ] @Varun Review Data Veil and Ken's recommendations for anonymizing production data, decide on an appropriate anonymization tool/approach, and finalize which data fields must be migrated from the legacy system into the new application.
[ ] @Ross. Pre-identify key test cases in the current system and, after the database import, perform side-by-side checks to confirm that all required data has imported correctly and no sensitive information remains exposed
[ ] Use the rollout plan from ID Fusion to brief the executive team on the overall timeline and, as go-live approaches, develop and communicate a staff communication cadence explaining what is happening, why, who to contact, and how it impacts them.
[ ] @Ross & Varun Schedule a pre-go-live stress test of the new environment where many users attempt to log in simultaneously, coordinating this as part of the overall go-live activities.
[ ] @Ross & Varun Hold a follow-up discussion with Ross to dive deeper into SQL-based data obfuscation and anonymization techniques relevant to the production data snapshot needed for the dev environment.
Outline
Video Documentation and Training Video Requirements
Marcus Morrisey discusses the need for video documentation for the sport, including training videos for each screen.
Ross confirms that the training component was not included in the original contract scope and suggests it is critical.
Ross mentions a conversation with Clement, indicating that the training videos should be updated for Waabanong 2.0.
Marcus and Ross agree on the importance of having on-demand training videos to reduce support calls and improve onboarding and refresher training.
Hosting and Storage of Training Videos
Marcus inquires about the hosting options for the training videos, suggesting SharePoint, a private YouTube channel, or local storage.
Ross mentions that the videos can be stored as MP4s and played locally on QuickTime Player.
Marcus plans to circle back with Rob to discuss the hosting options and other preliminary details.
Varun lists the loose ends that need to be tied together for the go-live, starting with the database import.
Database Import and Data Obfuscation
Varun discusses the challenges of importing a snapshot of the production database into the development environment.
Ross emphasizes the need for critical table information and the freedom to test without live sensitive data.
Varun mentions exploring tools like Data Veil for data obfuscation and anonymization.
Marcus and Ross discuss the need for manual spot checks and the involvement of Ross's team for privacy concerns.
Security and Access to Live Production Data
Ross highlights the importance of balancing security in the test environment with the need for Varun to test the data migration.
Marcus suggests using an on-server tool to anonymize the production data and delete the original copy.
Ross and Marcus discuss the potential use of Data Veil and other tools for data anonymization.
Marcus commits to circling back with Rob to discuss the training video enhancement and the application management support (AMS).
Planning and Communication for Go-Live
Ross tasks Marcus with discussing the order of operations and timelines with ID Fusion's team.
Marcus agrees to provide a detailed plan for the go-live, including the steps and their approximate timeframes.
Ross emphasizes the importance of clear communication with staff and the executive team to manage expectations and reduce nervousness.
Varun and Ross discuss the rollover plan for FamCare and the need for a stress test before the go-live.
Final Recap and Next Steps
Marcus recaps the key points discussed, including the video documentation, database import, and application management support.
Marcus plans to follow up with Rob and Varun to provide more detailed information and a timeline for the go-live.
Ross and Varun discuss the need for a stress test and the involvement of the entire team for the go-live.
Marcus commits to providing the updated plan within the next couple of days.
Transcript

2026-07-13_endOfProjectPlan
Mon, Jul 13, 2026 2:30PM • 19:12
SUMMARY KEYWORDS
video documentation, training video, database import, data anonymization, production database, onboarding, support calls, SharePoint repository, QuickTime Player, data obfuscation, stress test, application management support, go-live plan, communication cadence, FamCare rollout
SPEAKERS
Marcus Morrisey, Ross, Speaker 1

Marcus Morrisey  00:00
Yeah, honestly, one thing we do I actually wanted to flag to that you know we've been putting things on the roadmap, and one of them that was in the back of my mind that we need to connect on is yeah the because the level of sort of video documentation for the the sport because there was, and I know interest expressed on your end in having it, you know, sort of like a training video for each screen, and just want to confirm, you know, sort of talk about what the expectation is there. That's a bit more than we just sort of do by default, but you know, I'm not anything's possible. Just gotta, you know, figure that out. So that that's a conversation we'll have to sit down and have, with probably have to get Rob in on that. So that's just one thing.

Ross  00:53
Yep. Because I don't think that was captured as part of the original contract scope, was it?

Marcus Morrisey  01:01
There there was training. There is training included in the original contract scope, but I think it's just not as comprehensive, maybe as what you're looking for. So we can talk about you know how important it is, or you know what priority, you know

Ross  01:17
critical.

Marcus Morrisey  01:17
Yeah, yeah, that's what I figured. So, so yeah, and I and

Ross  01:22
I and I and I say that I say that with with confidence based on conversation with Clement. So having having for 1.0 we know that's going to change, right? We know that those videos are a snapshot in time of the system. So what we want then, and what we should keep in mind when scoping Wabadon 2.0 and things like that is that our documentation should include those training video changes, because the idea is that we can do it well. We can do it up front, and then we can get staff to ensure that they watch those and make them make them on demand as opposed to scheduling or things like that, and then that helps a lot with our onboardings or a lot with refreshers.

Marcus Morrisey  02:15
Right, for sure, absolutely.

Ross  02:18
Also, we'll reduce support calls to ID Fusion,

Marcus Morrisey  02:21
for sure. I think it's fundamentally a good idea. So yeah, and since we're talking about it now, anyway, is this something that you think that you would be hosting on your servers, like these, like where they might live at the end of the day, these videos?

Ross  02:39
Probably SharePoint if they're gonna be like MP4s or something like that. We can throw them in a repository, or we can throw them on a private YouTube channel. Worst case, something like that.

Marcus Morrisey  02:50
Yeah, for sure. Those are all like,

Ross  02:54
yeah, I think more so just as they come out as like an MP4 that can even get played locally on QuickTime Player on Mac, so

Marcus Morrisey  03:05
right. So yeah, well then I can circle back with Rob too and just give some of that preliminary. Let's go through the list of things that you were thinking about, Varun. Right, it all came at me quickly.

Speaker 1  03:21
Yeah, so sort of the stuff that I'm thinking about is just all the little loose ends we need to tie together for go live, I guess. So, the biggest one, obviously, that we're working on is the database import,

Marcus Morrisey  03:36
for sure.

Speaker 1  03:37
So that's a whole other discussion. Yeah, in its own thing,

Marcus Morrisey  03:44
Rocky. But how's it going in terms of that? It

Speaker 1  03:50
it's going like I guess we sort of know what the landscape of things are. We just have to try to now figure out. I think the biggest hurdle now is how are we going to get production a snapshot of the production database into our dev environment, and sort of scrub the data so that we have data, but fake data, but linked together data, hiding all the hiding all the important stuff that we shouldn't be seeing, I guess.

Ross  04:24
Yeah, that's the that's the challenge. I obviously we want you to have the critical the critical table information of of what kind of data goes here. Where is this record? You know, when we put you know Ross, where where does Ross in the table go? Like which table and and which field? But and I want you guys to have the I want Varun to have the freedom of absolutely going hog wild in there without any concern. That we've got someone perusing a ton of live sensitive data. Right. Yeah.

Speaker 1  05:08
Okay. So I've been looking at tools since you and I last chatted on Friday.

Ross  05:13
Yeah.

Speaker 1  05:14
But I also wanted to talk to Ken, so I've sent feeler out to him. He hasn't got back to me yet, just to see what lives in his brain in terms of doing the same thing, because he had mentioned that he's done some of that before. The way that I've done it is always in software. Like I would just write a script that would go and go through each, I guess, line in the table and overwrite them with something else. But I'm sure there's a better way to do it. I did find a piece of software called. Give me one sec. Data veil. That might work potentially, but just as just as I was about to go through it, I had to jump on some other calls, so I've left that for the time being. But I'm gonna jump back in to see that's usable or not. And then, yeah, like on my end, we just gotta sort of hammer down exactly all of the different pieces of data that we want coming in from the old old app to the new app, just to make sure that we check off all the boxes. So my, I guess my biggest concern for go live is making sure we have all the data we need brought in.

Marcus Morrisey  06:47
Yeah, obviously there are going to be mechanistic code-based checks on this, but we're probably going to need to also do some, you know, eyes on screen, sort of spot checking.

Ross  07:03
Yeah, 100%

Marcus Morrisey  07:05
So yeah, that's something. And I, I guess yeah, we might have to rely just for privacy. You know, let your team do that, Ross. You know, so if we can like support or, but you know, other than Varun, we don't want to be.

Ross  07:25
Yeah. So I think what it would come down to is we would just we internally would just pre-identify the cases, and we'd have to a side by side, and just be like, did did everything come over? Does everything look right? And if it didn't, then we can flag the data and the user, and we're not we're not going to be able to get around, and I want you to get. I'm. I'm realistic about this. We're not going to be able to get around your guys's access to to live production data, and that's not what I'm trying

Marcus Morrisey  07:50
to

Ross  07:51
be a pain in the rump with. What What I'm trying to make sure is that we strike this balance for for security in our test dev, with being able to get Verun to be able to just figure out what migration looks like, we're going to have to have access to the live production data at some point, or you know the latest copy of of live production data to facilitate a data import. Like that's going to have to happen, which means access to the to live sensitive things. So if if it comes down to and yeah, everyone, absolutely, please see what Ken says or what Ken's suggestions are here. Marcus, you had mentioned you had you'd used a tool previously, maybe as well.

Marcus Morrisey  08:42
Yeah, there's a package for this in R. I don't know if that's something that you know can go on the server or you know whatever. But

Ross  08:52
second, the one I had looked at. Oh my goodness.

Marcus Morrisey  09:13
As I recall, the the package was actually called Anon.

Ross  09:25
Yeah. No. Totally. Totally fair.

Marcus Morrisey  09:28
I don't know how that works with the SQL database. Probably not great.

Ross  09:42
Sorry. Yeah, this is anyway. That's that's kind of where we are. I think that there is going to be an on server tool that we can use, and that we can just ideally attach the production a copy of production to the tool. Have it anonymize it, delete the production copy, and then rock and roll with an anonymized version of

Marcus Morrisey  10:13
data. I mean, I know versions of that are out there. That that's sort of what that non package does.

Ross  10:18
Yeah,

Marcus Morrisey  10:19
in a way, maybe data available. will help us in that same way, but yeah, the video thing actually, I think I should make a commitment to circle back on that right away because as we were just finishing up some modules, so that's the perfect time to do the documentation and training materials. Yep. While we still have the feedback fresh in mind, and yeah, we'll have to figure out exactly what that looks like. Okay. So, other things we want to put on this list.

Ross  11:00
I think we just also want to, and if I could task you with even more, Marcus, talking with the team there and just kind of looking at our order of operations, what what what based on ID Fusion's experience with rolling out things like this, what steps do we need to be thinking about, and what time do those steps approximately take? Because that way, what we can start doing is is we can start looking at kind of the I don't know let's just because I don't know we've got these eight steps and these eight steps take this time so this is what we need to be planning for and thinking of

Marcus Morrisey  11:35
right yeah so just giving you a little bit more detail on what that sort of end part looks like

Ross  11:42
I think so because then we can we can we can build like iterative, right? So we can build on that, and as we come back and talk about it, we can be like, yes, we're moving towards this. Oh, don't forget now we need this, or okay, we've as Varun and I were talking too, you know, otherwise what ends up happening is we're going to very quickly just caught unaware with. All right, we're ready to go. What do we do? And what did we miss?

Marcus Morrisey  12:05
For sure, for sure. Yeah, absolutely. So yeah, I will circle back with the team too, just to make sure I don't miss any details in in making such a plan. But yeah, we can commit to getting that back to you so that you can get your more detailed planning, and you know, in part, where there'll be a dialog as well.

Ross  12:25
Yeah, yeah, yeah, exactly. It's it's also to let you know, I can let the rest of executive kind of know what that timeline looks like, and then as we get closer, we can start letting staff know, like, hey, this is this is what this looks like because we're going to we're going to be. I want us all to be very communications focused with our staff as we get a lot closer, or as we as we get closer, and that'll even probably be like planned communication cadence of we're going to have an update on these days, and this is what the update is going to entail. The reason for that is again just with our experience with FamCare rollout things like that. I want I want people I want people to know what's going on, where it's happening, why it's happening, who do they contact with questions, you know, and how and how does this impact them? So those are the those are the big ones that I want to help people feel excited and not nervous about. And a big one of that is then making sure that agency side is on the same page with ID Fusion, so we're all lockstep with with what's happening.

Speaker 1  13:35
That rollover plan too, right? Like when, how does that happen at the end? End of life for FabCare, and then moving on.

Ross  13:42
Yep. Yep. Yeah, because there's going to be a portion where we're like, all right, cool. Famcare is going read only. Famcare is going only accessible to these people. Then yeah. There's that whole portion as well. I know I'd also spoken with Rob about starting to talk about application management support.

Marcus Morrisey  14:01
Yes, that is the going

Ross  14:02
forward. Yep. So he talked. You guys already have like tiers and things like that. So

Marcus Morrisey  14:10
yeah, we do have some sort of you know recommended ones, but you know we can also customize you know based on your needs.

Ross  14:18
Yep. So I'll get Varuna desk, and Varun will hang out in my office with me for the first. It's not a bad. They've never

Speaker 1  14:29
let you leave at this point. Hey, there's a reason

Ross  14:32
why you always see my background is the same. I'm just kidding. No, it's good. You you can't get you can't get me to leave at this point. You have to drag me out.

Marcus Morrisey  14:42
Yeah, but no.

Ross  14:42
no,

Marcus Morrisey  14:43
yeah, no, and this took some of them. You know, we have alluded to, and yeah, but some of them we just need to put more detail into now. So

Ross  14:52
yeah, and that's just why I wanted the the three of us to meet was to just be like, hey, we kind of talked about this on the on the edges of things, but. It's going to be here before we know it.

Marcus Morrisey  15:03
No, 100% And so, what I'll say then, just to sort of do a quick sort of recap, and I apologize, I actually do have to jump off a bit early because I have a call after this.

Ross  15:14
No sweat.

Marcus Morrisey  15:15
I'll leave with you two to sort of sort out the whether it's datavail or whatever the tool is going to be, and just sort of keep me in the loop about what's going to be possible for that sort of data transition piece. I will circle back with Rob on the the AMS, and also I mean the help generally, and I'll I'll say like the thing that we put into the agreement is you know we would sort of train your team you know and then there would be like a train the trainers sort of thing, but

Ross  15:50
train the trainer approach okay yeah

Marcus Morrisey  15:52
so that's like the minimum for sure that's going to happen but you know maybe I know there was desire for a dialog about you know this enhanced video thing, so I will bring that back to the top of Rob's mind, and so that we can address it directly. Talk about the AMS a bit, and then just give you a bit of a more detailed layout of what the end looks like. Now, because that end is to some extent dependent on you know how the the transition goes with data and that kind of stuff. I you know I may not be able to at this moment say well this will be exactly June definitely won't be true no on like August 4 you know what I mean but we can say it'll be as of day minus yeah relative to yes kind of thing you know

Ross  16:41
yes and that's what I'm looking for right now because I've got a, you know, if you think of it like one package, that's a little bit movable on the calendar. Yeah, that's totally fine. I just want us to be aware of all those moving pieces and of like, hey, this is this is what it looks like. Yeah. Wherever that starts, wherever we start the process, that's what it looks like.

Marcus Morrisey  17:02
Yeah, and this is a question for you, Vroom, but I don't know. Like for this kind of like thing, do usually we would probably want campfire like around lunchtime, sort of on deck as well, or at least aware of what's going on.

Speaker 1  17:14
Yeah, absolutely. Because if there's any environment issues or domain issues or anything like that, campfire can got to make sure everyone's sort of around.

Marcus Morrisey  17:24
Yeah,

Ross  17:26
yeah. We'll have we'll have our nanny ready on standby for things like that. The thing is, from the domain side and all of that, we can get that stood up well in advance of cut over, and we can ensure that that it works.

Marcus Morrisey  17:42
Okay.

Ross  17:44
Like part of this, Varun could also we could also do a stress test pre, like pre go live. We could have everyone try to log into it, and you know if you're gonna you're gonna clear out the data on it anyway, or we put in redo. It's not we can figure that out. But if we want to do a stress test,

Speaker 1  18:02
probably. probably doesn't hurt.

Ross  18:04
I would say it does not hurt at all. In fact, let's do a stress test, guys. Let's let's let's schedule as part of as part of the go live to do a stress test.

Marcus Morrisey  18:15
Okay. All right. So yeah, I'm gonna take all those back, and it won't keep you waiting too long. But it won't be today. But in the next couple days, yeah, no worries.

Ross  18:30
Sounds good.

Marcus Morrisey  18:31
Yeah,

Ross  18:32
Varun, do you still have time?

Speaker 1  18:34
Yeah, I got a little bit of time.

Ross  18:36
Then maybe Varun, you and I will just pivot into talking a little bit more about data obfuscation and anonymization when SQL.

Marcus Morrisey  18:43
Sure. Perfect.

Ross  18:45
All right. Thanks, Marcus. I appreciate you.

Marcus Morrisey  18:46
Thank you for setting us up. And yeah, on the ball. See you later,

Ross  18:52
guys. I'm like that seal in the circus, and just not just not nearly as graceful. Right.

Marcus Morrisey  19:00
Well, we're impressed.

Ross  19:02
Oh, thank you, thank you, appreciate it. We'll see you guys later, Varun.

---

## Email — 2026-07-13 — FW: Invoice 13544 from IDFusion Software
**From:** Ross Gillingham <ross.gillingham@peguiscfs.org>
**To:** Peguis CFS Finance
**CC:** Marcus Morrisey; Rob Piché

Good morning Finance Team,

Please process the attached approved invoice. As always, please let me know if you have any questions.

Warm regards,
Ross Gillingham

> From: IDFusion Finance <finance@idfusion.com> — Sent: Friday, July 10, 2026 at 3:51 PM
> Subject: Invoice 13544 from IDFusion Software
> Dear Ross, Your most recent invoices are attached. If you have any questions or concerns, please do not hesitate to contact us. Thank you for your business - we appreciate it very much. Sincerely, Alain Chamizo, Finance, ID Fusion Software

---

## External Meeting — 2026-07-15
**File:** 2026-07-15_events\2026-07-15_events_transcript.docx

2026-07-15_events
Overview
Marcus Morrisey and Ross discussed the status of event management under category E, noting it was not prioritized for phase one. Ross highlighted the need to streamline data duplication and improve service referrals, including tracking for events like the annual women's gathering and community services. They addressed the capacity constraints of the current team and the potential need for additional development costs. Ross plans to gather detailed requirements in an upcoming meeting with Michelle Wilson and Natasha Tisone. Marcus will provide further information and coordinate with higher-ups to ensure clear communication and realistic timelines for future development.
Action Items
[ ] @Marcus Morrisey - Send additional context on the switch-over, AMS support agreement, and next-priority planning so the team can review roadmap implications.
[ ] @Marcus Morrisey - Check with Gabrielle to confirm whether any service-referral functionality has already been developed and what is planned for it.
[ ] Meet internally with Michelle Wilson and Natasha Tisone to gather event and reporting requirements before rescheduling with the vendor team.
Outline
Discussion on Technical Issues and Meeting Preparation
Marcus Morrisey and Ross discuss technical issues with Marcus's camera and computer performance.
Marcus mentions updating Ross on additional information and aligning with Brune on the final transition plan.
Ross apologizes for not responding to Marcus's email due to a medical appointment and a fire in Marcus's building.
They discuss the impact of the fire, including smoke damage and potential insurance issues.
Introduction to Event Management and Prioritization
Ross introduces the main topic of the meeting: event management under category E.
Marcus explains the prioritization exercise with Haley, where event management was not considered high priority for phase one.
Ross mentions a call received the previous day about starting discussions on event management.
Marcus offers to link the requirements document for event management.
Discussion on Duplicating Work and Data Management
Ross highlights the issue of duplicating work and data during the registration process.
They discuss the ease of data management and the importance of statistics for events.
Ross introduces the concept of service referrals, such as Rainbow Lodge and Sun Lodge referrals, and their integration with case management.
Marcus refers to the functional requirement section three, specifically 3.1, and the critical features agreed upon with Haley.
Challenges with Current Capacity and Long-term Planning
Marcus informs Ross that the current team does not have capacity to handle additional development work.
Ross mentions the upcoming launch of the community circle of care in September and its similarities to event management.
They discuss the need for long-term planning and strategic thinking to accommodate future requirements.
Ross suggests that some referral forms might need to be integrated into the system for version one.
Automating Stats Collection and Reporting
Ross explains the need to automate stats collection for events and services.
They discuss the importance of tracking participant information and generating reports.
Marcus mentions the possibility of using case notes for tracking referrals.
Ross highlights the need for quarterly and monthly reporting to track program participation and costs.
Planning for Future Development and Capacity Management
Ross emphasizes the importance of starting planning for community circle of care and events.
Marcus agrees to provide additional context and information about the switchover and support agreement.
They discuss the need to balance current development capacity with future requirements.
Ross mentions scheduling a meeting with Michelle Wilson and Natasha Tisone to gather more details on reporting requirements.
Finalizing Meeting Details and Next Steps
Ross confirms the meeting date for the following Tuesday to discuss reporting requirements with Michelle and Natasha.
Marcus agrees to send more information and involve higher-ups for better coordination.
They both express the importance of open dialog and clear communication to ensure smooth development and implementation.
Ross plans to hold off on sending invites until after the internal meeting to gather detailed requirements.

Transcript
Fri, Jul 17, 2026 11:08AM • 32:07
SUMMARY KEYWORDS
event management, service referrals, requirements document, capacity issues, community circle of care, data duplication, financial tracking, participant registration, reporting requirements, prioritization exercise, development timeline, case management, program tracking, operationalization, meeting scheduling
SPEAKERS
Marcus Morrisey, Ross

Marcus Morrisey  00:40
Good morning, Marcus. How are you doing? I'm very well, thank you.

Ross  00:57
Excellent.

Marcus Morrisey  00:59
A little bit mystified by my camera, so sorry about that.

Ross  01:06
Come on, I'm just kidding. It's all good. Almost, almost got you.

Marcus Morrisey  01:13
Okay.

Ross  01:19
Don't worry, I've got time for some troubleshooting here, I'm just pulling up your email.

Marcus Morrisey  01:25
I'll just actually update you to. I know we talked about me sending you some additional information. I wanted to circle back with my team on that meeting, which I got to do yesterday. So yeah, that planning around the sort of final transition. So just wanted to let you know that's on the go. I just yeah wanted to make sure I was in alignment with what Brune was thinking and all that kind of stuff before before laying out the plan.

Ross  01:54
Perfect. Sounds good. Um, sorry. One second.

Marcus Morrisey  02:39
The first time I said that, can't turn on your camera. Your computer's pretty busy. Try closing some apps. It's this.

Ross  02:46
Your computer's pretty pretty busy. I believe that you got a RAM issue, sir. I love that. No, that's great. I mean, they're they're making a lot of their error messages less technical, which does not help me. Right. Almost.

Marcus Morrisey  03:40
Yeah. Okay.

Ross  04:00
Monthly. Yep. yep. Sorry, I'm just reading through this agreement real quick. Thank you for sending that over. I apologize for not getting to this yesterday. I had I was out in the afternoon with a medical appointment, so I also

Marcus Morrisey  04:53
delayed a bit. There was actually a fire in my building.

Ross  04:57
Oh my goodness, are you all right?

Marcus Morrisey  04:59
Everyone's okay. But like our our fire escape right outside our back door burned and like window blew in, so it's a bit of disarray. Everything smells like

Ross  05:11
smoke. Oh goodness! Do you have? Hopefully you've got some renter's insurance or something. Worst case.

Marcus Morrisey  05:15
Sort of. Is

Ross  05:20
that smoke? That smoke damage is insidious.

Marcus Morrisey  05:22
Exactly. So we'll see. Sort of clears out a bit, or we have to play some things.

Ross  05:41
Okay. So. today we are really talking about on this agreement here. I believe really part of it's going to be category E, the event management. That's the big one, and then we're probably going to talk about how that's going to so many critical things. Yeah. Yep. Okay. Yeah, you already have the. I like the event management piece, which is. So that's what we're talking about today. I got a I got a call yesterday. I received I received a phone call yesterday asking if we were ready to start talking about that. I was like, well, I will meet with our team internally here. So yeah, it looks like it's captured under. category E for event management. So, let's talk about how we can where where that fits into our iterative testing and what information you need from us.

Marcus Morrisey  07:32
Okay, yeah, gotcha. So, yeah, that part was not. We basically haven't planned to build that in this time frame,

Ross  07:43
okay.

Marcus Morrisey  07:43
So, and that was part of the sort of prioritization exercise that we went through with Haley, saying like, so what are you know, what do you want to see first? What's important? What's not? Which sort of documented in that the requirements document that our shared drive, and we sort of went through that. Priority, this one event, they said no, it's not high priority. We're not. We're not going to put it in phase one at that time. There's always a dialog, but I'm just letting you know sort of where we landed on that.

Ross  08:19
For sure,

Marcus Morrisey  08:20
I can link that document for you if you like. Yeah,

Ross  08:26
let me just. I think I've got our. Is that agency? Is that under our execution?

Marcus Morrisey  08:34
Yeah, under execution, and then it would be documented. I believe requirements document. Myself to it as I say this, and I can tell you the sort of section where we save that as well. It's been a while since I visited here myself.

Ross  09:25
Yeah, no worries. I'm just waiting for my access code here. The reason this came up is because we've identified that during our registration process and things like that, we are just duplicating a ton of work, and we're duplicating data and holding data and PII in places that we shouldn't. And not only well, that's from my perspective. And then, and then, really, it's the the ease for for that and for statistics because this is all then all these events, and it's not just events. I guess the other question then is that I would like talk about today is because events is one thing, but the other is like service referrals. So, because these are really kind of like services, so like Rainbow Lodge or or Sun Lodge referrals,

Marcus Morrisey  10:27
okay.

Ross  10:28
Because that happens in case management and things like that, to where we're saying like, hey, you've been referred for for these services. We want to register for these services. How is how is that being captured, or how has that been captured?

Marcus Morrisey  10:41
Yes, I can talk to a little bit about that. Well, so the the thing I'm referring to is functional requirement section three, and then 3.1 Really, there's essentially a table that we went through. Okay, you know, based on all the features there, and essentially the critical things are what we agreed we would build with Haley. Okay, event management. Yeah, so I'll say you know it's always been the plan to to work with you folks long term. So we're I don't want this to be a conversation of no, but like what I've been told by our team is like we definitely don't have capacity within this schedule to do anything more. So you know sure it's a sort of how do we strategize around that sort of question, and yeah, I think maybe this is related to the I don't know if you're familiar with the community circle of care, which is maybe an older initiative. Yes, but it sounds like a similar thing where they wanted to potentially. Well, and

Ross  11:59
it's that's launching September, so

Marcus Morrisey  12:03
and is that that's similar? Yeah, where you have partner organizations and you're trying to do some tracking of of shared resources, or

Ross  12:12
that is that is similar. So it's a a little bit different. So this the the first one we're talking about with events and services; those are all internal things that we put on. So, for instance, let's just say that's our annual women's gathering. We want to be able to basically, and this is just high level, of course. The way I see it is, we'd be in the events tab or whatever we call this. New event, women's gathering, 2026 Yeah, and then once we've got that event created, now we can add people that have registered, and because their information is on their person record, that's how we verify that they're eligible. We'll be able to generate reports on that, and then we'll be able to also track costs for that event directly in Wabanong, so that any any receipts, invoices, or things would go to Wabanong, so that we can do a financial report at at the end as well to see like, well, we had you know it cost $1,000 and we had 1000 participants, so it cost $1 per per participant to

Marcus Morrisey  13:19
make sense, and I I did see that some of those things are. Yeah. Yeah. So.

Ross  13:33
So, the community circle of care then is where we've got Peggott Child and Family Services, and then we have other First Nation departments, or even like Red Cross, other organizations outside of the agency that we're able to collect some information from to be like, hey, you know, on january 1 we provided furniture to Ross. Okay, great. So then if Ross calls, we we know that or or submits a request for things that we know that well he already got you know a washer dryer so he doesn't need a another washer dryer or you know maybe we can see that something else is going and maybe we need to dig a little more and find a referral to other services or or provide some different types of services so yeah dialog absolutely. I tentatively like like full full disclosure here, Marcus. To like, I talked to Clement about this, and I said, okay. I said I've got to review the contract and see if this was captured in scope. I said this might, you know, be additional development cost to to do these, and so I think just I do see it's in the contract, and I do apologize. Like I should probably have done a better job getting up to speed on all of this, so. Those are going to be the two big things. There's going to be, and when I say events as well, it's part of like the services referral. So I guess events aside, referrals to service are a critical part of like ongoing services, like ongoing support. Do we do we know what we have, or do we have anything planned for that right now? Like when we talk about like Rainbow Lodge referrals or tracking things like that.

Marcus Morrisey  15:36
I don't believe we. I'd have to check in with Gabrielle to see if anything has developed there, but to my knowledge, we haven't really talked about that in any formal way. Yeah, we have to understand what works in your workflow and what that means exactly.

Ross  15:55
For sure. So I'm going to invite you to a meeting then for next. next Tuesday, just to start your data collection on it. Give me one moment here. Let me just find all this. For instance, the Devon and team will have their own events. So, for instance, we've got like land-based program, recreation program, education, community engagement, life skills. Same thing with field trips, and then we track participants. Same thing with Roe. So we've got like the reclaiming our ways has like the RCITT program, Sacred Rhythm activity programming, childminding, spring break extravaganza, the youth gathering, the Mother's Day event, Red River X tickets, like all these things. And then on top of that, we also track our. Where did that go? Yeah. Anyway, there's just a there's a lot on this piece. It's the the the nice the nice thing is we're we're building a lot of the pieces already, or you're building a lot of the pieces already. Financial tracking, budget track like okay so do do the thing here it's more complicated than that I'm not saying it's not don't get me wrong but that was

Marcus Morrisey  17:51
always the goal was to build a core system that's going to be extensible you know when we when we need to do that so yeah for sure.

Ross  18:03
Okay, so I think then the question comes down to with events and community circle of care, which are what I'm hearing is that the team at the current cadence doesn't have capacity for that addition, which I hear you. So then the question that I have is, what does that look like for, or what does that potentially look like for implementation after, and what and what timelines would we might be able to look at there because we're going to start all this, and I'm going to just have to temper expectation to be like cool. The roadmap, though, is that these is this the core functionality that's launching, and then we will have CCC and events.

Marcus Morrisey  19:04
Yeah, and exactly that's that's how we want to prioritize it for sure. And we'll just you know to sort of give you a good answer. We'll have to go back and look at our own resourcing and you know just trying to be realistic.

Ross  19:19
Yep.

Marcus Morrisey  19:21
Yeah.

Ross  19:23
Yep, for sure. The other thing is that, as far as referrals, this might be something that we need to try to fit in the referrals. My understanding is right now we have pre-made forms that we use for the referral. We might need to just have a version of a couple of our referral forms in Wabanon, and then they get filled out and can get sent and just track that this was. Like this, this request was made. That might be that might be acceptable for if we can fit it into version one.

Marcus Morrisey  20:11
Yeah, and those would typically be done as a case note, or do you know that? Fine if you don't know that detail.

Ross  20:20
I don't know that offhand, but give me a moment. Let me just let me just jump into. Oh, I'm already there. So if I go to my

Marcus Morrisey  20:40
and you had mentioned reporting. Is this something that you know, end of year, you would want to have the ability to say something like, you know, we made X referrals to these services, or

Ross  20:52
yeah, this number of this number of people did services. Right now, we track like elder services referral. It looks like it's a form that is completed,

Marcus Morrisey  21:08
or like a case.

Ross  21:15
Yeah. Yeah, I believe so, and we can get confirmation on that. I'll talk with Regan, Regan about that for.

Marcus Morrisey  21:23
Don't think we have that form.

Ross  21:29
No, you wouldn't. I don't believe because this is a fan care form, at least for this one. So a couple of others would be. Sorry, just brain thinking. Workflow-wise as well, it might be one of the case note document attached.

Marcus Morrisey  22:00
I mean that's, I mean the nice thing about that is that's implemented right now. If there's additional sort of like tracking, maybe that could be something we could look at too. Like with, it's like a, because if it's a specific form, then you know that's something we could count. Like the referral form, I mean, right, on the back end.

Ross  22:22
Yeah. Well, and that's what it is. Is a lot of this is just about automating our stats collection, because the stats. I I'm not going to share these just because I do have some PII on them right now. But for instance, it's not a like it's not a ton. It's a lot of what we're gathering for even like for the registration for these things. It would all exist in their person card, so first name, last name, phone number, you know, band member status, and because a lot of things are, you know, or a note, you know, things like that. The stats, if I look at our stats, it's things like you know, female participants between the ages of seven to 12, you know, or 13 to 17. Same thing with male participants. If parents participated. participated, all all stuff that dates of birth and things exist on

Marcus Morrisey  23:27
person record. So

Ross  23:31
yeah, it's just a database query at that point to to get stats, and then really looks like it's by month number of participants per program. program, and then there's quarterly as well.

Marcus Morrisey  23:53
A

Ross  23:55
core just quarterly reporting as well for you know in this quarter we had

Marcus Morrisey  24:00
this money. mentioned build a query. It's very easy to filter by by date. So yeah, quarterly, monthly, sort of same level of effort to do all that usually.

Ross  24:11
Yeah.

Marcus Morrisey  24:16
But yeah, okay. So that's that's good context. Yeah. Like hey, even if we wanted to, we probably we we won't be able to build it in a timely way. But yeah, that's a high priority thing for you. We can put some thought into planning the next step for that.

Ross  24:34
I think it's going to. I think it's going to be. I think it's going to have to be because a lot of what we're seeing as we operationalize is that we're doing more and more of these kind of unique programs or unique events. So even even building even building this out, like when you create an event, to be able to say. Like, are there a limited number of, you know, limited number of slots or things like that? Even just to track how track sign up things like that, and we can we can review all those requirements as well. But I just wanted to really get the ball rolling here because because I got that call yesterday, and I was just like, okay, I said I'll talk to the developer about this, and we'll start talking about it.

Marcus Morrisey  25:21
Yeah, that's fair. Okay, so I think then it's probably really it's all roadmap stuff, right? We're just trying to chart our course forward, so I can probably just put that together with that sort of additional context I'm going to send you about you know how we're doing the switch over that kind of thing, and then AMS the sort of you know support agreement, and then also talk about okay so if we want to move on to as a next priority what what what has to happen there was and yeah we we did talk to some, you know, so we're not unaware of the events that go on, and you know, the different organizations or sort of departments rather that that host them. But yeah, it was it's another piece for sure, and yeah, we would just have to plan around that.

Ross  26:24
Yeah, I'm still going to get you on this Tuesday meeting for information purposes, and this is really just going to be talking with Michelle Wilson, who is our claiming our ways coordinator for Main Office, and Natasha Tisone, who is our claiming our ways coordinator for Winnipeg. I don't know their title. That's horrible. I know Natasha very well. Exactly. Yeah, she's the reclaiming her ways coordinator for for Winnipeg. Sorry, apologies.

Marcus Morrisey  27:47
Looks like you got some deep thoughts going on.

Ross  27:51
There were some deep thoughts there, buddy. Yeah, once we once we know more on Tuesday as well. Obviously, we don't want to delay development, and there's a capacity issue. So those are our big issues with this. Honestly, it's just going to be.

Marcus Morrisey  28:22
We definitely don't want to derail getting you your product, at least to start. You know, could be a primary concern on our end. Actually, it's not. We always expected this to be a journey. We knew that things were going to develop and expand, so we're definitely happy to plan around that. Just want to be cautious about saying, "Yeah, we can do it all, and then we end up doing nothing, and then that's even worse.

Ross  28:56
Yeah. Yeah. Okay, I think that's kind of covers. Do you have any questions or anything that he's clarified at this point?

Marcus Morrisey  29:07
I think that's clear, and yeah, I will try and get some information back to you right away because I'm sure you have questions from people on your end. Yeah, get more people involved, or get our our higher ups talking to each other. We can do that for sure, and yeah, just make sure it's all really the yeah our goal is open dialog, and you know, make it clear what we what we're able to do and in what time frame, so that we can yeah move forward for you.

Ross  29:43
Yeah, absolutely. No, I think that's I think that makes sense. All right. No, I appreciate that. And yeah, I think changing circle of care and events are going to be something we're going to start on like right away. Like. Let's just we're gonna let's just start planning for that. I'll bring into that meeting with Michelle and Tasha on Tuesday. Do you want me to send Gabrielle an invite to that as well?

Marcus Morrisey  30:15
Sure. Yeah, might as well.

Ross  30:26
Let me check my Tuesday. Oh, good. That's the 20. It's the 28th It's not next Tuesday. It's Tuesday after. So

Marcus Morrisey  30:37
perfect. Plenty of time to plan around that. So there can yeah whatever time should work for me.

Ross  30:45
Okay, for sure we'll do. Oh, actually, you know what? Let's hold off for now. I'm think I'm going to meet with them internally here, get all their requirements and then work on scheduling. Because, yeah, sorry, sorry, Marcus. Yeah, pretty much. So, yeah, just to type, just know that it's know that it's something that is on the imminent horizon to to gather more details about.

Marcus Morrisey  31:27
Understood.

Ross  31:30
Because basically, that meeting, I think they're going to go through all of their reporting requirements to me, and I can talk just high level on expectations, and then I can collect info, and then we can regroup with you guys. Awesome. All right. Thanks, Marcus.

Marcus Morrisey  31:50
And we'll talk to you soon. Yeah. Yeah. I said I'll reach out with that. We'll talk soon. Other info this week, anyway.

Ross  31:59
All right. Sounds like a plan. Thank you. Yeah. Talks later.

---
