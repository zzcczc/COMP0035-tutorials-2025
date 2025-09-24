# Requirements elicitation, specification and prioritisation

This guide provides a summary of how to elicit, specify and prioritise requirements.

The contents of this guide are:

- [What is a requirement?](#what-is-a-requirement)
- [1. Consider what you already know about the context, product, users etc](#1-consider-what-you-already-know-comp0035)
- [2. Gather (elicit) the requirements](#2-gather-elicit-requirements)
- [3. Document (specify) the requirements](#3-specify-document-the-requirements)
- [4. Prioritise the requirements](#4-prioritise-the-documented-requirements)
- [Further information](#further-information)

## What is a requirement?

A requirement is some capability needed by a stakeholder to solve a particular problem or achieve an objective. The
requirements define a capability that the solution (web app) you will design and deliver has to have for it to be
considered by the stakeholders as meeting their needs.

In the context of the coursework project, the stakeholders are the imagined people who will be using the web app.

Requirements are often discussed in two broad categories:

1. **Functional requirements** are those that specify *what* the system should do; that is a behaviour, feature or
   function of a system. For example:

    - "Create a new customer account"

2. **Non-functional requirements** are those that specify *how* the system should. These often have implications for the
   system architecture and sometimes sub categorised by performance, availability, reliability, usability, flexibility,
   configurability, integration, maintainability, portability, and testability. For example:

    - "The application must support devices running OS verions 3.4, 3.5 and 3.6"
    - "The error rate of users submitting their payment details at the checkout page must not exceed 10%."

## 1. Consider what you already know

By this stage of a project you will have some understanding of what the project, or product, is about. You
may have one or more of:

- Problem statement
- Product vision or definition
- Goals/objectives
- Questions to answer from the data
- Persona or other description of the target audience

For example, you may be able to identify groups of functionality that the system should achieve from the product vision
or goals.

The questions to be answered from the data may help to guide the requirements for visualisations in a dashboard.

The persona might inform the requirements if there is information on current frustrations or goals. Its main use in
requirements is likely to be in trying to consider from the persona's perspective what the web app needs to do.

The persona may represent the main user base of your application, yet consider if there are others who will use the app
as they may have different needs.

While not essential, a context diagram may be useful as a next step as can help you to consider:

- what is the 'system' boundary, i.e., what is in the web app (the system), what is definitely not in it
- who or what (e.g., another system) interacts with the 'system' (external entities)
- what information needs to flow between the 'system' and the 'external entities'

## 2. Gather (elicit) requirements

The [Business Analysis Body of Knowledge (BABOK)](https://babokpage.wordpress.com/elicitation/) lists numerous
techniques that can be used in a real world project to elicit requirements. You would gather requirements (user stories)
by talking to the real users of an intended application, using one or more of these techniques:

- Interview
- Workshop
- Survey/ Questionnaire
- Interface analysis
- Focus group
- Observation or ethnography
- Brainstorming
- Prototyping
- Analysing documentation

In this course, since there are no users for you to talk to, and you are not allowed to involve others outside the
course, then your options will be limited.

Useful techniques for the coursework include brainstorming, low fidelity prototyping (e.g. wireframes), looking at
similar existing web apps.

**IMPORTANT**: Do not involve anyone outside this course in the requirements' elicitation. You must not carry out
questionnaires, surveys, interview etc. even if they are anonymous. This would require ethics approval which is not
possible to gain in the timescales of the course.

Consider from the user's perspective what the web application need to be able to do (functional) and how
it needs to be/perform (non-functional).

## 3. Specify (document) the requirements

Select a structure to formally record the requirements and apply it. The two options likely to be of most use for this
course are:

- User stories
- Functional and non-function requirements natural language specification

Consider if there is a format that better suite the nature of your project/product. For example, User Stories would be
expected if you are following an overall Agile approach to the project.

### User story format

Most agile methods use the user story format.

The basic user story template is:

**As a `_role_`, I want `_goal_` so that `_benefit_`.**

Acceptance criteria, or tests, are often added to the user story to clarify the definition. This is one way of adding
non-functional requirements (or 'constraints') to user stories.

For example:
<hr>
As a website user, I want search functionality to be available on all pages so that I can search for books using keywords.

Acceptance criteria:

1. Search box should accept alphanumeric values
2. Search results should display 10 items per page
3. System responds to all search requests within 2 seconds of receiving the request

<hr>

User stories are not typically classified as functional/non-functional. In some cases the non-functional requirements
may be covered by the acceptance criteria; other times you will
see [user stories written for the non-functional needs](https://www.mountaingoatsoftware.com/blog/non-functional-requirements-as-user-stories)
such as:

> "As a customer, I want to be able to run your product on all versions of Windows from Windows 95 on."

### Functional and non-functional requirements using natural language

![Natural language specification](../img/nat_lang_spec.png)

Each requirement should focus on a single distinct feature or behaviour and should be written in the same uniform
sentence structure. They should not be too vague or abstract; too general or imprecise; or include implementation
information. e.g. "32 The ATM system shall validate the PIN"

You will typically see these listed in a table format, and they may be grouped in some way e.g.

![Functional requirements](../assets/img/functional.png)

![Non functional requirements](../img/nonfunctional.png)

## 4. Prioritise the documented requirements

Once you have your initial list of documented requirements, decide how to prioritise them.

There are numerous techniques for prioritising techniques such as:

- [MoSCoW](https://www.lucidchart.com/blog/introduction-to-moscow-prioritization)
- [Forced pair ranking](https://www.lynda.com/Project-Management-tutorials/Forced-ranking-prioritization/471658/585113-4.html)
- [Story mapping](https://jpattonassociates.com/the-new-backlog/)
- [100 points / $100 method](http://www.modernanalyst.com/Careers/InterviewQuestions/tabid/128/ID/2122/How-is-the-100-point-method-used-to-prioritize-requirements.aspx)
- [Priority poker](http://www.uxforthemasses.com/priority-poker/)

This guide covers MoSCoW since it is widely used, though other techniques may be more relevant for user stories such as
forced pair.

### MoSCoW prioritisation

The [MoSCoW technique](https://www.lucidchart.com/blog/introduction-to-moscow-prioritization) uses a simple
categorisation for requirements:

*M*ust have: These requirements that are absolutely critical to the product/project's success.

*S*hould have: These requirements are also important, but may not be as time-sensitive or vital as the “must have”
requirements.

*Co*uld have: These requirements are nice to have and would make a great addition to the project, but are not critical.
If there’s time, consider adding these in.

*W*on't have for now: The value of these requirements is sufficiently low compared to the time, energy, or budget
needed. They could be considered at a later time.

Consider each of your requirements and assign the most appropriate categorisation. Use your own judgement, there isn't
a "correct" solution as to what the priorities are for the coursework!

## Further information

There are links in the Reading list to requirements elicitation, specification and prioritisation; and UML resources.

Or carry out your own research to investigate other techniques, such as:

- [context diagram](https://miro.com/blog/context-diagram/)
- [use cases](https://en.wikipedia.org/wiki/Use_case) - search Ivar
  Jacobsen, the author of use cases
- [use case diagram](https://www.youtube.com/watch?v=4emxjxonNRI) - a diagram that summarises use cases
- UML diagrams
  e.g., [sequence diagram](https://www.youtube.com/watch?v=pCK6prSq8aw), [activity diagram](https://www.youtube.com/watch?v=Wf_xlagfHmg)
- [scenarios](https://blog.yotako.io/user-stories-user-scenarios-and-use-cases-understanding-the-differences/)
- [user journeys](https://www.nngroup.com/articles/user-journeys-vs-user-flows/)