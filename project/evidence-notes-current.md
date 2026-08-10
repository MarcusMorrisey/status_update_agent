# Evidence Notes — Custom-CMS
**Period:** 2026-W32 (2026-07-24 → 2026-07-30)
**Generated:** 2026-08-04
**Meetings:** 0 internal, 1 external
**Emails:** 1

---

## Email — 2026-07-24 — Waabanong Production Environment Build
**From:** Ross Gillingham <ross.gillingham@peguiscfs.org>
**To:** Campfire Help Desk
**CC:** Varun Mehra; Rob Piché; Ken J; Marcus Morrisey; Antonio Faiazza

Good afternoon Campfire,

Good news, we are ready to start building our production environment for Waabanong.

Let's plan to all meet next week and start the build process.

Warm regards,

Ross Gillingham
Chief Information Officer
Peguis Child and Family Services
Winnipeg Office
500 Madison St
Winnipeg, MB R3H 0L4
PH: (204) 632-5404
https://peguiscfs.ca/

Our Children and Families Come First

---

## External Meeting — 2026-07-28
**File:** 2026-07-28_Case File UAT Walkthrough\2026-07-28_Case File UAT Walkthrough_transcript.docx

Summary

Overview
The meeting focused on the ongoing services portion of the Wabanon system, specifically case file management. Key features include dashboards for task overviews, search functionality to prevent duplicates, and detailed person profiles with intake and case files. The system automates task assignments and document tracking, including legal status and placement details. It also manages face-to-face visitations, risk assessments, and safety circles. The team discussed the need for thorough testing, including scenarios for different user roles, and the importance of minimizing email notifications to streamline workflow. Future enhancements include finance tracking and client profile printing.
Action Items
Send the test environment access email and a quick cheat sheet for logging tickets.
Coordinate a pretest session with CRDs and a few supervisors to validate worker, supervisor, and director views.
Pull the organizational chart from Bamboo and send the appropriate names to ID Fusion so test users and reporting lines can be set up in the system.
Send a meeting invite for the testing session on the 7th.
Outline
Ongoing Services Portion Overview
Speaker 1 introduces the ongoing services portion of Wabanon, focusing on case file management functionality.
Upon logging in, users will initially see a blank page, which will later display tasks and queues.
The system forces users to search for records before creating new ones to minimize duplicates.
Users can open person profiles in a new tab and switch between multiple records easily.
Person Profile and Intake Process
Person profiles include core records, intakes, case files, documents, and an audit log of changes.
Geneograms and current household information are maintained in the person profile and pulled into other records.
Ross finds the system straightforward and asks about geneograms and other features.
Speaker 1 explains the intake process, including creating a case file when ongoing services are required.
Case Management and Task Assignment
Speaker 1 demonstrates creating a case file, selecting case types and subtypes, and assigning team members.
The system automatically creates tasks and assigns them to specific team members based on the case type.
Users can manually create tasks and view open tasks related to the case file.
The system tracks legal status and placement, monitoring mandatory checklists and tasks.
Case Notes and Document Management
Case notes are created for any updates or contacts, with system-generated notes from intakes.
Users can add notes, specify categories, dates, and attach documents to case notes.
Edits to case notes are tracked, and users can view the edit history.
The system allows users to search for notes based on keywords and persons involved.
Placement and Legal Status Management
Placement tabs appear if a placement is made, showing current placements and legal status.
Users can create new placements, select placement types, and specify face-to-face pathways.
The system tracks progress on new admission to care checklists and allows users to mark items as complete or not applicable.
Legal status documents can be uploaded, and tasks are assigned to the legal team for expiry dates.
Signs of Safety and Supervisor Reviews
The signs of safety tab includes 13 steps, each with a description and document upload options.
Users can mark steps as complete and upload documents for each step.
Supervisors can review steps, log concerns, and assign tasks back to workers.
The system automatically creates tasks for supervisors to follow up on overdue steps.
Face-to-Face Visits and All My Relations Plan
Face-to-face visits are logged with details like date, location, and notes.
The system creates case notes automatically when visits are logged.
The all my relations plan tab allows users to create and update visitation schedules.
Users can log visitations, mark them as occurred or canceled, and add notes.
Document Management and Finance Tab
The documents tab consolidates all uploaded documents in one place.
Deleted documents are stored in the inactive section with a history of who deleted them.
The finance tab will track expenses tied to case files, including household budgets.
The system logs all actions and changes, providing a read-only view for users.
Client Profile and Report to Abuse Button
The client profile tab will eventually allow users to print an overview of the client.
The report to abuse button is not available in the current environment.
Users can link intakes to case files, view important information, and attach documents.
The system ensures that all necessary information is available for case management.
Testing and Future Enhancements
Ross emphasizes the importance of testing and coordinating with the team to identify bugs and enhancements.
Users are encouraged to provide feedback and report any issues for immediate resolution.
The team plans to meet next week to conduct detailed testing and ensure the system meets their needs.
The goal is to make the system intuitive, efficient, and reduce the workload for users.


Transcript

Tue, Aug 04, 2026 11:01AM • 1:19:18
SUMMARY KEYWORDS
case file management, ongoing services, intake process, person profile, geneogram, case notes, placements, legal status, signs of safety, face-to-face visits, all my relations plan, document management, supervisor review, task assignments, system testing
SPEAKERS
Speaker 3, Ross, Speaker 1, Speaker 4, Speaker 2, Speaker 5

Speaker 1  00:04
Okay, so what we want to review today is the ongoing services portion of Wabanon. So that is what we call kind of a case file or case file management functionality within the system. So when you first log in, hopefully soon you will start seeing some dashboards on your main landing page. So when you log in for now, you'll just see this blank page. That's totally normal. In the future, what will be here will be when we talk about tasks that are assigned to you or queues. It will be on this landing page. So it will give you an overview of kind of what what's on your plate as a worker, as a supervisor, as a director. It will give you an overview of what your staff has on their plate, but then also any tasks that are assigned to you. So during the intake process and also during the case file management process, there's certain either manual triggers or system generated triggers that will assign tasks to individuals, and that's where this would show up. Now the first thing you need to do to access any sort of record is you first have to do a search. So I've got a few records here that we can use. So you can type in name, a whole bunch of different search criteria, and then it'll give you a list of of users that match that criteria, and then kind of gives you an overview of some of the information to make sure that you're using the right, looking at the right person, and then also at the bottom here is actually where you would create a new person if your search didn't return the the individual that you were looking for. So to try to minimize the amount of duplicates in the system as much as possible. Is the system forces you to do a search before you can actually create a new person? So we'll start with we've got. I think this is the one I had. There's a few different ones here. So when you open up, when you click on the card, it opens the person profile in a new tab. So you can always go back to your search and bring up a bunch of records at the same time, and then just go tab to tab if ever you need to. And then this is covered in in other walkthroughs, so I'll just quickly go through it. But it's where you have your your person profile. So this is kind of your core record that you maintain throughout kind of the life of the this person, and it's also where you have the intakes and case files that are assigned to them. Any documents, eventually we'll have the finance, and and there's also an audit log of any changes that happen on this record, so it's where you have kind of your core contact information, address history, any sort of medical issues. There's your your geneogram, so this carries into the intake and case file quite a bit. So you maintain it here, but then that gets pulled in to the different records, and then also the the current household. So based on individuals in the system that have the same address, it'll create a household for you. Any questions so far?

Ross  04:04
Seems nice and straightforward. So perfect. So just remember that too. Now we're gonna we'll jump into the the case management there. But when we talk about geneograms, things like that, a lot of that happens back on these on these people records or these person records.

Speaker 1  04:16
Yeah. So the first thing, obviously, before you create a case since you need an intake. So here we have an intake that's already been created. We have the an overview of here's the household during that intake, which is kind of a snapshot in time. So if I add new people to the household, this won't get updated because this intake is closed, and it kind of gives you a a history of what the household was like at the time of this intake. And when a intake is closed and it's determined that ongoing services are required, it automatically creates. It's a task that is assigned to Kelvin, and then Kelvin is the one who will actually open up the new the new case file. So I can create a case related to this intake. So I just create click on new case here, and then it kind of starts opening up a case record. So the first thing I need to select is the type of case. So we have service to family, child and care, all the different options here. If I pick service to family, I can then specify the the case subtype, and then this will kind of determine the different tabs that we see here, the different tasks that are created. So this is obviously very important for this example. Just because it opens up a little bit more, we'll do a child and care case file so that you can see that placement tab, and then you assign kind of the team that's assigned to this case. So in the system, we have directors. Under each director, we have a group of supervisors, and then under the supervisor, we have a group of workers. So the first thing you would do is you would pick your director, and then under this director, I may have one or multiple supervisors, and then under this supervisor, I would have multiple workers. Does that follow your your structure, right? Like, let's say, Leanne, you would be the director, and then you'd have your list supervisors, and then each supervisor would have their list of workers.

Speaker 2  06:49
Yeah, I guess the only time that there might there's like one offs where a supervisor is, for whatever reason, maybe a conflict of interest, providing supervision to one case for a worker that's on someone else's team.

Speaker 1  07:10
Okay, so we can once I save this, we can actually kind of play around with the assignment, and if it is confidential, and then you can name specific people that should have access. So it kind of overrides that.

Speaker 2  07:22
Okay.

Speaker 1  07:24
So now I can save and open a case file, so that will officially create the record for me. And then now that I've created it, you can see that my overview tab is now opened up quite a bit, and I can see a lot more information. So at the top we've got an at at a glance. So it's kind of a dashboard within the case file, and it gives you an overview of what's happening on the case file without having to dig through each of the tabs. So each of these kind of relate to the different tabs. So you've got your face to face here. So it would tell you if it was monthly or biweekly or whatever you've defined on your on your placement, and it tells you when the next due date is, and would kind of flag it if it's overdue. Signs of safety. It will show you kind of what steps you have left in your signs of safety checklist. These are any open tasks that are related to this case file. So right away, because I created the case file, the system actually created one for the data entry person to go in and enter the CFIS ID, so automatically because I created that case file, the system has already told data entry, "Hey, there's a new case file. You need to enter it into CFIS and then put in the the CFIS number. From here, you can also manually create any tasks. So, if as a director or if a supervisor is going through it, and you see that there's things that you want the worker to to address, or or for whatever reason, you can manually create a task here, and it'll show up in your in your queue. And then legal status and placement, so it will kind of monitor the the mandatory checklist for placements. If there's any legal status tied to it, it will show up here, so you don't have to dig through. now the persons involved section. So this gets updated. This gets it pulls in the from the intake anybody that was in the persons involved. If. As you're going through the the case, if you determine that well this person actually shouldn't be there, you can actually remove them from the case. They'll stay on the intake; that won't change. But you can remove them from from the case if if applicable. And then whenever you're removing somebody, you always get a prompt to make sure you're not clicking something by mistake. You can also add additional people, so you can add them from the geneogram. So I won't let you add people that are already on there, obviously, but you can add anybody else from There and then it refreshes automatically and adds your new people, or you can also do a search and add anybody that's not on their geneogram. We also had to track

Speaker 3  11:00
a question. Oh, go ahead. For adding and removing people, this is something that everyone has access to, right? Caseworker, supervisor, CRDs.

Speaker 1  11:10
Yes. Okay. Perfect. And then everything, any change here will also be reflected in the log.

Speaker 3  11:19
Okay. Perfect. Sounds good. Thank you.

Ross  11:21
Keep track of all the people Ross add and remove, and then repend. You'd be like, Ross, why did you add and remove all these people? And be like, oh, it was a mistake, and and but it gives you that insight as the director to be like, okay, well, maybe don't do those things.

Speaker 4  11:35
Yeah, you

Speaker 1  11:38
can also track if the individuals were in the home or out of the home. So by default, it'll look at the current address and determine if they're in the home or out of the home. But if for whatever reason you need to override that, if it's not updated, you can you can make that change. If these individuals had open files of their own, they would show up here, and you could click on them and open their file in a new tab. This section is where you can reassign the case to to different people, so it pulls in the first, like when I first set it up, it pulls in those individuals. But if I just want to reassign the supervisor, I can pick from a different the different supervisor list, and I can say, let's say conflict of interest, and then I now have the supervisor user is now the supervisor, but it didn't change the worker or the director. So that's that example Leanne was asking about before.

Speaker 3  12:56
Yes, sounds good. Thank you.

Speaker 1  12:58
And then you can also see a history of all of the changes.

Ross  13:04
So, director got moved over with the auto assignment as well. So you might want to see.

Speaker 1  13:09
Yeah. So that shouldn't have shouldn't have changed the director. Just quickly take a screenshot of that. You can also restrict a case. So, if there's a bigger conflict of interest or there's a safety concern, you can limit to authorized users, so you can start typing people's names, and it will show up. And then, so whoever you've selected here are the only people who are allowed to view the case. Update status is if you want to close it or mark it for waiting for closure for director review. This is where you would change your your status. I believe this is only I'm logged in as an administrator, but a worker wouldn't be able to change the status. It would only be a supervisor,

Ross  14:31
like supervisor director. So, like supervisor. Yes.

Speaker 4  14:34
Yeah. Okay.

Speaker 1  14:37
And then the administration section is where the data entry person would enter the the CFIS number and confirm that they've entered the new case file in CFIS. So that's the overview tab. So this the idea here is this kind of gives you at a glance what's going on. The case, who's assigned to it, who's involved, and then the actual work itself happens in all the other taps. Any questions before I go to the case notes?

Speaker 3  15:20
Looks good to me. No question too.

Speaker 1  15:23
Thanks, RuPen. I'm going to be leaning on you a bit for your opinion today.

Speaker 1  15:27
We're going to put you. Oh,

Ross  15:30
and there's Leanne back too. Perfect. So we'll put we'll put both you and Leanna Leanne on the spot.

Speaker 1  15:37
So Leanne, just to

Speaker 2  15:39
sorry, here you're putting me on the spot.

Ross  15:42
Yeah, we're gonna put you guys on the spot. Don't worry.

Speaker 2  15:45
Okay.

Speaker 1  15:47
We we we're just getting started on the case notes tab, so you haven't missed anything on this tab yet. So this is where you or the workers would enter any sort of notes associated to the case. The first note, whenever you create a case file, this will bring up the. It will create a note with the follow-up notes from the intake. So when I'll actually just open this intake to show you quickly. So on the intake here, when we have the the actions taken, there's a follow up here. So any notes that are entered here, so to give kind of an overview of what's what's been done during intake, any sort of pertinent information that a caseworker would need automatically gets carried over to the case file here, and then you can see when it was logged and who logged it. But it's also where you can create other notes. So you click Add note. You pick from the list of categories that we have here. If these don't apply, you can also have an other and then specify what that is. But let's say there was some sort of contact, and then we say. You can you would specify the date and the time that that contact occurred. You can enter as many notes as you'd like, and then if if there are certain people involved, so let's say if it was a visit or if you had a a meeting and there was different more than just this individual was involved, you can bring in the people that are showing up in that person's involved section on the case, or you can add people from the geneogram or search for individuals if they're not actually so. Like if a social worker was on was was part of the discussion, they wouldn't necessarily be in the persons involved, but you could search for their limited profile and then bring them into this note. And then you can also attach any sort of documents. So if you had a meeting transcript or notes you took that are much more detailed than just having to retype them in here, you can attach that to this specific note. So I'll show you what that looks like. If we do document, let's say it's a correspondence, and then save. So now, so you can attach multiple multiple documents at the same time to to this note too, and we'll say that Michelle was there. So now, if we save this note, so most recent note shows up at the top here. You can see the details because I created the note, I can edit it. A supervisor can also edit the note, and admin can also edit the note. But if another caseworker was working on this before me, I wouldn't be able to edit their their notes. So you can see the The details of the note here. You can see who was involved. You can see the attached document. You can click on it, and then it'll bring up the document.

Speaker 2  19:49
I have a question. Sorry, did you say that new case managers are able to edit previous case managers' notes?

Speaker 1  20:00
No, so you can only as a worker. You a worker can only edit their own notes.

Speaker 2  20:06
Okay, okay.

Speaker 1  20:08
But a supervisor or an admin can update anybody's notes.

Speaker 2  20:15
And is there a record to show that who updated and when?

Speaker 1  20:21
Yes. So let's say I change this and say gave us issues. If I update that, so you can see that I logged it at this time. I edit it at this time, and then you can actually view the edit history, and it shows you what the original note was, and then you can see the new note.

Speaker 4  20:52
Okay. No, that's a great

Ross  20:53
question, Leanne. I love I love that you're asking that because those are the important things to make sure that if you're if I'm going in and making an adjustment or a correction, that sure that's okay because you know we want the latest information there, but we also need to have that record that Ross made this change. This is what Leanne had in there before.

Speaker 1  21:15
Yeah, and then anybody that anybody who can access the case file can view this this history. That's not limited to just the supervisor or myself who made the edit.

Speaker 5  21:26
And so, for the persons involved, can does that case note go on their record as well?

Speaker 1  21:34
If they know, because it's only it only lives within this case file.

Speaker 4  21:42
Okay,

Speaker 5  21:44
that's a cool feature. Is it

Ross  21:48
more so there too, so that we can quickly find the the profile for that user that or for that person that's involved? That maybe if we can go and check. Oh, was the dad involved? Where is he living? Click there, and away we go. Yeah, and

Speaker 1  22:02
then you can also use that as your search. So you have your search categories here, so you can pick your your categories, the dates, the event, who created the note. But then this is kind of a general search where it actually searches for keywords in the description, but then also in the persons involved. So if you want to see, I want to see any notes where the social worker was involved. For example, you could type in the person's name, and then any notes where Michelle is persons involved or even mentioned in the description would show up.

Speaker 4  22:44
Nice.

Ross  22:45
Now, just to kind of clear. Oh, go ahead, Ruben.

Speaker 3  22:49
Just to be sure. So I know. Let's say we have sibling visits or family visits, and workers are usually creating the case node under one sibling and just adding, you know, other siblings to it. So if that's done, then the same case node is not going to show up on other siblings' profile, right? It will only be here.

Speaker 1  23:16
The way it's working now, yes, the note only lives within this case file. If it's something, it's it's definitely something that we could look at. I don't know if it's something that we can necessarily have for version one, just because there's a lot of complexity. Like it would have to look at, hey, does Michelle have an open case. If yes, then like the persons involved would need to change and show the other individuals, and so there's there's a lot of changes there that are needed. But it's definitely something that we could implement in the future.

Ross  23:57
Just a question for Rupa and Leanne: At what level are cases open? To cases, when a case is opened or a file is opened, is that under one of the parents that it's opened?

Speaker 2  24:11
If it's a services to family, yes.

Speaker 4  24:15
Okay.

Speaker 2  24:15
But child service files or files for ECA or an agreement with a minor when it's open under the child,

Ross  24:27
okay,

Speaker 2  24:28
as the case reference.

Speaker 1  24:30
Okay, so that we might have to fix something there then, because right now you're opening because you're creating the intake under the parent, right, and then at the end of the intake,

Speaker 3  24:48
oh sorry, the intake will be created under the parent, and from there, if a child is placed under apprehension, then a child services file will be opened.

Speaker 1  25:01
Okay, because right now it's creating it. So because the intake was under Danny, who's the parent,

Speaker 4  25:08
it

Speaker 1  25:09
created that child in care under Danny. So we would have to then change it so that when you're creating a new case, and it's a child in care. We'd have to have like another drop down where you pick who's who's the child, so that it creates the case file under that child instead of under the parent. And then a

Speaker 5  25:35
protection file is open too for the parent.

Speaker 1  25:39
There's a protection file that's open

Speaker 5  25:42
for the parent who has the intake. Like, if the child, the children are apprehended, then there's like a protection file that's open from the intake, and the children that were under the parents' care who are apprehended, they go under apprehension, and then our child service file. So is that so that would be like the parent? Yeah, the parent. If you're creating like a case from Cephas from intake, and then you would it would open up a protection, and then you can have that from like the oh it's been a while.

Speaker 1  26:34
So let's say okay, so let's say I'm I so this is the parent, and I'm creating a new case. So here it would be,

Speaker 5  26:47
oh yeah, yeah,

Speaker 1  26:48
a service to family case.

Speaker 3  26:51
Yep,

Speaker 4  26:52
yep.

Speaker 1  26:54
And then it would be one of these. Yeah,

Speaker 5  26:57
those options, yeah.

Speaker 1  26:59
But then you

Speaker 5  26:59
would no, that's

Speaker 1  27:00
also. But then you would also need to create a second case under that child for it to be, and then that would be a child in care case.

Speaker 3  27:10
Yes.

Speaker 1  27:14
And then does that child in care case need to be linked back to the intake, or would it just be I would go under. Sorry, I'm going to bounce all over. So let's say I would go under. This is the child. Oh, she's actually an adult, but let's say it's a child. And would I just go on new case here and create a child in care, or do you need it to be linked to that original intake,

Speaker 3  27:45
I don't think we can have two case references for the same intake, right? So if we are already using the parent as the case reference for the PRT file, the the CS file or the child services file is going to be separate.

Speaker 1  28:05
So you would just come. So this is the child. You would click new case, and then you would pick a child in care.

Speaker 3  28:12
Child in care, yes.

Speaker 4  28:13
Okay.

Speaker 3  28:15
And then in the family, like in the client relationships, we will link the parents. Basically, we will add the parents' name, their profiles as well.

Speaker 1  28:28
Okay, so if I pick this, this open the case, the person's involved, then you would pull in the Parents,

Speaker 3  28:40
yes.

Speaker 1  28:41
Okay, so the way it's set up now is fine. It's just my example didn't necessarily follow your your flow.

Speaker 3  28:49
Yep, that's yep. This okay just seems right to me. Unless the end, you have. If you think it needs to be yeah, it seems

Speaker 2  28:56
right to me too. Yeah, no, looks looks good.

Speaker 1  29:01
Okay, so we'll just pretend that we're creating this child in care on a child record for now. Okay. Any other questions about case notes before I? So really, this is just where you keep adding notes. There are some system-generated ones like these intake notes. When you do a face-to-face visit or an AMR, that will also create case notes automatically. So, which I can which I can show you, but the idea here is this is where the workers log any sort of updates or contacts or anything. Does this

Ross  29:54
mentioned Gabrielle? You had mentioned limited profiles for workers and things, so. Just to just to confirm, just by adding staff into the system, a limited profile gets created for them.

Speaker 4  30:08
Yes.

Ross  30:09
Okay. Perfect.

Speaker 1  30:15
Wait. So if there's no questions on case notes, we'll go to placements. So this tab obviously just shows up if a placement is makes sense. So if it's a service to family, this tab doesn't show up at all. So there's two different sections. You've got your current placement, and then you've got your legal status. So this is where the legal team will be able to upload any sort of legal status documents, and they'll get tasks assigned to them to know when they need to do that. So the first thing you do is click on new placement, and then you've got your list of placement types. I notice this list doesn't match what's supposed to be in there, so this will change before it gets opened for you guys to test. But here, there would be like kinship one, kinship two, all of that. So we'll just pick, let's say, guardianship for now. You'd pick the start date of your placement, and then you select your face-to-face pathway. So let's say it's monthly face-to-face, and then the reason for for opening the placement. So you've got this is the initial placement, and then we can save it. Before I save it and close this, any questions or any information that's maybe missing on a new placement that you would expect to see?

Speaker 5  31:54
What is that face-to-face pathway again?

Speaker 1  31:58
So that determines how often you have to have the worker has to have a face to face visit, and then that will kind of so based on that it will carry over to this the face to face tab here, and then it'll also create tasks and alerts based on when those those are due.

Speaker 2  32:22
So what would it look like if we were to for placement type? So, I'm just I'm seeing this through the lens of entering a placement for a child in care. So, then placement type. Can we go through that list again? Because you you said that that might be changed though.

Speaker 1  32:42
Yeah, so this is where you would have your kinship, your different kinship types. There would be I'm trying to think of what the other ones are. The resource hold

Speaker 2  32:57
those.

Speaker 4  32:59
Yeah.

Speaker 2  32:59
Where do we type in the details of the actual placement, including like who the caregiver is, if it's licensed through PCFS or another licensing body?

Speaker 1  33:12
So, if these were the correct ones, so let's say I was picking group home or resource home. There's a there's a list that you guys can maintain of what those resource homes are, what the address is, who the primary contact is, and how many beds or rooms are available. So that would give you a drop down. So if you pick resource home, it would give you a drop down of here the resource homes. If it was kinship, then it would give you the option to select who that primary caregiver is, whether it's from their geneogram or just a basic search to bring in an existing profile.

Speaker 2  34:00
What if there's not an existing profile because placement is so it's someone that's not been involved with the child or with our system to date?

Speaker 1  34:09
So when you do a search, it would give you the option to create a new profile from there,

Speaker 2  34:16
and we would create a new profile for for the sake of entering a placement,

Speaker 1  34:23
yes.

Speaker 2  34:24
Okay, thank you.

Speaker 1  34:24
And then you'd have your address, and then so it would take that person's address and then update the child's address automatically when when they're on a placement. So you don't have to go back to the profile and update update their address again.

Speaker 2  34:40
I don't know who to direct this question to, but who, because who would be entering placements

Ross  34:49
right now? It's our FamCare admin team.

Speaker 2  34:54
So it would be case managers that are going to create new profiles for placement.

Ross  35:00
I'll defer to Christina. Christina, our current process is like Hope does a lot of that creation and entry, right? So I I foresee that continuing unless Christina has any objection to that. But yeah, we'd have a like our FamCare admin team would probably become like our Wabanong admin team. Yeah.

Speaker 2  35:18
Okay. Yeah, makes sense to me. Thank you.

Speaker 1  35:22
So I think we had it that it was supervisors who were creating placements, so workers couldn't. And yeah, no worries. This is a specialized. So we'll have them maybe change.

Ross  35:36
Hope's a specialized role, so they're like a fam care admin.

Speaker 4  35:40
Okay, so we'll probably just have to create that that role. Yeah, we can give them access. We can,

Ross  35:47
yeah, we can review what those permissions are for that.

Speaker 1  35:53
So if I save that, I now have my current placement, and then now because I have a placement open, I now I have the new admission to care checklist that I can go through. So I can open the checklist, and this is similar to what I think the workers already. Pass alerts tied to this, so I can see all of the the different items that I have to do when there's a new placement. So I can edit that, and then I can mark it as complete, or I can mark it as not applicable, so things like I think there was, so let's say like daycare registration that's not applicable, and car seat isn't applicable. But then these are complete, so then I can close this. I can save it first for making a change. So let's say photo child, car seat, care. We'll move. We can have

Ross  37:15
a we'll move the save button there.

Speaker 4  37:18
Yes.

Speaker 1  37:22
So now I can see the progress. So I've finished one of 22 items. So before I was 24, because I marked two that are not applicable, it's now changed my total to 22, and I've marked one of those as complete. So now I can see the progress bar of how much is done, and then it's also updated on my on my overview tab here. I can see that some items have been checked off. So, as a supervisor, a director, you can just go in here and see. Okay, they're actually working on things without having to dig through all the tabs. I can also edit the placement for whatever reason. I can also end this placement. So by ending it, you give a reason why you're ending it and why, or and when, and then it will also because you're now ending the placement and not putting them into a new one. It will kind of it'll also put an end date on the child's current address automatically. If you are moving them from one home to another, you don't need to end the placement and then create a new one. You can just click on New Placement. It'll force you to close the current one first, and then you can enter a new a new placement all in the same Screen. Any questions for placements?

Speaker 2  39:13
No.

Speaker 5  39:13
Do these placements have their own, like their own page too, like their own profiles?

Speaker 1  39:23
So by like, do the

Speaker 5  39:27
when you search providers, yeah, the care providers.

Speaker 1  39:32
So they should all have either like a full profile if they're a family member or something, but they maybe

Speaker 5  39:41
yeah.

Speaker 1  39:42
But otherwise, they would have a limited profile.

Speaker 4  39:46
Okay,

Speaker 1  39:47
and then you, when you look at their current household, any child that's living with at the same address would show up there.

Speaker 5  39:56
Oh yeah.

Speaker 1  40:00
Then the legal status is where the legal team can upload any sort of customary care agreement or any documents here. So you have a start date and an expiry date, any sort of notes that you want to add, and then you can upload the document. So let's say we do this, this, and then you can see the the documents here. When it's nearing the expiry date, there's also tasks that are assigned to the worker and the legal team, just to to get ahead to get a new agreement if you need or or anything like that. And then this will also show up on the dashboard for the legal team, so they'll be able to to kind of keep track of that too. Any questions there? Okay. The next tab is signs of safety. So this has all the 13 steps for signs of safety. By default, it shows you all of them. If you just want to see the ones that are to do, that means that they they are near the due date or past the due date. So right now, I don't have anything, or you can just filter on just the ones that are completed. So the first one is the genogram. So each item has, if you hover over, it gives a short description from your policy manuals of what each item is. So for this, it's just to make sure that the geneogram is complete. So if you click on this, it will open up that person's profile, bring you straight to the geneogram section, and then you just go in, make sure that it's complete, and then you can come back and mark it as complete. So now it shows that I marked it as complete on the 28th. So each step has after that has a document upload. So let's say for your harm matrix, you can upload a document. It will store the most recent document. But if later on you need to to upload a a more up to date harm matrix, you can upload another one. It will remove the previous one from here, but it'll still always live in the Documents tab. So you always have the history, but this tab just shows you the most, the most current document. Trying to think of some, so let's say the safety circles. So this one has can have multiple ones. So if I pick, no, sorry, it's the sharing circle as Nathan. So the sharing circle, you have a little bit different options. So you can pick which one if it's the initial, ongoing, or final circle, and then the purpose of the circle. So this is a multi-select that you can pick, and then you can upload your document. And then when you save this, so you can see your document. You can see who added it, and then you can see the different things that were discussed here. And then, because this needs multiple steps, the status is ongoing, so it's not completed until that final circle is uploaded. And then, so that way, when you go to to do, you can see that there's still actions needed for this step here. You also have the safety scale at the top here. So right now, it hasn't been assessed yet, but when I do my risk assessment, I can pick what the the safe the score is. So zero to two is high, three to five is medium, and then so on. So if I pick, let's say a one, so it's high risk. I attach my document. So there's a two-step here. So you have to share the risk assessment with the family. So that tells you you have 90 days remaining to share it with the family. If it's with close to the 90 days, there's a task that's automatically assigned to the worker to let them know that this is coming up, and then this is where you would update that you actually share the document with the family, and then it'll kind of close that that risk assessment, but then the number that I put also shows up here now, at the top. And if I remember correctly, this also triggers a task, which we could maybe find here. So already you can see there's a whole bunch of tasks that were created just as I'm going through the case file.

Speaker 1  46:06
So, because it's a high a high risk, there's a task that was created for the supervisor to to do a review. And then, yeah. So you can see every time. So, like, I created a placement. So there's there's documents that need to be signed and all that. All of that is automatically created and assigned to either the worker or the supervisor, depending on what it is. Yeah, so I don't won't necessarily go through each of these different steps, but most of them is just standard document upload, and then it'll mark it as complete. If there's more than one document that's required, it'll do like like the sharing circles here and just mark it as an ongoing task that's needed. If a worker logs in, they'll see it in this order. So they'll see the 13 steps, and then they'll see the supervisor review at the bottom. If a supervisor logs in, they'll actually see the opposite. They'll see the supervisor review first because that's the one that they care about most, and then they'll see the 13 steps below it. So the supervisor review, you would click the add review button. It defaults to the current date, but you can change that. And then a review type. So let's say this is a new case. And then I reviewed the genogram. I reviewed the risk assessment. And then you can log any sort of concerns or direction that you want to send back to the worker if you want them to do another risk assessment or something. So you can either save this right away, or you can save and assign a task back to the worker if you want them to to do an extra step or something. So if you click on if you click on Save and Assign Task, it will bring up the the task module or modal, and then you can assign a task back to the worker, and it'll take the the direction text from your review. It'll bring it into the the task automatically, but you can also add or update that text if you like. Then, because I save that, I can see my review here, and then so you see the the full history of any review the supervisor's done. Good so far.

Speaker 3  49:17
Yep.

Speaker 1  49:21
Now we've got the face-to-face and all my relations plan. So these are like one might not be needed, so you can collapse the the section if you don't want to see it. But this pulls in the pathway from the placement, so because I selected monthly, this automatically is set to monthly, and then it's it tells you when the next face-to-face visit should be. So, supervisor can also. So edit the pathway if if that's necessary. So if there's higher risk and you want to do it weekly instead, you can change that, and then it'll adjust the the the due dates and the tasks that are assigned. So let's say I log a visit. So you have either an actual visit that occurred, or if you just attempted and weren't able to reach them or meet with them, you can log back. You've got the date. You've got who conducted the visit. So by default, it'll be whoever's entering this, but if I'm entering it for somebody else, I can pick that person. We've got the location of where that visit happened. It was a one-on-one visit. You can upload the signed form, and then the worker here has the option to either save it as it is now without adding any sort of information about the note, because if they just want to, if they're in their car and they want to gather their notes and they just want to document that the visit occurred, they can save it, or they can enter notes right away, and this will actually create a case note on this the case notes tab. So if they save it now, they'll get. I think if I remember, it was something like 30 days or 15 days or so before they have to actually enter a case note. So the system will generate a task for them to remind them that they need to update the the note on the visit If they don't, if they just create it, then it won't create the task for them. So just to show you that it creates the note, well.

Speaker 3  51:55
So once a face-to-face or note is created, like is it going to? Like, would the supervisor be notified for any of those?

Speaker 1  52:08
When when a visit is done,

Speaker 3  52:11
or when a case notice entered,

Speaker 1  52:14
supervisor wouldn't be alerted, but they'd be able to see it

Speaker 3  52:18
in the record. Yeah,

Speaker 1  52:19
yeah. I'm assuming if they'd get alerted for every note, they'd probably get inundated with yes notifications.

Speaker 3  52:32
Yeah, with FamCare, I think it was like when worker would enter note and like save it. They had the option to like email the supervisor, so we would get like multiple emails, and then, yeah.

Ross  52:47
I think we're gonna we're gonna find with Wabanong that we're moving far away from that approach. In in so far as that there will not be email alerts sent out, so it's a bit of a shift where we have to be living more in the system, and then for supervisors and directors and things, keeping an eye on those dashboards and then ensuring that you know we define the dashboards that that we need to stay on top of of tasks and things like that. I think that's where we're going to see a big shift, and that and like what you said, Ruben, is if you're getting seven emails because I updated a case note, like you're going to stop looking at your email and you're going to stop looking at those notifications, and

Speaker 3  53:33
yeah, you're going to that's what's

Ross  53:36
no, and that's 100% fair because as humans, we only have so much attention span, we only have so much brain power, and our brains, after a while, are like, "Well, that's not an important email. I'm not paying attention to that. It's just Ross updating a case note. I don't need seven. So, what we want to try to do is empower you all to be able to be more aware of the critical things that you need to be alerted to through these dashboards, and then other things that you can bake into your routine of. And I'm going to go check these these places and these things.

Speaker 3  54:08
Yep, sounds fair.

Speaker 1  54:11
So now you can see the the visit that I logged. So you can see the details. You can view the document that I attached. You can view the note from here, and then it also-I go here. It also created this note automatically. So again, it gives you when you go to this case notes tab, it gives you a full picture of what's happening, and you're not having to enter notes in multiple multiple areas. There's also reels in there, which is a little bit harder to show because of timing. But if there's been multiple attempts within the period and a visit hasn't happened, then it triggers. Tasks for supervisors to follow up and and all that, but I won't necessarily show you all of those different scenarios in this walkthrough, though. Then at the bottom we have the all my relations visit plan. So first thing you do is you first create a plan. So it defaults to step one, but I don't know if it ever happens where you jump right into, let's say, unsupervised visitations. But if if that's the case. You can always jump ahead. So start with step one. Then you would add your visiting schedule. So let's say you have schedule with the mother, and how many times they can visit with the child, so if it's weekly, the duration, where the visits happen, any sort of authorized participants. So this again brings in people that are on the case file. So let's say these people can be there. If there's any sort of other conditions specific to the schedule, you can add that, and then you can upload the signed plan once you've when you reviewed the plan with the family, and then actually enter it. You can do that here, and then you can add multiple ones. So if there's another one with with the dad that has a different kind of plan, you can add it here. And then these are just overall visitation rules or conditions that you need to track. So when you save that. It then gives you the different the different plans, and then now you can start logging visitations in relation to that plan. So you can view the plan details. So you can see right now I'm in step on step one. We've got the mother's schedule. If father had a schedule too, it would show up here, and then you can also update the plan. So if I want to now move to monitored, I can click Update Plan, and I can change this now to Step Two. The rest is the same, and then I can start a new version of it. Start a new version. That's interesting. As you can see, we're still. This is a beta version of of the environment, so there might be some a few bugs.

Ross  58:29
Yeah, no worries. That is a high res logo, though. I will say that.

Speaker 5  58:32
Yeah.

Speaker 1  58:37
Let's go back. I don't know what's changed, all of a sudden. Sorry

Speaker 4  59:24
about that. Okay.

Speaker 1  59:39
Let me just zoom in again. So now I can see we go back. So I updated that plan. So now I can see that I'm on version two of the plan, and I'm now doing monitored visitations. And if you click on View Plan Details, so you can see I'm now installing. Two, but then you can also see a history of the plan, so you can see what version one was. And then now that I've got the plan, I can actually log visitations to it. So if I had multiple schedules, I'd be able to pick from them. And then you can say if the visit occurred or if it was canceled. If it was canceled, you give the reason, and then notes so describe the behavior of the parents or children. If it occurred, you can say who was present? So this pulls in from the schedule that I created. I said that DJ and Michelle were were members that are allowed to be present. So that's why they show up in this list here, and then you can say who supervised it. So if it was staff, who who that person was, or if it was a family community member, you can bring them into. And then obviously, once it moves up to unsupervised, then these fields wouldn't wouldn't show up. I can save that, and then that now shows up in my history of visits here, and then because I added a note here, it also creates a visit note on the case notes tab. Any questions there? Nope. Okay. This one's going to require quite a bit of testing and playing around with because there's a lot of different rules, and you might need to backdate things so that you can test some of the tasks and and all that that get triggered when things are due. But that'll be a Ross thing to coordinate.

Ross  1:02:17
I will coordinate that, and Leander Pen will will have to get some time, all of us together in the same room, to to run through this and and make sure that it meets needs and that we identify bugs and that we can get any changes that your team needs to see in the queue.

Speaker 1  1:02:35
Then documents tab is all this does is it pulls every single document that's been uploaded in all these other tabs and brings them all into one area so that you can, if you need to find a document, it's a lot easier to come in here and search for it instead of trying to figure out where it lives. It also gives you a history of any documents that have been deleted, they're actually they're they're just deleted from the tab, but they're never actually deleted from the record, so they'll live in here. So if, for example, if I maybe I'll go here to show you. So if I want to remove this risk assessment document, it's now no longer there. My status has gone back to not started, but when I go to my documents and show inactive. It shows up here, so it shows who deleted it and when, and that it was a risk assessment document. And you can still view that document. It's just not as available as it was when it was still active. So from here, same thing. You've got your search. You can see any documents that have been uploaded within a certain range, if you'd like. You've got the different document types here, and then you can also search, obviously not within the text of the document itself, but the document name, or you can do a search here to find the document you're looking for. Finance will be coming shortly, but this is where you'd be able to track expenses that are tied to the to the case file. So the wireframes we went through last week. This is where that would lift. So you'd be able to monitor the household budget and the. Tied to it, and then the log is the system generated. So you can see just walking through the case file, it logged 21 different entries. So this is just a read-only view. You can't delete anything or edit anything, but you can filter on the different type of action and then who did the change. So this is going to get very very long, but it shows you the first 15 records and then you can go through the different pages. The other thing at the top, so the top will always show you your case file ID. That's auto automatically generated. You've got your status, and then you've got your case file type here. Then it shows who it's for, and you can always click on their name, and it'll take you directly to the person record in a new tab. If ever you want to look at information, it shows when it was opened, who's assigned to it, the CFIS ID once it's entered, and then the linked intake if there is one, and then it'll bring in any sort of important information. So obviously court orders, if there's medical emergency or things that are identified on the person profile, that will also show up here. This is another area where you can just attach documents. So you can pick a document, give it a type, add any sort of notes, and then you can attach multiple documents all at once, and then it will add it to the Documents tab here. Client profile isn't in place yet, but this was something that you had asked for to be able to print to hand off to other people, or for people to get an overview of. the client profile. So while you're testing, if you can think of what you would like on this client profile, that would be helpful so that we can put that in place for you. Not sure if this is a version one or a version two thing at this point, but the idea was that you can kind of go into the case file, see what information you need, because you might not need this anymore if people have enough information at their fingertips. The report to abuse button you will not have in your environment because we haven't opened the abuse module yet. But this is where, as you're going through, you might notice that I don't know there's some abuse happening within the the placement home. This is where you would submit a a request for the abuse team to to open up an investigation, and that covers the case file.

Speaker 1  1:08:35
So now that I have this case file open, if I go to Danny's profile and go to the intake and case management tab. I can now see that there's an open case file. This is the type. This is who it's assigned to, and that they're currently placed in a group home. And then from there, I can click on it and open the case file, and then from here, this little icon here shows that it's linked to this intake, so that's where it originated from. And that's it for case management. Any questions? I know this was very quick. There's a lot to cover on a case file, so if I glossed over something that you want to spend more time on, we do have some time left. If you'd like, okay.

Speaker 3  1:09:42
cannot think of any questions, but just the the visitation one. So the visitation schedule will come along with face to face, and then is there because like like right now workers they. Are creating like a word document for visitation, right? So, is like is this going to replace that? And workers will create the visitation schedule in here. But does it give us an option to print that visitation schedule, or is it just a record of visitation whether it has occurred or no?

Speaker 1  1:10:24
So it's more a record at the visitation because if I correct me if I'm wrong, but the visitation-the reason they're doing it in in that Word document is they're kind of working with the families to create that plan, and then they get sign off from from the caregivers or from the family.

Speaker 3  1:10:45
Yes, and then a couple years with everyone. Yeah,

Speaker 1  1:10:48
yeah. So that would continue, and then this is more for to log it in the system so that they can now know like when the next visitation should should occur and and all that.

Speaker 4  1:11:02
So that's why when you

Speaker 1  1:11:09
do here. So when you update the plan, you can upload the signed plan here. So that would be the Word document that they create, and then yeah, this is more for the system to then monitor it going forward.

Speaker 3  1:11:29
Okay, sounds good.

Speaker 1  1:11:35
Any other questions?

Speaker 2  1:11:42
Not at this time for me.

Speaker 1  1:11:43
No. Okay. Any scenario that maybe you wanted to see to see understand how it's working or know it's going to be better when you're actually clicking through and testing it? But

Speaker 3  1:11:59
yeah, maybe we'll try the testing.

Ross  1:12:02
Yeah, I think that's going to be our next step here. Is Rupen Leanne will have to get together ourselves, and then with some of your maybe with one or two your supervisors, and spend spend honestly either a morning or an afternoon, which I know is tough to do, but it is critical for this testing to to go through together, to say, all right, you're the worker. This is the view you're seeing. You're the supervisor. This is the view you're seeing. I'm the director. This is the view I'm seeing, and and going through these scenarios together to make sure that that it works as you guys need it to.

Speaker 1  1:12:40
Yes,

Ross  1:12:41
that's that's part of the fun of testing,

Speaker 1  1:12:44
and the idea of testing is to try to break the system and use like real, real scenarios. Obviously, keeping things anonymous, so changing the names, but actually using real case files to make sure that you're able to track everything that you need to track, that it's intuitive enough, and that it's not causing more work for you and your workers. Because the the whole point of the system is to make to make things easier for you, and then just seeing if there's any bugs along the way. So I noticed a few just during the walkthrough. I took a few screenshots, so we'll get those addressed for you. But if you see anything, please let us know, and we can also make some some changes. But at this point, if they're not mission critical, like if it's not stopping you from actually doing your work, then we may have to look at pushing that into version two or or a future enhancement. But still, please let us know if you notice anything, so that we can prioritize and and keep track of those. Now, for the two of you, you haven't been part of testing before, so what we'll do. You should both have a a login already. We'll just we'll have to make sure that your teams are set up properly so that you've got the right supervisors and the right users under you. And then I don't know if you want to, Ross. It'll just keep going how it was before, where you'll log the tickets, or

Ross  1:14:44
yep, I'll still be we'll still be logging tickets here. I think it probably makes sense to to meet with with our CRDs and come up with kind of the the pretest or the the the pre. Testing, testing, where we'll make sure that I don't know. Do you guys already have a document of, I guess, org structure almost at work? You know, where it's who your who our CRDs are, who their supervisors are, and who the workers are, and then we can just make sure that we add the appropriate levels into into the test system. Do we already have that somewhere in a document?

Speaker 2  1:15:26
I need major updating the what document I have.

Ross  1:15:31
Okay,

Speaker 3  1:15:32
we have the the organizational chart on Bamboo. I'm not sure. Okay, download like print or something like that.

Ross  1:15:41
I'll I'll just take a look at it. We'll just go off of Bamboo, and I'll just get those those names over to ID Fusion to get set up in the system. Perfect. We don't have to use everyone there, but the I'll make sure everyone gets in the system at that point because then if someone drops in with us for testing or we identify someone to come in, they'll be able to log right in right away, and we'll be able to get them up to speed pretty quickly.

Speaker 1  1:16:05
And then we can carry that over to the live system too, so that you only enter it once, and then it's it's done.

Ross  1:16:14
Yeah, for sure.

Speaker 1  1:16:15
And then you also have still have access to the permissions table, right? I do. If if you want to see here's what a supervisor should see versus here's what a worker should see, just to give you an idea of why somebody's seeing something different, and whether it's intentional or not. Yeah,

Ross  1:16:36
absolutely.

Speaker 1  1:16:39
Good. So if there are aren't any other questions, I we can wrap it up if you'd like. I'll send you an email with the link to access the test environment for Wabanaq, and then also just kind of a quick cheat sheet on how to log tickets if ever Ross isn't available, and you see something right away that you want to send send to us directly. You you'll have access to doing that. So it's just sending us an email. It goes comes to me and the development team, and then we can address those issues for you, kind of as you're testing. So we try to do it within the same day, next day type thing, so that as you're testing, you see those changes come in right away.

Ross  1:17:37
Rufan, Leanne, do you guys have any time on this Friday?

Speaker 2  1:17:45
I have to go to the Sundance.

Speaker 4  1:17:50
Ah, yes. You guys are going to Sundance, okay? Totally fair.

Ross  1:17:59
We'll plan probably to meet early next week? Then it's tough with it being the holiday there, but we'll we'll figure it out. We'll figure it out.

Speaker 3  1:18:15
Well, if it's a day off, then you figure it out. Cut us out.

Ross  1:18:23
Yeah, and it's not Monday. Don't worry.

Speaker 2  1:18:28
I can't do Tuesday or Wednesday. I'm fully. I'm looking to be off Tuesday for Pan. I'll talk to you about that. And Wednesday, I have a day long meeting.

Ross  1:18:41
Okay. So, how's our Thursday afternoon next Thursday look? The sixth.

Speaker 3  1:18:47
Calvin and I have to go take a tour for a venue at 3p.m.

Ross  1:18:51
Okay.

Speaker 3  1:18:52
On sixth, but before that, like before 2p.m. I can make it work or seventh anytime.

Ross  1:19:00
Oh, maybe let's plan out for the seventh. Then I'll send an invite over.

Speaker 2  1:19:03
Okay.

Ross  1:19:05
All right. Thanks, everyone. Appreciate all your time. In the meantime, if you have any questions, let us know.

Speaker 3  1:19:09
Yep. Thank you. Thank you so much. Thank you very much.

Ross  1:19:14
Thanks, everyone.

Speaker 1  1:19:15
Bye.

---
