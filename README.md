# COMP 361 - Final Exam
## Section 1: Definitions – Concepts, Tools, and Processes
### 1.	Abstract class

**Definition:** An abstract class is intended to be a base or "blueprint" for other classes, but cannot be instantiated. It often contains at least one method that is defined but has no implementation, forcing subclasses to provide the specific logic.

**Example:** In a banking system, Account could be an abstract class defining common behaviors like deposit(). Specialized subclasses like SavingAccount or CheckingAccount then provide the specific, functional implementation. 

**Context:** In Object-Oriented Design, abstract classes are used to capture common characteristics of a group of objects while preventing developers from accidentally creating "incomplete" objects that don't make sense in the real world.

### 2.	Activity diagram
**Definition:** An activity diagram is a behavioral diagram that visualizes the sequential and parallel flow of activities, actions, and decisions within a system process or a specific use case.

**Example:** In a car-sharing reservation system, an activity diagram would map the steps from “Search Vehicle” through “Select Time Slot” and “Confirm Booking”, including loops for invalid inputs and branches for payment success.

**Context:** System analysts use activity diagrams during the Analysis Phase to document complex business workflows. They are essentially "advanced flowcharts" that can handle complex, simultaneous actions.

 
### 3.	Adaptive/predictive approaches
**Definition:** A Predictive approach assumes the project can be planned in advance, while an Adaptive approach assumes the project must evolve as it progresses.

**Example:** Predictive: Building a bridge where every measurement must be calculated before construction begins (Waterfall). Adaptive: Building a mobile app where features are added based on monthly user feedback (Agile/Scrum).

**Context:** Analysts choose between these based on project risk and requirement clarity. Predictive models suit stable, low-risk systems (e.g., payroll), while adaptive models are preferred for innovative projects where rapid change and constant stakeholder interaction are necessary for success.

### 4.	Alpha/beta versions
**Definition:** Alpha versions are early, unstable software builds tested internally by developers. Beta versions are more mature, feature-complete builds released to a limited group of external users to find remaining bugs.

**Example:** A car-sharing app Alpha version might be tested by the internal IT team to ensure the “Book Car” button works. The Beta version is then released to 100 actual members to test real-world GPS accuracy.

**Context:** In Implementation and Testing, these stages represent the transition from "it works on the developer's machine" to "it works for the actual customer."

### 5.	Client/server architecture
**Definition:** Client/server architecture is a distributed computing model that partitions tasks or workloads between the providers of a resource or service, called servers, and service requesters, called clients.

**Example:** In a car-sharing system, a mobile app (the client) requests a list of available vehicles from a central database and business logic controller (the server) via an API call.

**Context:** Architects use this model to improve scalability and maintainability. By separating the user interface (client) from data management (server), developers can update the database schema or business rules without requiring a complete reinstallation of the end-user’s software.

### 6.	Component diagram
**Definition:** A component diagram is a structural diagram that describes how a system is split into physical components (like DLLs, database schemas, or executables) and the dependencies between them.

**Example:** In the car-sharing system, a component diagram might show a "Payment Component," a "User Profile Component," and a "Vehicle Tracking Component" that all plug into a central "API Gateway."
**Context:** In System Architecture, these diagrams help developers and stakeholders see how the system is organized into modular blocks that can be developed, tested, and replaced independently.

### 7.	Communication diagram
**Definition:** A communication diagram is a type of interaction diagram that shows how objects associate and collaborate to perform a specific task or use case. Communication Diagram focuses on the organizational structure and relationships between objects.

**Example:** In a car-rental system, a Communication Diagram would show the Clerk object connected to the Reservation object, with a numbered arrow like 1: createReservation() pointing from the Clerk to the Reservation.

**Context:** In Object-Oriented Design, these diagrams are used to model the dynamic behavior of a system. They are often used interchangeably with Sequence Diagrams because they contain the same information but present it in a different visual layout.

### 8.	Data access class
**Definition:** A data access class is a specific class in an object-oriented system that contains the logic required to fetch, insert, update, or delete data from a database. It acts as a "bridge" or intermediary between the business logic and the physical database.

**Example:** In the car-sharing system, a CustomerDA (Data Access) class would contain the SQL code to SELECT * FROM Customers WHERE ID=101, so that the Customer object doesn't have to "know" how to talk to the database itself.

**Context:** In Object-Oriented Design, these classes are part of a Multilayer Architecture. By separating data access into its own class, you can change your database (e.g., moving from MySQL to Oracle) without having to rewrite your entire application's business rules.

### 9.	Database normalization
**Definition:** Database normalization is a systematic, multi-step process used to organize the fields and tables of a relational database to minimize data redundancy (duplication) and improve data integrity.

**Example:** Instead of storing a customer's address in every "Order" record, you create a separate "Customers" table and link it to the "Orders" table using a unique ID.

**Context:** In Database Design, normalization ensures that if a piece of data changes (like a phone number), it only needs to be updated in one place.

### 10.	DBMS
**Definition:** A DBMS is a specialized software suite that serves as the interface between users, applications, and the actual data stored in a database. It allows users to create, read, update, and delete (CRUD) data while managing the database's structure.

**Example:** In the car-sharing system, Microsoft SQL Server or MySQL would act as the DBMS, managing the tables for Members, Vehicles, and Reservations while ensuring that two people cannot book the same car simultaneously.

**Context:** In Database Design, the DBMS is the "engine" that enforces security, handles multi-user access (concurrency), and ensures that the data follows the rules defined in the Relational Database schema.

### 11.	Deployment
**Definition:** Deployment is the final phase of the systems development process where the completed and tested software is moved into the live production environment for use by the end users.

**Example:** In the car-sharing project, deployment involves moving the web application files to the production server, updating the live database schema, and releasing the mobile app version to the Apple and Google stores.

**Context:** Analysts plan deployment strategies (e.g., direct cutover, parallel, or phased) to minimize business disruption. Successful deployment ensures all software components are correctly integrated and operational for the client.

### 12.	Design pattern
**Definition:** A design pattern is a repeatable, proven solution to a commonly occurring problem in software design. It is not a finished piece of code, but a template or description of how to solve a problem that can be used in many different situations.

**Example:** The Observer Pattern, where a "Subject" (like a weather station) automatically notifies all "Observers" (like a phone app and a website) whenever the temperature changes.

**Context:** In Object-Oriented Design, using established patterns helps developers communicate more effectively and creates systems that are easier to maintain, flexible, and robust.

### 13.	Dialog metaphor
**Definition:** The dialog metaphor is a design concept where the interaction between a user and a computer is modeled after a human-to-human conversation.

**Example:** An installation wizard that asks, "Where would you like to save this file?" and provides a "Next" button, simulating a back-and-forth exchange.

**Context:** In HCI (Human-Computer Interaction), this metaphor helps users understand how to navigate a system by following familiar social patterns of listening, thinking, and responding.

### 14.	Digital signature
**Definition:** A digital signature is a mathematical technique used to validate the authenticity and integrity of a digital document, message, or software. It is the digital equivalent of a handwritten signature or stamped seal, but far more secure.

**Example:** When an executive signs a digital contract, the system uses their private key to create a unique code (the signature) that proves they were the one who signed it.

**Context:** In System Security, digital signatures ensure non-repudiation, meaning the sender cannot later deny sending the message, and they guarantee that the data hasn't been altered during transit.

 
### 15.	Encryption/decryption
**Definition:** The process of scrambling data into an unreadable format (encryption) and converting it back into its original form (decryption).

**Example:** Changing a user’s password into a random string of symbols so a hacker cannot read it if stolen.

**Context:** In System Security, these processes protect sensitive information during transmission and storage, ensuring data remains private and secure.

### 16.	End users
**Definition:** End users are specific people who will actually operate and interact with the software system on a daily basis.

**Example:** In a car-sharing system, the end users are the drivers booking cars and the clerks managing fleet schedules.

**Context:** Understanding end users is critical for HCI design, as the system must match their skills, needs, and work habits.

### 17.	Event
**Definition:** Event is a significant or noteworthy occurrence that takes place at a specific time and location, often triggering a system response.

**Example:** A customer clicks the "Confirm Booking" button, which acts as a trigger for the system to reserve a vehicle.

**Context:** In Systems Analysis, events are used to identify use cases by determining how the system must react to external or temporal changes.
 
### 18.	Extreme programming
**Definition:** Extreme programming is an Agile software development framework that focuses on high-quality code through constant feedback, simple designs, and frequent releases.

**Example:** A team uses "Pair Programming" and "Test-Driven Development" to ensure every line of code works before it is finished.

**Context:** In Project Management, Extreme Programing reduces the cost of changes by emphasizing technical excellence and continuous communication with the customer.

### 19.	HCI
**Definition:** Human Computer Interaction is a field of study focusing on the design and use of computer technology, specifically the interfaces between people and computers.

**Example:** Researching how a driver interacts with a car’s touchscreen to ensure it is not distracting while the vehicle moves.

**Context:** HCI principles guide designers to create user interfaces that are efficient, easy to learn, and reduce user errors.

### 20.	Integrity controls
**Definition:** Integrity controls are internal mechanisms built into a system to ensure that data is entered correctly and remains accurate and complete. 

**Example:** A system rejecting a "February 30" date entry or preventing a user from deleting a customer who has active orders.

**Context:** In System Design, these controls protect the database from human error or system glitches, maintaining "one version of the truth."

 
### 21.	Model
**Definition:** Model is a representation of a complex reality, used to understand, design, or document a system's structure and behavior.

**Example:** A blueprint for a house or a flowchart showing how a customer's order is processed by a computer.

**Context:** Analysts use models (like Class or Sequence diagrams) to communicate ideas clearly between business stakeholders and the technical development team.

### 22.	Object
**Definition:** An object is a specific "thing" or instance in a system that has its own identity, data values, and behaviors.

**Example:** If "Car" is a general category, "John’s Red Ford" is a specific object with its own license plate.

**Context:** In object-oriented analysis, objects are the basic building blocks that interact by sending messages to one another to perform tasks.

### 23.	Object-oriented design
**Definition:** Object-oriented design is a software design approach where a system is modeled as a collection of interacting objects that contain both data and behavior.

**Example:** Designing a "Car" object that has data like "Fuel Level" and actions like "Start Engine" or "Accelerate."

**Context:** Object oriented design uses principles like GRASP and SOLID to create flexible, reusable code that is easy to maintain and change.

 
### 24.	Pair programming
**Definition:** Pair programming is an Agile development technique where two programmers work together at one workstation to write and review code simultaneously.

**Example:** One developer acts as the "driver" typing the code, while the "navigator" reviews each line for errors and logic.

**Context:** In Scrum or XP methodologies, it improves code quality and team knowledge sharing, though it initially requires more man-hours.

### 25.	Perfect technology assumption
**Definition:** The perfect technology assumption is a principle used during analysis where you assume that the system's hardware and software will work perfectly without any failures.

**Example:** When designing a login process, you ignore the possibility of a forgotten password or a broken internet connection at first.

**Context:** This allows analysts to focus on the essential business requirements and user goals (the "what") before worrying about technical limitations (the "how").

### 26.	Project
**Definition:** a project is a temporary endeavor undertaken to create a unique product, service, or result within a specific timeframe and budget.

**Example:** Developing and launching a new mobile app for a car-sharing company over a period of six months.

**Context:** In systems development, projects are managed using a SDLC to ensure that business goals are met while managing risks and resources.

 
### 27.	Relational database
**Definition:** a relational database is a digital collection of data organized into predefined tables with rows and columns that are linked by shared keys.

**Example:** A system where a "Customers" table connects to an "Orders" table using a unique ID number for each person.

**Context:** Analysts design relational databases using Entity-Relationship Diagrams (ERDs) to plan storage, these ensure data integrity and minimize redundancy.

### 28.	Requirements
**Definition:** Requirements are the specific descriptions of the services a system must provide and the constraints under which it must operate.

**Example:** A car-sharing app must allow users to lock doors remotely and must load every screen in under two seconds.

**Context:** Analysts categorize these into functional (what it does) and non-functional (how it performs), often using the FURPS+ framework to ensure quality.

### 29.	Requirements determination
**Definition:** Requirements determination is the process of seeking, capturing, and consolidating the specific needs and constraints that a new system must satisfy.

**Example:** Interviewing a manager to learn that the new car-sharing app must generate monthly profit reports by Friday.

**Context:** This occurs during the Analysis phase and involves using techniques like interviews, questionnaires, and observation to define system scope.

 
### 30.	Scrum
**Definition:** Scrum is an Agile framework that uses short, fixed-length cycles called Sprints to deliver small portions of working software.

**Example:** A team meets daily for 15 minutes to discuss progress on building a new checkout feature for an app.

**Context:** Project Managers use Scrum to help teams handle changing requirements through constant feedback and defined roles like the Scrum Master.

### 31.	SDLC
**Definition:** System Development Life Cycle is a structured process used by teams to plan, create, test, and deploy high-quality information systems effectively.

**Example:** In the car-sharing project, the System Development Life Cycle follows a series of steps to move a project from a basic idea to a finished, working app.

**Context:** Analysts use the System Development Life Cycle to provide a framework of phases—like planning, analysis, design, and implementation—to ensure software meets business needs and budget.

### 32.	Security controls
**Definition:** Security controls are technical or administrative safeguards put in place to protect a system's data and resources from unauthorized access or damage.

**Example:** Requiring a "Strong Password" and "Two-Factor Authentication" (2FA) before a member can access their car-sharing account details.

**Context:** Analysts design these controls to ensure data integrity and privacy by preventing hackers from stealing sensitive information or disrupting services.

 
### 33.	Stakeholders
**Definition:** Stakeholders are any individual, group, or organization that has an interest in, or can be affected by, the success of a project.

**Example:** In the car-sharing project, stakeholders include the drivers, the software developers, the company owners, and even government regulators.

**Context:** In systems analysis, identifying all stakeholders ensures that everyone’s requirements are heard so the final system provides real business value.

### 34.	System
**Definition:** A system is a collection of interrelated components that function together as a single unit to achieve a specific set of goals.

**Example:** The car-sharing information system is a system made of website, mobile app, database, GPS hardware, and payment gateway working together to achieve the goal of providing members with seamless vehicle access.

**Context:** In Information Systems, this includes hardware, software, data, and people collaborating to process information and solve business problems.

### 35.	System Vision Document / Systems Development Methodology
**Definition:** System Vision Document is a brief document that defines the business's need, the proposed solution's features, and the expected benefits of the project.

**Example:** A two-page report explaining why a new car-sharing app is needed and how it will increase monthly reservations.

**Context:** In the Inception phase, it serves as a high-level guide to help stakeholders decide if the project is worth the investment.

### 36.	Systems Development Methodology
**Definition:** System Development Methodology is a standardized process or "road map" that provides specific guidelines and steps for every activity in system development.

**Example:** Using the Agile method to build software through small, quick updates rather than one giant release at the end.

**Context:** It ensures consistency and quality by telling the team exactly how to plan, analyze, design, and test the new system.

### 37.	Top-down versus bottom-up development
**Definition:** Two opposite strategies for building systems: starting with the main structure (Top-Down) or starting with individual components (Bottom-Up).

**Example:** In Top-Down, you design the main menu first; in Bottom-Up, you write the database connection code first.

**Context:** Systems analysts choose between these to manage complexity, ensuring either high-level logic or low-level technical functions work correctly first.

### 38.	Three-layer architecture
**Definition:** Three-layer architecture is a design pattern that organizes a system into three logical sections: the user interface, business logic, and data storage.

**Example:** A website where the browser shows the page, a server calculates prices, and a database stores the customer's info.

**Context:** In system design, this separation (UI, Domain, and Data layers) makes the software easier to maintain, update, and scale.

### 39.	UML
**Definition:** Unified Modeling Language is a standardized set of symbols and diagrams used to visualize, specify, and document the design of software systems.

**Example:** In the car-sharing project, drawing a diagram with boxes and arrows to show how "Customer" and "Order" objects interact in a system.

**Context:** It acts as a universal blueprint language, allowing analysts and developers to communicate complex system structures without writing code.

### 40.	Unified Process
**Definition:** Unified process is a software framework that builds systems in small, repeatable cycles while focusing on high-risk areas first.

**Example:** A team develops a banking app by first building the login security, then adding features like transfers later. 

**Context:** Unified process uses UML diagrams and four phases – Inception (define scope), Elaboration (identify requirements), Construction (build product), and Transition (move from system development to testing, training and deployment) – to guide teams through complex system development.

### 41.	Unit Testing
**Definition:** Unit Testing is the process of testing the smallest functional parts of an application, such as individual methods or classes, in isolation.

**Example:** A developer writes a short script to verify that a “Calculate Tax” function returns the correct decimal value.

**Context:** In system development, it ensures code quality early, making it easier to find bugs before integrating different system components.

### 42.	Usability Test
**Definition:** Usability Test is an evaluation method where real users attempt specific tasks to measure how easy and satisfying a system is to use.

**Example:** Watching a customer try to book a car in the new app to see if they get stuck or confused.

**Context:** In System Design (HCI), it identifies layout flaws and navigation issues, ensuring the final interface meets the needs of the end-user.

### 43.	Use case
**Definition:** Use case is a text-based or visual description of a specific way a user interacts with a system to achieve a goal.

**Example:** A customer uses an ATM to "Withdraw Cash," which involves entering a PIN, choosing an amount, and receiving money.

**Context:** In requirements gathering, use cases help analysts identify system boundaries and ensure all functional requirements of the business are met.

### 44.	Use case realization
**Definition:** Use case realization is the process of describing how a specific use case is implemented within the system using collaborating objects and software classes.

**Example:** Creating a sequence diagram that shows how "Customer," "Booking," and "Car" objects work together to complete a reservation.

**Context:** It bridges the gap between analysis (what the system does) and design (how it does it) using interaction diagrams.

### 45.	User goal technique
**Definition:** User goal technique is an approach to identify use cases by asking users what specific tasks they need the system to help them perform.

**Example:** An analyst asks a clerk, "What are the main things you do each day?" and identifies "Create New Order."

**Context:** It is a common requirements gathering method that ensures the system design focuses on supporting actual business processes and goals.

### 46.	User interface
**Definition:** User interface is the specific set of screens, buttons, and menus that allow a human to interact with a computer or software.

**Example:** The icons, search bar, and "Book Now" button you see on a mobile app when trying to rent a car.

**Context:** In System Design (HCI), the UI must be intuitive and consistent to ensure users can complete tasks efficiently and without errors.

 
# Section 2: Short-Answer Questions and Exercises

# Chapter 2 - Investigating System Requirements

## **1. List and briefly describe the five activites of systems analysis.** 
* Gather detailed information - meet with users to understand the business processes and needs 
* Define requirements document findings by building models such as use case diagram and class diagram 
* Prioritize requirements - Decide which requirements (such as use cases) should be done first 
* Develop user-interface dialogs work with the users to define exactly how they will use the system and what interactions with the system are required 
* Evaluate requirements with users  - ensure that the requirements are complete, accurate, and prioritized correctly 

## **2. What are three types of models?** 
Textual models, graphical models, and mathematical models 

## **3. What is the difference between functional requirements and nonfunctional requirements?** 
Functional requirements describe the business rules that must be supported by the new system, while non-functional requirements are the system characteristics such as speed, throughput, response time, and security.  Both are important. 

## **4. Describe the steps in preparing for, conducting, and following up an interview session.** 
Prepare for an interview by establishing the objective, determining the users and project team members, write questions, review preliminary materials, set up the interview time and location and tell everybody.  Conduct the interview by asking questions, looking for exception conditions and probing for good details.  Also take good notes, and document all the follow-up items.  Follow-up the interview by reviewing everybody's notes, building the models as necessary, document open issues, then follow-up with them.  Be sure to thank contributors. 

## **5. What are the benefits of doing vendor research during information-gathering activities?** 
It can inform the current team and users of new ideas and possibly more effective methods  The team can possibly find out about more current state-of-the-art solutions that vendors have created.  It may even be cheaper, faster, and more effective to purchase a solution instead of building. 

## **6. What types of stakeholders should you include in fact finding?** 
Both internal and external stakeholders.  Internal stakeholders would include operational people who work with the system and executive stakeholders who may receive executive reports, or depend on the success of the system. [cite: 486, 489] External stakeholders may include customers or partner organizations, who also receive information directly from the system.  At the executive level, external stakeholders may be investors or regulators. 

## **7. Describe the open-items list and then explain why it is important.** 
During fact finding activities, and in fact throughout all the project, some issues can be answered immediately, but others cannot be answered immediately.  Some questions may not be answered because more research may need to be done, or other items may need to be decided first, or the user procedure has not be finalized, etc.  Those items will need to be tracked so that they are not left out of the solution system.  The open-items list provides that tracking function by noting the item, assigning a responsible person, and tracking the completion of the open item. 

## **8. List and briefly describe the six information gathering techniques.** 
Information gathering techniques include 
* Interview users and stakeholders - the most effective for information gathering, but the most expensive 
* Distribute questionnaires  - good for finding overview or summary information from many people [cite: 500, 501]
* Review current system documentation - good for understanding current processes 
* Observe current business processes  - also good for understanding the user's processes and requirements [cite: 504, 505]
* Research vendor solutions good for generating new ideas and learning what already has been done 
* Collect user comments good for finding out about problems with current processes 

## **9. What is the purpose of an activity diagram?** 
One purpose of an activity diagram is to document current user workflows.  Activity diagrams are often called workflow diagrams.  They can be used to document a user procedure as he/she interacts with the computer system. 

## **10. Draw and explain the symbols used on an activity diagram.** 
See Figure 2-14. 
<img width="1190" height="688" alt="activity_diagram" src="https://github.com/user-attachments/assets/1532db43-a28a-4f2b-83f2-ef75c6a52586" />
---

### Problems and Exercises 

## **1. Provide an example of each of the three types of models that might apply to designing a car, a house, and an office building.** 
* **Car:**  Mathematical model might be a set of calculatations having to do with horse-power, torque and acceleration.  Graphical model might be a set of 3 dimensional drawings of the body style.  Textual model might be some written specification of the materials to be used. 
* **House:**  Mathematical model might be some calculations to deteremine angle of roof and types of materials needed.  Graphical would be a set of blueprints.  Descriptive textual model might be a description of the materials to be used. 
* **Office building:**  An office building might have all types of mathematical models of the stresses and earthquake requirements.  Graphical would be blueprints or even a 3 dimensional physical model.  Descriptive textual model could be of materials or steps in the construction process. 

## **2. One of the toughest problems in investigating system requirements is to make sure they are complete and comprehensive.**  **How would you ensure that you get all the right information during an interview session?** 
Answers should include the following points: 
* Ensure that all stakeholders are identified and included in the requirements definition activities. 
* Review every existing form and report to make sure that all information needs are understood. 
* Identify and understand every business activity.  Be sure that all business procedures have been discussed. 
* Ensure that all exception conditions have been identified and associated processing has been defined. 
* Maintain an open-items list and ensure that all items are resolved. 

## **3. One of the problems you will encounter during your investigation is "scope creep" (i.e., user requests for additional features and functions).**  **Scope creep happens because users sometimes have many unsolved problems and the system investigation may be the first time anybody has listened to their needs.**  **How do you keep the system from growing and including new functions that should not be part of the system?** 
This problem is really a project management issue.  The project manager should establish guidelines to control this problem.  One preventative method is to be sure that the initial scope definition is adequate and comprehensive.  A partial definition during the scoping activities will exacerbate the problem of scope creep. [cite: 542, 545] Even for Agile projects, the users and the project team should attempt to do a thorough job of identifying all of the functional requirements. 
An effective way to control scope creep is to establish a committee that consists of both project team members and user (or client) members.  All new additions to the scope of the system need to be approved by the committee.  Prior to approval, an estimate should be done to determine the criticality of the request and the impact on the project schedule.  The client and the users should participate in the decision so that it is a combined decision and not dictated by the project manager.  An additional technique is to begin a list of enhancements for the next version of the system.  Some requests can easily be deferred to a later version. 

## **4. What would you do if you got conflicting answers for the same procedure from two different people you interviewed?**  **What would you do if one was a clerical person and the other was the department manager?** 
The first thought would be to take the opinion of the department manager as the correct answer.  However, it is not uncommon for the department manager to be behind on some of the latest details of business procedures.  The best solution in this case is to get the two people together and let them discuss the differences until they both agree on the correct procedure.  The systems analyst should not make the decision as to which answer is correct, nor should he or she try to resolve the difference.  It is the users' responsibility to do so. 

## **5. You have been assigned to resolve several issues on the open-items list, and you are having a hard time getting policy decisions from the user contact.**  **How can you encourage the user to finalize these policies?** 
Delayed policy decisions impact the project schedule.  Sometimes the user does not understand the impact of delayed decisions.  Thus, the first approach should be to explain the negative impact that a given decision is having on the project.  If that doesn't work, then stronger measures can be taken, such suggesting that the project steering committee review the outstanding-items list.  Also, if the outstanding-items list indicates the length of time that items have been open, the analyst can assign or adjust the priority of those items that have become critical. 

## **6. In the running case of RMO, assume that you have set up an interview with the manager of the shipping department.**  **Your objective is to determine how shipping works and what the information requirements for the new system will be.**  **Make a list of questions-open ended and closed ended-that you would use.**  **Include any questions or techniques you would use to ensure you find out about the exceptions.** 
Three areas should be addressed in this answer: (1) closed-ended questions, (2) open- ended questions, and (3) questions related to exception conditions. 
Sample closed-ended questions: 
* What is the volume of shipments on an average day? 
* How does the volume vary across time? 
* How many employees are there in shipping? 

Sample open-ended questions: 
* What is the procedure for getting an order ready for shipment? 
* What forms are used? 
* How is the system updated when a shipment is sent? 
* How are back-orders handled? 
* How are returns handled? 
* What information is updated when a shipment is sent? 
* What reports does the system produce? 
* How are employee responsibilities divided among the various procedures? 

Sample exception condition questions: 
* What happens when items are not in stock for an order? 
* How do you handle errors in the inventory system and physical counts? 
* What happens when shipments are returned due to a bad address? 
* What do you do about lost shipments?  How are you notified? 

## **7. Develop an activity diagram based on the following narrative.**  **Note any ambiguities or questions that you have as you develop the model.**  **If you need to make assumptions, also note them.** 
The purchasing department handles purchase requests from other departments in the company.  People in the company who initiate the original purchase request are the "customers" of the purchasing department.  A case worker within the purchasing department receives the request and monitors it until it is ordered and received.  Case workers process requests for the purchase of products under $1,500, write a purchase order, and then send it to the approved vendor.  Purchase requests over $1,500 must first be sent out for bid from the vendor that supplies the product.  When the bids return, the case worker selects one bid and then writes a purchase order and sends it to the vendor. 

* In-house Customer 
    * Make purchase request 
* Purchasing Department 
    * Receive requests 
    * <1500? 
    * Yes -> Write purchase order [cite: 606, 612]
    * No -> Request bid [cite: 607, 608]
    * Select bid 
    * Write purchase order 
    * Send out bid 
* Vendar 
    * Develop bid 

## **8. Develop an activity diagram based on the following narrative.**  **Note any ambiguities or questions that you have as you develop the model.**  **If you need to make assumptions, also note them.** 
The shipping department receives all shipments on outstanding purchase orders.  When the clerk in the shipping department receives a shipment, he or she finds the outstanding purchase order for those items.  The clerk then sends multiple copies of the shipment packing slip.  One copy goes to Purchasing, and the department updates its records to indicate that the purchase order has been fulfilled.  Another copy goes to Accounting so a payment can be made.  A third copy goes to the requesting in- ouse customer so he or she can receive the shipment.  After payment is made, the accounting department sends a notification to Purchasing.  After the customer receives and accepts the goods, he or she sends notification to Purchasing.  When Purchasing receives these other verifications, it closes the purchase order as fulfilled and paid. 

* Shipping 
    * Receive shipment 
    * Find purchse order/copy 
* Purchasing 
    * Update purchse records 
    * Close purchase order 
* Accounting 
    * Make payment 
    * Send notification 
* In-house Customer 
    * Receive shipment 
    * Send notification 

## **9. Conduct a fact-finding interview with someone involved in a procedure that is used in a business or organization.**  **This person could be someone at the university, in a small business in your neighborhood, in the student volunteer office at the university, in a doctor's or dentist's office, or in a volunteer organization.**  **Identify a process that is done, such as keeping student records, customer records, or member records.**  **Make a list of questions and then conduct the interview.**  **Remember, your objective is to understand that procedure thoroughly (i.e., to become an expert on that single procedure).** 
Responses will vary.  Answers should include both closed-ended questions and open-ended questions.  Anwers might also include some questions to address exception conditions.  Answers to the questions can be written in text form or presented in an activity diagram. 

## **10. Using RMO and the CSMS as your guide, develop a list of all the procedures that may need to be researched.**  **You may want to think about the exercise in the context of your experience with such retailers as L.L. Bean, Lands' End, or Amazon.com.**  **Check out the Internet marketing done on the retailers' Web sites and then think about the underlying business procedures that are required to support those sales activities.**  **List the procedures and then describe your understanding of each.** 
Answers will vary, but a good set of procedures might include all of the use cases identified in Figure 3-11 of the next chapter.  Figure 3-11 has five subsystems, each with several use cases. 

---

## Solutions to End-of-Chapter Cases 

### Case Study: Jacob and Jacob, Inc. On-Line Trading System 

## **1. What is the best method for Edward to involve the brokers (users) in development of the new online trading system?**  **Should he use a questionnaire? Should he interview the brokers in each of the company's 30 offices, or would one or two brokers representing the entire group be better?**  **How can Edward ensure that the information about requirements is complete, yet not lose too much time doing so?** 
This situation is a viable candidate for a questionnaire.  The users are dispersed and probably diverse.  The questionnaire should focus on needs and preferences and can also help to establish which topics need further refinement.  It will probably cost too much to interview the brokers in all of the offices.  One way to select offices is to develop a set of characteristics that distinguish the various offices, and then to select a representative office from each set of similar offices.  If the answers to questions are very similar as interviews progress, it may be possible to abbreviate or shorten later visits to offices.  If there is a wide variation between needs and procedures, then additional interviews can be scheduled. 

## **2. Concerning customer input for the new system, how can Edward involve customers in the process?**  **How can he interest them in participating? What are some ways that Edward can be sure that the customers he does involve are representative of Jacob and Jacob's entire customer group?** 
This may also be a viable candidate for a questionnaire.  Statistically, sampling can guarantee that a large enough group can be studied, at least for the questionnaire.  The questionnaire should focus on the types of services and reports (statements) that the customer receives from the system.  If interviews are needed, some distinguishing characteristics should first be identified.  Then, representative samples of customers could be interviewed.  The cost of interviewing can also be controlled through the use of telephone interviews. 

## **3. As Edward considers what other stakeholders he should include, what are some criteria he should use?**  **Develop some guidelines to help him build a list of people to include.** 
Guidelines include: 
* Look at all the existing reports and destinations.  All of the destination persons will have an interest in the information provided by the system. 
* Look at all the different departments in the company to see if they currently receive or need to receive information from the new system. 
* Consider senior management to see if strategic information needs to be maintained and reported. 

---

### Running Cases: Community Board of Realtors 

## **1. Who are the stakeholders for the issues related to real estate in your community, and what are their main interests?** 
Answers will vary.  Usually for each state/county there are such organizations as: 
* A Division of Real Estate for the state.  Often in a state's department of commerce 
* A state Association of Realtors 
* A state Multiple Listing Service 
* Local Realtor Boards and Associations 
* Real Estate Offices and Agents 

## **2. What types of information does the board collect and make available to its members and to the community?** 
Answers will vary. 
* **Real Estate Offices:** 
    * Collects information about offices 
    * Collects information about agents and brokers 
    * Provides search and display of offices, agents, and brokers with addresses 
    * Provides services to real estate offices, such as advertising, training, banking information, lender information etc. 
* **Real Estate Listings:** 
    * Collects Information about property listings 
    * Collects Information about sales of property 
    * Provides seach and display about listed properties 
    * Provides maps of listed properties 

## **3. Research the real estate industry in at least two countries other than the United States.**  **For each of these countries, what are some of the cultural and legal issues that differ from those in the United States?**  **If you were working on support for an international real estate cooperative system, in what ways would the information collection activity process be complicated?** 
Answers will vary. 

---

### Running Cases: The Spring Breaks 'R' Us Travel Service 

## **1. Who are the stakeholders for SBRU? For each type of stakeholder, what aspects of the SBRU booking system are of particular interest?** 
* Students Student booking, Social Networking, Accounting and Finance 
* Resorts - Resort relations, Student Booking, Social Networking, Accounting and Finance 

## **2. What are the main functional requirements for the major subsystem areas (i.e., resort relations, student booking, accounting and finance, and social networking)?** 
* **Resort Relations:** 
    * Sign up with SBRU (get an account) 
    * Edit account information 
    * Create/enter resort information for SBRU website 
    * Post availability and prices of rooms/facilities 
    * View/edit room availability 
    * Retrieve completed reservations (View, report, or system interface) 
    * Submit damage report 
* **Student Booking:** 
    * Join SBRU/enter personal and financial information 
    * View resort information and availability of rooms/facilities 
    * Make a reservation (book a room/facility) 
    * Make a payment for reservation 
    * Cancel a reservation 
* **Accounting and Finance:** 
    * Process student payments 
    * Make refunds/correct payment errors 
    * Process payouts to resorts 
    * Edit/update/correct payouts 
* **Social Networking:** 
    * Set personal privacy settings (viewable by friends only, resort users, resort employees, etc.) 
    * Link up with "friends" 
    * Chat with friends 
    * Post comments on personal page 
    * Upload pictures to personal page 
    * Post comments on resort page 
    * Upload pictures to resort page 

## **3. Describe some usability requirements for students, booking interactions, and social networking interactions.** 
Students will be using all types of laptops, tablets (iPads), smartphones (iPhones) to make reservations, check status, and especially social networking.  Displays must be adaptable for all these types of computing devices.  Internet access will also be through ethernet, Wifi, and telephone access, with the varying speeds associated with each.  Hence images and text should be combined judiciously. 

## **4. Assuming that social networking at the resorts will require wireless communication and connection to the Internet, what are some reliability requirements that resorts might be asked to maintain?**  **What are some performance requirements? Is this a bigger issue because resorts are in international locations?** 
Social networking capabilities can be provided two ways, either through SBRUs central servers or locally through the resort's server.  For smaller resorts using SBRU servers - provide high-bandwidth access to the Internet.  Service level should be close to 100% availability with very wide bandwidth.  For those resorts with high usage of SBRU clients, they may want to provide local connectivity services.  This would require the same support as the smaller resorts, but also allow local chatting and communication ability.  For international resorts sometimes there are problems of connectivity, bandwidth, and reliability.  Resorts that want to join SBRU will require a minimum service level guarantee. 

## **5. What are some security requirements? Is there any reason why students in Europe, Asia, or other locations could not book rooms through SBRU?**  **What issues might be anticipated?** 
There are many security issues that must be addressed. 
1. Resorts have accounts with resort availability, reservations, accounts, and payments.  Different levels of security, data transmittal, and authorization is required.  Resort information only requires protection from hacking and defacing.  Reservations contain personal information and use HTTPS sites with TLS.  Consideration should be given to encryption.  Account and payment information most definitely requires TLS and encryption. 
2. Student information is also personal and private.  It will include payment and credit card information.  All financial information requires TLS and encryption. 
3. Social networking capabilities require protection of personal information and "friend" information. 
It SBRU should be able to support students from throughout the world. [cite: 774, 775] However, supporting international students may require web pages to be translated into other languages.  It will also require establishing relationships with international bank clearing houses to handle different currency systems. [cite: 777, 780]

## **6. To collect information on functional requirements for the social networking subsystem, what are some techniques that might be used?**  **Be specific and include some sample questions you might ask by using various techniques.** 
Assuming SBRU has an existing system, with existing student customers and desires to add social networking (thus an existing customer base does exist).  The social networking system should be heavily driven by student desires and requests.  Some possible ways to determine the functional requirements are: 
1. Review other social networking sites to see how they work. 
2. Send out questionnaires to existing customers on the desirability and possible use of social networking. 
3. On selected customers conduct telephone interviews to elaborate student desires. 
4. After a social networking capability has been added, then use ongoing evaluation questionnaires to refine the usability and functional effectiveness of the system.  (For example after a vacation give an incentive to collect student feedback on the resort, the booking system, and the social networking system) 

---

### Running Cases: On the Spot Courier Services 

## **1. Who are the stakeholders for On the Spot? How involved should On the Spot's customers be in system definition?**  **As the business grows, who else might be potential stakeholders and interested in system functions?** 
Stakeholders include: 
* Bill Wiley owner 
* Customers, usually businesses 
* Delivery persons 
* Warehouse staff 
Since Bill was the visionary for the business and the system, he will understand the needs of the system.  However, since he is letting business customers use the system to schedule packages, it would be a good idea to form a focus group of users who would be willing to help in requirements definition. [cite: 802, 803] Both the delivery persons and the warehouse staff will have suggestions on how to make their jobs easier.  They should be involved in requirements definition.  Bill's accountant should be involved to ensure that the system has sufficient financial information and controls. 

## **2. If you were commissioned to build a system for Bill, how would you determine the requirements?**  **Be specific in your answer. Make a list of the questions you need answered.** 
Since this is a small start-up company, the work procedures are very probably not efficient and probably are not scaleable.  Therefore, care should be taken not to build the system to only support these small scale work procedures.  Either of two approaches can be taken.  If Bill has a good vision of how he wants his business to function as it expands and grows, then interviewing Bill is a good starting place.  However, if Bill is still focusing on the current procedures, it may be a good idea to start by research commercial solutions from vendors.  The courier business is well established with many players and several commercial systems available.  Researching commercial solutions can expand the vision and view of how On The Spot can provide expanded services.  After researching commercial solutions, Bill should be interviewed to discuss the exact requirements for On The Spot.  Other stakeholders, as identified in Answer 1, should also be interviewed. 
Kinds of questions that need answers. 
* Services offered by On The Spot: Same-day delivery, Overnight delivery, Package pickup, sizes and rates 
* Customers: Cash only customers, account customers, new customers, billing 
* Scheduling of pickup: What is allowed, phone, web page, fax 
* Payment: Cash only, on web page, monthly account 
* Routes: How to organize, pickup and delivery, standard routes, ad hoc routes, multiple per day 
* Warehouse: Windows of processing, equipment required, what information is tracked 
* Package delivery: routes, tracking of packages, 

## **3. What technology and communication requirements do you see? What are the hardware requirements, and what kind of equipment will provide viable options to the system?**  **What would you recommend to Bill?** 
There appear to be four locations that will require interaction with the system. 
1. Customer Web pages where customers can list packages for pickup and also make payment. [cite: 829, 830] Regular customers may also print out their own labels. 
2. A work station where a clerk can handle phone requests for pickup. 
3. The warehouse where sorting occurs and tracking information is entered. 
4. The delivery trucks where pickups are noted, payments are accepted, labels are printed, deliveries are noted. [cite: 833, 834] These delivery trucks are mobile, and should have real time interaction with the home server. 

Equipment to support these functions might be: 
* A central server for the Web pages and for clerk entered pickup requests 
* Warehouse equipment, such as scanners, to note tracking information. 
* Mobile devices for the trucks.  Probably tablet computers Internet access and with scanning wand.  Also a mobile printer in the truck.  (If rates are by size, then they can be measured.  If rates are by weight, then set of scales is also needed.)  The mobile devices will need Internet access to communicate with the home office.  This can be provided either with cell phone technology and support, or with wide-area Wi-fi that is available in some cities.  Cell phone access to the Internet is more widespread. 

## **4. What are the primary functional requirements for the system as described so far in the case?** 
Functional requirements can be listed as use cases. 
* Add/update a customer 
* Request a pickup 
* Pickup a package 
* Deliver a package 
* Enter package tracking information 
* Track a package 
* Sort packages by route 
* Display a route (print, view) (list of pickups/deliveries) 
* Update a route (add pickups or deliveries real time) 
* Print monthly bills (print, electronic) 
* Accept payment 

---

### Running Cases: Sandia Medical Devices 

## **1. Who are RTGM's stakeholders? Should NMHS's patients be included in defining the system requirements? Why or why not?**  **Should RTGM interact with medical professionals other than physicians? Why or why not?** 
Stakeholders include: 
* Patients (users of the monitoring device and of the phone application) 
* Doctors (users of the information transmitted) 
* Other medical staff (those who enter patient medical information on phone app) 
* Medical equipment engineers (developers of the mobile monitoring equipment) 
* Technical staff (developers of the central server system, and the database) 
* Project team members (developers of the phone app) 

Patients should be included in defining system requirements for those areas that impact their use.  This would include the medical device (comfort, wearability, maintenance), and the phone app (installing, executing, user interface screen).  Other medical professionals other than physicians may need to be involved.  This would include medical staff that are involved in the design of the device (is it sensitive enough to read glucose levels, etc.).  Other medical professionals may want to research results for medical studies.  As such they will dictate what data should be captured. 

## **2. If you were the lead analyst for RTGM, how would you determine the requirements? Be specific in your answer.**  **List several questions you need answered.** 
Assuming we are limiting the fact finding and requirements definition to the smartphone app.  Questions for the medical equipment engineers would include: What are the specifications for the device - range, transmit parameters, data formats, occurance of transmittal, ranges of values for normal, abnormal, and dangerous?  What "test" capabilities does it have and how is it enabled?  Questions for the patient would be about the user interface for the phone app how readable, how understandable, signalling for normal and abnormal conditions, message format?  How usable are the screens for entering data, reading information, "testing" the equipment?  Questions for the medical professionals include information about the data formats to be sent, how often data should be sent, how to notify the system about abnormal, emergency situations, what other patient information needs to be captured? 

## **3. What are the primary functional requirements for the system as described so far in the case?** 
* Enter user (patient) information 
* Test monitoring device 
* Receive monitor-device data 
* Send monitoring data to server 
* Receive data from server 
* Alert patient (user) of abnormal situation 

## **4. Are the parameters for alerting patients and medical personnel the same for every patient?**  **Can they vary over time for the same patient? What are the implications for the system's functional requirements?** 
The case does not describe medical parameter variation by patient, but it may be assumed that depending on severity of illness, or weight of the patient, or sex may impact the acceptable and dangerous levels.  Hence entering patient may need to be done by trained medical personnel, or it needs to be accessed from the central server.  The case does not address if alerts can change over time.  But assuming that severity of illness will cause the parameters to change, patient information should be updated as appropriate.  The functional requirements may need to change to maintain or access from the server, history information to automatically update alert levels. 

## **5. Briefly describe some possible nonfunctional requirements for RTGM.** 
* **Usability** - Patients may be completely non-technical, may also be ill, may be disabled.  Usability needs to be assessed very carefully. 
* **Reliability** - Both the monitoring device and the phone app must be error free.  In addition, some type of fail safe capability should be built in.  For example if the monitoring device fails to communicate, the phone app should sound an alert.  The phone app should have a "normal operation" icon showing at all times (maybe a green light). 
* **Performance** - Probably not a problem for the phone app.  Performance, e.g. throughput will need to be evaluated for the central server and the telephone connectivity. [cite: 900, 901]
* **Security** - all medical information must conform to HIPAA requirements.  Transmittal of data over phone lines should be encrypted.  Care should taken so that multiple devices that are located near to each other do not interfere. 
The "+" requirements should also be address.  How easy is it to install the phone app?  How much memory does it require?  What kinds of devices is it compatible with?  How does it interface with the server application? 
# Chapter 3 - Identifying Use Stories and Use Case

## **1. What are the six activities of systems analysis, and which activity is discussed beginning with this chapter?** 
The five activities of systems analysis are: 

1.  Gather detailed information - begun in Chapter 2 with discussion of fact finding, stakeholders, interviewing, etc. 
2.  Define requirements - begun in this chapter by creating use cases 
3.  Prioritize requirements 
4.  Develop user-interface dialogs 
5.  Evaluate requirements with users 

## **2. What is a use case?** 
A use case is an activity that the system performs as a result of some event or action by a user. 

## **3. What are the two techniques used to identify use cases?** 
User goal technique and the event decomposition technique 

## **4. Describe the user goal technique for identifying use cases.** 
The user goal technique is done by interviewing a user (or user role) to see what their work "goals" or objectives are.  These are low level objectives to accomplish a piece of work or to complete a work procedure.  The system then must have use cases to support each user goal. 

## **5. What are some examples of users with different functional roles and at different operational levels?** 
Functional roles may be like department organization such as shipping, or sales, or accounting.  Different operational level may be like clerks, or middle management like supervisors, and then executives. 

## **6. What are some examples of use case names that correspond to your goals as a student going through the college registration process?** 
Be sure to use the verb-noun naming convention. 
Answers will vary: 

  * Find a course and section 
  * Register for a section of a course
  * Cancel a registration 

## **7. What is the overarching objective of asking users about their specific goals?** 
To discover and document every use case that the system must support. 

## **8. How many types of users can have the same user goals for using the system?** 
No real limit. Users from different departments can access the same use cases, e.g.  can have the same user goal for using the system. 

## **9. Describe the event decomposition technique for identifying use cases.** 
Look at all of the business processes that result in some type of business event.  The business events are triggers that require system processing, e.g. that require use cases. 

## **10. Why is the event decomposition technique considered more comprehensive than the user goal technique?** 
Event decomposition not only looks at user initiated events (the same as the user goal technique), but it also considers temporal events and state events.  Hence it is more comprehensive. 

## **11. What is an elementary business process (EBP)?** 
An EBP is a fundamental business process that may input data and receive information, but upon completion of the EBP the system has finished processing and can enter a quiescent state ready for a new event. 

## **12. Explain how the event decomposition technique helps identify use cases at the right level of analysis.** 
Since event decomposition depends on EBP, then it automatically arrives at the right level of analysis.  EBP, where the system has finished a complete transaction, is the same level that is required for a use case definition. 

## **13. What is an event?** 
Something that occurs at a specific time and place. It can be identified, and for purposes of systems analysis, the system must recognize it and capture some information from it or about it. 

## **14. What are the three types of events?** 

  * External event - usually from a user 
  * Temporal event - occurs at a point in time, or due to a time interval
  * State event a change of state or condition of some data within the system 

## **15. Define an external event and then give an example that applies to a checking account system.** 
An external event is something that occurs external to the system, and is trigger by a user action.  An example might be that a user makes a direct deposit to his/her account. 

## **16. Define a temporal event and then give an example that applies to a checking account system.** 
A temporal event is one that occurs at a point in time.  An example might be that at the end of the month interest (or monthly checking account fee) is calculated and credited to the account. 

## **17. What are system controls, and why are they not considered part of the users' functional requirements?** 
System controls are safety procedures or mechanisms that protect the system and the data.  They are not part of the users' functional requirements because the users normally do not initiate nor activate these controls.  They must exist above and overriding the external events. These controls are not normally part of the users' work processes. 

## **18. What is the perfect technology assumption?** 
It assumes that technology will work perfectly and that in the early stages of systems analysis we do not worry about such things as security, logging in, database backup, etc. Those issues are addressed after the initial functional requirements are determined. 

## **19. What are three examples of events that are system controls in a typical information system that should not be included as a use case because of the perfect technology assumption?** 

  * Backing up a database 
  * User logging onto the system 
  * Restoring the database 

## **20. What are the four operations that make up the CRUD acronym?** 

  * C= Create 
  * R= Read or Report (output) 
  * U= Update 
  * D= Delete 

## **21. What is the main purpose of using the CRUD technique?** 
The CRUD technique is a good way to validate the use cases that have been identified using the user goal and event decomposition techniques.  It is a double check to make sure the list of use cases covers all of the processes against the database.  When it is used as the primary method to find use cases, the 
use cases often do not track the business procedures very well. 

## **22. What is a brief use case description?** 
A one or two sentence description of the use case and what it accomplishes. 

## **23. What is UML?** 
UML stands for Unified Modeling Language, and it is the graphical modeling technique used to model object-oriented models.  It is the industry standard for OO modeling. 

## **24. What is the purpose of UML use case diagrams?** 
Use case diagrams provide a graphical view of use cases and the actors that invoke those use cases.  They provide a nice overview of use cases. They can organize use cases together in meaningful ways. 

## **25. What is another name for "actor" in UML, and how is it represented on a use case diagram?** 
An actor is also an external agent. In a use case diagram it is represented as a stick figure. 

## **26. What is the automation boundary on a use case diagram, and how is it represented?** 
The automation boundary is the boundary between the automated system, i.e. the application, and the external world, including the actors.  It is represented by a rectangular boundary box. 

## **27. How many actors can be related to a use case on a use case diagram?** 
As many as necessary. All those that use that particular use case. 

## **28. Why might a systems analyst draw many different use case diagrams when reviewing use cases with end users?** 
An analyst will draw different use case diagrams to organize the use cases in different ways to illustrate different subsystems, or departments, or work associations. 

## **29. What is the «includes relationship between two use cases?** 
The \<\<includes\>\> relationship is where one use case effectively uses the services of another use case.  It is as though one use case were embedded within another use case. 


### Problems and Exercises 

## **1. Review the external event checklist in Figure 3-3 and then think about a university course registration system.**  What is an example of an event of each type in the checklist?  Name each event by using the guidelines for naming an external event. 

  * External agent wants something - Student registers for a section of a course
  * External agent wants some information - Student searches for a course 
  * Data changed and needs to be updated - Instructor assigned to teach a course section
  * Management wants some information - Show enrollments for all courses in a department 

## **2. Review the temporal event checklist in Figure 3-4. Would a student grade report be an internal or external output?**  Would a class list for the instructor be an internal or external output?  What are some other internal and external outputs for a course registration system?  Using the guidelines for naming temporal events, what would you name the events that trigger these outputs? 

  * Grade report: External 
  * Class list: Internal 
  * Other external: Financial aid confirmation, graduation notice, employment confirmation letter
  * Other internal: Enrollment report and paycheck 
    To name the temporal events, include Time to produce with the output name, as well as the recipient.  For example, Time to produce grade report for students. Others are similar. 

## **3. Consider the following sequence of actions taken by a customer at a bank.**  Which action is the event the analyst should define for a bank account transaction-processing system?  (1) Kevin gets a check from Grandma for his birthday. (2) Kevin wants a car.  (3) Kevin decides to save his money. (4) Kevin goes to the bank. (5) Kevin waits in line.  (6) Kevin makes a deposit in his  savings account. (7) Kevin grabs the deposit receipt. (8) Kevin asks for a brochure on auto loans. 
The event for the bank is Customer makes a deposit.  Grabbing the receipt is just the way the response (receipt) is implemented.  Asking for a brochure on auto loans might be a separate event if the bank wants to remember that Kevin asked about it, or if they want to deduct one brochure in their brochure inventory system (if they have such a thing).  If the bank does not need to remember the event, then doing something by the system is not "required." 

## **4. Consider the perfect technology assumption, which states that use cases should be included during analysis only if the system would be required to respond under perfect conditions.**  Could any of the use cases listed for the RMO CSMS be eliminated based on this assumption? Explain.  Why are such use cases as Log on to the system and Back up the database required only under imperfect conditions? 
All of the events listed must be included because the system must do something each time one 
of the events occurs even if there is perfect technology.  User logs on to system and Time to back up the data are only required because users are not perfectly honest, and disk drives are prone to crash or corrupt data. 

## **5. Visit some Web sites of car manufacturers, such as Honda, BMW, Toyota, and Acura.**  Many of these sites have a use case that is typically named Build and price a car.  As a potential customer, you can select a car model, select features and options, and get the car's suggested price and list of specifications.  Write a brief use case description for this use case (see Figure 3-10). 

| Use case name: | Brief Description: |
|---|---|
| Build and price a car | Customer selects the model; the system displays the options; customer selects all the options; the system displays final result and suggested retail price. |



## **6. Again looking at a Web site for one of the car manufacturers, consider yourself a potential buyer and then identify all the use cases included on the site that correspond to your goals.** 
Answers will vary: 

  * View available models 
  * View available options 
  * View detailed specifications 
  * Compare vehicles 
  * Build and price a car 
  * Find a dealer 
  * Get a quote on specific model 

## **7. Set up a meeting with a librarian. During your meeting, ask the librarian to describe the situations that come up in the library to which the book checkout system needs to respond.**  List these external events. Now ask about points in time, or deadlines, that require the system to produce a statement, notice, report, or other output.  List these temporal events. Does it seem natural for the librarian to describe the system in this way?  List each event and then name the resulting use case. 
Answers will vary. 
External events might include 

  * Student checks out book 
  * Student returns book 
  * Student wants to check book availability 
    Temporal events might include 
  * End of month → Time to send overdue notice 
  * End of month → Time to produce monthly summary reports 
  * Book has not returned in a year → Time to declare book is lost 

## **8. Again considering the library, ask some students what their goals are in using the library system.**  Also ask some library employees about their goals in using the system.  Name these goals as use cases (verb-noun) and discuss whether student users have different goals than employee users. 
Answers will vary: 
Students may have goals of: 

  * Check book availability
  * Verify books checked out 
  * Check outstanding fines 
  * Reserve library materials 
    Librarians will have goals 
  * Patron wants to check out book 
  * Patron returns book 
  * Check book availability 
  * Reserver library materials
  * Add a new book to library
  * Remove a book from library
  * Update book information 

## **9. Visit a restaurant or the college food service to talk to a server (or talk with a friend who is a food server).**  Ask about the external events and temporal events, as you did in exercise 7. What are the events and resulting use cases for order processing at a restaurant? 
Answers will vary. External events might include Customer places order, Customer changes order, Kitchen returns completed order, Customer pays bill, and so on.  Temporal events might include Time to produce daily order totals report, Time to produce weekly sales analysis reports, and so on. 

## **10. Review the procedures for course registration at your university and then talk with the staff in advising, in registration, and in your major department.**  Think about the sequence that goes on over an entire semester. What are the events that students trigger?  What are the events that your own department triggers? What are the temporal events that result in information going to students?  What are the temporal events that result in information going to instructors or departments?  List all the events and the resulting use cases that should be included in the system. 
Answers will vary. Events might include Department schedules a class, Student enrolls in a class, Student changes schedule, Student drops a class, Instructor submits final grades, Time to generate grade report for students, Time to produce enrollment totals report for administration, and Time to produce class lists for faculty.  Note that the event names should indicate information about the external agent or actor involved.  Temporal events make the most sense if Time to is used at the beginning of the event name. 

## **11. Refer to the RMO CSMS Order Fulfillment subsystem shown in Figure 3-11.**  Draw a use case diagram that shows all actors and all use cases.  Use a drawing tool such as Microsoft Visio if it is available. 

  * Shipping 
  * Track shipment 
  * Marketing 
  * Ship items 
  * Manage shippers 
  * Provide sugggestion 
  * Rate and comment on product 
  * Customer 
  * Create backorder 
  * Create item return 
  * Management 
  * Look up order status 
  * Review suggestion 

## **12. Again for the Order Fulfillment subsystem, draw a use case diagram showing just the use cases for the shipping department in preparation for a meeting with them about the system requirements.**  Use a drawing tool such as Microsoft Visio if it is available. 

  * Track shipment 
  * Ship items 
  * Shipping 
  * Manage shippers 
  * Create backorder 
  * Create item 
  * return 
  * Look up order 
  * status 

## **13. Refer to the RMO CSMS Marketing subsystem shown in Figure 3-11.**  Draw a use case diagram that shows all actors and all use cases.  Use a drawing tool such as Microsoft Visio if it is available. 

  * Add/update product information 
  * Marketing 
  * Add/update promotion 
  * Add/update accessory package 
  * Merchandising 
  * Add/update business partner link 


## **14. Refer to the RMO CSMS Reporting subsystem shown in Figure 3-11.**  These reports were identified by asking users about temporal events, meaning points in time that require the system to produce information of value.  In most actual systems today, an actor is assigned responsibility for producing the reports or other outputs when they are due.  Recall that the actor is part of the system-the manual, non-automated part.  Thus, this is one way the "system" can be responsible for producing an output at a point in time.  In the future, more outputs will be produced automatically. Draw a use case diagram that shows the use cases and actors, as shown in Figure 3-11.  Use a drawing tool such as Microsoft Visio if it is available. 

  * Management 
  * Produce daily 
  * transaction summary 
  * report 
  * Produce sales history 
  * report 
  * Produce sales trends report 
  * Produce customer usage reeport 
  * Marketing 
  * Produce pormotion 
  * impact report 
  * Produce business 
  * partner activity report. 
  * Shipping 
  * Produce shipment history report 

### Case Study: The State Patrol Ticket-Processing System 

## **1. To what events must the ticket-processing system respond? List each event, the type of event, and the resulting use case.** 

| Event | Type | Use case |
|---|---|---|
| Officer submits a ticket | External | Record new ticket |
| Driver sends in fine payment | External | Record fine payment |
| Driver requests trial | External | Process trial request |
| Court sends verdict | External | Record verdict |
| Time to produce warrant request | Temporal | Produce warrant request |



## **2. Write a brief use case description for each use case.** 

| Use case | Description |
|---|---|
| Record new ticket | A clerk will enter the data recorded on a paper ticket which has been sent in from the officer. |
| Record fine payment | A clerk will enter the data from the payment sent in by the driver. |
| Process trial request | A clerk will enter the data from the trial request check-box and the envelop sent in by the driver. The system must generate a trial request and send it to the court system. It also produces a questionnaire for the driver. |
| Record verdict | The system records the verdict information sent by the court system. |
| Produce warrant request | After two weeks, the system produces a warrant request to be sent to the court. |


## **3. The portion of the database used with the ticket-processing system involves driver data, ticket data, officer data, and court data.**  Driver data, officer data, and court data are read by the system, and the ticket-processing system creates and updates ticket data.  In an integrated system like the ticket-processing system, some domain classes are created by and updated by other systems, as described in this case.  Create a table with systems down the rows and the four types of data (domain classes) across the columns.  Indicate C, R, U, or D for each domain class and each system. 

| Use Case/Class | Driver | Ticket | Officer | Court |
|---|---|---|---|---|
| TICKET SYSTEM <br> Record new ticket <br> Record fine payment <br> Process trial request <br> Record verdict <br> Produce warrant request <br> ACCIDENT SYSTEM | R <br><br><br><br><br><br> U <br><br> U | C <br><br> U <br><br> U <br><br> U <br><br> U <br><br> R | R | R |
| DRIVING RECORDS SYSTEM | RU | R | | |
| DRIVER'S LICENSE SYSTEM | CRU | | | |


### Running Cases: Community Board of Realtors 

## **1. To what events must the MLS system respond? List each event, the type of event, and the resulting use case.**  Be sure to consider all the use cases that would be needed to maintain the data in the MLS system, thinking in terms of the CRUD technique. 

| Event | Type | Use case |
|---|---|---|
| Real estate office submits new listing | External | Add new listing |
| Agent request listing information | External | Provide listing information |
| Time to produce multiple listing book | Temporal | Produce multiple listing book |
| Real estate office submits listing change request | External | Record listing change |
| New real estate office opens (implied) | External | Add new real estate office |
| Change real estate office information | External | Update real estate office info |
| New agent is hired (implied) | External | Add new real estate agent |
| Change agent information | External | Update real estate agent info |
| House is sold (from CRUD) | External | Delete listing |
| Real estate office closes (from CRUD) | External | Delete real estate office |
| Agent retires/quits (from CRUD) | External | Delete real estate agent |


## **2. Draw a use case diagram based on the actors and use cases you identified in question 1.** 

  * Real estate Office 
  * Add new listing 
  * Provide listing Information 
  * Record listing change 
  * Update real estate office info 
  * Add new real estate agent 
  * Update real estate agent info 
  * Delete listing 
  * Delete real estate agent 
  * Produce multiple listing book 
  * Agent 
  * Add new real estate office 
  * Management 
  * Delete real estate office 
    3-15 

## **3. Given the information available in the system, consider yourself a potential customer looking for real estate.**  List as many specific use cases you would like to see based on your specific goals. 
Answers will vary. 

  * Find real estate agent 
  * Search for property (by various criteria) 
  * View property details 
  * View property images (video or pictures) 
  * Request a property visit 
  * Send a message to real estate agent 

## **4. Draw a use case diagram for all the use cases for the potential customer you identified in question 3.** 

  * Buyer 
  * Find real estate agent 
  * Search for property 
  * View property details 
  * View property images 
  * Request property visit 
  * Send a message to agent 

### Running Cases: The Spring Breaks 'R' Us Travel Service 

## **1. Using the event decomposition technique for each event you identify in the description here, name the event, state the type of event, and name the resulting use case.**  Draw a use case diagram for these use cases. 

| Event (Booking subsystem) | Type | Use Case |
|---|---|---|
| Student browses resorts | External | Display resort information |
| Student browses resort packages | External | Display resort package information |
| Student group requests reservations | External | Book student group |
| Group addsdeletes /participants | External | Change group booking |
| Time to send out payment requirements | Temporal | Send payment notices |
| Check on booking details | External | Display booking details |
| Students check in | External | Update reservation info (hotel) |
| Students check out | External | Update reservation info (hotel) |



## **2. Consider the new Social Networking subsystem that SBRU is researching.**  Think in terms of the user goal technique to identify as many use cases as you can think of that you would like to have in the system.  SBRU is guessing you might want to join, send messages, and so forth, but there must be many interesting and useful things the system could do before, during, and after the trip.  Draw a use case diagram for these use cases. 
Answers will vary. A few possibilities 

  * Create an individual account (join)
  * Set preferences on account
  * Create a group account 
  * Assign admin rights to account
  * Search for a person or group 
  * Link up with a person or group 
  * Send a private message to a friend 
  * Chat with friend(s) 
  * Post a comment to a friend/group/photo 
  * Upload photo or video 
  * Tag photo 
  * Write/update vacation experience 
  * Create individual 
  * Set prerferences 
  * account 
  * Create group account 
  * Assign admin rights to group 
  * Search for person 
  * or group 
  * Individual 
  * Link with person or 
  * group 
  * Write vacation experience report 
  * Post a comment 
  * Chat with friend(s) 
  * Tag photo 
  * Send private message to friend 
  * Upload a photo or video 

### Running Cases: On the Spot Courier Services 

## **1. From this description as well as the information from Chapter 2, identify all the actors that will be using the system.** 

  * Bill Wiley (owner and manager) 
  * Delivery person 
  * Warehouse person 
  * Customer 

## **2. Using the actors that you identified in question 1, develop a list of use cases based on the user goal technique.**  Draw a use case diagram for these use cases. 
Note: This list is based on the use case descriptions so far.  See Chapter 9 for a more complete list of use cases based on narratives and CRUD analysis. 

  * Bill Wiley 
  * Enter a request for pickup 
  * Enter package pickup info 
  * Print label (may be part of pickup, or may request independently) 
  * Print bills 
  * Enter payments 
  * Delivery person 
  * Enter package pickup info 
  * Enter package delivery info 
  * Warehouse person 
  * Scan package 
  * Customer 
  * Sign for delivery 
  * Delivery person 
  * Sign for delivery 
  * Enter payments 
  * Enter request for pickup 
  * Enter package pickup info 
  * Bill 
  * Print label 
  * Enter package delivery info 
  * Print bills 
  * Scan package 
  * Warehouse person 
  * Customer 

  **3. Using the event decomposition technique for each event you identify in the description here, name the event, state the type of event, and name the resulting use case.**  Draw a use case diagram for these use cases. 

| Event | Type | Use case |
|---|---|---|
| Request package pickup | External | Enter pickup request info |
| Pickup package | External | Enter package info |
| Time to print bills | Temporal | Print customer bills |
| Receive payments | External | Enter payment info |
| Package scanned in warehouse | External | Scan package info |
| Deliver package | External | Enter delivery info |



It is interesting in this case the event decomposition yielded fewer use cases.  Individual use cases (Print label and Sign for delivery) are part of other business events and do not immediately show up. 

  * Bill 
  * Enter request for pickup 
  * Enter package info 
  * Print customer bills 
  * Delivery person 
  * Enter payment info 
  * Scan package info 
  * Warehouse person 
  * Enter delivery info 

### Running Cases: Sandia Medical Devices 

## **1. Identify all the actors that will use RTGM.** 

  * Patient 
  * Health-care provider (Physician) 
  * Nurse (physician assistant) 

## **2. Using the actors that you identified in question 1, develop a list of use cases based on the user goal technique.**  Draw a use case diagram for these use cases. 

  * Patient: 
  * View current data 
  * View trend data 
  * Enter text message 
  * Enter voice message 
  * Nurse: 
  * View current data 
  * View trend data 
  * Physician: 
  * View current data 
  * View trend data 
  * Record patient-specific activity 
  * Enter voice message 
  * Enter text data 
  * Nurse 
  * Patient 
  * View current data 
  * 00000 
  * View trend data 
  * Record patient-specific activity 
  * Physician 


## **3. Using the event decomposition technique for each event you identified in the description, name the event, state the type of event, and name the resulting use case.**  Draw a use case diagram for these use cases. 

| Event | Type | Use Case |
|---|---|---|
| Monitor records data value | Temporal | Record data value |
| Patient views current value | External | View data value |
| Patient views trend chart | External | View trend data |
| Nurse views current value | External | View data value |
| Nurse views trend chart | External | View trend data |
| Physician views current value | External | View data value |
| Physician views trend chart | External | View trend data |
| Physician responds to data | External | Record activity |
| Patient responds to data | External | Record message (voice or text) |


Note: Physician activity and patient activity may be quite different, hence we have identified separate use cases. 

  * Record data value 
  * Monitor 
  * Record message 
  * Nurse 
  * Patient 
  * View current data. 
  * View trend data 
  * Record patient-specific activity 
  * Physician 

  
# Chapter 4 – Domain Modeling 

### Review Questions 

## **1. What are the two key concepts—one from Chapter 3 and one from this chapter—that define functional requirements?** 
Use cases and Problem domain model (objects) 

## **2. What is the problem domain?** 
The area of the user's business need.  It is called “problem” because there is a need or something to be fixed. 
It is the domain, or the area of the business. 

## **3. What is a “thing” called in models used by traditional analysts and database analysts?** 
Data entity 

## **4. What is a “thing” called in newer approaches that use UML?** 
Object or object class 

## **5. What are two techniques for identifying things in the problem domain?** 
The Brainstorming technique and the Noun technique 

## **6. What are some examples of tangible things in the problem domain of a restaurant?** 
Meal, food item, menu... 

## **7. What are some sites or locations in the problem domain of a restaurant?** 
Restaurant location (for a chain), 

## **8. What are some roles played by people in the problem domain of a restaurant?** 
Customer, cook, waiter, supplier 

## **9. What are the main steps of the brainstorming technique?** 
1. Identify a group of users and their related use cases. 
2. Brainstorm with this group about all the things they need to keep track of with these use cases. 
3. Expand the list of things by asking related questions about locations, roles, etc. 
4. Return to step 1 with different groups of users. 
5. Combine and merge, eliminating duplicates. 

## **10. Explain why identifying nouns helps identify things in the problem domain?** 
Nouns are always “things.”  So finding all the nouns will find all the things (and more, so it needs to be refined). 

## **11. What are the main steps of the noun technique?** 
1. Using use cases, dialogs, conversations, etc. list all the nouns. 
2. Using information from existing systems, etc. list all the nouns. 
3. Refine the list by asking 3 questions for each noun – Include it?  Exclude it?  Research it more? 
4. Create a master list out of step 3. 
5. Review the list with users, stakeholders, and other team members. 

## **12. What is an attribute, an identifier or key, and a compound attribute?** 
An attribute is a a descriptor of a data entity (Object).  For example a Customer (object) has a name (attribute). 
So although attributes are also nouns, they are descriptor or qualifier nouns. 
An identifier or key is an attribute that can uniquely identify a particular object. 
A compound attribute is an attribute consists of “sub-attributes” or components, like address consists of street, city, state, postal code. 

## **13. What is an association, and what system development standard defines it?** 
An association is a relationship between things in the problem domain.  It is the term used by UML. 

## **14. How would you describe or name the association between a ship and a captain?** 
A captain is in charge of a ship.  or A captain directs a ship. 

## **15. What is the term used for association by traditional analysts and database analysts?** 
It is called a relationship. 

## **16. What is multiplicity, and what is the other term used by traditional analysts and database analysts?** 
It is a measure of the number of links in an association between an object in one class and the objects in another class. 
In traditional analysis it is called cardinality. 

## **17. What is the minimum multiplicity for the association that reads a customer places zero or more orders?** 
Zero 

## **18. What is the maximum multiplicity for the association that reads an order is placed by exactly one customer?** 
One 

## **19. What are some examples of multiplicity constraints?** 
Customer places one or more orders. 
Customer has only one account. 
Order is place by only one customer. 

## **20. What are the three types of associations, and which is the most commonly used?** 
Binary, unary, ternary.  Binary is most common. 

## **21. What are the three key parts of an entity relationship diagram (ERD)?** 
Data entities, relationships, and cardinality constraints. 

## **22. Sketch a simple ERD that shows a team has zero or more players and each player is on one and only one team.** 


## **23. Sketch a semantic net that shows two teams and five players based on your ERD.** 


## **24. What is a class, a domain class, and the key parts of a class diagram?** 
A class is a set of objects that are similar in nature had have the same “classification.” 
A domain class is a class in the problem domain. 
A class diagram has classes with attributes, associations, and multiplicity constraints. 

## **25. What does a domain model class diagram show about system requirements, and how is it different from an ERD?** 
A domain model shows the classes, i.e. the things, and their relationships and constraints. 
These are the specific system requirements that must be built into the database. 
The problem domain classes are the classes from the domain and are “persistent”, e.g.  they must be stored in a database. 
An ERD has different notation than a domain model.  An ERD is not as powerful as a domain model to model specific real world conditions. 

## **26. List appropriate UML class names by using the camelback notation for the following classes: graduate student, undergraduate major, course instructor, and final exam feedback.** 
GraduateStudent 
UndergraduateMajor 
CourseInstructor 
FinalExamFeedback 

## **27. List appropriate UML attribute names for the following attributes: student name, course grade, major name, and final exam quantity score.** 
studentName 
courseGrade 
majorName 
finalExamQuantityScore 

## **28. Draw a simple domain model class diagram for the example in question #22 where a team has zero or more players and each player is on one and only one team.** 


## **29. What is an association class? Extend the domain model class diagram for teams and players about to show a record of game statistics for each player in each game.** 
An association class is an association that needs to also be treated as a class. 
It is an association that requires attributes just like any class. 


## **30. In UML, what are three types of relationships found on a class diagram?** 
Regular association, Generalization/Specialization, Whole-part 

## **31. What is a generalization/specialization relationship, and what object-oriented terms does it illustrate?** 
A generalization/specialization is a hierarchical relationship between classes, where some classes are subsets (e.g. subclasses) of other classes. 

## **32. Compare/contrast superclass and subclass. Compare/contrasts abstract class and concrete class.** 
A superclass is higher in the relationship hierarchy and is a superset. 
A subclass is lower and is a subset of the superset. 
An abstract class is a class with no objects allowed. 
It serves only as a template for attributes so that subclasses, which are concrete classes, will have objects with inherited attributes. 

## **33. What is a whole-part relationship, and why does it show multiplicity?** 
A whole-part relationship in which a class is part of another class. 
It can have multiplicity constraints that allow multiple part-classes to belong to a single whole class. 

## **34. Compare/contrast aggregation with composition for a whole part relationship.** 
Aggregation is where the “part” objects may exist outside of the whole-part relationship. 
This often applies to physical devices that can exist prior to becoming part of the aggregate. 
Composition is where the parts do not exist outside of the whole-part relationship. 
An example might be a sale which is “composed” of sale items. 
The sale items do not exist separate and apart from the “sale” object. 

---

### Problems and Exercises 

## **1. Draw an entity-relationship diagram, including minimum and maximum cardinality, for the following: The system stores information about two things: cars and owners.** 
A car has attributes for make, model, and year. The owner has attributes for name and address. 
Assume that a car must be owned by one owner and an owner can own many cars, but an owner might not own any cars (perhaps she just sold them all, but you still want a record of her in the system). 


## **2. Draw a class diagram for the cars and owners described in exercise 1, but include subclasses for sports car, sedan, and minivan, with appropriate attributes.** 


## **3. Consider the domain model class diagram shown in Figure 4-16—the refined diagram showing course enrollment with an association class.** 
Does this model allow a student to enroll in more than one course section at a time? 
Does the model allow a course section to contain more than one student? 
Does the model allow a student to enroll in several sections of the same course and get a grade for each enrollment? 
Does the model store information about all grades earned by all students in all sections? 
More than one section? → Yes, he/she can enroll in zero to many 
Course section more than one student? → Yes, zero to many students in a section 
More than one section of same course? → Yes, there is no constraint to limit it 
Store of grades? → Yes it captures all student grades 

## **4. Again consider the domain model class diagram shown in Figure 4-16.** 
Add the following to the diagram and list any assumptions you had to make: A faculty member usually teaches many course sections, but some semesters, a faculty member may not teach any. 
Each course section must have at least one faculty member teaching it, but sometimes, faculty teams teach course sections. 
Furthermore, to make sure that all course sections are similar, one faculty member is assigned as course coordinator to oversee the course, and each faculty member can be the coordinator of many courses. 


## **5. If the domain model class diagram you drew in exercise 4 showed a many-to-many association between faculty member and course section, a further look at the association might reveal the need to store some additional information.** 
What might this information include? (Hint: Does the instructor have specific office hours for each course section? Do you give an instructor some sort of evaluation for each course section?) Expand the domain model class diagram to allow the system to store this additional information. 


## **6. Consider a system that needs to store information about computers in a computer lab at a university, such as the features and location of each computer.** 
What are the domain classes that might be included in a model? 
What are some of the associations among these classes? What are some of the attributes of each class? 
Draw an domain model class diagram for this system. 


## **7. Consider the domain model class diagram for the RMO CSMS Sales subsystem shown in Figure 4-21.** 
If an InStoreSale is created, how many attributes does it have? 
If an OnlineSale is created, how many attributes does it have? 
If an existing customer places a telephone order for one item, how many new objects are created overall for this transaction? 
Explain. 
InStoreSale has 6 + 3 = 9 attributes 
OnlineSale has 6 + 2 = 8 attributes 
For a telephone sale to an existing customer: 
TelephoneSale 
SaleItem 
Sale Trans 
No Sale is created because it is an abstract class. 

## **8. Again consider the domain model class diagram shown in Figure 4-21.** 
How many attributes does an active cart object have? Can an on-reserve cart contain cart items? Explain. 
An active cart object has 4 + 1 = 5 attributes 
OnReserveCart → Yes it can have CartItems.  An OnReserveCart is also an OnlineCart (It is a subset). 

## **9. A product item for RMO is not the same as an inventory item.** 
A product item is something like a men’s leather hunting jacket supplied by Leather ‘R’ Us. 
An inventory item is a specific size and color of the jacket—like a size medium brown leather hunting jacket. 
If RMO adds a new jacket to its catalog and six sizes and three colors are available in inventory, how many objects need to be added overall? 
Explain. 
New jacket requires 1 product item object and 3 * 6 = 18 inventory item objects.  Total of 19. 

## **10. Consider the domain model class diagram shown in Figure 4-24, which includes classes for college, department, and faculty members.** 
a. What kind of UML relationships are shown in the model? 
There are two binary association relationships 
b. How many attributes does a “faculty member” have? Which (if any) have been inherited from another class? 
FacultyMember has 5 attributes.  None inherited. 
c. If you add information about one college, one department, and four faculty members, how many objects do you add to the system? 
You add 6 objects. 
d. Can a faculty member work in more than one department at the same time? Explain. 
Using minimum and maximum multiplicity (cardinality), we can say that a faculty member can be in more than one department at the same time. 
In the real world, for example, one teacher can be part of both the computer science and computer information systems departments (a split appointment is possible). 
e. Can a faculty member work in two departments at the same time, where one department is in the college of business and the other department is in the college of arts and sciences? 
Explain. 
This is a good question to discuss in class. Draw a circle for a FacultyMember object (Billy Bob) and two circles for two separate Department objects (computer science and CIS). 
Connect the FacultyMember to each Department with two lines.  These lines associate one FacultyMember object with two Department objects. 
Next, draw two College objects (business and sciences). Connect computer science to sciences and CIS to business. 
Now it should be clear that a faculty member can be part of two departments at the same time. 

## **11. Review information about your own university. Create generalization/specialization hierarchies by using the domain model class diagram notation for (1) types of faculty, (2) types of students, (3) types of courses, (4) types of financial aid, and (5) types of housing.** 
Include attributes for the superclass and the subclasses in each case. 
Answers will vary. Types of faculty might include tenure track or lecturer, and tenure track might include tenured or non-tenured. 
Types of students might include undergraduate or graduate or, in some cases, day student (full time) or evening student (part time). 
Financial aid might include scholarships, loans, or work-study. Housing might include on campus or off campus. 
On campus might include dorm, suite, or apartment. Please note that a subclass is included only if there are additional attributes (or methods) for it that do not apply to the superclass. 
Also, the subclass and its attributes are only included if the system being described requires keeping track of the distinction. 
Should there be a subclass? Only if the system must remember the additional specific details it provides. 


## **12. Consider the classes involved when modeling a car and all its parts.** 
Draw a domain model class diagram that shows the whole-part relationships involved, including multiplicity. 
Which type of whole-part relationships are involved? 


## **13. Refer to the complete RMO CSMS domain model class diagram shown in Figure 4-23.** 
Based on that model and on the discussion of subsystems in Chapter 3, draw a domain model class diagram for the CSMS Marketing subsystem. 
Answers may vary depending on how they interpret the use cases. 


## **14. Again based on the complete RMO CSMS domain model class diagram shown in Figure 4-23, draw a domain model class diagram for the CSMS Order Fulfillment subsystem.** 
Answers may vary.  But this subsystem reads a lot of database classes, although it does not necessarily create or update all the data. 


---

### Solutions to End-of-Chapter Cases 

#### Case Study: Metropolitan car Service Bureau 

## **1. Draw a UML domain model class diagram for the system as described here.** 
Be as specific and accurate as possible, given the information provided. If needed information is not given, make realistic assumptions. 


## **2. Answer True or False to the following statements, which are based on the domain model.** 
You may want to draw a semantic net to help you think through the questions 
a. This domain model is for a single car dealer service department. 
False 
b. This domain model is for a single car manufacturer. 
False 
c. A vehicle can have service records with more than one dealer. 
True 
d. A dealer can service vehicles from more than one manufacturer. 
True 
e. Current mileage is recorded for service records and warranty service records. 
True 
f. An owner can have each of his or her cars serviced by a different dealer. 
True 
g. A warranty service for a car can include many parts. 
True 
h. A vehicle can be made by more than one manufacturer. 
False 

#### Running Cases: Community Board of Realtors 

## **1. Based on the information here, draw a domain model class diagram for the MLS system.** 
Be sure to consider what information needs to be included versus information that is not in the problem domain. 
For example, is detailed information about the owner, such as his employer or his credit history, required in the MLS system? 
Is that information required regarding a potential buyer? 


## **2. Draw a second domain model class diagram that adds the following specifications.** 
First, there are two types of listings: a listing for sale and a listing for lease. 
Additionally, a listing might include no structures, such as vacant land, or it might include more than one structure, such as a main house and a guest house, each with separate values for square footage, number of bedrooms, and number of bathrooms. 


Note: Here is an additional solution to Question 2 with a few more attributes added that are not requested by the case, but that will be helpful for later chapters. 
It adds some attributes to produce more reports. 


## **3. Draw a third domain model class diagram that assumes a listing might have multiple owners.** 
Additionally, a listing might be shared by two or more agents, and the percentage of the commission that each agent gets from the sale can be different for each agent. 


#### Running Cases: The Spring Breaks 'R' Us Travel Service 

## **1. For the Social Networking subsystem as described here, list the domain classes and their attributes that should be included in the Social Networking subsystem.** 
Be creative and add those you think should be included to make the system useful and appealing. 
See solution below 

## **2. Based on the domain classes you identified, draw a domain model class diagram showing domain classes with attributes and associations with multiplicity.** 


Note: Student solutions will vary.  “Comment” will probably not appear on student solutions. 
Note: Some students might try to make an accommodation class as an association class between Traveler and Resort, e.g.  on an association such as Traveler stays at Resort. 
However, this will only work if it is defined as CurrentAccommodation and only one is allowed in the database at a time. 
In other words, a given Traveler may stay at the same Resort on multiple dates. 
In that case an Accommodation association would not be unique by the keys TravelerID-ResortID, and the above solution is more general. 

#### Running Cases: On the Spot Courier Services 

## **1. Using the noun technique, read through this case and identify all the nouns that may be important for this system.** 
You may also find it helpful to read back through the case descriptions in the previous chapters. 
The noun technique yielded the following list. 
* pickup requests - class 
* package pickups – class ? 
* mobile phone - ? 
* packages - class 
* driver - class 
* warehouse - ? 
* warehouse employee – class ? 
* deliveries – class ? 
* desk – self: not important 
* delivery van - ? 
* business – self: not important 
* services – ? 
* customers – class 
* businesses – class 
* individuals – subclass 
* address – attribute 
* contact information – attribute 
* contact person – attribute 
* monthly statements – output 
* shipments – class ?  duplicate 
* bill month – attribute 
* cost – attribute 
* cash – attribute 
* running account – class 
* outstanding balances – attribute 
* payments – class 
* invoices – output 
* type of payment – attribute 
* amount – attribute 
* delivery request – class 
* delivery order – class ?  duplicate 
* pickup location – attribute 
* date and time – attribute 
* delivery order – class ?  duplicate 
* delivery person – duplicate 
* delivery to name – attribute 
* type of delivery – attribute 
* weight – attribute 
* names – duplicate 
* dateTimeStamp - attribute 
* delivery trip – class 

## **2. Once you have identified all the nouns, identify which are classes and which are attributes of these primary classes.** 
Begin constructing a class diagram based on the classes and attributes you have identified. 
Note: In the analysis, it was determined that dateTimeStamp was an attribute of package movements. 
However, no Movement noun was identified.  So we added a general class called “MovementEvent” to track package movements, such as pickups, deliveries, warehouse movements. 
Also a trip noun was not specifically mentioned but it was strongly implied by the driver delivering packages. 
“Delivery Trip” was included above, which has been added as RouteTrip since it handles both deliveries and pickups. 
See below for solution. 

## **3. Now that you have identified the classes, determine what the relationships should be among the classes.** 
Add multiplicity constraints, being especially cognizant of zero-to-many versus one-to-many differences. 
See below for solution. 

## **4. Finalize the class diagram, including all your classes, attributes, primary keys, relationships, and multiplicity constraints.** 
Note: With this domain model it becomes evident that the use cases identified in Chapter 3 are insufficient. 
A CRUD analysis will yield additional use cases. 
Note: DT means Date & Time, such as DTRequested. 


#### Running Cases: Sandia Medical Devices 

## **1. Modify the diagram (Figure 4-25) to incorporate the changes under consideration.** 
You may need to use association classes and generalization/specialization (inheritance). 


## **2. Are a set of abstract and concrete classes needed to represent variations among cell phones? Why or why not?** 
Answers will vary. 
Possibly to distinguish between different types of cell phones, a general abstract class and specialized concrete classes might be necessary. 

# Chapter 5 - Use Case Modeling

Systems Analysis and Design in a Changing World, sixth edition
5-1

# Chapter 5 - Extending the Requirements Models

## Solutions to End-of-Chapter Problems

### Review Questions

## **1. What are the models that describe use cases in more detail?**
Fully developed use case description, activity diagrams, and system sequence diagrams.

## **2. What two UML diagrams are used to model domain classes?**
Problem domain class diagram and state machine diagram.

## **3. Which part of a use case description can also be modeled by using an activity diagram?**
The "flow of activities" section.

## **4. Explain the difference between a use case and a scenario. Give a specific example of a use case with a few possible scenarios.**
A use case is the entire function or user goal or event. A scenario is one specific version or instance of that use case.
From RMO we have Create customer account as a use case. But we might have Create online Customer account and Create instore customer account and even Create phone customer account as different scenarios.

## **5. List the parts or compartments of a fully developed use case description.**

  * Use case name
  * Scenario
  * Triggering event
  * Brief description
  * Actors
  * Related use cases
  * Stakeholders
  * Preconditions
  * Postconditions
  * Flow of activities
  * Exception conditions

## **6. Compare/contrast precondition and postcondition.**
A precondition describes the "states" of data and the system that must exist before the use case can begin. For example to add an item to a shopping cart, the item must exist in the database.
A postcondition describes the states of data and the system that must exist after the use case completes. For example after Create a customer account use case, a customer account object (record) must exist.

-----

Systems Analysis and Design in a Changing World, sixth edition
5-2

## **7. Compare/contrast postcondition and exception condition.**
A post condition, as explained about describes states of the data and the system. An exception condition describes some non-normal situation in the processing, i.e. in the flow of activities, that must be handled in some way.

## **8. Compare/contrast business process and flow of activities for a use case. Explain how an activity diagram can be used to model both.**
A business process is larger than a use case. A business process might include various manual business procedures both before and after the "business event" that causes the use case to occur. However, an activity diagram is a powerful model to describe all types of sequences of tasks and activities. The various swimlanes can represent various users or user groups as well as system activities.

## **9. What is the purpose of an SSD? What symbols are used in an SSD?**
An SSD (system sequence diagram) is used to describe the messages that flow into and out of a system, i.e. between the system and the use case user.
The symbols include:

  * Stick figure for the actor
  * Box with object name for the system object
  * Vertical dashed lines for object lifelines
  * Horizontal arrows for messages
  * Horizontal dashed arrows for return data
  * Comment box for comments

## **10. What are the steps required to develop an SSD?**

1.  Identify the input messages (from the activity diagram)
2.  Describe the input message using the SSD message syntax
3.  Add message conditions such as looping or true/false conditions
4.  Add all output message data

## **11. Write a complete SSD message from the actor to the system, with the actor asking the system to begin the process for updating information about a specific product.**
`updateProductInformation (productID, updateInformation)`

## **12. What is the name of the sequence diagram symbol used to represent the extension of an object throughout the duration of a use case?**
Lifeline or object lifeline

## **13. What are the two ways to show a returned value on a sequence diagram?**
Either with a return value on the left hand side of the equal $(:=)$ sign, or with a return message shown by a dashed line and labeled with the return data.

-----

Systems Analysis and Design in a Changing World, sixth edition
5-3

## **14. What are two ways to show repetition on a sequence diagram?**
Either with an asterisk on the message label or a loop frame around the message(s).

## **15. What are the three types of frames used on a sequence diagram?**

  * Loop frame - repeat or loop the contents of the frame
  * Opt frame - send or do not send the message based on true/false condition
  * Alt frame - if-else alternative flows based on condition

## **16. What is the symbol for a true/false condition on a sequence diagram?**
A true/false condition is shown in brackets `[]`

## **17. What are the parameters of a message?**
The parameters represent the input data, i.e. the data that is being passed to the destination object.

## **18. List the primary steps for developing a SSD.**
Ooops, duplicate question. See question 10.

## **19. What is an object state?**
An object state is the state of being of an object, and is usually measured by a set of values. It is comparable to a status condition.

## **20. What is a state transition?**
A state transition is the movement of an object from one state to another state.

## **21. When considering requirements, states and state transitions are important for understanding which other diagram?**
States and Transitions are part of the state machine diagram for an object class. Therefore, they help to understand the objects in the class diagram.

## **22. What UML diagram is used to show the states and transitions for an object?**
States and Transitions are part of the state machine diagram, which describes the activity of the objects in an object class.

## **23. List the elements that make up a transition description. Which elements are optional?**

-----

Systems Analysis and Design in a Changing World, sixth edition
5-4

`Transition-name (parameters,...) [guard-condition]/action-expression`
Any of the three elements may be empty, i.e. are optional.

## **24. What is a composite state? What is it used for?**
A composite state is a high-level state in that it may have other states and transitions inside of it. It is used to represent concurrent states. For example, a printer may be in the "on" state, which is a composite state, and it may be "idle" which is an internal state within "on."

## **25. What is meant by the term path?**
A path is a sequence of states and transitions. It may be a complete path to describe an entire origin to destination path, or it may be a "snippet" of a path and only contain a few states and transitions.

## **26. What is the purpose of a guard-condition?**
A guard-condition determines whether or not a transition can fire. Usually first the trigger fires to notify the transition that it should execute, but before it begins execution, it tests to see if the guard-condition is true.

## **27. Identify the models explained in this chapter and their relationship to one another.**
The two main models for requirements are the Use case model, which identifies the use cases or the "processes," and the Domain model class diagram, which identifies the information or data for the system.
The Use case diagram is supported by Use Case Descriptions, Activity diagrams, and System Sequence diagrams.
The Domain model class diagram is supported by State machine diagrams.

-----

### Problems and Exercises

## **1. After reading the following narrative, do the following:**
i. Develop an activity diagram for each scenario.
ii. Complete a fully developed use case description for each scenario.

**Contractor Sale fully developed use case description:**

| Field | Description |
|---|---|
| **Use Case Name:** | Create a new sale |
| **Scenario:** | Create new sale to a contractor (on account sale) |
| **Triggering Event:** | Contractor wants to purchase items. |
| **Brief Description:** | A contractor wants to purchase items. The clerk rings up the items and then adds them to the contractor's account. |
| **Actors:** | Sales clerk |
| **Stakeholders:** | Sales clerk, Accounting department, Sales department |
| **Preconditions:** | Customer account must exist. Inventory items must exist. |
| **Postconditions:** | New sale is created. Sales line items are created and connected to the sale. Customer (contractor) account is updated. |
| **Flow of Activities:** | **Actor**<br>1. Clerk enters contractor ID.<br>2. Clerk enters each item.<br>3. Clerk indicates the end of the sale.<br>4. If contractor wants receipt, requests receipt.<br><br>**System**<br>1.1 System validates contractor account.<br>2.1 System finds item in inventory, finds price, adds to total.<br>3.1 System calculates total and adds to contractor account.<br>4.1 System prints receipt. |
| **Exception Conditions:** | 1.1 If contractor account is out of balance, treat this sale as a cash sale, or stop process and send contractor to accounting clerk.<br>2.1 If system has information missing, sales clerk calls manager and manually enters information.<br>3.1 If contractor account balance is over the limit, treat as cash sale, cancel, or send contractor to accounting clerk. |

-----

**Sale to public fully developed use case description:**

| Field | Description |
|---|---|
| **Use Case Name:** | Create a new sale |
| **Scenario:** | A new cash sale |
| **Triggering Event:** | Cash customer wants to purchase items. |
| **Brief Description:** | A cash customer wants to purchase items. The clerk enters the item ID, and the system creates a sales ticket. Customer pays with cash, check or credit card. |
| **Actors:** | Sales clerk |
| **Stakeholders:** | Sales clerk, Accounting department, Sales department |
| **Preconditions:** | Inventory items must exist. |
| **Postconditions:** | New sale is created. Sales line items are created and connected to the sale. Payment transaction is created. |
| **Flow of Activities:** | **Actor**<br>1. Clerk starts new cash sale.<br>2. Clerk enters each item.<br>3. Clerk indicates the end of the sale.<br>4. Clerk indicates type of payment and enters information.<br><br>**System**<br>2.1 System finds item in inventory, finds price, displays information, adds to total.<br>3.1 System calculates total.<br>4.1 System processes payment and creates payment transaction. |
| **Exception Conditions:** | 2.1 If system has information missing, sales clerk calls manager and manually enters information.<br>4.1 If customer credit card fails approval, require cash or cancel sale. |

-----

## **2. Based on the following narrative, develop either an activity diagram or a fully developed description for the use case of Add a new vehicle to an existing policy in a car insurance system.**

| Field | Description |
|---|---|
| **Use Case Name:** | Add a new vehicle to an existing policy |
| **Scenario:** | Telephone instance with customer and clerk |
| **Triggering Event:** | Customer buys a new vehicle. |
| **Brief Description:** | Customer provides car information, requests coverage with amounts, identifies drivers of the new car. System updates the policy. |
| **Actors:** | Customer service clerk |
| **Stakeholders:** | Customer, Customer service department |
| **Preconditions:** | Customer policy must exist and be up to date. Standard Vehicle control tables for this vehicle type and year must exist. StandardCoverage tables exist. |
| **Postconditions:** | New vehicle object created and connected to policy. Also connected to Standard Vehicle. New coverage objects created and connected to vehicle. Also connected to StandardCoverage. New driver (InsuredPerson) (if necessary) created and added to policy. Existing drivers and percentages updated. Policy updated with new premiums. |
| **Flow of Activities:** | **Actor**<br>1. Clerk enters customer information.<br>2. Clerk verifies policy is current.<br>3. Clerk enters car identification information.<br>4. Clerk enters each type of coverage customer requests, including deductibles and coverage amount.<br>5. Clerk indicates all coverages have been entered.<br>6. Clerk invokes Add new person use case if necessary.<br>7. Clerk changes driver percentages on this car and other cars.<br>8. Clerk indicates everything is complete.<br><br>**System**<br>1.1 System finds policy and displays details.<br>3.1 System validates that car has known standard.<br>4.1 System validates coverage requests.<br>5.1 System does combination validation on policy.<br>7.1 System updates driver information.<br>8.1 System updates policy, calculates new premium, prints new statement. |
| **Exception Conditions:** | 2.1 If policy is not current, clerk requests payment or collects necessary information.<br>3.1 If car type is not in system, clerk refers customer to underwriting to handle this situation.<br>4.1 If coverage requests are out of range, clerk asks customer for changed amount.<br>5.1 If some combination is invalid, return to step 4. |

-----

## **3. Given the following list of classes and associations for the previous car insurance system, list the preconditions and postconditions for the use case Add a new vehicle to an existing policy.**

| Field | Description |
|---|---|
| **Preconditions:** | Customer policy must exist and be up to date.<br>Standard Vehicle control tables for this vehicle type and year must exist.<br>StandardCoverage tables exist. |
| **Postconditions:** | New vehicle object created and connected to policy. Also connected to Standard Vehicle.<br>New coverage objects created and connected to vehicle. Also connected to StandardCoverage.<br>New driver (InsuredPerson) (if necessary) created and added to policy.<br>Existing drivers and percentages updated.<br>Policy updated with new premiums. |

-----

## **4. Develop an SSD based on the narrative and your activity diagram for problem 1.**

-----

## **5. Develop an SSD based on the narrative or your activity diagram for problem 2.**

-----

## **6. Review the cellular telephone state machine diagram shown in Figure 5-21 and then answer the following questions.**

  * **i. What happens to turn on the telephone?**
    A person has to switch it on with some external event.
  * **ii. What states does the telephone go into when it is turned on?**
    It goes into the composite state (unlabeled, but should have a label of ON). It goes into the Quiet state for one path. It can also go into Charged, Low Warning, or Discharged.
  * **iii. What are the three ways the telephone can be turned off?**
    SwitchOff, Quiet and Low Warning, or Discharged.
  * **iv. Can the telephone turn off in the middle of the Active (Talking) state?**
    Yes, if it is discharged, it leaves the Discharged nested state and the On composite state.
  * **v. How can the telephone get to the Active (Talking) state?**
    Through the origin state of connecting or by answering from the origin state of ringing.
  * **vi. Can the telephone be plugged in while someone is talking?**
    No. The state chart says it can only be plugged in from the Quiet state.
  * **vii. Can the telephone change battery states while someone is talking? Explain which movement is allowed and which isn't allowed.**
    It can go from Charged to Low Warning and from Low Warning to Discharged. However, because it cannot be plugged in while someone is talking, it cannot move back up from Discharged to Low Warning or Charged.
  * **viii. What states are concurrent with what other states? Make a two-column table showing the concurrent states.**

| Concurrent States | |
|---|---|
| Quiet, Dialing, Connecting, Ringing, Active, and Plugged In | Charged, Low Warning, Discharged |

-----

## **7. Based on the following description of a shipment made by Union Parcel Shipments, identify all the states and exit transitions and then develop a state machine diagram.**

| STATE | EXIT TRANSITION |
|---|---|
| active | delivered ( ), [misplaced two weeks] |
| in transit | onTruck ( ) |
| delivery pending | delivered ( ) |
| delivered | final ( ) |
| handedOver | delivered ( ) |
| misplaced | [for two weeks] |
| lost | final ( ) |

-----

## **8. Locate a company in your area that develops software. Consulting companies or companies with a large staff of information systems professionals tend to be more rigorous in their approach to systems development. Set up an interview. Determine the development approaches that the company uses...**
Answers will vary.

-----

### Solutions to End-of-Chapter Cases

#### Case Study: TheEyes Havelt.com Book Exchange

For this case, develop these diagrams:

## **1. A domain model class diagram**

## **2. A list of uses cases and a use case diagram**

## **3. A fully developed description for two use cases: Add a seller and Record a book order**

| Field | Description |
|---|---|
| **Use Case Name:** | Register |
| **Scenario:** | Register/add a new seller |
| **Triggering Event:** | A new seller wants to sell books. |
| **Brief Description:** | Seller decides he/she would like to list a book(s). Seller registers and receives a confirmation e-mail. |
| **Actors:** | Seller, E-mail server |
| **Preconditions:** | Seller must not exist in the system. Seller must have all information necessary to register. |
| **Postconditions:** | Seller has an account to list books. |
| **Flow of Activities:** | **Actor**<br>1. Seller connects to EyesHavelt.com and fills out registration form.<br>2. Seller submits registration form.<br><br>**System**<br>2.1 System notifies seller a confirmation e-mail will be sent.<br>2.2 System e-mails confirmation of registration to seller. |
| **Exception Conditions:** | 1.1 If the seller already exists in the system, the system sends prior login and password to e-mail address.<br>2.1 If the seller was removed from the system for bad transactions/credit, the system sends the seller an e-mail notifying the seller of the situation and no account is created. |

| Field | Description |
|---|---|
| **Use Case Name:** | Purchase a book |
| **Scenario:** | Purchase a book |
| **Triggering Event:** | A buyer decides to purchase a book from EyesHavelt.com. |
| **Brief Description:** | Customer searches for a book(s) on EyesHavelt.com. Customer selects from search results and adds a book(s) to the shopping cart. Customer then proceeds to checkout. If an account exists, the customer confirms purchase, and the system sends a confirmation e-mail to the customer. If an account doesn't exist, an account is created, the purchase is confirmed, and the confirmation e-mail is sent. |
| **Actors:** | Buyer, E-mail server, Seller |
| **Preconditions:** | Books and book information must exist in the system. |
| **Postconditions:** | Customer account must exist. Order must be placed. E-mail must be sent to seller. |
| **Flow of Activities:** | **Actor**<br>1. Buyer searches EyesHaveIt.com for a book(s).<br>2. Buyer selects a book(s) to purchase from search results.<br>3. Repeat steps 1 and 2 until all desired books are added to shopping cart.<br>4. Customer proceeds to checkout by selecting the Checkout button.<br>4a. If customer wishes to remove an item, he/she selects the item to be removed and then selects the Delete button.<br>4b. If buyer wishes to add an item, he/she selects the Continue Shopping button and proceeds to steps 1 and 2.<br>5. Buyer verifies displayed information.<br>6. If information is incorrect or buyer account does not exist, buyer updates displayed information or enters new information into the registration form.<br>7. Buyer confirms purchase.<br><br>**System**<br>1.1 Searches for all matches related to buyer's search criteria.<br>2.1 Creates shopping cart. Adds selected item(s) to the shopping cart.<br>4.1 Displays list of shopping cart items for verification.<br>4a.1 Displays list of shopping cart items with deleted items removed.<br>5.1 Displays buyer information.<br>6.1 Updates new buyer information for existing account.<br>6.2 Creates account for new buyer and sends confirmation.<br>7.1 Records order.<br>7.2 Sends e-mail to seller. |
| **Exception Conditions:** | 1.1 If book is sold out, buyer cannot add book to shopping cart.<br>2.1 If buyer account does not exist, a new account must be created. If buyer is rejected for new account based on credit, system sends buyer notification.<br>3.1 If payment is rejected, system notifies buyer and seller. |

## **4. An SSD for each of the two use cases in question 3**

-----

#### Running Cases: Community Board of Realtors

## **1. For the use case Add agent to real estate office, write a fully developed use case description and draw an SSD.**

| Field | Description |
|---|---|
| **Use case name:** | Add agent to real estate office |
| **Scenario:** | MLS clerk adding agent |
| **Triggering event:** | New agent hired in a real estate office |
| **Brief description:** | The correct real estate office is identified, and the new real estate agent information is entered into the system. |
| **Actors:** | MLS clerk |
| **Related use cases:** | Real estate office adds new agent (Web based version scenario) |
| **Stakeholders:** | Real estate office, real estate agent |
| **Preconditions:** | The real estate office must exist |
| **Postconditions:** | Real estate agent is created and associated with real estate office |
| **Flow of activities** | **Actor**<br>1. Find correct real estate office<br>2. Enter new agent information<br><br>**System**<br>1.1 Display real estate office information<br>2.1 Create new agent record, including with relationship to real estate office |
| **Exception conditions:** | 1.1 No real estate office found for requested id/name. Display not found message. |

## **2. For the use case Create new listing, write a fully developed use case description and draw an SSD.**

| Field | Description |
|---|---|
| **Use case name:** | Create a new listing |
| **Scenario:** | MLS clerk creates a new listing |
| **Triggering event:** | New property is put up for sale |
| **Brief description:** | The listing agent is identified and verified. The new property information is entered into the system, along with images etc. |
| **Actors:** | MLS clerk |
| **Related use cases:** | Real estate office/agent creates a new listing (Web version scenario) |
| **Stakeholders:** | Real estate office, Real estate agent, Property owner |
| **Preconditions:** | Real estate office must exist, Real estate agent must exist |
| **Postconditions:** | New listing must be created and associated with RE office and RE agent |
| **Flow of activities** | **Actor**<br>1. Find real estate agent<br>2. Enter new listing information<br><br>**System**<br>1.1 Display agent and office information<br>2.1 Create new property listing record, associated with agent. Display results. |
| **Exception conditions:** | 1.1 Agent information not found. Display not found message. |

## **3. Draw a state machine diagram showing the states and transitions for a Listing object.**

| State | Exit transition |
|---|---|
| For sale | Offer to buy |
| Sale pending | Close the sale |
| Sold | |
| Removed | Reinstate listing |

-----

#### Running Cases: The Spring Breaks 'R' Us Travel Service

## **1. For the use case Book a reservation, write a fully developed use case description and draw an SSD.**

| Field | Description |
|---|---|
| **Use case name:** | Book a reservation |
| **Scenario:** | Book a reservation online |
| **Triggering event:** | Student wants to make a reservation and initiates booking |
| **Brief description:** | Student searches or browses the resorts. He/she checks accommodations and availability. Then he/she makes a reservation for either a single person or a group. (Allow both individual and group reservations.) |
| **Actors:** | Student |
| **Related use cases:** | Create individual account (includes Traveler), Create group account, Add person to group (new use case previously undefined) |
| **Stakeholders:** | Student, Resort |
| **Preconditions:** | Traveler and Individual account must exist. Group must exist (for group reservation). Resort must exist. |
| **Postconditions:** | Reservation must be created and associated with Resort and Group/Traveler. Payment must be created and associated with IndividualAccount. |
| **Flow of activities** | **Actor**<br>1. Find a resort (search or browse)<br>2. Check availability of accommodations<br>3. Choose reservation type<br>4. Enter reservation details<br>5. Enter reservation payment information<br><br>**System**<br>1.1 Display resort and accommodation information<br>2.1 Display accommodation availability information<br>4.1 Make reservation<br>5.1 Verify individualInfo and paymentInfo. Create Payment Transaction for Reservation. Display confirmation. Send email confirmation. |
| **Exception conditions:** | 5.1 Payment transaction fails |

## **2. For the use case Add new resort, write a fully developed use case description and draw an SSD.**

| Field | Description |
|---|---|
| **Use case name:** | Add a new resort |
| **Scenario:** | Add a new resort |
| **Triggering event:** | A new resort contracts with SBRU to participate in the vacation program |
| **Brief description:** | A new resort is added with descriptive information. Information about the accommodations available to this program are entered. Information about the facilities available for activities in this program are entered |
| **Actors:** | SBRU clerk, Resort employee |
| **Stakeholders:** | SBRU management, Resort management |
| **Preconditions:** | Resort must not already exist |
| **Postconditions:** | Resort is created. Facilities are created and associated with the resort. Accommodations are created for this resort. |
| **Flow of activities** | **Actor**<br>1. Verify that the resort does not exist<br>2. Enter resort description<br>3. (loop) Enter facilities information<br>4. (loop) Enter accommodations information<br><br>**System**<br>1.1 Check database for resort information<br>2.1 Create resort record<br>3.1 Create facilities record<br>4.1 Create accommodations record |
| **Exception conditions:** | 1.1 Resort already exists |

## **3. Draw an activity diagram to show the flow of activities for the use case Add a new resort.**

## **4. Draw a state machine diagram showing the state and transitions for a Reservation object.**
| State | Exit transition |
|---|---|
| Open | Fulfill reservation, cancel reservation |
| Fulfilled | |
| Canceled | |

-----

#### Running Cases: On the Spot Courier Services

## **1. Based on this description, develop the following for the use case Request a package pickup and for the Web customer scenario: i. A fully developed use case description ii. An activity diagram iii. An SSD**

| Field | Description |
|---|---|
| **Use case name:** | Request a package pickup |
| **Scenario:** | Web customer requests package pickup |
| **Triggering event:** | Web customer has package(s) to be picked up and requests pickup |
| **Brief description:** | User enters package information (TO address, type of service, size/weight). System returns the cost, expected pickup time, and prints label |
| **Actors:** | Web customer |
| **Related use cases:** | Request package pickup (phone in), Enter package info (pickup package) |
| **Stakeholders:** | Bill, Customer, Delivery employee |
| **Preconditions:** | Customer and customer account must exist |
| **Postconditions:** | Pickup request is created and associated with Customer |
| **Flow of activities** | **Actor**<br>1. For each package<br>1.1 Enter type of service<br>1.2 Enter TO information<br>1.3 Enter package size/weight<br>1.4 Request label print<br><br>**System**<br>1.3.1 Display Cost<br>1.3.2 Display expected pickup time<br>1.3.3 Create Request record. Create Package record.<br>1.4.1 Print label |
| **Exception conditions:** | 1.4.1 Label cannot print |

## **2. Based on the same description, develop the following for the use case Pickup a package: i. A fully developed use case description ii. An activity diagram iii. System sequence diagram**

| Field | Description |
|---|---|
| **Use case name:** | Pickup a package (Enter package pickup information) |
| **Scenario:** | Delivery employee picks up package |
| **Triggering event:** | Delivery employee arrives at customer's location and picks up a package |
| **Brief description:** | Delivery employee verifies package with pickup request information, OR enters new package information. If cash customer, process payment. |
| **Actors:** | Driver |
| **Related use cases:** | Create customer and customer account, Accept payment, Scan package (movement) |
| **Stakeholders:** | Customer, Driver, Bill |
| **Preconditions:** | Customer should exist (else invoke Create customer use case) |
| **Postconditions:** | Create package record and connect with Customer, PickupRequest, Movement event |
| **Flow of activities** | **Actor**<br>1. If package has NO label, search for request by Customer name<br>2. If pickup request not found, enter new package info<br>3. Request print label<br>4. Scan package label<br>5. If cash customer, enter payment info<br><br>**System**<br>1.1 Access pickup info, update package. If no pickup info, display none.<br>2.1 Process new package info<br>3.1 Print label<br>4.1 Update pickup request, package. Create pickup MovementEvent<br>5.1 Process payment |
| **Exception conditions:** | 5.1 Invalid payment data |

## **3. Develop a state machine diagram describing all the possible status conditions for a Package object.**

| State | Exit transition |
|---|---|
| Pending pickup | packagePickup () |
| Picked up | arriveAtWarehouse () |
| At warehouse | loadedOnDeliveryTruck () |
| Out for delivery | delivered () |
| Delivered | none |
| Lost | found () |

-----

#### Running Cases: Sandia Medical Devices

Figure 5-22 shows a set of use cases for the patient and physician actors. Answer the following questions and/or complete the following exercises:

## **1. Which use cases include which other use cases? Modify the diagram to incorporate included relationships.**

## **2. Consider the use cases View/respond to alert and View history. Both actors share the latter, but each has a different version of the former. Why do the actors have different versions of the View/respond to alert use case? Would the diagram be incorrect if each actor had his own version of the View history use case? Why or why not?**

  * **View/respond to alert**: Even though the names are the same, the detail steps might be very different. It would be possible to make them different scenarios of the same use case. But making them separate use cases also works since the actors are different, the steps are different, and the system responses are different.
  * **View history**: View history does the same activities no matter who the actor is. In this case it would not make sense to have separate use cases since the processing steps, the data, the activities are both the same.

## **3. Develop an SSD for the View history use case. Assume that the system will automatically display the most recent glucose level, which is updated at five-minute intervals by default. Assume further that the user can ask the system to view glucose levels during a user-specified time period and that the levels can be displayed in tabular form or as a graph.**

# Chapter 6 - Foundation for System Design
# Chapter 6 – Essentials of Design and Design Activities

## Solutions to End-of-Chapter Problems

### Review Questions

## **1. What is the primary objective of systems design?**
The objective of systems design is to define, organize, and structure the components of the final solution system that will serve as the blueprint for construction.

## **2. What is the difference between systems analysis and systems design?**
The objective of systems analysis is to understand the needs and requirements, while the objective of design is to figure out the solution to those needs and requirements. Analysis is to understand the problem, design is to solve the problem. (and implementation is to build the solution.)

## **3. List the major elements that must be designed for a new software application.**
From figure 6-1 the elements that must be designed include:

  * The application software
  * The database
  * The user interface
  * The network and environment
  * The security and controls
  * The system interface

## **4. List the models that are used for systems analysis.**
Analysis models include

  * Class diagrams
  * Use case diagrams
  * System sequence diagrams
  * Use case descriptions
  * Activity diagrams
  * State machine diagrams

## **5. List the models that are used for systems design.**
Design models include

  * Package diagrams
  * Nodes and locations diagrams
  * Design class diagrams
  * Sequence diagrams
  * Database schema
  * User-interface layouts
  * Security and controls documents
  * Communication diagrams

## **6. What is the difference between user-interface design and system-interface design?**
User-interface design has to do with designing the screens (and reports) that the users see and interact with. Those require substantial user input and consideration for ease of use. System-interface design has to do with those automated interfaces with other systems and tends to consist of technical specifications.

## **7. On a project that uses iterations to develop the system, in which iteration does systems design begin? Explain why.**
Adaptive projects that use iteration include analysis, design, and implementation in every iteration. So design will begin within the first iteration. Depending on the desire result of the first iteration, the design activities may be primarily high-level structural design, but may also include low-level detailed program design.

## **8. What is the difference between architectural design and detail design?**
Architectural design is sometimes called high-level design. It has to do with the overall structure and configuration of the solution system, including network, applications, databases, and how they all work together. Detailed design focuses on the internal methods and logic of the classes or modules.

## **9. Designing the security and controls impacts the design of which other elements?**
Security and controls affects all other elements of the design and of the system. For example, security is required for the network. Security and controls are required to protect the database. Security and controls are required for the application software to protect from attacks as well as normal input errors.

## **10. Describe what is required for database design.**
The database consists of identifying those classes that are persistent (must exist between executions). It also includes defining attributes (fields), keys, indexes, and relationships between those classes. Finally storage and throughput requirements also impact the design.

## **11. What is a LAN? When would it be used in deploying a new system?**
A LAN is a local area network and is used to refer to the network of computers that exists within an organization at a localized site. Depending on the system, a LAN may be used to allow work stations to access data on a central database server within the local site. Also if the employees that work together must communicate together and “see” each others work, then a LAN configuration is required.

## **12. What is three-layer design?**
Many systems are designed with a view layer, which consists of the user interface, a program logic layer, which contains the business processing, and a data layer, which contains the database and data storage routines.

## **13. Describe the contents of each layer in three-layer design.**

  * View layer – user interface for inputs and outputs – screens and reports.
  * Logic layer – program logic to process business rules and processes
  * Data layer – stored data in the database and the routines to retrieve and update it

## **14. List the different types of client devices in a client/server architecture.**
Client devices range from desktop workstations to laptops and notebooks to small digital mobile devices such as smart phones. Client devices also would be printers that handle system outputs.

## **15. What is the difference between HTTPS and HTTP?**
HTTP is the Hypertext Transport Protocol to send and receive data over the Internet. HTTPS stands for Hypertext Transport Protocol Secure and adds a layer of security by encrypting the data being sent.

## **16. In the use of software over the Internet, what are the two main security issues that must be considered?**
One security issue is how to protect the data and the system residing on the server computer. In other words the server itself must be made secure. Another security issue is how to protect the data when it is in transit across the Internet. In other words the transmission of the data must also be done in a secure manner.

## **17. Describe the primary factors that affect throughput for Internet systems.**
Several factors affect throughput for Internet systems including:

  * Server computer power and capacity
  * Database capacity – both the computer and the database efficiency
  * The number of computers (e.g. server farms)
  * The location of the server computers (e.g. content delivery networks)
  * Internet connections and Internet capacity

## **18. List five issues that are important when considering an external hosting company.**
Important issues include:

  * Reliability of the hardware environment
  * Security of both hardware and software
  * Physical facilities including buildings, connection points, etc
  * Staff of the hosting company for expertise and ability to respond to problems
  * Growth of the hosted site and can the hosting company handle the growth

## **19. What is the difference between cloud computing and virtual servers?**
A virtual server environment provides the ability to grow and add servers easily for a client. However, the client is still involved in deciding the number and configuration of the virtual servers. Cloud computing, on the other hand, attempts to provide computing power much like a utility that the customer just uses as much computing capability only when he actually needs it.

## **20. Why do companies use colocation facilities?**
Colocation facilities provide several benefits to a company, which can be summarized by cost savings and increase reliability and security. Colocation companies have specially constructed sites to handle high volumes and which have highly reliable sites with backup equipment. Since the cost of these sites are shared by multiple clients a high level of service and reliability can be provided with less expense than if one company tried to do it all for itself.

## **21. Describe the issues to be considered when designing for multiple clients.**
When designing for multiple clients is the wide range of client devices that must be supported. This affects both software design and environment design.

## **22. What is a VPN? Why would a company use a VPN?**
A VPN is a virtual private network which is a private network but which uses the public Internet as the basic transport mechanism. It includes additional security levels to secure the transmission and use of the Internet. A company would use a VPN if it has information that must be very secure, but must be transmitted to remote locations where the company did not have its own private network lines.

-----

### Problems and Exercises

## **1. A financial corporation has desktop applications running in several different offices that are all supported by a centralized application bank of two computers. In addition, there is a centralized database, which requires three servers. Draw a network diagram representing this requirement.**
Note: The problem definition of “several different offices” implies a WAN requirement or an Internet requirement. We will represent the WAN or Internet by the cloud. Various types of client devices are illustrated to indicate that there are multiple types of devices that must be supported.

## **2. A sales organization has an Internet-based customer support system that needs to support every type of client device. The server configuration should be a normal layered application server and database server. Draw a network diagram representing this requirement.**

## **3. A medium-sized engineering firm has three separate engineering offices. In each office, a local LAN supports all the engineers in that office. Due to the requirement for collaboration among the offices, all the computers should be able to view and update the data from any of the three offices. In other words, the data storage server within each LAN should be accessible to all computers, no matter where they are located. Draw a network diagram that will support this configuration.**
Note: We show the LANs connected together with a router, or device that supports the LANs. Then the router devices are connected to the Internet to provide peer-to-peer connectivity possibly with a VPN.

## **4. A small start-up company has a Web-based customer sales system that is written by using PHP and JavaScript. The company is deciding whether to host the system on its own servers, contract with a hosting company for a virtual server, or go to Amazon’s cloud. Volumes are expected to be low at the beginning, and it is hard to predict a growth pattern, although there is potential for rapid growth. Decide which alternative the company should choose. Defend your decision by giving advantages and disadvantages of each solution based on the characteristics of the start-up company.**
Answers will vary. Here is one possible approach.

| Issue | Self hosted (Pros) | Self hosted (Cons) | Virtual Server (Pros) | Virtual Server (Cons) | Cloud (Pros) | Cloud (Cons) |
| --- | --- | --- | --- | --- | --- | --- |
| Building Setup and maintenance | | Expensive | Shared | | Included | |
| Connectivity to Internet | | Expensive | Shared | | Included | |
| Computer purchase | | Expensive | | Expensive | | |
| Computer maintenance | | Staffing | Available | | Included | |
| Network and OS maintenance | | Staffing | Available | Purchase | Included | |
| Scalability for future growth | | Difficult | Possible | Stepwise | Included | |
| Unpredictable growth | | Difficult | Possible | | Included | |
| Backup and recovery options | | Setup | Available | Expensive | | Expensive |
| Exact configuration | Yes | | Yes | | | Unknown |

Note: It appears that the cloud might be the best option. With the Virtual server second, and hosting it in-house as the least desirable.

## **5. Describe the differences between HTTPS and a VPN. What kinds of computing and networking situations are better suited to HTTPS? What kind of computing and networking situations are better suited to VPN?**
HTTPS adds secure transmission to Internet traffic. It establishes an encrypted connection between the client and the server. Then it transmits all data in encrypted form. This kind of connection works well for data that must be secure but that is also used by the general public. For example commercial sites where customers purchase items and pay for them with credit cards is a valid use of HTTPS. It is available to everyone and provides a fairly secure method of transmission.

VPN adds another layer of security on top of HTTPS. VPN also requires personalized software and/or hardware to add this additional encryption and protection. Therefore VPN is best used for Private networks where each end of the network is controlled by the same organization. VPN is often used by national security groups such as FBI or military. Corporations also use VPN on internal systems. Computers at both ends of the transmission are owned and controlled by the organization.

## **6. Find four separate hosting providers and compare their offerings, including prices. Put your answer in a table showing the results of your research.**
Answers will vary and will change over time as offerings change.
Note: Students will find that hosting websites is a two-tiered market. There is one tier for small sites for individuals. The prices for this type of hosting is usually only a few dollars a month. The hosted website shares a computer usually with dozens of other websites on the same connection and same computer. The second tier is for higher volumes and more robust computing environments. This type of hosting usually begins at the low end of $100 to $200 per month. The difference is the level of service provided and the bandwidth allocated to support higher volumes.

## **7. Compare screen size, resolution, and other important display characteristics of five popular Internet-enabled smart phones. Which would you rate as the best? Defend your answer.**
Answers will vary. Answers will change over time as technology improves. Answers should have a table of size, resolution, colors – students may also want to consider apps for streaming and viewing video, messages. Also possible voice activation and voice interface. The focus should be on user interface issues as well as computability issues.

## **8. Research the issues related to supporting a very large database that must be distributed across multiple servers. Write a list of the issues that need to be addressed and the alternative solutions for a distributed and partitioned database where (a) all servers are colocated in the same data center and (b) the servers are located in separate data centers.**
Answers will vary. Issues might include:

  * How to partition the database (horizontally or vertically)
  * How to synchronize the data
  * How to backup the data
  * How to balance workloads
  * Federated databases (some students might discover this issue)

-----

## Solutions to End-of-Chapter Cases

### Case Study: County Sheriff Mobile System for Communications (CSMSC)

**Your assignment: Recommend a communication and network solution for the county sheriff’s department. It can be any combination of Internet, VPN, Wi-Fi , telephone, and satellite communication. The applications can be custom built, with device-specific or HTML-based user interfaces. Although HTML tends to be more versatile, it has drawbacks regarding security; display can also be an issue on devices that don’t have browser support. As always, the budget is tight, so your solution should be as economical as possible. Develop a network diagram that depicts your proposed solution. Also, explain your solution and justify your design.**

Answers will vary with many valid solutions. The objective of this case is to get the students thinking about solutions rather than developing one particular solution.
Note: Although this case allows for the use of the public Internet via VPN as well as 3G or 4G cell phone solutions, almost all law enforcement agencies in the US have their own radio and wireless transmission systems including transmission towers. This solution shows a private law enforcement system.

### Running Cases: Community Board of Realtors

**The Community Board of Realtors’ Multiple Listing Service (MLS) will be a Web-based application with extensions to allow wireless smart phone interaction between the agents and their customers. Review the functional and nonfunctional requirements you have developed for previous chapters. Then, for each of the six design activities discussed in this chapter, list some specific tasks to design the environment, application architecture and software, user interfaces, system interfaces, database, and system controls and security. You may want to refer back to the Tradeshow System discussed in Chapter 1 for some design specifics.**

  * **Design the environment:** The environment is basically a client/server architecture. The application software will run under a Web server and the database will be directly supported. Design tasks will consist of defining the server and hosting requirements.
  * **Design application architecture and software:** As mentioned the application is a three-layer design consisting of the database, the application logic, and the user interface. Design will follow the normal design steps of specifying the code structure and the methods. Since the client will consist of browser based display on many different types of devices, the code will have to discern what to send depending on the type of client device. Tasks will include creating use case descriptions, sequence diagrams, and other application models.
  * **Design the user interface:** The user interface will be one of the more difficult portions of this system. Listing information can include text, images, and even possible videos. To be able to have meaningful display of all three types on desktops, laptops, and mobile devices some care will need to be given in designing the user interface. Tasks will include design sessions with some users for each type of device. Perhaps even some trial prototypes will need to be built to test the effectiveness of different screen layouts.
  * **Design system interfaces:** It does not appear that there are extensive system interfaces for this application other than the printed reports. Report design should also involve user input on the best way to print multiple listing books and brochures.
  * **Design the database:** Design of the database will require defining the various indexes and searching options. Other tasks include defining the attribute characteristics and foreign keys.
  * **Design system controls and security:** The primary concern with security in this system is to protect the listing data as it resides on the server. The server, the database, the applications must all be protected against hacking and defacing. Output data is created for the general public so it is not private or confidential at that point. Design tasks will be to integrate secure data input, update, and protection.

### Running Cases: The Spring Breaks 'R' Us Travel Service

**Let us say that the SBRU information system includes four subsystems: Resort relations, Student booking, Accounting and finance, and Social networking. The first three are purely Web applications, so access to those will be through an Internet connection to a Web server at the SBRU home office. The Social networking subsystem has built-in chat capabilities. It relies on Internet access for the students, as students compare notes before they book their travel reservations and as they chat while traveling. To function properly, the system obviously requires a wireless network at each resort during the trip. SBRU isn’t responsible for installing or maintaining the resort wireless network; they only plan to provide some design specifications and guidelines to each resort. The resort will be responsible for connecting to the Internet and for providing a secure wireless environment for the students.**

## **1. Design the environment for the SBRU information system by drawing a network diagram. Include what might be necessary to support online chatting capabilities.**

## **2. Considering that everything is designed to operate through the Internet with browsers or smart phones, how simple does this architecture appear to be? Can you see why Web and smart phone applications are so appealing?**
This is a simple three-layer client/server configuration. The complexity of communicating with client devices only required definition of HTML pages for the user interface. Even the chat capability fits into the same configuration.

## **3. What aspect of design becomes extremely important to protect the integrity of the system?**
Answers can vary. Integrity can refer to both the security of the system and to the robustness of being available for use at all times. Probably the weakest link will be the access points in the various hotels and resorts.

### Running Cases: On the Spot Courier Services

## **1. Make a list of the equipment that Bill should purchase to support his new system. Include all equipment that will be needed for the home office, the drivers, and at Bill’s residence. Identify and describe actual equipment that can be purchased today. Estimate the cost of the equipment.**
Answers will vary. Especially as technology changes over time. This is one possible configuration. Also note this is for a beginning configuration as the business grows, Bill may want to go with a hosted server.

| Location | Equipment | Cost |
| --- | --- | --- |
| Home office/Warehouse | Application/Database server – $3,000<br>Backup/Mirror Server - $2,000<br>Uninterrupted power supply (2) – $1,000<br>Wireless Router (2) – $500<br>Hand-held scanning devices (4) – $1,000<br>Printers (2) – $1,000<br>Desktop workstation with extra monitor $1,000 | $9,500.00 |
| Trucks/drivers (per each driver) | Tablet computer with stylus & telephony – $500<br>Portable label printer – $500 | $1,000.00 |
| Bill home | Wireless router – $100<br>Laptop computer with extra monitor – $700 | $800.00 |

## **2. Describe any special software that may be needed. The software engineer is developing the application software (package scheduling and processing, accounting, etc.), but no special software is required for connecting the devices or communications between them.**
Additional software includes:

  * Mirroring software (between servers)
  * Software to capture signatures on the tablet

## **3. Develop a network diagram showing how all the equipment will be connected. Identify Internet connections, VPNs, and telephony links as appropriate.**
Answers will vary as technology changes.
There are two possible places that On-The-Spot might want to emply VPN capabilities. Bill can connect his home office with the warehouse server using a VPN. In that way, anything he wanted to do on his office server would be fully securt. The other place where On-the-Spot might want to consider VPN is with the truck drivers and their mobile devices. However, the data being transmitted to and from the trucks is not extremely confidential. It consists primarily of delivery and pickup requests. There most sensitive data is probable payment data for cash customers. However, those kinds of payment transactions from customers are most often sent with purely HTTPS security.

### Running Cases: Sandia Medical Devices

**Answer these questions in light of HIPPA requirements:**

**Does HIPAA apply to the RTGM system? Why or why not?**
It would appear that HIPAA regulations do apply to the RTGM system. The system maintains personal health related information about the patient, hence it must comply. It also transmits detailed monitoring results over public links and therefore should encrypt the data that is being sent.

**How should the system ensure data security during transmission between a patient’s mobile device(s) and servers?**
Since the data is being sent over telephone links, it is only as secure as cellular telephone signals. Someone could possibly receive those transmissions by finding the correct frequency. Therefore, the data itself should be encrypted before being sent. Hence Sandia will need to provide, and patients will need to install encrypted SMS to receive their text message alerts. Sending the glucose monitoring results should also be sent securely and encrypted.

**Consider the data storage issues related to a patient’s mobile device and the possible ramifications if the device is lost or stolen. What measures should be taken to protect the data against unauthorized access?**
This is an interesting problem. Most patients will not want to have to enter a password or a pin every time they need to access their alert messages or to activate the transmission of monitoring data. It is not clear how much responsibility rests on the patient (to keep his/her phone secure), and how much responsibility rests on Sandia (to require a password or pin to activate). The data itself could be encrypted on the smart phone, but of course, the application is able to decrypt it to access it. Perhaps a middle ground might be to require a pin when the smartphone is turned on, or once each day.

**Consider the issues related to health care professionals accessing server data by using workstations and mobile devices within a health care facility. How will the system meet its duty to record and examine access to ePHI? If a health care professional uses a mobile device outside a health care facility, what protections must be applied to the device and/or any data stored within it or transmitted to it?**
Requirements for health care professionals can be more stringent to access secure ePHI data. Each health care person can be required to enter ID and password to access the data within the facility on workstations or laptop computing devices. Mobile devices can also require a login process in order for the professional to access the data. And the data should be encrypted when it is transmitted. Something as simple as a 4 digit pin for mobile devices is not too burdensome, yet still provides a level of security.
All access to the data should also be logged so that Sandia knows who has access and who has accessed the data. The system will maintain login information for authorized users. (See Chapter 12 for more details.)

**Consider the issues related to wired and wireless data transmission between servers and workstations within a health care facility. What security duties, if any, apply to transmissions containing ePHI? Does your answer change if the servers are hosted by a third-party provider?**
Security of wired and wireless data transmission and hosted servers requires first that the servers are hosted in a secure environment and second that all data, stored and transmitted be encrypted. Encryption of local data is easier because the access program maintains the encryption key. (Hence the program itself must be kept physically secure.) Transmitted data is more complex because the encryption must be dynamic due to the remote nature of mobile devices and distributed computers.
The solution will need to be the same whether the servers are hosted in house or with a third-party provider. The physical facilities and access to the servers themselves must be in a HIPAA secure facility.

# Chapter 7 - Defining the System Architecture

# Chapter 8 - Designing the User Interface
Systems Analysis and Design in a Changing World, sixth edition
8-1

# Chapter 8 - Approaches to System Development

## Solutions to End-of-Chapter Problems

### Review Questions

## **1. What is a project?**
As defined in Chapter 1, a project is a planned undertaking, with a beginning and end, that produces a well-defined result or product.

## **2. What is the range of sizes of an information system development project?**
Some system development projects are very large, requiring thousands of hours of work by many people and spanning several calendar years. Many smaller projects still require several months to deploy.

## **3. What is the system development life cycle (SDLC)?**
SDLC is the term used to describe the process and methodology for developing, deploying, and maintaining a software system. A particular SDLC will include a description of the methods, the tools, techniques, models, and project management processes that are used in the development of a new system. It is called a life cycle because it can cover the entire life of a system from initial idea to deployment to ongoing maintenance.

## **4. What characteristics of a project call for a predictive approach to the SDLC?**
Predictive: Projects are well understood technology is well known; user requirements are well known; development methodology is well known; project team is experienced and familiar with the system; and there are few known risks.

## **5. What characteristics of a project call for an adaptive approach to the SDLC?**
Adaptive: Projects are not well understood-technology is new or unfamiliar; requirements are not very clear; team is not experienced with the type of system or methodology.

## **6. What are the seven phases of the traditional predictive SDLC?**

1.  Project initiation
2.  Project planning
3.  Analysis
4.  Design
5.  Implementation (programming)
6.  Deployment
7.  Support

-----

Systems Analysis and Design in a Changing World, sixth edition
8-2

## **7. What are the objectives of the support phase?**
The objective of the support activities is to keep the system running productively during the years following its initial deployment. Three major activities occur during support:

  * Maintaining the system
  * Enhancing the system
  * Supporting the users

## **8. Explain how the waterfall model of the SDLC controls the changes that occur during a project.**
The pure waterfall attempts to specify completely the requirements during the analysis phase, and then tries to "freeze" those requirements so that things do not change. Another solution is to have a modified waterfall so that additional analysis (i.e. specifying new requirements) can be done as the project progresses. However, neither situation is well suited to handle big changes during the life of a project.

## **9. Explain the advantages of having the phases of a predictive SDLC overlap.**
As indicated in Question 8, having overlap allows the project to handle ongoing analysis and requirements definition even after design and programming have begun. Another advantage is that the development team can work more efficiently by doing design and even programming on those requirements and specifications that are being worked on (i.e. in analysis).

## **10. What organizing concept is included in all adaptive SDLCs?**
Adaptive SDLCs are all oriented to being able to handle changing requirements during the life of the project. All include iterations as the method to be able to integrate newly discovered requirements into the project work.

## **11. What is considered the first adaptive SDLC? Sketch it.**
The Spiral model was one of the very first adaptive SDLCs. (Sketch see Figure 8-5)

## **12. For an adaptive SDLC, explain what goes on during each iteration.**
Each iteration is like a mini-project. Withing each iteration, the activities related to the phases of the predictive SDLC occur, e.g. planning, analysis, design, implementation, and deployment.

## **13. The SDLC used in this text is based on what adaptive SDLC?**
The SDLC used in the this text is a simplification of and variation on the Unified Process (UP), which is a well known and well accepted formal iterative approach.

-----

Systems Analysis and Design in a Changing World, sixth edition
8-3

## **14. What are the core processes in the SDLC used in this book, and what traditional predictive SDLC phase corresponds to each process?**

1.  Identify the problem and obtain approval - Initiation Phase
2.  Plan and monitor the project - Planning Phase
3.  Discover and understand details - Analysis Phase
4.  Design system components - Design Phase
5.  Build, test, and integrate system components - Implementation Phase
6.  Complete system tests and deploy the solution - Deployment Phase

## **15. What is the iterative approach that involves completing and deploying part of an application over a few iterations and then completing and deploying another part of that application after a few more iterations?**
This is usually referred to as incremental development. A variation of incremental development that builds the entire structure at first is called a walking skeleton.

## **16. Why do adaptive SDLCs not explicitly include the support phase?**
Support does not fit into an "iteration" project model. Hence, the Support Phase is either treated as separate follow-on projects, or it reverts back to the predictive model and becomes a Support Phase.

## **17. What are the three activities of the support phase?**
Three major activities occur during support:

  * Maintaining the system
  * Enhancing the system
  * Supporting the users

## **18. What is a popular support technique used to answer users' questions and help them increase productivity?**
One way to support users is to provide a "help desk" type of capability. A help desk is a standard place, with procedures and staff, to provide both technical and application support for users.

## **19. What is a system development methodology?**
A methodology is more than just a method. It is an entire set of guidelines and procedures to develop a new system. Included in the components of a methodology would be what modeling approach to use, what tools, what techniques to do analysis and design and programming. A methodology provides the guidelines for the entire development process.

-----

Systems Analysis and Design in a Changing World, sixth edition
8-4

## **20. What are some examples of models included in a methodology?**
In a systems development methodology there would be graphical models, such as class diagrams and use case diagrams. There would also be descriptive models such as use case descriptions. There are also models associated with the management of the project such as Gantt chart or NPV spreadsheet. (See Fig 8-9)

## **21. What are some examples of techniques included in a methodology?**
Techniques have to do with completing specific tasks or activities. Examples might be how to model use cases, or how to develop a class diagram. User-interface design uses techniques such as story boards. Other techniques might be how to interview users etc. (See Fig 8-11)

## **22. What are some examples of tools included in a methodology?**
Tools might include drawing tools, such as Microsoft Visio, or an Integrated Development Tool (IDE), such as Struts, Eclipse, or Netbeans. Testing tools are also often used for program tests. (See Fig 8-10)

## **23. What are the two approaches to software construction and modeling?**
The two primary approaches to software construction are the Structured Approach (sometimes called the Traditional approach), and the Object-oriented Approach.

## **24. What are the basic characteristics of the traditional approach?**
The traditional approach is Structured development. Its basic approach was to break a problem into smaller components and write programs a set of modules in a hierarchical structure. By dividing a solution into these smaller modules, developers could focus on one thing at a time, which was easier to write programs and to maintain systems.

## **25. What are the basic characteristics of the object-oriented approach?**
All processes and data can be thought of as "objects." A program consists of interacting objects that work together by sending messages to each other and executing internal functions (methods).

## **26. What are the three main structured techniques?**
The structured approach includes:

  * Structured programming - one entry, one exit point; sequence, iteration, decision
  * Structured analysis - DFDs, flowcharts; flows of data across processes and agents
  * Structured design - Structure charts; boss modules call submodules

-----

Systems Analysis and Design in a Changing World, sixth edition
8-5

## **27. What are three diagrams created by the structured approach?**
The three primary diagrams are the:

  * Data flow diagram
  * Structure chart
  * Entity Relationship diagram (ER)

## **28. What are the main object-oriented techniques?**

  * Object oriented analysis - OOA
  * Object oriented design - OOD
  * Object oriented programming - OOP

## **29. What is Agile development?**
Agile development is a philosophy and set of guidelines for developing information systems in an unknown, rapidly changing environment, and consists of a statement of core philosophy and a set of values or guidelines for how to build models.

## **30. What are the four "values" reflected in Agile development?**
The four basic values of the core philosophy are:

  * Value responding to change over following a plan
  * Value individuals and interactions over processes and tools
  * Value working software over comprehensive documentation
  * Value customer collaboration over contract negotiation

## **31. What is Agile modeling (AM)?**
Agile modeling is a guiding philosophy about modeling. Only models that are necessary to move the project forward and that are really needed for the development of the software.

## **32. What are the 11 Agile modeling principles?**
The 11 Agile modeling principles are:

1.  Develop software as your primary goal.
2.  Enable the next effort as your secondary goal.
3.  Minimize your modeling activity-few and simple.
4.  Embrace change, and change incrementally.
5.  Model with a purpose.
6.  Build multiple models.
7.  Build high-quality models and get feedback rapidly.
8.  Focus on content rather than representation.
9.  Learn from each other with open communication.
10. Know your models and how to use them.
11. Adapt to specific project needs.

-----

Systems Analysis and Design in a Changing World, sixth edition
8-6

### Problems and Exercises

## **1. Write a one-page paper that distinguishes among the fundamental purposes of the analysis phase, the design phase, and the implementation phase of the traditional predictive SDLC.**
Answers will vary. For analysis, the primary focus is on discovery and understanding. The purpose is to understand at a detailed level the needs of the users. This can be based on existing systems and procedures or based purely on the desired business processes. The focus should not be on the solution system but instead on understanding the business need.
For design, the focus changes from understanding to thinking about a viable solution. The purpose of design is to synthesize or develop a solution. The two layers of design are the architecture layer and the detailed module layer. At the architecture layer, the purpose is to think of the entire solution system and how it is structured. At the detailed design layer, the purpose is to think about the individual modules or classes and define the details of the executable code.
For implementation, the focus is on building a robust system. The activities of this phase are oriented towards taking the design and building a high quality working system. Also included in this phase are the support or ancillary activities needed to train users, convert data, and fine-tune the working environment.

## **2. Describe an information system project that might have three subsystems. Discuss how three iterations might be used for the project.**
An iteration is a min-project in that it often takes a smaller component, or subsystem of a larger system, does analysis, design, and implementation within the iteration. So if there are three subsystems, AND if they are small enough, each subsystem might be done in a single iteration. (Larger subsystems might require multiple iterations each.) Another approach might to verify that the more complex or risky parts of the system are handled within the first iteration. Some work should be done within each subsystem for each iteration because doing so reduces schedule dependencies.

## **3. Why might it make sense to teach analysis and design phases and activities sequentially, like a waterfall, even though iterations are, in practice, used in nearly all development projects?**
Usually analysis and design and implementation are taught separately, as though in a waterfall project because the knowledge and skills for each is a separate topic. It is also valid to teach them in a waterfall fashion because within each iteration of an adaptive project a modified waterfall mini-project often occurs. Also teaching analysis and design sequentially like a waterfall helps to organize the course and helps to explain the specific work that is done in each SDLC phase. Teaching an iteration approach first can confuse the work that is done in analysis and design.

-----

Systems Analysis and Design in a Changing World, sixth edition
8-7

## **4. List some of the models that architects create to show different aspects of a house they are designing. Explain why several models are needed.**
Answers will vary. Blue prints show floor plan, front and rear elevation, roof framing plan, plumbing layout, electrical layout, foundation, and placement of house on lot. A scale 3D model shows what the house looks like. Mathematical calculations define stresses and forces affecting the roof or walls. Each model "abstracts" or highlights certain aspects of the house. No one model can contain everything needed. All models must fit together to define a house. Example models might include:

  * Floor plan layouts
  * Wiring diagrams
  * Plumbing diagrams
  * Detailed materials diagrams
  * Detailed blueprint diagrams
  * Landscaping diagrams
    Different models are included to be able to explain and specify the various aspects of the home. Obviously the plumbing diagram does no good for the electrician.

## **5. What models might an automotive designer use to show different aspects of a car?**
Answers will vary. Again, graphical models show what the car looks likes from different views, and there are many calculations and specifications for the different car components. Some look like the car, and some, like engineering models, are schematic diagrams or tables of specifications. Some models might include:

  * Body frame specifications
  * Electrical wiring diagram
  * Fuel flow specification model
  * Suspension specification model
  * Braking system specification
  * Body specifications
  * Accessory option specifications
  * Engine specifications
  * Exhaust specifications

## **6. Sketch and write a description of the layout of your room at home. Are both the sketch and the written description considered models of your room? Which is more accurate? More detailed? Which would be easier to follow by someone unfamiliar with your room?**
Answers will vary. Yes, both are models. They might be equally accurate and detailed, or one could be more accurate and/or detailed than the other. The sketch would be easier to follow for people, hence the use of graphical models in system development.

-----

Systems Analysis and Design in a Changing World, sixth edition
8-8

## **7. Describe a technique you use to help you complete the activity "Get to class on time." What are some of the tools you use with this technique?**
Answers will vary. A technique is a strategy for completing an activity. So a strategy for getting to class on time might include setting the alarm, getting to bed early, checking the class schedule each night, checking the bus schedule over breakfast, and so on. The tools in this example are the alarm, the class schedule, and the bus schedule.

## **8. Describe a technique you use to make sure you get assignments done on time. What are some of the tools you use with this technique?**
Answers will vary. The technique might include reading assignments right away, getting started early, making sure you have the materials needed ahead of time, checking with instructor as soon as you have a question about the assignment, using the appropriate computer tools to complete the assignment, making a backup copy of your work as you go, and getting to class on time the day the assignment is due. Tools might include the assignment, a calendar, e-mail, phone, computer tools used to create the assignment (word processor, spreadsheet), and online access to order materials needed.

## **9. What are some other techniques you use to help you complete activities in your life?**
Answers will vary, probably widely. Career selection techniques, job search techniques, spouse selection techniques, house buying techniques, job survival techniques, health maintenance techniques, retirement planning techniques, and grief coping techniques.

## **10. There are at least two approaches to the SDLC, two approaches to software construction and modeling, and a long list of techniques and models. Discuss the following reasons for this diversity of approaches: The field is young; the technology changes quickly; different organizations have different needs; there are many types of systems; developers have widely different backgrounds.**
Answers will vary. All of the listed reasons are valid in some ways. No one approach or technique is appropriate for all system projects. We need to be able to select the approach and the techniques that are right for the problem at hand.
The field is young: Even though it may not appear so to many young developers, information systems and software development is rather young. (Compared to other disciplines such as accounting or engineering or manufacturing.) In a young field there is always a lot of experimentation and change to discover better ways to do work.
The technology changes quickly: The technology in both hardware and software tools changes rapidly. Faster computers, mobile computing, new programming languages, and so forth, all enable new techniques and tools to develop systems. This rapidly changing technology forces systems developers to change to try to take advantage of these changes.

-----

Systems Analysis and Design in a Changing World, sixth edition
8-9

Different organizations have different needs: Some organizations have rapidly changing needs to meet a dynamic, changing market place. Other organizations, and within an organization, have a slower pace of work and of change. New systems may not be necessary and older systems, using older technology maybe adequate for the processing and workflow requirements.
There are many types of systems: Systems also are very different. From mobile systems, to business systems, to engineering systems, to scientific systems. Some systems have a high usage of detailed data and are very database sensitive. Other systems must be real time and respond rapidly to external inputs. Different specifications require different types of development techniques.
Developers have widely different backgrounds: Obviously developers use the tools that they are familiar with. So even though this does affect the tools and techniques used, developers should also be amenable to learning new and more powerful techniques and tools.

## **11. Go to the campus placement office to gather some information on companies that recruit information systems graduates. Try to find any information about the companies' approaches to developing systems. Is their SDLC described? Do any mention an IDE or a visual modeling tool? Visit the companies' Web sites to look for more information.**
Answers will vary. Larger companies might post information on methodologies used as part of the recruiting information. Otherwise, companies sometimes tend to keep this information confidential. Students might suggest to recruiters that this information could help students understand the way development is done at the company.

## **12. Visit the Web sites of a few leading information systems consulting firms. Try to find information about their approaches to developing systems. Are their SDLCs described? Do the sites mention any tools, models, or techniques?**
Answers will vary. If it is a consulting firm, they might publish a lot about their methodology (or even sell their methodology to clients). Some will brag about the state-of-the-art approach that they use. Some will be vague about it.

-----

Systems Analysis and Design in a Changing World, sixth edition
8-10

### Solutions to End-of-Chapter Cases

#### Case Study: A "College Education Completion" Methodology

## **1. What are the phases that your college education completion life cycle might have?**
## **2. What are some of the activities included with each phase?**
## **3. What are some of the techniques you might use to help complete those activities?**
## **4. What models might you create? Differentiate the models you create to get you through college from those that help you plan and control the process of completing college.**
## **5. What are some of the tools you might use to help you complete the models?**
Answers will vary. One approach involves planning for going to college, analyzing the requirement for what you want out of college, designing a specific program of study, and implementing the schedule and completing the classes for the program of study until college is complete.
Another approach is to make up more specific phases: getting in, moving away from home, meeting new friends, deciding on a major, establishing a social life, completing courses, planning for the job hunt, hunting for a job, participating in final graduation activities (social and academic), and moving on after graduation.
Remember:

  * Technique: A strategy or guidelines for getting an activity or task completed.
  * Model: Something created as an outcome of a task or an activity.
  * Tool: Something that is used by the technique to create the model.

-----

Systems Analysis and Design in a Changing World, sixth edition
8-11

#### Running Cases: Community Board of Realtors

## **1. Compared to the Tradeshow application described in Chapter 1, how long might this project take, and which approach to the SDLC would be most appropriate?**
Answers will vary.
In the Tradeshow system in Chapter 1 we illustrated an iteration as a week-long mini-project. In reality it will probably require a normal iteration of 3 or 4 weeks. The other subsystem will probably also require an iteration of 3 or 4 weeks. The Community Board of Realtors is a comparable sized system - maybe a little larger with about 12 to 15 use cases. It will probably require three or four iterations.
The Community Board of Realtors system is also a well defined requirement. So rather than do it as an adaptive project with iterations, it could very easily be done as a single predictive type of project. In fact, probably most developers would proceed with a normal modified waterfall approach to this system.

## **2. If you use a predictive SDLC, how much time might each phase of the project take? How much overlap of phases might you plan for? Be specific about how you would overlap the phases.**
Answers will vary.
Using a predictive approach with a modified waterfall approach some estimates (guesses) of time required:

  * Planning: Schedule, cost estimate, work team - probably a week.
  * Analysis: Use cases and domain models - probably around three or four weeks.
  * Design: Packages, network, domain model, user interfaces, use case realization (use case design) - probably another three or four weeks.
  * Implementation: Programming and testing - probably about six to eight weeks.
    Overlapping the last three phases is desirable. There are three primary users (from chapter 3), and working on the new system can be partitioned by those use cases. The analysis phase could focus first on the domain model, which impacts all use cases. Then it could focus on the use cases associated with the MLS office and begin designing and implementing those use cases. Additional analysis, design and implementation could then follow for the Real Estate Office and the RE Agent.

-----

Systems Analysis and Design in a Changing World, sixth edition
8-12

## **3. If you use an adaptive SDLC, how many iterations might you plan to include? What use cases would you analyze, design, and implement in the first iteration? What use cases would you work on in the second iteration? In additional iterations? Think in terms of getting the core functionality implemented early and then building the supporting functionality.**
Answers will vary.
Assuming about 12 to 15 use cases, this project would probably be handled in three or four iterations. (The list of use cases developed in Chapter 2 will need to be revisited and probably expanded. CRUD analysis will indicate if enough use cases have been defined to maintain and report data. There may need to be some more 'R'eporting use cases defined.) The most important data for this application is the property listing data. However, the property listing information is dependent on real estate offices and real estate agents. The interdependencies are quite tight and it does not make sense to try to deploy part of the system early. The core functionality is to build and maintain the database. The supporting functionality is to report and view the data.
Hence a possible solution might be:

  * Iteration 1: Use cases to create and update real estate offices and agents.
  * Iteration 2: Use cases to create and update property listings
  * Iteration 3: Use cases to produce views and reports of the data

## **4. Let us say this project focused on Web access to the MLS. If you also plan to deploy a smartphone application for use by the public and by the agents and brokers, how might this affect your choice of the approach to the SDLC? What are the implications for including the smartphone application in the initial project versus having a separate project for wireless later?**
Answers will vary.
Including a smart phone application will add considerable complexity to the system. The current approach is to use desktop and web based systems. Smart phone is an entirely new requirement with new user interface issues, communication issues, and usability issues. There are also a lot of unknowns with smart phones because the capability of smart phones tends to change rapidly. By including a smart phone app, it would appear that an adaptive approach to the system development would be best.
If the smart phone requirement was included in the original project, it could be isolated into its own iteration(s). However, the deployment of the entire system might be delayed if it is included in the original project. It might make more sense to go ahead and deploy desktop and Web solution, and then add smart phone functionality as a separate project. The danger with that approach, is that the original solution should be designed and constructed so that it does not have obstacles to later implementing smart phone capability.

-----

Systems Analysis and Design in a Changing World, sixth edition
8-13

## **5. Consider using incremental development to include the Web application and the wireless support. Describe what would be included in the first and second deployments of the project. Take into consideration that you might want to work on some initial problem solving for requirements, design, and implementation of the wireless support at the same time you are working on the Web application.**
Answers will vary.
As indicated in Problem 4, the original design should consider the implications and issues related to smart phone applications. The core functionality is to maintain the database, e.g. create, update, delete offices, agents, and property listings. This functionality is best done via desktop and web applications (typing critical data on a smart phone tends to be error-prone). Hence there is not as much need to implement the core database maintenance functions on a smart phone.
Viewing and reporting should be available for desktop, tablet, and smart phone devices. Hence after the basic database update is constructed, it might make sense to address the smart phone technical issues in a short iteration early in the project. Any new requirements for network, communications, user interfaces, etc. can then be addressed early in the project. Follow-on iterations could then complete the implementation of all the viewing and reporting functions.

-----

Systems Analysis and Design in a Changing World, sixth edition
8-14

#### Running Cases: The Spring Breaks 'R' Us Travel Service

## **1. The SBRU information system includes four major subsystems: Resort relations, Student booking, Accounting and finance, and Social networking. Although you have only worked with the domain model class diagram for the social networking subsystem, list as many of the domain classes that would probably be involved in each of the subsystems. Note which classes are used by more than one subsystem.**
Note: In Chapter 5 we enhanced the domain model from Chapter 4 in order to discuss Student Reservations. We will use that domain model as our starting point and add other classes as necessary.

| Subsystems | Classes |
|---|---|
| Resort relations | Resort<br>Accommodation<br>Facility<br>Activity<br>Traveler<br>TravelerInRoom<br>Comment (read) |
| Student booking | Reservation<br>Traveler<br>PersonAccount<br>Group<br>Resort (read)<br>PaymentTxn |
| Accounting and finance | PaymentTxn<br>PersonAccount (read)<br>Traveler (read)<br>Resort (payments to resorts) |
| Social networking | Traveler (read)<br>Group (read)<br>Interest\*\*<br>Comment<br>Resort (read)<br>TravelerInRoom (read)<br>Accomodation (read)<br>Facility (read)<br>Activity (read)<br>MultimediaInfo\*\* |

Note: \*\* denotes class NOT used by multiple subsystems. All other classes are accessed by multiple subsystems.

-----

Systems Analysis and Design in a Changing World, sixth edition
8-15

## **2. Based on the overlapping classes, what domain classes seem to be part of the core functionality for SBRU? Draw a domain model class diagram that shows these classes and their associations.**
Core functionality will be to allow students to make reservations at resorts. That is the first and most important functionality. That requires resort information and student information.

-----

Systems Analysis and Design in a Changing World, sixth edition
8-16

## **3. Let us say you plan to implement the basic uses cases that create and maintain the classes that are part of the core functionally you just modeled. Describe what domain classes you would focus on in each iteration if you assumed that you would need two iterations for the initial core functionality and two additional iterations to complete each of the subsystems.**
The above (Question \#2) domain classes cross two subsystems, Student booking and Resort relations. So we will have two iterations on the core functionality in these two subsystems, and then the remainder of the use cases (from Chapter and domain classes to finish those two subsystems.

| Iteration | Subsystem | Use Cases | Domain Classes |
|---|---|---|---|
| \#1 | Resort relations | Sign up with SBRU<br>Edit resort info<br>Create SBRU website<br>Post availability of rooms | Resort<br>Accomodation |
| \#2 | Student booking | Join SBRU<br>View Resort info<br>Make a reservation | Traveler<br>PersonAccount<br>Reservation<br>PaymentTxn |
| \#3 | Resort relations | Create facility info<br>Create Activity info<br>View comments<br>Assign traveler to accommodation | Facility<br>Activity<br>TravelerInRoom<br>Comment |
| \#4 | Student booking | Create group<br>Make payment<br>Cancel reservation | Group<br>PaymentTxn |

## **4. How might you use incremental development to get some core functionality or some subsystems deployed and put into use before the project is completed?**
These first two subsystems are the most critical and could be deployed first. Even assigning travelers to rooms does not need to occur until the students arrive. So given the above (Question \#3) approach these subsystems could be deployed prior to the Accounting and Finance and the Social Networking subsystems.

-----

Systems Analysis and Design in a Changing World, sixth edition
8-17

#### Running Cases: On the Spot Courier Services

## **1. In what order would you develop the four subsystems? Support your answer.**

1.  Customer account subsystem (like customer account)
2.  Pickup request subsystem (like sales)
3.  Package delivery subsystem (like order fulfillment)
4.  Routing and scheduling subsystem
    The above list would allow On the Spot system to start supporting picking up and delivering packages. Although all of the Customer account system is not needed at first, at a minimum the customer class is required to be able to assign requests and packages to customers. So either the entire Customer account system can be implemented first, or at least a single Customer class can be implemented and next the Pickup request followed by the Package delivery subsystem.
    After the pickup and delivery subsystems are working, the rest of customer account subsystem is highest priority. The routing and scheduling subsystem is purely internal and could be done by hand if necessary until the system was completed.

## **2. Reviewing your work from Chapter 3, assign each of your use cases to a particular subsystem. Does this change your answer or does it strengthen your original premise? Support your answer.**
Note: As this case unfolds, it becomes evident that additional use cases can be defined from a CRUD analysis of the domain classes in Chapter 4. The table below includes some of those additional use cases.

| Subsystem | Use Case |
|---|---|
| Pickup request | Enter/update request for pickup information<br>Cancel request for pickup<br>Enter package pickup information (scan)<br>Update package pickup information<br>Print label |
| Package delivery | Enter package delivery information (scan)<br>Enter customer signature (delivery)<br>Get package tracking information |
| Customer account | Add/update a customer<br>Delete a customer<br>View customer account information<br>Print invoices<br>Enter payment information |
| Routing and scheduling | Enter package event information (scan)<br>Create trip manifest<br>Update trip manifest<br>Print trip manifest (packages to be delivered)<br>Display trip manifest (real time) |

-----

Systems Analysis and Design in a Changing World, sixth edition
Assign package to trip (truck route)
8-18

## **3. Reviewing your work from Chapter 4, assign each of your classes to a subsystem. (Note: Some classes may be in multiple subsystems. The primary subsystem is the one that "creates" the objects in that class.) Does this change your answer or does it strengthen your original premise? Support your answer.**

| Subsystem | Class |
|---|---|
| Pickup request | PickupRequest<br>Package<br>Customer<br>Custome Account<br>Payment<br>MovementEvent<br>Route Trip |
| Package delivery | Package<br>Customer<br>MovementEvent<br>Employee<br>Route Trip |
| Customer account | Customer<br>Individual Customer<br>Business Customer<br>Customer Account<br>Payment |
| Routing and scheduling | Route Trip<br>Employee<br>Package<br>MovementEvent |

-----

Systems Analysis and Design in a Changing World, sixth edition
8-19

## **4. Considering the Agile modeling principles, discuss each of the following:**
**(a) In Chapter 3, you developed a list of use cases and a use case diagram. If you follow the Agile modeling philosophy, how much or how little of this model do you think is necessary? Support your answer.**
Since many activities of analysis and design are "use case" driven it is absolutely necessary to have a list of use cases. The Use Case diagram is simply a way to organize the use cases and to show the actor that invokes the use cases. So even though a list of use cases will contain the same information as the Use Case diagram, the diagram is extremely useful to communicate relationships and utility. It is useful as a monitor for later work such as detailed design. Keep it.

**(b) In Chapter 4, you developed a class diagram. If you follow the Agile modeling philosophy, how much or how little of this model do you think is necessary? Support your answer.**
A class diagram has essential business rules expressed in the relationships and cardinality constraints. It is also heavily used by developers in the development of the database. This model is absolutely necessary.

**(c) In Chapter 5, you developed some use case descriptions, activity diagrams, and system sequence diagrams. If you follow the Agile modeling philosophy, how many or how few of these models do you think are necessary? Support your answer.**
Minimizing the models, as proposed by the Agile philosophy will enable us to eliminate some of the models used in Chapter 5. For simple use cases, there may be no need for any of the three models. Also there is some duplication between the fully developed use case description and the activity diagrams. For those that are visually oriented, an activity diagram may be more helpful. However a compbination of fully developed use case description and a system sequence diagram will provide a strong base of understanding. In many cases not all three models are required, even for complex use cases.

**(d) In Chapter 6, you developed a network diagram and specified hardware requirements. If you follow the Agile modeling philosophy, how many or how few of these models do you think are necessary? Support your answer.**
The modeling requirements from Chapter 6 would depend heavily on the complexity of the system. A simple system may not require a network diagram and the model can be eliminated. Complex solutions, however, may require a model in order to know how to configure the solution.

-----

Systems Analysis and Design in a Changing World, sixth edition
8-20

#### Running Cases: Sandia Medical Devices

## **1. Given the system goals, requirements, and scope as they are currently understood, is the project schedule reasonable? Why or why not?**
Although the technical issues related to this project are complex, the number of use cases and the application functions is limited. A six month development period should be adequate. The three month testing period is good given that this is a health system and could have serious consequences if it did not work correctly.

## **2. How well understood are the system requirements at the start of the project? What are the implications of your answer for using a predictive, adaptive, or mixed SDLC? What are the implications of your answer for using Agile techniques?**
Answers will vary.
Given the use cases and problem description provided, it would appear that the overall view of the requirements is quite good. However, the details are very much unknown at this time. And the technical difficulties may not be understood. Hence probably an adaptive approach would be best in this case.
Agile techniques would fit well in this environment working closing with the users and building code without a lot of modeling.

## **3. Medical personnel at NMHS have very busy schedules. NMHS's decision to assign two medical practitioners to the project for one day a week represents a significant investment in salary and lost revenue. How should project iterations be structured to ensure rapid progress to completion, high quality, and efficient use of medical practitioner time?**
Answers will vary.

-----

Systems Analysis and Design in a Changing World, sixth edition

## **4. Prepare a detailed work schedule for the first iteration. If you have access to project management software, prepare the schedule and a Gantt chart by using the software.**
Answers will vary. This project is highly technical, and especially this iteration requires little user involvement. It addresses technical areas.

| Discipline | Activity | Effort | Dependency |
|---|---|---|---|
| Planning | Set up work environment | 1 day | |
| | Develop WBS and plan work | $1/2$ day | |
| Analysis Activities | Meet with tech staff on specs of monitoring device | 2 days | |
| | Learn specs on selected phone devices | 4 days | |
| | Define data | 1 days | |
| | Define interface requirements | 2 days | |
| Design Activities | Design detailed interfaces | 1 days | |
| | Design program structure | 2 days | |
| Build Activities | Write program code | 8 days | |
| | Set up for communication/integration test | 1 day | |
| | Conduct communication & integration test | 2 days | |
| | Do retrospective | $1/2$ day | |
| Total Days | | $25~days=5$ wks | |

8-21

| Task Mode | Task Name | Duration | Start | Predecessors |
|---|---|---|---|---|
| | - Planning Activities | 1.5 days | Mon 6/4/12 | |
| | Set up work environment | 1 day | Mon 6/4/12 | |
| | Develop WBS and plan | 4 hrs | Tue 6/5/12 | 2 |
| | - Analysis Activities | 9 days | Tue 6/5/12 | |
| | Meet with tech staff | 2 days | Tue 6/5/12 | 3 |
| | Learn specs on phones | 4 days | Thu 6/7/12 | 5 |
| | Define data | 1 day | Wed 6/13/12 | 6 |
| | Define interfaces | 2 days | Thu 6/14/12 | 7 |
| | - Design Activities | 3 days | Mon 6/18/12 | |
| | Design Interfaces | 1 day | Mon 6/18/12 | 8 |
| | Design programs | 2 days | Tue 6/19/12 | 10 |
| | - Build Activities | 11 days | Thu 6/21/12 | |
| | Write program code | 8 days | Thu 6/21/12 | 11 |
| | Set up comm test | 1 day | Tue 7/3/12 | 13 |
| | Conduct comm test | 2 days | Wed 7/4/12 | 14 |
| | Do retrospective | 4 hrs | Fri 7/6/12 | 15 |
# Chapter 9 - Designing the Database

# Chapter 10 - Approaches to System Development

# Chapter 11 - Project Planning and Project Management
# Chapter 9 - Project Planning and Project Management

## Solutions to End-of-Chapter Problems

### Review Questions

## **1. List the six major reasons that projects fail.**

1.  Undefined project management practices
2.  Poor IT management and procedures
3.  Inadequate executive support
4.  Inexperienced project managers
5.  Unclear business objectives
6.  Inadequate user involvement

## **2. List six critical factors that contribute to project success.**
Oops. Only a summary of these critical factors was included in this edition. However, the success factors are basically the reverse of the failure reasons. Here is a list of a few:

  * Clear system requirement definitions
  * Substantial user involvement
  * Support from upper management
  * Thorough and detailed project plans
  * Realistic work schedules and milestones

## **3. Define project management.**
Project management is the organizing and directing of other people to achieve a planned result within a predetermined schedule and budget.

## **4. List five internal responsibilities of a project manager.**

  * Developing the project schedule
  * Recruiting and training team members
  * Assigning work to teams and team members
  * Assessing project risks
  * Monitoring and controlling project deliverables and milestones

## **5. What is the difference between the client and the user?**
The user is the person that actually will use the new system. The client is the person or group that is paying for the development of the new system. In some cases they can be the same person, but they do not need to be.

## **6. What is meant by an organic approach?**
The way a plant or animal grows is an organic approach. It starts small and increases in size. But even when it is small it still has all the essential components and is fully functional. As it grows it develops more capability and expands its scope. Developing a piece of software "organically" attempts to take a similar approach. It starts small, but is functional, and grows piece by piece adding more capability.

## **7. What is the importance of "ceremony"?**
Another word for ceremony is formality. Instead of letting the ceremony of the project happen by default without any thought, the project ceremony should be a conscious and deliberate decision. Without define level of ceremony, the project stakeholders and team members will not know what is expected of them and how to work together.

## **8. List the nine areas of the PMBOK.**

1.  Scope Management
2.  Time Management
3.  Cost Management
4.  Quality Management
5.  Human Resource Management
6.  Communications Management
7.  Risk Management
8.  Procurement Management
9.  Integration Management

## **9. What is meant by Agile project management?**
Agile project management is an approach to project management that includes the Agile philosophies in managing the project and the team of people. Basically Agile project management focuses on being flexible in project procedures, working relationships, and working software. Chapter 8 described the four basic values of Agile development.

## **10. How is scope management accomplished with Agile project management?**
Since Agile projects are more flexible, frequently there are more requests for additional functionality to be added. To control these requests a prioritized list of functions is maintained. In order for new functions or requirements to be added, they must go through a review process and be added to the prioritized list.

## **11. What are the four activities of Core Process 1?**

  * Identify the problem
  * Quantify the project approval factors
  * Perform risk and feasibility analysis
  * Review the approval factors with the client to obtain approval

## **12. What are three reasons that projects are initiated?**

  * To respond to an opportunity
  * To resolve a business problem or need
  * To respond to an external (such as legal) mandate

## **13. What is the difference between system capabilities and business benefits?**
The business benefits are measured in the dollars that are brought to the organization, either as increased revenue or reduced costs. (Intangible benefits are those where a dollar amount cannot be easily assigned, but still will add value to the organization.) The system capabilities are the functions that support the business procedures. The system capabilities are those things that enable or lead to the business benefits.

## **14. What factors are usually considered when approving a project?**

  * How long will the project take?
  * How much will it cost?
  * What are the anticipated benefits to the organization?

## **15. List 10 types of benefits that may be considered when approving a project.**

  * Opening up new markets with new services, products, or locations
  * Increasing market share in existing markets
  * Enhancing cross-sales capabilities with existing customers
  * Reducing staff by automating manual functions or increasing efficiency
  * Decreasing operating expenses, such as shipping charges for "emergency shipments"
  * Reducing error rates through automated editing or validation
  * Reducing bad accounts or bad credit losses
  * Reducing inventory or merchandise losses through tighter controls
  * Collecting receivables (accounts receivable) more rapidly

## **16. Explain how net present value (NPV) is calculated.**
Net present value is the net, i.e. the difference between costs and benefits, brought back to present value dollars. First the cost of development is considered as being done in year 0. The for each future year, up to some number of years, the costs, which are negative dollars, and the benefits, which are positive dollars, are netted together. Then that amount for each year is brought back to present value using the discount factor for the percentage rate and the number of years in the future.

## **17. What is the difference between tangible benefits and intangible benefits?**
A tangible benefit is one that can be estimated or measured in terms of dollars. An intangible benefit may be just as important, but the client is not able to quantify it by assigning a dollar value to it.

## **18. What are some factors to consider when assessing organizational feasibility?**
Organizational feasibility is a consideration of the risks within the organization itself - these risks are usually people risks, i.e. that they will be unable to accept or utilize the new system. Such things as computer phobia, fear of losing a job, political impacts on people's importance or position, or difficulty of changing work procedures.

## **19. What are the five activities of Core Process 2?**

  * Establish the project environment.
  * Schedule the work.
  * Staff and allocate resources.
  * Evaluate work processes.
  * Monitor progress and make corrections.

## **20. List seven types of information that should be captured during a project.**

  * Project plans and schedules
  * Analysis documentation
  * Design specifications
  * Test cases and test results
  * Outstanding issues and problems
  * Screen and report definitions
  * Program code

## **21. What is the difference between the project iteration schedule and the detailed work schedule?**
The project iteration schedule is a broad, overview schedule that identifies the iterations and the use cases or functions assigned to each iteration. Generally this schedule is not detailed enough to assign work. The detailed work schedule is a shorter view and more detailed schedule, such as for each iteration, from which work assignments can be made and progress can be measured.

## **22. What is a work breakdown structure used for?**
The work breakdown structure is the first step in building a detailed work schedule. It identifies all of the pieces of work that must be done to complete a certain milestone or that covers a period of the project. Along with identifying the work, it can be used to organize the work by noting which tasks are dependent on other tasks. It also describes how much effort is estimated for each task.

## **23. What is the benefit of an iteration review and retrospective?**
The purpose of a retrospective is to improve the project management and work processes within the project. Since most iterative projects have many iterations, by taking the time to review the processes at the end of each iteration, the project team can improve how it works. The purpose of a retrospective is to ask "How are we doing as a project team?"

-----

### Problems and Exercises

## **1. Read this description and then make a list of expected business benefits that the company might derive from a new system:**
*Especially for You Jewelers is a small jewelry company in a college town. Over the last couple of years, it has experienced a tremendous increase in its business. However, its financial performance hasn't kept pace with its growth. The current system, which is partly manual and partly automated, doesn't track accounts receivables sufficiently, and the company is finding it difficult to determine why the receivables are so high. It runs frequent specials to attract customers, but it has no idea whether these are profitable or if the benefit if there is one comes from associated sales. Especially for You wants to increase repeat sales to its existing customers, thus it needs to develop a customer database. It also wants to install a new direct sales and accounting system to help solve these problems.*

  * Reduce the level of accounts receivables.
  * Determine which type of specials and promotions increased sales.
  * Increase repeat sales to existing customers.
  * Closely track financial performance of the store.

## **2. Read this narrative and then make a list of system capabilities for the company:**
*The new direct sales and accounting system for Especially for You Jewelers will be an important element in the growth and success of the jewelry company. The direct sales portion needs to track every sale and be able to link to the inventory system for cost data to provide a daily profit and loss report. The customer database needs to be able to produce purchase histories to assist management in preparing special mailings and special sales to existing customers. Detailed credit balances and aged accounts for each customer would help solve the problem with the high balance of accounts receivables. Special notice letters and credit history reports would help management reduce accounts receivable.*

  * Track individual sales.
  * Report on cost data for inventory items.
  * Produce daily profit and loss reports.
  * Track purchase histories of individual customers.
  * Produce special mailings.
  * Maintain accounts aging with reporting.

## **3. Develop a System Vision Document for Especially for You Jewelers based on the work you did for Problem 1 and Problem 2.**
Answers will vary. See Figure 9-5 on page 244 for an example of a project charter. Students should create a system scope document similar to Figure 9-5. The business benefits and system capabilities from problems 1 and 2 can also be included. A brief description of the problem should be taken from the case description.

## **4. Develop a work breakdown structure (WBS) based on the following narrative. It should cover all aspects of the move-from the beginning of the project (now) to the end, when all employees are moved into their new offices. Format your solution in tabular form with the following column headings: Task ID No, Task Description, Estimated Effort, Predecessor Task ID.**
*(Narrative text omitted for brevity...)*

Answers will vary. Here is one group's solution.

| ID | Task Name | Predecessor | Effort |
|---|---|---|---|
| 1 | Prepare the Building | | |
| 2 | Design refurbish work | | |
| 3 | Research Designers | none | 4 hrs |
| 4 | Choose Top 3 | 3 | 4 hrs |
| 5 | Write/Send Request for Proposal | 4 | 16 hrs |
| 6 | Review Proposals | 5 | 8 hrs |
| 7 | Select Designer | 6 | 5 hrs |
| 8 | Develop Draft Plan (Designer) | 7 | 16 hrs |
| 9 | Review Plan and Give Feedback | 8 | 12 hrs |
| 10 | Develop Final Plan (Designer) | 9 | 8 hrs |
| 11 | Approve Plan | 10 | 2 hrs |
| 12 | Setup Network/Phones | | |
| 13 | Plan wiring and cabling | 11 | 25 hrs |
| 14 | Install Network Jacks | 13 | 34 hrs |
| 15 | Install Phones | 14 | 34 hrs |
| 16 | Test Network Jacks and Phones | 15 | 16 hrs |
| 17 | Refurbish Building | | |
| 18 | Paint walls | 16 | 40 hrs |
| 19 | Install New Carpet | 18 | 25 hrs |
| 20 | Purchase Furniture | 11 | 16 hrs |
| 21 | Place Furniture in Cubicles | 20 | 25 hrs |
| 22 | Decorate | 18,21 | 25 hrs |
| 23 | Inspect building | 22 | 8 hrs |
| 24 | Organize the Move | | |
| 25 | Review Calendar for Long Weekends | 11 | 4 hrs |
| 26 | Select Moving Date | 25 | 4 hrs |
| 27 | Notify Employees About the Move | 26 | 10 hrs |
| 28 | Plan Employee Moving Meeting | 27 | 8 hrs |
| 29 | Create Moving Agenda for Employees | 28 | 8 hrs |
| 30 | Conduct Meeting/Distribute Agenda | 29 | 3 hrs |
| 31 | Gather Boxes and Moving Equipment | 30 | 5 hrs |
| 32 | Arrange for Moving Trucks | 31 | 3 hrs |
| 33 | Notify Clients of New Address and Phone | 32 | 16 hrs |
| 34 | Plan for Client Services Continuity | | |
| 35 | Review Outsourcing Provider Options | 11 | 4 hrs |
| 36 | Select Outsourcing Provider | 35 | 3 hrs |
| 37 | Make Arrangements During Transition | 36 | 4 hrs |
| 38 | Carry Out the Move | | |
| 39 | Pack and Move Employee Office Supplies | | |
| 40 | Provide Boxes and Start Packing | 23, 33, 37 | 12 hrs |
| 41 | Load onto Trucks | 40 | 8 hrs |
| 42 | Move to New Office | 41 | 3 hrs |
| 43 | Unload into New Office Space | 42 | 16 hrs |
| 44 | Pack and Move Servers and Equipment | | |
| 45 | Outsourcing Vendor Temporarily Takes Over | 23, 33, 37 | 2 hrs |
| 46 | Disconnect Servers | 45 | 2 hrs |
| 47 | Test Outsourcing Vendor Service | 46 | 2 hrs |
| 48 | Pack Equipment | 47 | 6 hrs |
| 49 | Move Equipment | 48 | 2 hrs |
| 50 | Set up Equipment in New Location | 49 | 10 hrs |
| 51 | Test Equipment in New Location | 50 | 3 hrs |
| 52 | Turn off Outsourcing Service | 51 | 3 hrs |
| 53 | Re-test Equipment | 52 | 4 hrs |

## **5. Enter your WBS from Problem 4 into MS Project. First, enter the tasks, dependencies, and durations. Write a paragraph on your experience using MS Project.**
Answers will vary. Students can take a snapshot of their schedule to turn in.

## **6. Develop a six-year NPV spreadsheet similar to the one shown in Figure 9-10. Use the following table of benefits, costs, and discount factors (see Figure 9-20). The development costs for the system were $225,000.**

| | Year 0 | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 | Year 6 |
|---|---|---|---|---|---|---|---|
| Value of benefits | | $55,000 | $60,000 | $70,000 | $80,000 | $80,000 | $80,000 |
| Costs | -$225,000 | -$5,000 | -$5,000 | -$5,000 | -$5,000 | -$5,000 | -$5,000 |
| Net | -$225,000 | $50,000 | $55,000 | $65,000 | $75,000 | $75,000 | $75,000 |
| Discount factor (6%) | 1.0000 | 0.9524 | 0.9070 | 0.8638 | 0.8227 | 0.7835 | 0.7462 |
| NPV | -$225,000 | $47,620 | $49,885 | $56,147 | $61,703 | $58,763 | $55,965 |
| Cumulative NPV | -$225,000 | -$177,380 | -$127,495 | -$71,348 | -$9,646 | $49,117 | $105,082 |
| Payback Period | | | | | 4 years + 60 days | (.164 \* 365) | $9,646/(9,646+49,117)=.164 |

## **7. Build a Gantt chart by using MS Project based on the table shown in Figure 9-21. Enter the tasks, dependencies, and durations. Print out the PERT chart (Network chart) and the Gantt chart.**
Figure 9-21 presents a list of tasks for a student who wants to have an international experience by attending a university abroad. Assume that all predecessor tasks must finish before the succeeding task can begin (the simplest version). Also, insert a few overview tasks, such as Application tasks, Preparation tasks, Travel tasks, and Arrival tasks. Be sure to state your assumption.

*(A table describing the schedule tasks, durations, and dependencies follows in the source text, representing typical inputs for MS Project.)*

## **8. The state university wants to implement a better system to keep track of all the computer equipment it owns and needs to maintain. The university purchases a tremendous number of computers and software that are distributed throughout the campus and are used by faculty, staff, departments, and colleges. Currently, the university has very sparse records of its equipment and almost no records about maintenance or the software that has been purchased. A list of use cases has been defined; it will serve as the starting point to develop this system. Take the following list of use cases to create a project iteration schedule. You should try to arrange the use cases so similar ones are developed together. Also, the most important use cases should be developed first. State your assumptions, and explain your reasons for your solution.**
Note: For brevity, we use the word computer to refer to any type of computing equipment, such as a desktop computer, laptop computer, server computer, printer, monitor, projector, wireless access point, and so forth.
*(Use case list omitted for brevity...)*

Answers will vary. Here is one possible solution.

| Iteration | Use Cases |
|---|---|
| \#1 | Buy a computer.<br>Put a computer in service.<br>Assign a computer to a person. |
| \#2 | Assign a computer to a department or college.<br>Record the location of a computer.<br>Purchase a warranty for a computer.<br>Record a warranty for a computer. |
| \#3 | Buy a software license.<br>Renew a software license.<br>Install software on a computer. |
| \#4 | Identify computers ready for replacement.<br>Take a computer out of service (surplus).<br>Sell a computer. |
| \#5 | Search for a specific computer by various options.<br>Search for multiple computers by various options.<br>Search for software on computers by various options. |
| \#6 | Remove software from a computer.<br>Repair a computer (in house).<br>Return a computer for repair. |

-----

### Solutions to Chapter 9 Cases (found at the end of the textbook)

#### Case Study: Custom Load Trucking

## **1. Do you think the decision by CLT to build project managers from its existing employee base is a good one? What advice would you give CLT to make sure it has strong project management skills in the company?**
Answers will vary. Generally students will respond that it is a good idea to promote from within. Two points however. First the set of skills to be a project manager is not the same as those skills required to be a good programmer or analyst. So not every programmer or analyst will make a good project manager. Second, good mentoring and training is necessary to ensure good project managers.

## **2. What kind of criteria would you develop for Monica to use to measure whether Stewart (or any other potential project manager) is ready for project management responsibility?**
Answers will vary. The case gives some good insight. Stewart has shown aptitude in leading people (as a team leader), and in building the schedule, etc. Having a list of project management skills and aptitudes and then observing if Stewart has an aptitude to develop those skills will indicate if he is ready and able to become a project manager.

## **3. How would you structure the job for new project managers to ensure or at least increase the possibility of a high level of success?**
Answers will vary. A few points might be to start with smaller, less complex projects. Also projects that are not high risk in all the areas that were discussed. Projects with a similar deployment environment as the existing environment. Also assign a mentor project manager to watch and coach his project.

## **4. If you were Monica, what kind of advice would you give Stewart about managing his career and attaining his immediate goal of becoming a project manager?**
Answers will vary. Project management is a career of advancement. There is always a need for good project managers, so it can be a highly beneficial career with substantial income. However, it tends to be a high-stress position trying to meet deadlines in the face of many problems and unknowns. It requires extensive people skills. Project managers often drop out of the details of technology and programming. So if the employment satisfaction is from getting one's fingers into the code, a project management career might not be satisfying.

-----

#### Running Cases: Community Board of Realtors

## **1. Given the total vision of this system, develop a System Vision Document. Focus primarily on finding the benefits to the community board, the real estate agents, and home buyers.**

**Community Board of Realtors System Vision Document**

**Problem Description**
In any community or metropolitan area there are normally many different real estate offices, each with many different real estate agents. Each of the offices will have a clientèle of sellers who list their properties with the real estate office. Each office will also have a clientèle of buyers who are looking to buy a property. Since these real estate offices are independent there is a need to have a common database of all properties available for sale within the entire metropolitan area. This service is usually provided by a centralized organization, often called the Community Board of Realtors. Centralized information is required of all properties with detailed descriptions. This information needs to be available to all real estate offices and agents, as well as to buyers. The system needs to support adding and updating property information by the offices and agents. The system also must keep track of information about the real estate offices and the agents.

**System Capabilities**
The following functional areas must be supported in the new system:

  * Maintain listing information
  * Maintain real estate office information
  * Maintain real estate agent information
  * Provide listing data in book form
  * Provide search and view of property details
  * Support requests for property visits
  * Centralized database of all property listing information

**Business Benefits**
Benefits apply to the centralized board, real estate offices and agents, the sellers and the buyers.

  * Board benefits: Easy to maintain information. Small staff
  * Offices and agents: Current information on all listings, Automated updates and changes to listing information, Listing books for perusing listings and for advertising, Better able to serve clientèle
  * Sellers: Broad listing of property listing, Wide advertising of property listing, Availability of listing information throughout the area
  * Buyers: Detailed information and images available, Easily able to schedule property visits

## **2. Including the uses cases and functions identified in Chapters 3 and 8, make a list of all the uses cases that must be developed. Divide them into subsystems as appropriate. You should have at least two subsystems: one for viewing data and one for updating data. Add any additional use cases (and subsystems) that might be important to the Community Board of Realtors itself.**
Answers will vary.

| Subsystem | Use Cases |
|---|---|
| Update Data | Add new listing<br>Record listing change<br>Delete listing<br>Add real estate office<br>Update real estate office info<br>Delete real estate office<br>Add new real estate agent<br>Update real estate agent<br>Delete real estate agent |
| View Data | Obtain listing data (View listings)<br>Produce ML book<br>Produce list of RE offices and agents<br>View statistics on RE office (History, Open, Sold)<br>View statistics on RE agents (History, Open, Sold)<br>View histories of sold properties<br>View statistics of open properties |

## **3. Decide on a work sequence, and develop a project iteration schedule.**
Answers will vary.

| Iteration | Use Cases |
|---|---|
| \#1 | Add real estate office<br>Update real estate office info<br>Delete real estate office<br>Add new real estate agent<br>Update real estate agent<br>Delete real estate agent |
| \#2 | Add new listing<br>Record listing change<br>Delete listing<br>Obtain listing data (View listings)<br>Produce ML book |
| \#3 | Produce list of RE offices and agents<br>View statistics on RE office (History, Open, Sold)<br>View statistics on RE agents (History, Open, Sold)<br>View histories of sold properties<br>View statistics of open properties |
| \#4 | Cleanup and acceptance test |

## **4. Estimate the development cost and the time required.**
Answers will vary.

| Subsystem | Function Requirements | Iterations | Estimated time |
|---|---|---|---|
| Update Data | 9 | 2 | 8 weeks |
| View/Report Data | 7 | 2 (some overlap) | 6 weeks |
| Final Cleanup | | 1 | 2 weeks |
| Total | | | 16 weeks |

| Expense Category | Amount |
|---|---|
| Salaries (2 person team @ $1500/week) | $46,000.00 |
| Equipment/Install (1 server + network) | $5,000.00 |
| Training (1 person 1 week) | $1,500.00 |
| Facilities | $5,000.00 |
| Total | $59,500.00 |

## **5. Develop a work breakdown structure (WBS) for the project's first iteration.**

| Discipline | Activity | Effort | Dependency |
|---|---|---|---|
| Planning | Set up work environment<br>Develop WBS and plan work | 2 days<br>1 day | |
| Analysis Activities | Meet with Community Board users<br>Meet with several agents<br>Define data<br>Model use cases | 2 days<br>2 days<br>1 day<br>2 days | |
| Design Activities | Design screen layouts<br>Design Database<br>Design use case processing | 3 days<br>1 day<br>3 days | |
| Build Activities | Build database<br>Write program code<br>Build test data<br>Set up for user test<br>Conduct acceptance test<br>Release first use cases<br>Do retrospective | 1 days<br>8 days<br>2 days<br>1 day<br>2 days<br>$1/2$ day<br>$1/2$ day | |
| Total Days | | 32 days = 6.5 weeks | |

## **6. Enter your WBS into MS Project to create a detailed work schedule.**
Answers will vary.

-----

#### Running Cases: The Spring Breaks 'R' Us Travel Service

## **1. Based on the answers you gave to the Chapter 2 running case questions, develop a System Vision Document.**

**Spring Breaks 'R' Us Travel Service System Vision Document**

**Problem Description**
Spring Breaks arranges with travel resorts for spring break vacation packages and markets those packages to students. Historically it has done its business using campus sales persons and printed fliers. However, students now prefer to do their own browsing and vacation scheduling using the Internet. Hence Spring Breaks needs to build an entirely new Web based system that allows resorts to self-publish their vacation packages, and supports student desires to browse and schedule their vacations. Additional features are to be added to the system to enhance utility for students. One popular feature is a social networking component to the system.

**System Capabilities**

  * Resort Relations: Create/enter resort information, Post availability and prices of rooms/facilities, Retrieve completed reservations
  * Student Booking: View resort information and availability of rooms/facilities, Make a reservation (book a room/facility)
  * Accounting and Finance: Process student payments, Process payouts to resorts
  * Social Networking: Link up and chat with "friends", Post comments and pictures

**Business Benefits**

  * For Spring Breaks: Increased student use (increase sales), Social media marketing of Spring Breaks services, Better support for resorts will help to recruit additional resorts, Reduce costs of 'on-campus' sales representatives
  * For Resorts: Easier to add vacation packages, Faster payments for reservation, Closer, more rapid communication with Spring Breaks
  * For Students: Easier to browse vacation packages, More detailed information about vacation packages, Mobile access to resorts, packages, friends, Easier to reserve and change packages, Easier to form vacation 'groups' with friends, Locating and connecting with friends via social networking capability

## **2. Based on the functional descriptions you provided for the Chapter 2 running case and the use cases you defined in Chapter 3, finish identifying a complete list of use cases for each of the four subsystems. One important decision you will have to make is which subsystems to develop first.**
Answers will vary. Probably the best order to deploy the system is:

1.  Resort relations - so they can start entering vacation packages
2.  Student booking - so students can start using the system
3.  Accounting and finance about as important as student booking. Need to process payments
4.  Social networking - Some portions will need to be done early (individual and group accounts that book rooms together). Other portions are not required until students begin taking vacations

<!-- end list -->

  * Resort Relations: Sign up with SBRU (get an account), Edit account information, Create/enter resort information for SBRU website, Post availability and prices of rooms/facilities, View/edit room availability, Retrieve completed reservations, Submit damage report
  * Student Booking: Join SBRU/enter personal and financial information, View resort information and availability of rooms/facilities, Make a reservation (book a room/facility), Make a payment for reservation, Cancel a reservation
  * Accounting and Finance: Process student payments, Make refunds/correct payment errors, Process payouts to resorts, Edit/update/correct payouts
  * Social Networking: Create an individual account (join), Set preferences on account, Create a group account, Assign admin rights to account, Search for a person or group, Link up with a person or group, Send a private message to a friend, Chat with friend(s), Post a comment to a friend/group/photo, Upload photo or video, Tag photo, Write/update vacation experience

## **3. A related decision is whether to organize your programmers into one larger team or multiple smaller teams and how many programmers you can use on this project. Make that decision and then defend your answer.**
Answers will vary. One way would be to have a "Student functions" team, and a "Resort functions and finance" team.

## **4. Once those decisions are made, develop a project iteration plan. If you have multiple independent teams, your project iteration plan will have parallel paths.**
Answers will vary. This solution is for a two team project. Note due to dependencies, the database for the resorts will need to be developed first. It is important for both teams. Immediately thereafter student reservation information is required for both teams. Both teams will coordinate together on database development.

| Iteration | Student Function Team | Iteration | Resort Function Team |
|---|---|---|---|
| \#1 | Join/Enter account info<br>Create an individual account<br>Create group account | \#1 | Sign up with SBRU<br>Create/enter resort information<br>Post room and package info |
| \#2 | View resort information<br>View vacation package options<br>Make a reservation<br>Change/Cancel a reservation | \#2 | Edit account information<br>View/edit rooms/packages<br>Retrieve reservations<br>Submit damage report |
| \#3 | Set preferences on individual account<br>Set admin rights to group<br>Make a payment | \#3 | Process payments<br>Make corrections on payments<br>Process payouts<br>Correct payouts |
| \#4 | Search for person/group<br>Link up with person<br>Send message<br>Post comment | \#4 | Write vacation experience<br>Upload photo/video<br>Tag photo/video |

## **5. Based on your previous answers, develop an estimate for the total project cost and the time required to complete the project.**

| Iter | Student Function Team (No. Use cases / Estimate) | Iter | Resort Function Team (No. Use cases / Estimate) |
|---|---|---|---|
| \#1 | 3 / 6 weeks | \#1 | 3 / 6 weeks |
| \#2 | 4 / 5 weeks | \#2 | 4 / 5 weeks |
| \#3 | 3 / 4 weeks | \#3 | 4 / 4 weeks |
| \#4 | 4 / 4 weeks | \#4 | 4 / 4 weeks |
| \#5 | Cleanup/Test / 4 weeks | \#5 | Cleanup/test / 4 weeks |

| Expense Category | Amount |
|---|---|
| Salaries (2 person teams @ $1500/week+ PM @ $2000/week + support staff @ $1200/week) | $208,400 |
| Equipment/Install (2 servers + network) | $25,000 |
| Training | $15,000 |
| Facilities | $20,000 |
| Licenses | $10,000 |
| Travel/miscellaneous | $20,000 |
| Total | $298,400 |

## **6. Assuming an annual revenue increase of $250,000 per year (benefit) and an annual operating cost of $75,000, develop a five-year NPV worksheet by using your estimates for developing the system. Use a 6 percent discount factor.**
The following answer uses a constant $250,000 for the benefit and constant $75,000 for the costs. In reality, the benefit would increase gradually, and costs would also increase over time. For consistency we provide this simple solution.

| Category | Year 0 | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 |
|---|---|---|---|---|---|---|
| Value of benefits | | $250,000 | $250,000 | $250,000 | $250,000 | $250,000 |
| Development costs | -$298,400 | | | | | |
| Annual Expenses | | -$75,000 | -$75,000 | -$75,000 | -$75,000 | -$75,000 |
| Net benefit/costs | -$298,400 | $175,000 | $175,000 | $175,000 | $175,000 | $175,000 |
| Discount Factor (6%) | 1.0000 | 0.9524 | 0.9070 | 0.8638 | 0.8227 | 0.7835 |
| Net Present Value | -$298,400 | $166,670 | $158,725 | $151,165 | $143,973 | $137,113 |
| Cumulative NPV | -$298,400 | -$131,730 | $26,995 | $178,160 | $322,133 | $459,245 |
| Payback Period | | 1 year + | $131,730/(158,725)=.83 | 1 year + 303 days (.83\*365) | | |

-----

#### Running Cases: On the Spot Courier Services

## **1. Create a System Vision Document.**

**On The Spot Courier Services System Vision Document**

**Problem Definition**
Currently information about requests for pickup, package pickups and deliveries is maintain manually on spreadsheets and paper forms. A new system is needed to allow regular customers to use the Web to request pickups and enter information about their packages. The system needs to also track the movement of packages from pickup, through the warehouse, and on to delivery. Finally, the system should also support real time communication with the delivery trucks to facilitate rapid pickup from recent requests. In order for this business to handle the day to day processes, as well as prepare for future growth, it is mandatory that the system be built and deployed as soon as possible.

**System Capabilities**
The system should support the following functions:

  * All customers able to request pickups through the Internet
  * Support call in requests for package pickups
  * Track all movements of packages from pickup, through warehouse, until delivery
  * Provide tracking information over the Internet
  * Support customer accounts for regular customers
  * Provide delivery trip information about what to deliver and what to pick up
  * Send out invoices and accept payments

**Business Benefits**
First, of course, the new system will enable On the Spot to support the current level of business. Additionally the benefits include:

  * Provide support for growth and increased volumes
  * Support customer requests for Web access and tracking of packages
  * Increase customer service through Web capabilities and tracking information
  * Improve speed of pickup and delivery by real time communication with delivery trucks

## **2. Review all the use cases that you identified in Chapter 2 and then enhance the list to achieve a complete solution. Assign each use case to one of these four subsystems from Chapter 8.**
Note: After doing a CRUD analysis based on the class diagram from Chapter 4, another subsystem called "Administration" will need to be added to support purely management use cases. CRUD analysis showed that we need use cases to maintain the Employee table. Also to 'R'eport data, we need new use cases.

| Subsystem | Use Cases |
|---|---|
| Customer account subsystem | Add/update a customer<br>Delete a customer<br>View customer account information<br>Print invoices<br>Enter payment information |
| Pickup request subsystem | Enter/update request for pickup information<br>Cancel request for pickup<br>Enter package pickup information (scan)<br>Update package pickup information<br>Print label |
| Package delivery subsystem | Enter package delivery information (scan)<br>Enter customer signature (delivery)<br>Get package tracking information |
| Routing and scheduling subsystem | Enter package event information (scan)<br>Create trip manifest<br>Update trip manifest<br>Print trip manifest (packages to be delivered)<br>Display trip manifest (real time)<br>Assign package to trip (truck route) |
| Administration subsystem | Adjust customer account information<br>Add/update employee information<br>Delete employee information<br>View employee information<br>Report statistics on package activity (on time, late, volumes, etc)<br>Report statistics on revenues<br>Report statistics on Customer accounts (receivables) |

## **3. Create a project iteration schedule for each subsystem. The project consultant is planning to assign one team of two people to this project, and the subsystems will be built consecutively.**
Answers will vary. We show only the final combined answer.

| Iteration | Subsystem | Use case |
|---|---|---|
| \#1 | Customer account | Add/update a customer<br>Delete a customer<br>View customer account information |
| \#2 | Customer account | Print invoices<br>Enter payment information |
| \#3 & \#4 | Pickup request / Package delivery / Routing | Enter/update request for pickup information<br>Cancel request for pickup<br>Enter package pickup information (scan)<br>Update package pickup information<br>Print label<br>Enter package delivery information (scan)<br>Enter customer signature (delivery)<br>Get package tracking information<br>Enter package event information (scan) |
| \#5 | Routing and scheduling | Create trip manifest<br>Update trip manifest<br>Print trip manifest (packages to be delivered)<br>Display trip manifest (real time)<br>Assign package to trip (truck route) |
| \#6 | Administration | Adjust customer account information<br>Add/update employee information<br>Delete employee information<br>View employee information |
| \#7 | Administration | Report statistics on package activity (on time, late, volumes, etc)<br>Report statistics on revenues<br>Report statistics on Customer accounts (receivables) |

## **4. Create a work breakdown structure (WBS) for the first iteration of the project as you have outlined it. Estimate the effort required for each task in the WBS.**

| Discipline | Activity | Effort | Dependency |
|---|---|---|---|
| Planning | Set up work environment<br>Develop WBS and plan work | 1 day<br>1 day | |
| Analysis Activities | Meet with Bill about customer info<br>Define data<br>Model use cases | 2 days<br>$1/2$ day<br>1 day | |
| Design Activities | Design screen layouts<br>Design Database<br>Design use case processing | 2 days<br>1 day<br>1 day | |
| Build Activities | Build database<br>Write program code<br>Build test data<br>Set up for user test<br>Conduct acceptance test<br>Release first use cases<br>Do retrospective | $1/2$ day<br>4 days<br>$1/2$ day<br>$1/2$ day<br>1 day<br>$1/2$ day<br>$1/2$ day | |
| Total Days | | 17 days | |

## **5. Enter the WBS into MS Project to create a detailed work schedule.**
Answers will vary.

-----

#### Running Cases: Sandia Medical Devices

## **1. Based on the use case diagram and other project information, develop a list of software components (subsystems) that must be acquired or developed. Describe the function(s) of each component in detail.**

| Subsystem | Use cases |
|---|---|
| Patient alert subsystem | View/respond to alert<br>View history<br>Annotate history<br>Phone system receive monitor data (internal use case)<br>Phone system send data to server (internal use case) |
| Patient message subsystem | Send message to physician<br>View/hear message from physician |
| Physician alert subsystem | View/respond to alert<br>View history (monitor data)<br>Set alert conditions<br>Server receive data from phone (internal use case) |
| Physician message subsystem | Send message to patient<br>View/hear message from patient |

## **2. Prioritize the list of software components based on risk.**
Answers will vary. Students should justify their answers. Technological risk would indicate the following use cases are highest risk:

1.  Phone system receive monitor data (internal use case)
2.  Phone system send data to server (internal use case)
3.  Server receive data from phone (internal use case)
4.  View/respond to alert (patient)
5.  View history (patient)
6.  Annotate history (patient)

## **3. Prepare a project iteration schedule based on iterations that last between two and four weeks.**
Answers will vary.

| Iteration | Subsystem | Use case |
|---|---|---|
| \#1 & \#2 | Patient alert | Phone system receive monitor data (internal use case)<br>Phone system send data to server (internal use case)<br>(note: this is complex due to multiple mobile devices) |
| \#3 & \#4 | Patient alert | View/respond to alert<br>View history<br>Annotate history<br>(note: this is complex due to multiple mobile devices) |
| \#5 | Physician alert | Server receive data from phone (internal use case)<br>View/respond to alert<br>View history (monitor data)<br>(note: this is medium complex due to multiple sending devices) |
| \#6 | Physician message | Send message to patient<br>View/hear message from patient |
| \#7 & \#8 | Patient message / Integration test | Send message to physician<br>View/hear message from physician<br>(3 weeks) |
| \#9 | Acceptance test | (3 months) |

## **4. Prepare a detailed work schedule for the first iteration. If you have access to project management software, prepare the schedule and a Gantt chart by using the software.**
Answers will vary. This project is highly technical, and especially this iteration requires little user involvement. It addresses technical areas.

| Discipline | Activity | Effort | Dependency |
|---|---|---|---|
| Planning | Set up work environment<br>Develop WBS and plan work | 1 day<br>$1/2$ day | |
| Analysis Activities | Meet with tech staff on specs of monitoring device<br>Learn specs on selected phone devices<br>Define data<br>Define interface requirements | 2 days<br>4 days<br>1 days<br>2 days | |
| Design Activities | Design detailed interfaces<br>Design program structure | 1 days<br>2 days | |
| Build Activities | Write program code<br>Set up for communication/integration test<br>Conduct communication & integration test<br>Do retrospective | 8 days<br>1 day<br>2 days<br>$1/2$ day | |
| Total Days | | 25 days = 5 wks | |
# Chapter 11 - Project Management Techniques

# Chapter 10 – Object-Oriented Design: Principles

## Solutions to End-of-Chapter Problems

### Review Questions

**1. Describe in your own words how an object-oriented program works.**
As per Figure 10-1, view objects (windows) receive inputs, and send and receive data via messages to business layer objects. As required, business objects send and receive data to database access objects, which retrieve and update the database. The basic approach is that an object-oriented program is a set of interacting objects that get work done sending messages and requesting services from each other.

**2. What is instantiation?**
It is the process of creating and new “instance” of an object using the template provided by the class definition.

**3. List the models that are used for object-oriented systems design.**
The primary UML models are component diagrams deployment diagrams, design class diagrams, Interaction diagrams (sequence diagrams and communication diagrams), state machine diagrams, and package diagrams. Although not a UML model, CRC cards can also be considered a model.

**4. What UML diagram is used to model architectural design?**
Component diagrams can be used to model architectural design.

**5. Explain how domain classes are different from design classes.**
Domain classes usually contain the class name and a list of attributes. Design classes extend domain classes by type casting the attributes, identifying keys, identifying initial values. Design classes also include method signatures with return type and passed parameters.

**6. What is an enterprise-level system? Why is it an important consideration in design?**
An enterprise-level system is one which is used by multiple people or groups and has common resources that must be shared by all users. Designing an enterprise-level system requires considerations about the network and how these common resources will be made available to all users. Hence designing an enterprise-level system requires a broader view of the system and how it will fit into the organization.

**7. What are some of the differences between a client-server network system and an Internet system?**
There are three primary differences identified in the chapter (Figure 10-3).
* **State** – or the ability of the system (both clients and server) to remember what was the last activity and know what to do next. Client-server systems have state, particularly remembering the last connection activity, where Internet system is stateless and the server does not remember what each client was doing.
* **Screens and reports** – a client-server has its screens directly programmed, while an Internet system depends on a browser to display and present the screens. “Active screens” which do things dynamically on Internet system must also use browser accepted programming languages, where client-server can program the screens directly in any desired language.
* **Server configuration** – client-server systems are connected directly where an Internet system uses the services of an Internet server.

**8. What is an API? Why is it important?**
API stands for Application Program Interface and it is mechanism that a subsystem or a component provides its services to the world. An API is set of method signatures for public methods that can be used by other systems to access internal services. Since OO systems depend on objects (and at a higher level, subsystems or components) to work together by invoking methods, the API is a critical part of this interacting set of objects.

**9. What notation is used to identify the interface of a component?**
The notation is a port and socket. The port is represented by a ball and the socket is represented by a cup into which the ball fits.

**10. What is the difference between the notation for problem domain classes and design classes?**
Problem domain classes usually only contain two internal compartments, one for the class name, and the other for the attribute list. Design classes add an addition compartment to list the method names.

**11. In your own words, list the steps for doing object-oriented detailed design.**
* The domain model is enhanced to add type information to the attributes and to add navigation visibility. (First cut).
* The following steps are done on a use-case by use-case basis, i.e. for each use case independently.
* For simple use cases use CRC cards to design the method interactions.
* For more complex use cases use sequence diagrams to define multi-level interactions.
* Update the design class diagram to add method signatures and additional navigation visibility.
* Add package diagrams as necessary.

**12. What do we mean by use-case driven design, and what is use case realization?**
Use case driven design means that detailed design is performed on a use-case by use-case basis. Use case realization is the process of identifying and defining all of the internal messages (methods) between the view layer, business logic layer, and data access layer objects for the specified use case.

**13. What are a) persistent classes, b) entity classes, c) boundary classes, d) control classes, and e) data access classes?**
* **Persistent classes** are those where the data must be stored between program executions, usually in a database. The genesis of persistent classes are usually the problem domain classes.
* **Entity classes** are the business classes, which also come from the problem domain classes.
* **Boundary classes** are the view layer classes.
* **Control classes** are those classes that act as the interface between the view layer and the business layer. These classes are like switchboard classes.
* **Data access classes** are those in the data layer and contain the logic necessary to read and write to the database.

**14. What are class-level methods and class-level attributes?**
Class-level methods and attributes are those that are maintained at the class level and do not need an instantiated object. A class level method can either provide a service method that does not depend on an object, or it can provide a service across all instantiated objects.

**15. What are attribute and method visibility, and what are the types of visibility shown on a design class diagram?**
Attribute and method visibility define whether attributes and methods are public or private, if objects from other classes can access them or if only objects of the same type (class) can access them. On a design class diagram are attribute and method visibility plus navigation visibility, which indicates which classes (objects) have references to which other classes (objects).

**16. What is a method signature?**
A method signature is a unique identifier of a method. Depending on the programming language, it usually consists of the method name, the return type, and the list of all the parameters with the type of each.

**17. Compare and contrast abstract and concrete classes. Give an example of each.**
An abstract class is one which cannot have any objects instantiated. A concrete class does allow for objects to be instantiated. An abstract class might be a “vehicle”, with concrete subclasses of “car” and “truck.” There are no vehicles that are not also a car or truck.

**18. Describe navigation visibility. Why is it important in detailed design?**
Navigation visibility is the ability of the objects in one class to have a reference to, and thus access the API, of the objects in another class. Obviously, if a class does not have a reference to another class, it cannot access its methods. It is a critical design concept.

**19. List some typical conditions that dictate in which direction navigation visibility occurs.**
* A superior/subordinate relationship with the superior being able to view the subordinate
* Mandatory relationship such as a client and order. A client object should know about its orders.
* Informational requirements will need visibility to access the class with the information

**20. What information is maintained on CRC cards?**
CRC cards have one card for each class. On the card are listed the class name, the responsibilities (which are like the methods), other classes that are required to collaborate, and on the back a list of the attributes for that class.

**21. What is the objective of a CRC card design session?**
A CRC design session is to define a set of collaborating classes (i.e. a set of CRC cards) that work together to carry out a use case. It is a simple way to do use case realization.

**22. Compare and contrast the ideas of coupling and cohesion.**
* **Coupling** has to do with how closely connect two (or more) classes are connected. Ideally classes are loosely coupled so that programming changes to one do not also require changes to the other class. So coupling is a concept describing the relationship between classes.
* **Cohesion** is an internal concept to describe the “focus” or “unity” within a class. A class with high cohesion is easier to maintain because it does not have a lot of extraneous methods of functions that may be negatively impacted to programming changes.

**23. What is protection from variations, and why is it important in detailed design?**
Protection from variations is a technique to isolate or segregate those portions of the system that change frequently from those portions that are more stable. By isolating the less stable portions, changes can be made without having to investigate large portions of the system. It isolates the changes to a few classes.

**24. What is meant by object responsibility, and why is it important in detailed design?**
Object responsibility is a principle to help decide which classes should have which methods. By considering object responsibility during design, the result is a set of classes with high cohesion. Classes are given responsibility for their own data and for their own functions.

---

### Problems and Exercises

**1. Given the following system description, develop a component diagram for a desktop-operated internal network system (i.e., Internet access not required).**
The new Benefits for Employees, Spouses, and Dependents (BESD) system will be used primarily by the human resources department and will contain confidential information. Consequently, it will be built as a totally in-house system, without any Internet elements. The database for the system is the human resource employee database (HRED), which is shared by several other systems within the company. There are two types of screens from a systems design viewpoint: simple inquiry screens and complex inquiry/update screens. The simple inquiry screens just access the database, with no business logic required. The complex screens usually do fairly complicated calculations based on sophisticated business rules. These programs often have to access other data tables from other databases in the company. The database will always remain on a central database server. The application program itself will be installed on each desktop that is allowed access. However, authentication is a centralized process, and it will control which screens and program functions can be accessed by which users.


**2. Develop a component diagram for the following description of a Facebook application.**
The Facebook platform is available for entrepreneurs to develop applications for use among all Facebook users. A new application is being written that allows Facebook users to send gifts and greeting cards to their friends. (These are real gifts and greeting cards, not just electronic images.) The application running within Facebook is on its own server and has its own database of information, which includes a list of gifts and cards that have been sent or received. The actual retail store of gifts and cards to send must be located on a different server because it is part of a regular Internet sales storefront. This storefront maintains the database of inventory items to sell and collects credit card payment information.


**3. In this chapter, we developed a first-cut DCD, a set of CRC cards, and a final DCD for the Create phone sale use case for RMO. Create the same three drawings for the Look up item availability use case.**


**4. Find a company that does object-oriented design by using CRC cards. The information systems unit at your university often uses object-oriented techniques. Sit in on a CRC design brainstorming session. Interview some of the developers about their feelings regarding the effectiveness of doing CRC design. Find out what documentation remains after the sessions and how it is used.**
Answers will vary.

**5. Find a company that has an enterprise system. (If you are working for a company, see what systems they use.) Analyze the system and then develop a component diagram and a deployment diagram.**
Answers will vary.

**6. Find a system that was developed by using Java. If possible, find one that has an Internet user interface and a network- based user interface. Is it multi-layered—three layers or two layers? Can you identify the view layer classes, the domain layer classes, and the data access layer classes?**
Answers will vary.

**7. Find a system that was developed by using Visual Studio .NET (Visual Basic or C#). If possible, find one that has an Internet user interface and a network-based user interface. Is it multi-layered? Where is the business logic? Can you identify the view layer classes, the domain layer classes, and the data access layer classes?**
Answers will vary.

**8. Pick an OOP language with which you are familiar. Find a programming IDE tool that supports that language. Test its reverse-engineering capabilities to generate UML class diagrams from existing code. Evaluate how well it does and how easy the models are to use. Does it have any capability to input UML diagrams and generate skeletal class definitions? Write a report on how it works and what UML models it can generate.**
Answers will vary.

**9. Draw a UML design class that shows the following information.**
The class name is Boat, and it is a concrete entity class. All three attributes are private strings with initial null values. The attribute boat identifier has the property of “key.” The other attributes are the manufacturer of the boat and the model of the boat. There is also an integer class-level attribute containing the total count of all boat objects that have been instantiated. Boat methods include creating a new instance, updating the manufacturer, updating the model, and getting the boat identifier, manufacturer, and model year. There is a class-level method for getting the count of all boats.


---

### Solutions to End-of-Chapter Cases

#### Case Study: The State Patrol Ticket-Processing System (Revisited)
In Chapter 3, you identified use cases and considered the domain classes for the State Patrol Ticket Processing System. Review the descriptions in Chapter 3 for the use case Record a traffic ticket. Recall that the domain classes included Driver, Officer, Ticket, and Court.

**1. Draw a domain class diagram for the ticket-processing system based on the four classes just listed and include attributes, association, and multiplicity.**

**2. List the classes that would be involved in the use cases and decide which class should be responsible for collaborating with the other classes for the use case Record a traffic ticket.**
Consider some possibilities: 1) a driver object should be responsible for recording his/her ticket; 2) the officer object should be responsible for recording the ticket that he or she writes; and 3) a ticket object should be responsible for recording itself. To record a traffic ticket, the system will want to verify the officer, verify the driver information, and then record the ticket. The ticket should be responsible for recording itself. The officer and driver are only verification.

**3. Create a set of CRC cards showing these classes, responsibilities, and collaborations for the use case.**

**4. Draw a first-cut design class diagram (DCD) based on your CRC cards.**

#### Running Cases: Community Board of Realtors
In Chapter 3 and Chapter 5, you identified and then modeled use cases for the Multiple Listing Service (MLS) application. You also identified and modeled domain classes. Use your solutions from these chapters to do the following:

**1. Draw a basic component diagram showing the architectural design for the system, assuming that it is a two-layer Internet architecture.**

**2. Use the CRC cards technique to identify the classes that are involved in the Create new listing use case.**
Recall that creating a new listing involves an agent, a real estate office, and a listing. Decide which class should have the primary responsibility for collaborating with the other classes and then complete the CRC cards for the use case.

**3. Draw a first-cut design class diagram (DCD) based on the CRD cards for this use case.**

#### Running Cases: The Spring Breaks 'R' Us Travel Service
In Chapter 3, you identified use cases for the Spring Breaks ‘R’ Us Travel Service. In Chapter 5, you elaborated those use cases. In Chapter 4, you identified the classes associated with these use cases. Using your solutions from these chapters, do the following:

**1. Draw a basic component diagram showing the architectural design for the system, assuming it is a two-layer Internet architecture.**
Note: Three components (subsystems) are identified for this architectural design. Each basically operates independently. The Reservation component works with student travelers, while the Resort component is for the resorts. They share several tables in the database. The Chat/Message component also shares some of the database, but also has its own chat data.

**2. Use the CRC cards technique to identify the classes that are involved in the Book a reservation use case.**
Recall that creating a booking involves at least a student group, a resort, a week, and a room type. Decide which class should have the primary responsibility for collaborating with the other classes and then complete the CRC cards for the use case.
Note: We are using the expanded class diagram developed in Chapter 5. We are also using the SSD developed for in Chapter 5 for Book a Reservation use case. It has five input messages to:
* findResorts
* showResortDetails
* checkAvailability
* requestReservation
* payForReservation
As shown in the solution, it has many classes involved in the solution. We used UML notation to show class level methods. This use case is pushing the limits of CRC cards. It is fairly complex.

**3. Draw a first-cut design class diagram (DCD) based on the CRD cards for this use case.**
Note: A first-cut design class diagram is a “best guess” at the navigation visibility required. It often changes as the detail design progresses. Notice in this solution that the Resort and the Traveler take responsibility for many of the actions.

#### Running Cases: On the Spot Courier Services
In Chapter 6, you considered the issues relevant to the specification of the hardware equipment and networking requirements. The case description in Chapter 6 also reviewed the three primary types of users for the system and many of their respective system-supported activities. 

**Consistent with the network that you recommended in Chapter 6, develop a component diagram.** Show which parts of the system may use general Internet access and which parts may use VPN capabilities.

In Chapter 5, you developed activity diagrams and system sequence diagrams for two use cases: Request a package pickup and Pickup a package. In Chapter 4, you developed a domain model class diagram for the system.

**For each of the two use cases, develop a first-cut design class diagram and a set of CRC cards.** The design class diagram should elaborate the attributes and show navigation visibility. You may also need to add more classes from your solution in Chapter 4. It isn’t uncommon for developers to enhance early models as they begin to understand system requirements better. The CRC cards should include classes for the Controller class and any classes for screens you identified in Chapter 7.

#### Running Cases: Sandia Medical Devices
Review the original system description in Chapter 2, additional project information in Chapters 3, 4, 6, 8, and 9, and the use case diagram shown in Figure 10-20 to refamiliarize yourself with the proposed system. Complete these tasks:

**1. Develop a deployment diagram that shows the equipment specified in Chapter 6 and the list of software components you developed while answering question 1 in Chapter 9.**

**2. For the moment, assume that the database will store two glucose levels for each patient—normal minimum and normal maximum—and that an alert will be generated if three or more consecutive glucose readings are above or below those levels. Expand the domain class diagram in Chapter 4 to include this information and then develop a firstcut design class diagram to support the patient use case View/respond to alert.**

# Chapter 12 - Object-Oriented Design: Fundamental

# Chapter 13 - Object-Oriented Design: Use Case Realization
Systems Analysis and Design in a Changing World, sixth edition
11-1

# Chapter 11 - Object-Oriented Design: Use Case Realizations

## Solutions to End-of-Chapter Problems

### Review Questions

**1. What is meant by the term use case realization?**
The term realization means to create or bring into reality. Hence use case realization means to bring the use case to life or into reality by defining the detail steps and processes required to implement it.

**2. What are the benefits of knowing and using design patterns?**
Design patterns are a widely held approach to implementing standard programming constructs. It is important to know about and to understand both the idea of design patterns and to have a repertoire of understood patterns. Just as the vocabulary for any discipline is important in order to be educated in that discipline, system developers should be aware and have a working knowledge of design patterns.

**3. What is the contribution to systems development by the Gang of Four?**
The Gang of Four were the first developers to specifically define the idea of design patterns and to identify several fundamental common design patterns.

**4. What are the five components of a standard design pattern definition?**
The name, the description of the problem or need, the description of the solution, an example or diagram of the solution, and specific benefits or consequences of this solution.

**5. List five elements included in a sequence diagram.**
An actor, objects, lifelines, activation lifelines, messages, and loop control boxes.

**6. How does a sequence diagram differ from an SSD?**
A systems sequence diagram only has one object, the system. A sequence diagram explodes the system object into all of the internal objects of the system. The idea is similar to a black box test and a white box test—one looks only at the outside while the other observes the details of what is going on inside.

**7. What is the difference between designing with CRC cards and designing with sequence diagrams?**
CRC cards is a more elementary process. It does not try to identify the messages at the same level of detail as is done with a sequence diagram. CRC cards gives an overview of the process, but leaves many details to the programmer. Sequence diagram goes more in depth.

**8. Explain the syntax of a message on a sequence diagram.**
* `*` - means multiply occurring or looping
* `[true/false]` - means test condition which is tested before the message is sent
* `return-value` - is the return value which is returned to the originator of the message
* `:=` - is used to denote that a return value exists
* `message-name` - this is the message name or service requested
* `(parameter-list)` - this is the list of data parameters being sent with the message

**9. What is the purpose of the first-cut sequence diagram? What kinds of classes are included?**
The purpose of the first-cut sequence diagram is to design and describe the logic within the problem domain objects, or the set of messages and connections between the various problem domain classes, e.g. business layer logic. Only problem domain classes are included.

**10. What is the purpose of the use case controller?**
A use case controller class is a completely artificial class that is used to provide a link between the view layer and the domain layer. A controller helps reduce the coupling between the view and domain layers in that the view layer does not need to know about all the classes in the domain layer. It only needs to know about the controller.

**11. What is meant by an activation lifeline? How is it used on a sequence diagram?**
An activation lifeline indicates the active execution or 'life' of the destination object. It is used as part of the lifeline of an object, but denoting that period of time when the object is actively executing some logic.

**12. Describe the three major steps in developing the set of messages for the first-cut sequence diagram.**
1. Start with each input message and identify all information and services that it will need in order to complete the requested service, e.g. identify all internal messages.
2. Identify all of the classes that will be involved to process.
3. Make sure each internal message is complete with parameters, true/false condition, and looping.

**13. What assumptions do developers usually make while doing the initial use case realization?**
* Perfect technology assumption
* Perfect memory assumption
* Perfect solution assumption

**14. When doing multilayer design, what is the order in which layers should be designed? Why?**
The business logic layer is done first to yield the first-sequence diagram. Often the data access layer is done next. Finally the view layer is added.

**15. What is the "separation of responsibilities" principle?**
Separation of responsibilities is the concept that each unique task within a use case should be done by a separate method/object. Don't try to jam all of the processing logic into one giant method in one class. Make the methods and the objects cohesive by having them complete the task that applies to their primary purpose or reason for being.

**16. Explain the two methods of accessing the database to create new objects in memory.**
One method is to create an empty shell of an object, say by the controller or a factory. Then in the constructor of that newly instantiated object, it will call the data access object to read the database and fill in all of the fields. The other method is to issue a call to the data access object and have it read the database and instantiate a new object, or multiple objects, based on what is returned from the database.

**17. What symbols are used in a communication diagram, and what do they mean?**
* Stick figure is an actor
* Boxes mean classes
* Lines between the boxes are links to pass messages - much like navigation visibility. Arrows with labels are the messages

**18. Explain the components of message syntax in a communication diagram. How does this syntax differ from that of a sequence diagram message?**
* `[true/false]` is the true/false condition to determine if the message is sent
* `number` is the sequence number or order of the message on the diagram
* `return-value :=` is the value returned to the originating object
* `message-name` is the name of the requested service
* `(parameter-list)` - is the data fields that are sent with the message

**19. Explain the method syntax on design classes.**
* `+/-` - is the visibility. + is visible externally, - is hidden
* `name` is the name of the method
* `parameter` - is the parameter list required by the method
* `type` - is the type of any returned values by the method

**20. What is meant by a dependency relationship? How is it indicated on a drawing?**
A dependency relationship is shown by a dashed arrow. It indicates that the item that the arrow points from (tail) is dependent on the item that the arrow points to (head). If something changes in the independent item, then the dependent item probably will also have to change.

**21. List the major implementation responsibilities of each layer in a three-layer design.**
* View layer - display forms and screens, capture external events, capture entered data, edit entered data, forward data to domain layer, start and stop the system.
* Domain layer - create and manage problem domain/persistent objects, process business logic.
* Data access layer - connect to database, access the database with SQL or equivalent, process data returned from data base and write to database, disconnect from database.

**22. What is the purpose of the adapter pattern?**
The adapter pattern is used when a new component needs to be "plugged into" an existing system, but the API is not exactly the same. The adapter adapts the API of the new component so that it can fit into the existing system.

**23. What common element is found in the singleton pattern and the factory pattern? What is the basic difference between the two patterns?**
Both have code to test if the object exists and if not to create the object. If it does exist just return it. The difference is that the singleton has responsibility for itself, where the factory takes responsibility for other objects.

---

### Problems and Exercises

**EXPLANATORY NOTE:** Chapter 11 refers to two sets problems from Chapter 5 that review the student's skills to develop a problem domain class diagram and a use case diagram. Unfortunately those two sets of problems were not included in the final iteration of Chapter 5. To do the problem sets in Chapter 11, you will need to either supply the students with a class diagram and a use case diagram, or alternatively, you may provide the problem descriptions to allow them to create a class diagram and use case diagram. The second option provides a good review alternative. Both the diagrams and the descriptions are provided below.

Problems 1 through 7 are based on the solutions you developed in Chapter 5 for problems 1 and 2, which involved a university library system. Alternatively, your instructor may provide you with a use case diagram and a class diagram.

**University Library System**
This case is a simplified version of a new system for the University Library. Of course, the library system must keep track of books. Information is maintained both about book titles and the individual book copies. Book titles maintain information about title, author, publisher, and catalog number. Individual copies maintain copy number, edition, publication year, ISBN, book status (whether it is on the shelf or loaned out), and date due back in.

The library also keeps track of its patrons. Because it is a university library, there are several types of patrons, each with different privileges. There are faculty patrons, graduate student patrons, and undergraduate student patrons. Basic information about all patrons is name, address, and telephone number. For faculty patrons, additional information is office address and telephone number. For graduate students, information such as graduate program and advisor information is maintained. For undergraduate students, program and total credit hours are maintained.

The library also keeps information about library loans. A library loan is a somewhat abstract object. A loan occurs when a patron approaches the circulation desk with a stack of books to check out. Over time a patron can have many loans. A loan can have many physical books associated with it. (And a physical book can be on many loans over a period of time. Information about past loans is kept in the database.) So, in this case, an association class should probably be created for loaned books.

If a patron wants a book that is already checked out, the patron can put that title on reserve. This is another class that does not represent a concrete object. Each reservation is for only one title and one patron. Information such as date reserved, priority, and date fulfilled is maintained. When a book is fulfilled, the system associates it with the loan on which it was checked out.

Patrons have access to the library information to search for book titles and to see whether a book is available. A patron can also reserve a title if all copies are checked out. When patrons bring books to the circulation desk, a clerk checks out the books on a loan. Clerks also check books in. When books are dropped in the return slot, clerks check in the books. Stocking clerks keep track of the arrival of new books.

The managers in the library have their own activities. They will print reports of book titles by category. They also like to see (online) all overdue books. When books get damaged or destroyed, managers delete information about book copies. Managers also like to see what books are on reserve.


**1. Figure 11-25 is an SSD for the use case Check out books in the university library system. Do the following:**
a. Develop a first-cut sequence diagram that only includes the actor and problem domain classes.

b. Develop a design class diagram based on your solution. Be sure to include your controller class.

**2. Using your solution to problem 1, do the following:**
a. Add the view layer classes and the data access classes to your diagram. You may do this with two separate diagrams to make them easier to work with and read.

b. Develop a package diagram showing a three layer solution with view layer, domain layer, and data access layer packages.

**3. Figure 11-26 is an activity diagram for the use case Return books in the university library system. Do the following:**
a. Develop a first-cut sequence diagram that only includes the actor and problem domain classes.
Note: As with all design solutions, there are several ways to implement the solution. This one assumes that information that can be scanned from the book includes a bookID and a copy#.

b. Develop a design class diagram based on the domain class diagram.

**4. Using your solution to problem 3, do the following:**
a. Add the view layer classes and the data access classes to your diagram.

b. Develop a package diagram showing a three layer solution with view layer, domain layer, and data access layer packages.

**5. Figure 11-27 is a fully developed use case description for the use case Receive new book in the university library system. Do the following:**
a. Develop a first-cut communication diagram that only includes the actor and problem domain classes.

b. Develop a design class diagram based on the domain class diagram.

**6. Using your solution to problem 5, do the following:**
a. Add the view layer classes and the data access classes to your diagram.

b. Develop a package diagram showing a three layer solution with view layer, domain layer, and data access layer packages.

**7. Integrate the design class diagram solutions you developed for problems 1, 3, and 5 into a single design class diagram.**

---

Problems 8 through 14 are based on the solutions you developed for problems 3 and 4 in Chapter 5, which involved a dental clinic system. Alternatively, your instructor may provide you with a use case diagram and a class diagram.

**Dental Clinic System**
A clinic with three dentists and several dental hygienists needs a system to help administer patient records. This system does not keep any medical records. It only processes patient administration. Each patient has a record with his or her name, date of birth, gender, date of first visit, and date of last visit. Patient records are grouped together under a household. A household has attributes such as name of head of household, address, and telephone number. Each household is also associated with an insurance carrier record. The insurance carrier record contains name of insurance company, address, billing contact person, and telephone number.

In the clinic, each dental staff person also has a record that tracks who works with a patient (dentist, dental hygienist, x-ray technician). Because the system focuses on patient administration records, only minimal information is kept about each dental staff person, such as name, address, and telephone number. Information is maintained about each office visit, such as date, insurance copay amount (amount paid by the patient), paid code, and amount actually paid. Each visit is for a single patient, but, of course, a patient will have many office visits in the system. During each visit, more than one dental staff person may be involved by doing a procedure. For example, the x-ray technician, dentist, and dental hygienist may all be involved on a single visit. In fact, some dentists are specialists in such things as crown work, and even multiple dentists may be involved with a patient. For each staff person does procedure in a visit combination (many-to-many), detailed information is kept about the procedure. This information includes the type of procedure, a description, the tooth involved, the copay amount, the total charge, the amount paid, and the amount the insurance company denied.

Finally, the system also keeps track of invoices. There are two types of invoices: invoices to insurance companies and invoices to heads of household. Both types of invoices are fairly similar, listing each visit, the procedures involved, the patient copay amount, and the total due. Obviously, the totals for the insurance company are different from the patient amounts owed. Even though an invoice is a report (when printed), it also maintains some information such as date sent, total amount, amount already paid, amount due and the total received, date received, and total denied. (Insurance companies do not always pay all they are billed.)

The receptionist keeps track of patient and head-of-household information, and will enter this information in the system. The receptionist will also keep track of office visits by the patients. Patient information is also entered and maintained by the office business manager. In addition, the business manager maintains the information about the dental staff.

The business manager also prints the invoices. Patient invoices are printed monthly and sent to the head of household. Insurance invoices are printed weekly. When the invoices are printed, the business manager double-checks a few invoices against information in the system to make sure it is being aggregated correctly. She also enters the payment information when it is received.

Dental staff are responsible for entering information about the dental procedures they perform. The business manager also prints an overdue invoice report that shows heads of household who are behind on their payments. Sometimes dentists like to see a list of the procedures they performed during a week or month, and they can request that report.


**8. Figure 11-28 is an SSD for the use case Record dental procedure in the dental clinic system. Do the following:**
a. Develop a first-cut sequence diagram that only includes the actor and problem domain classes.

b. Develop a design class diagram based on the domain class diagram.

**9. Using your solution to problem 8, do the following:**
a. Add the view layer classes and the data access classes to your diagram.

b. Develop a package diagram showing a three layer solution with view layer, domain layer, and data access layer packages.

**10. Figure 11-29 is an activity diagram for the use case Enter new patient information in the dental clinic system. Do the following:**
a. Develop a first-cut sequence diagram that only includes the actor and problem domain classes.

b. Develop a design class diagram based on the domain class diagram.

**11. Using your solution to problem 10, do the following:**
a. Add the view layer classes and the data access classes to your diagram.

b. Develop a package diagram showing a three layer solution with view layer, domain layer, and data access layer packages.

**12. Figure 11-30 is a fully developed use case description for the use case Print patient invoices in the dental clinic system. Do the following:**
a. Develop a first-cut communication diagram that only includes the actor and problem domain classes.

b. Develop a design class diagram based on the domain class diagram.

**13. Using your solution to problem 12, do the following:**
a. Add the view layer classes and the data access classes to your diagram.

b. Develop a package diagram showing a three layer solution with view layer, domain layer, and data access layer packages.

**14. Integrate the design class diagram solutions that you developed for problems 8, 10, and 12 into a single design class diagram.**

**15. In Figure 11-31, the package on the left contains the classes in a payroll system. The package on the right is a payroll tax subsystem. What technique would you use to integrate the payroll tax subsystem into the payroll system? Show how you would solve the problem by modifying the existing classes (in either figure). What new classes would you add? Use UML notation.**

---

### Solutions to End-of-Chapter Cases

#### Case Study: Move Your BooksNow.com Book Exchange
For this case, develop the following diagrams:

**1. A domain model class diagram**

**2. A use case diagram**

**3. SSDs for two use cases, such as Add a seller and Record a book order**

**4. A first-cut sequence diagram for each of the above use cases**

**5. An integrated design class diagram that includes classes, methods, and navigation attributes**

---

#### Running Cases: Community Board of Realtors
In Chapter 3, you identified use cases for the business events for the Community Board of Realtors. In Chapter 5, you elaborated on those use cases. In Chapter 4, you identified the classes associated with the business events. Using your solutions from those chapters, develop:

**1. A first-cut DCD by using the problem domain classes that you identified in Chapter 4.**

**2. A first-cut communication diagram for the Create new listing use case (domain classes and controller class only).**

**3. A first-cut sequence diagram for the Update agent information use case (domain classes and controller class only).**

**4. A multilayer sequence diagram for the Update agent information use case that includes domain classes and data access classes.**

**5. A separate multilayer sequence diagram for the Update agent information use case that includes the domain classes and the view layer classes.**

**6. A final design class diagram that includes the classes from both use cases. Include elaborated attributes, navigation arrows, and all the method signatures from both use cases.**

---

#### Running Cases: The Spring Breaks 'R' Us Travel Service
In Chapter 3, you identified use cases for the business events for the Spring Breaks 'R' Us Travel Service. In Chapter 5, you elaborated on those use cases. In Chapter 4, you identified the classes associated with the business events. Using your solutions from those chapters, develop:

**1. A first-cut DCD by using the problem domain classes you identified in Chapter 4.**
Note: This DCD is an expanded one, which also includes the classes that were added in Chapter 5 to support the use cases. Student answers will not have as many classes.

**2. A first-cut communication diagram for the Add a resort use case (domain classes and controller class only).**

**3. A first-cut sequence diagram for the Book a reservation use case.**
Note: Students can use the SSD given in Chapter 5 or the CRC cards from Chapter 10 as guidelines.

**4. A multilayer sequence diagram for the Book a reservation use case that includes domain classes and data access classes.**

**5. A separate multilayer sequence diagram for the Book a reservation use case that includes the domain classes and the view layer classes.**
Note: Due to the complexity of this diagram, it will be best to divide this use case into two pages. A good dividing point is before checkAvailability () message.

**6. A final design class diagram that includes the classes from both use cases. Include elaborated attributes, navigation arrows, and all the method signatures from both use cases.**

**7. A package diagram of the four subsystems (Resort relations, Student booking, Accounting and finance, and Social networking) that includes all the problem domain classes.**

---

#### Running Cases: On the Spot Courier Services
In Chapter 10, you developed a first-cut design class diagram and CRC card solutions for two use cases: Request a package pickup and Pickup a package. Let us extend your solution from that chapter by developing the following:

**1. A first-cut sequence diagram for each use case (domain classes and controller classes only).**

**2. A multilayer sequence diagram for each use case that includes domain classes and data access classes.**

**3. A separate multilayer sequence diagram for each use case that includes the domain classes and the view layer classes.**
(We won't combine view and data access layers on the same drawing. It makes the drawing too complex.)

**4. A final design class diagram that includes the classes from both use cases. Include elaborated attributes, navigation arrows, and all the method signatures from both use cases.**

In Chapter 9, we defined four subsystems:
* Customer account (like customer account)
* Pickup request (like sales)
* Package delivery (like order fulfillment)
* Routing and scheduling

Even though these subsystems are somewhat arbitrary, we can treat each one as a separate package. **Develop a package diagram for each of the four subsystems by assigning domain model classes to each package. A domain model class should belong to only one subsystem package. Normally, it is the subsystem that instantiates objects from that class. Also, show dependency relationships among the various packages and classes.**

---

#### Running Cases: Sandia Medical Devices
Review your answers to the case-related questions in Chapter 10 and then do the following:

**1. Develop a first-cut sequence diagram for the patient use case View/respond to alert.**

**2. Develop a multilayer sequence diagram that includes domain classes and data access classes.**

**3. Develop a separate multilayer sequence diagram that includes the domain classes and the view layer classes.**
(We won't combine view and data access layers on the same drawing. It makes the drawing too complex.)

**4. Update your DCD from Chapter 10 to include the methods you have identified. Also, include any changes you may have made to navigation visibility and attribute details.**

# Chapter 14 - Deploying the New System

Systems Analysis and Design in a Changing World, sixth edition

# Chapter 12 - Database, Security, and Controls

## Solutions to End-of-Chapter Problems

### Review Questions

## **1. List the components of a DBMS and describe the function of each.**
* **Application program interface** - An interface engine or library of precompiled subroutines that enable application programs (such as those written in C or Java) to interact with the database.
* **End-user query processor** - A program or utility that allows end users to retrieve data and generate reports without writing application programs.
* **Data definition interface** - A program or utility that allows a database administrator to define or modify the content and structure of the database (for example, add new fields or redefine data types or relationships).
* **Data access and control logic** - The system software that controls access to the physical database and maintains various internal data structures (for example, indexes and pointers).
* **Database** - The physical data store (or stores) combined with the schema.
* **Schema** - A store of data that describes various aspects of the "real" data, including data types, relationships, indexes, content restrictions, and access controls.
* **Physical data store** - The "real" data as stored on a physical storage medium (for example, a magnetic disk).

## **2. What is a database schema? What information does it contain?**
A database schema is a store of data that describes the content and structure of the physical data store (sometimes called metadata—data about data). It contains a variety of information about data types, relationships, indexes, content restrictions, and access controls.

## **3. Why are databases the preferred method of storing data used by an information system?**
Databases are a common point of access, management, and control. They allow data to be managed as an enterprise-wide resource while providing simultaneous access to many different users and application programs. They solve many of the problems associated with separately maintained data stores, including redundancy, inconsistent security, and inconsistent data access methods.

## **4. With respect to relational databases, briefly define the terms row and attribute value.**
* **Row** - The portion of a table containing data that describes one entity, relationship, or object.
* **Attribute value** - The portion of a table (a column) containing data that describes the same fact about all entities, relationships, or objects in the table.

## **5. What is a primary key? Are duplicate primary key values allowed? Why or why not?**
A primary key is a field or set of fields, the values of which uniquely identify a row of a table. Because primary keys must uniquely identify a row, duplicate key values aren't allowed.

## **6. What is the difference between a natural key and an invented key? Which type is most commonly used in business information processing?**
A natural key is a naturally occurring attribute of or fact about something represented in a database (for example, a human fingerprint or the atomic weight of an element). An invented key is one that is assigned by a system (for example, a social security or credit card number). Most keys used in business information processing are invented.

## **7. What is a foreign key? Why are foreign keys used or required in a relational database? Are duplicate foreign key values allowed? Why or why not?**
A foreign key is a field value (or set of values) stored in one table that also exists as a primary key value in another table. Foreign keys are used to represent relationships among entities that are represented as tables. Duplicate foreign keys are not allowed within the same table because they would redundantly represent the same relationship. Duplicate foreign keys may exist in different tables because they would represent different relationships.

## **8. Describe the steps used to transform a domain class diagram into a relational database schema.**
1. Create a table for each class.
2. Choose a primary key for each table.
3. Add foreign keys to represent one-to-many relationships.
4. Create new tables to represent many-to-many relationships.
5. Define referential integrity constraints.
6. Evaluate schema quality and make necessary improvements.
7. Choose appropriate data types and value restrictions for each field.

## **9. What is referential integrity? Describe how it is enforced when a new foreign key value is created, when a row containing a primary key is deleted, and when a primary key value is changed.**
Referential integrity is a content constraint between the values of a foreign key and the values of the corresponding primary key in another table. The constraint is that values of the foreign key field(s) must either exist as values of a primary key or must be NULL. A valid value must exist in the foreign key field(s) before the row can be added. When a row containing the primary key is deleted, the row with the foreign key must also be deleted for the data to maintain referential integrity. A primary key should never be changed; but in the event that it is, the value of the foreign key must also be changed.

## **10. What types of data (or attributes) should never be stored more than once in a relational database? What types of data (or attributes) usually must be stored more than once in a relational database?**
Non-key fields should never be stored more than once. If a table represents a class, the primary key values of each class represented in the table are redundantly stored (as foreign keys) for every relationship in which the class participates.

## **11. What is relational database normalization? Why is a database schema in third normal form considered to be of higher quality than an unnormalized database schema?**
Relational database normalization is a process that increases schema quality by minimizing data redundancy. A schema with tables in third normal form has less non-key data redundancy than a schema with unnormalized tables. Less redundancy makes the schema and database contents easier to maintain over the long term.

## **12. Describe the process of relational database normalization. Which normal forms rely on the definition of functional dependency?**
The process of normalization modifies the schema and table definitions by successively applying higher order rules of table construction. The rules each define a normal form, and the normal forms are numbered one through three. First normal form eliminates repeating groups that are embedded in tables. Second and third normal forms are based on a concept called functional dependency—a one-to-one correspondence between two field values. Second normal form ensures that every field in a table is functionally dependent on the primary key. Third normal form ensures that no non-key field is functionally dependent on any other non-key field.

## **13. What is the difference between a primitive data type and a complex data type?**
A primitive data type (for example, integer, real, or character) is directly supported (represented) by the CPU or a programming language. A complex data type (for example, record, linked list, or object) contains one or more data elements constructed using the primitive data types as building blocks.

## **14. Briefly describe these distributed database architectures: replicated database servers, partitioned database servers, and cloud-based database servers. What are the comparative advantages of each?**
* **Replicated database servers** - An entire database is replicated on multiple servers, and each server is located near a group of clients. Best performance and fault tolerance for clients because all data is available from a "nearby" server.
* **Partitioned database servers** - A database is partitioned so that each partition is a database subset used by a single group of clients. Each partition is located on a separate server, and each server is located close to the clients that access it. Better performance and less replication traffic than replicated servers if similar collocated clients use only a subset of database content.
* **Cloud-based database servers** - A cloud based database server is really one of the previously defined architectures, but implemented using the cloud-based services of a cloud computing vendor. The cloud provider hosts the database and provides the services across defined geographical areas. The cloud provider manages the database including synchronization and backup.

## **15. What additional database management complexities are introduced when database contents are replicated in multiple locations?**
Replicated copies are redundant data stores. Thus, any changes to data content must be redundantly implemented on each copy. Implementing redundant maintenance of data content requires all servers to periodically exchange database updates.

## **16. Describe the risk factors associated with database design.**
Since the database is an integral part of any information system, the performance and operation of the database is critical. Hence design decisions about what DBMS to use, how to configure it, and how to optimize it are usually quite complex and critically important. Another risk factor is how to integrate a new database with existing databases. New systems normally are not completely independent of existing systems and databases, and usually must interface with existing architectures. It is important that the new database not only integrate well, but that it not cause problems with existing configurations. Finally, good database design depends on having a complete, or mostly complete problem domain model. While enhancing and adding tables and attributes is possible to already constructed databases, doing so can sometimes cause sub-optimization of data structures.

## **17. When should database design be performed? Can the database be designed iteratively or must the entire database be designed at once?**
Database design is usually done as early as possible in the project. For an iterative project, it is usually designed and implemented in the earlier iterations. The database does not have to be designed completely all at once, however, it should be designed and refined as much as possible in the early iterations.

## **18. Explain four types of integrity controls for input forms. Which have you seen most frequently? Why are they important?**
* **Field combination controls** verify that the data in one field is based on the data in another field or fields.
* **Value limit controls** identify when a value in a field is too large or too small.
* **Completeness controls** ensure that all necessary fields on an input form have been entered.
* **Data validation controls** validate the input data for correctness.
*(Answers will vary on importance and frequency).*

## **19. What are the objectives of integrity controls in information systems? In your own words, explain what each of the three objectives means. Give an example of each.**
* **Ensure that only appropriate and correct business transactions occur.** This objective ensures that no erroneous or fraudulent transactions are entered. *Example:* A control to ensure that a clerk does not request a check for a service that was never provided.
* **Ensure that the transactions are recorded and processed correctly.** This objective ensures that the system processes and stores the data completely. *Example:* A control to ensure that a double-entry bookkeeping entry always processes both entries.
* **Protect and safeguard the assets (including information) of the organization.** This objective ensures that information is not lost due to theft, fire, or some other mishap. *Example:* Storing backup data periodically off site.

## **20. What are the four types of input controls used to reduce input errors? Describe how each works.**
* **Field combination control:** An integrity control that verifies that the data in one field is based on the data in another field or fields.
* **Value limit control:** An integrity control that identifies when a value in a field is too large or too small.
* **Completeness control:** An integrity control that ensures that all necessary fields on an input form have been entered.
* **Data validation control:** An integrity control that validates the input data for correctness and appropriateness.

## **21. What is the basic purpose of transaction logging?**
Transaction logging takes every update to the database and logs exactly how it happened (sometimes with an image of the transaction). It is extremely important for audit trails and for recovery in case something goes wrong.

## **22. What are the two primary objectives of security controls?**
* Maintain a stable, functioning operating environment for users and application systems (usually 24 hours a day, seven days a week).
* Protect information and transactions during transmission outside the organization (public carriers).

## **23. Briefly define or describe authentication, access control lists, and authorization.**
* **Authentication** is the process used to identify who a user is to authenticate that this is the right person. This process is often done with user ID and password. Other methods of identifying a person might be with smart card, biometric devices, and questions and answers.
* **Authorization** is done after authentication. Once a user has been verified, i.e. the system knows who it is, then that user will have rights or privileges to access particular data and system functions. He/she is authorized to access particular parts of the system.
* What parts of the system a user has access to is often determined by an **Access Control list**. An access control list contains a list of all the users and what rights or privileges he/she has.

## **24. How does single-key (symmetric) encryption work? What are its strengths? What are its weaknesses?**
A single key is used to encrypt and decrypt a message. Both parties must have the key. Its strength is that it is simple and fast. Its weaknesses are that it might be easy to break the encryption and that it is difficult to distribute the key in a secret fashion to all the authorized participants.

## **25. How does public key (asymmetric) encryption work? What are its strengths? What are its weaknesses?**
A public-key encryption has two keys, a public one that is widely distributed and a private one that is secret. To send data to the owner of the keys, someone uses the public key. The data can then only be decrypted with the private key. So, the owner is the only one who can decrypt the data. After the message is encrypted, it can only be decrypted with the private key. Its strengths are that it is very secure, and the public key can be widely distributed. So if an entity wants to receive secret messages, it can distribute its public key, and it will be the only one able to decrypt the message. One weakness is that it tends to be quite slow in decrypting. So it is not suitable for high volume, rapidly changing data.

## **26. What is a digital certificate? What role do certifying authorities play in security systems?**
A digital certificate is an institution's name and public key (plus other information such as address, Web site URL, and validity date of the certificate) that is encrypted and certified by a third party. Certifying authorities are companies that are very well known so that everybody knows for sure what their public keys are. These certifying authorities sell digital certificates to other companies (that are not as well known) so that these companies can convince their customers that they are legitimate.

## **27. What is a digital signature? What does it tell a user?**
A digital signature is a technique in which a document is encrypted using a private key to verify who wrote the document. If you have the public key of an entity, and that entity sends you a message with its private key, you can decode it with the public key. You know that the party is the one you want to communicate with because that entity is the only one who can encode a message with that private key.

---

### Problems and Exercises

## **1. The Universal Product Code (UPC) is a bar-coded number that uniquely identifies many products sold in the United States. For example, all printed copies of this textbook sold in the United States have the same UPC bar code on the back cover. Now consider how the design of the RMO database might change if all items sold by RMO were required by law to carry a permanently attached UPC (e.g., on a label sewn into a garment or on a radio frequency ID tag attached to a product). How might the RMO relational database schema change under this requirement?**
The change to the schema is relatively simple. ProductID is replaced with the UPC bar code both as the primary key of ProductItem and all corresponding foreign keys. The change might be more complex if the DBMS were previously responsible for generating values of ProductItem.Number. That function would now be removed from the DBMS because the key values would be externally assigned. This would potentially add more complexity to the system in order to determine what the UPC values were and to get them entered into the system.

## **2. Assume that RMO will begin asking a random sample of customers who order by telephone about purchases made from competitors. RMO will give customers a 15 percent discount on their current order in exchange for answering a few questions. To store and use this information, RMO will add two new classes and three new associations to the class diagram. The new classes are Competitor and ProductCategory. Competitor has a one-to-many association with Product Category, and the existing Customer class also has a one-to-many association with Product Category. Competitor has a single attribute called Name. Product Category has four attributes: Description, Dollar Amount Purchased, MonthPurchased, and YearPurchased. Revise the relational database schema shown in Figure 12-10 to include the new classes and associations. All tables must be in 3NF.**
The following tables must be added to the relational database schema:
* Competitor = **Name**
* ProductCategory = **CompetitorName**, **CustomerAccountNo**, **Month Purchased**, **YearPurchased**, Description, DollarAmount Purchased

Primary keys are shown in bold, and foreign keys are shown in italics. Note that the primary key of ProductCategory is guaranteed to be unique only if multiple customer purchases from a competitor in the same month and for the same product category (description) are combined in a single row.

## **3. Assume that RMO will use a relational database, as shown in Figure 12-10. Assume further that a new catalog group located in Milan, Italy, will now create and maintain the product catalog. To minimize networking costs, the catalog group will have a dedicated database server attached to its LAN. Develop a plan to partition the RMO database. Which tables should be replicated on the catalog group's local database server? Update Figure 12-18 to show the new distributed database architecture.**
Assumptions: Milan will have responsibility for describing and maintaining product items and accessory packages. Milan will also have responsibility for supporting and maintaining Promotions. The following tables will need to be replicated on the local LAN. Access requirements (C,R,U, and D) are shown in parentheses.
* Promotion (CRUD)
* PromoOffering (CRUD)
* ProductItem (CRUD)
* AccessoryPackage (CRUD)
* InventoryItem (R)

Updates to all of these tables are assumed to be relatively infrequent and, thus, the performance cost of complete replication with immediate or frequent updates is minimal. Milan can be represented in Figure 10-32 in the same manner as the warehouse LAN or retail store LAN.

## **4. Visit the Web site of an online catalog vendor similar to RMO (such as [www.llbean.com](https://www.llbean.com)) or an online vendor of computers and related merchandise (such as [www.cdw.com](https://www.cdw.com)). Browse the online catalog and note the various types of information contained there. Construct a list of complex data types that would be needed to store all the online catalog information.**
Answers will vary. Some examples of typical complex data types include:
* Graphic images in formats such as GIF and JPEG.
* Motion video in formats such as MPEG and AVI.
* Sound in formats such as WAV and MP3.
* Executable programs in formats such as Java and VBScript.
* Browser-formatted documents in HTML and XML.
* Hard-copy documents in formats such as Postscript or Acrobat.

## **5. This chapter described various situations that emphasized the need for controls. In the first scenario presented, a furniture store sells merchandise on credit. Based on the descriptions of controls given in this chapter, identify the various controls that should be implemented in the system to ensure that corrections to customer balances are made only by someone with the correct authorization.**
Answers will vary but should include at least the following:
* Transaction logging to note all changes (especially financial) made to the database. Log records should include the login ID of the person making the transaction.
* Financial transaction screens should be available (and visible) only via authorization of the correct level of registered user.
* Possibly a notification report of any changes (other than standard payments) made to correct account balances.

**In the second scenario illustrating the need for controls, an accounts payable clerk uses the system to write checks to suppliers. Based on the information in this chapter, what kinds of controls would you implement to ensure that checks are written only to valid suppliers, that checks are written for the correct amount, and that all payouts have the required authorization? How would you design the controls if different payment amounts required different levels of authorization?**
Answers will vary but should include at least the following:
* Both manual and automated controls might be needed for this process. The manual control will require authorization by a supervisor on paper documents for payment. Also, a paper audit trail (numbered invoice) might be required.
* Payments made only to valid suppliers can be controlled by having pre-defined PayTo fields that come from a supplier file. The supplier file should be maintained by different people to ensure separation of duties.
* Ensuring that checks are written for the correct amount can be accomplished by making sure a payment amount corresponds with the invoice amount in the system.
* A supervisor can also verify payments for correct amounts and viable suppliers. This can be done either with paper documents or with electronic forms.
* Before a check is written, a payment transaction can be approved by an electronic signature of a different person. Output reports detailing payments should be provided and reviewed.
* Internal edits can be developed to note whether payments are customary and normal. Out-of-range payments can be flagged as exceptions and verified by a manager. Different levels of payments will require the same types of controls; however, they may require different electronic signatures by higher-level registered users.

## **6. Look on the Web for an e-commerce site (such as Amazon.com or eBay). What kinds of security and controls are integrated into the system?**
Answers will vary. The following explanation uses Amazon.com as an example.
* **Data Site Pages:** Fairly easy to navigate. Lots of tabs. Has plenty of search capability. Can narrow focus by entering different portals. Some pages seem fairly busy; however, most pages are laid out fairly well. Hotlinks appear to be easy to find.
* **Data Entry:** Mostly done with clicks, which reduces data errors. Gives lots of opportunities to double check and correct choices. Implements one-click method to expedite data entry and reduce errors.
* **Security and Controls:** Use user ID and password. Do not give option of system remembering password. Make user sign in to secure server. Use secure socket layer.
* **Potential Security Problems:** Will let you work with standard, non-secure servers. If you forget your password, system allows you (or someone else) to set up a new one. Remembers all credit card information for various credit cards.

## **7. Examine the information system of a local business, such as a fast-food restaurant, doctor's office, video store, grocery store, etc. Evaluate the screens (and reports, if possible). What kind of integrity controls are in place? What kinds of improvements would you make?**
Answers will vary.

## **8. Search the Web and find out what you can about Pretty Good Privacy. What is it? How does it work? Find what you can about a pass phrase. What does it mean? Start your research at www.pgpi.org.**
Answers will vary. PGP is a program that makes your e-mail messages private. It does this by encrypting your e-mail so that nobody but the intended person can read it. When encrypted, the message looks like a meaningless jumble of random characters. PGP has proven itself quite capable of resisting even the most sophisticated forms of analysis aimed at reading the encrypted text. PGP can also be used to apply a digital signature to a message without encrypting it. This is normally used in public postings where you don't want to hide what you are saying, but rather want to allow others to confirm that the message actually came from you. After a digital signature is created, it is impossible for anyone to modify either the message or the signature without the modification being detected by PGP. PGP uses public key encryption to encrypt and decrypt e-mail messages. A pass phrase is a longer version of a password. It can be an entire phrase. It is used to generate the public key/private key combination for a PGP user.

---

### Solutions to End-of-Chapter Cases

#### Case Study: Computer Publishing, Inc.

## **1. Consider the contents of this textbook as a template for CPI's database content. Draw a class diagram that represents the book and its key content elements. Expand your diagram to include related product content, such as a set of PowerPoint slides, an electronic book formatted as a Web site or PDF file, and a Web based test bank.**

## **2. Develop a list of data types required to store the content of the book, slides, and Web sites. Are the relational DBMS data types listed in Figure 12-15 sufficient?**
Relational databases have the option of storing the actual data or of only storing a pointer to the data. Where the data is complex such as image files, video files, slide shows, and sound files, most often those are stored outside of the database with the address or locater stored in the database. If the data itself is stored in the database, then a data type of "blob" is often used.

## **3. Authors and editors are often independent contractors, not publishing company employees. Consider the implications of this fact for controls and security. How would you enable authors and editors to interact with the database? How would you protect database content from hackers and other unauthorized accesses?**
Interacting with an SQL relational database is not easy to do at the low level - at the SQL level. Therefore an entire system would need to be designed to allow authors to write text and create the figures and upload them into the appropriate places in the textbook structure. Writing and editing a textbook would probably require a different approach than an author simply sitting down and writing from front to back. The new system would need to have login capability to allow only authenticated authors to access the textbook materials. Authorization would also be required to control which parts of the textbook authors and editors could access and update. One potential problem is how to prevent the database for a particular textbook from becoming corrupted, or out of order, or jumbled if the authors entered the information incorrectly. The problem with hackers is the same as with any proprietary data that is available over the Internet. Access to the database must be through secure measures and encrypted passwords, or perhaps even more secure login procedures.

---

#### Running Cases: Community Board of Realtors

In Chapter 4, you developed a domain model class diagram. Using your previous solution or one provided to you by your instructor, update your domain model class diagram with any additional problem domain classes, new associations, or additional attributes that you have discovered as you worked through the previous chapters. Finalize this comprehensive domain model and then turn it in as part of your solution. Using this comprehensive domain model class diagram, develop a relational database schema. In the schema, identify the foreign keys that are required. Also, identify a key attribute for each table. You may need to add a key field if there isn't an attribute that could logically serve as the key. Remember that a candidate key for an association class is the combination of the keys of the connected classes. However, it may make sense to define a shorter, more concise key field. Verify that each table is in first, second, and third normal form. Discuss any discrepancies you had to fix from your first solution. Discuss any tables that may not be in third normal form and why you are leaving it as not-normalized.

Note: We will use the following class diagram from Chapter 4 problem 3 for this problem. The following changes/additions were made:
1. Commissioner was dropped. It is not a logical piece of the MLS system.
2. A few new attributes were added.


The following table:

| Table | Fields (columns) |
|---|---|
| REOffice | office_number, office_name, manager, street, city, state_province, postal_code, telephone |
| REAgent | agent_number, office_number, agent_lastname, agent_firstname, street, city, state_province, postal_code, office_phone, mobile_phone, email_address |
| Listing | listing_number, listing_type, property_street, property_city, property_state, property_postal, status_code, date_listed, date_sold, date_unlisted, asking_price, sold_price |
| ForLeaseListing | listing_number, rental_amount, rented_amount, date_available, furnishing_desc, utilities_desc |
| Owner | owner_number, owner_lastname, owner_firstname, street, city, state_province, postal_code |
| Structures | structure_number, listing_number, description, year_built, square_feet, number_bedrooms, number_bathrooms |
| AgentOnListing | agent_number, listing_number |
| OwnerOnListing | owner_number, listing_number |

Note:
* Primary key is bold. Foreign key is italicized.
* The ForSaleListing was combined with the listing table, since most listings are For Sale Listings. ForRentListing is a separate table because the information is unique and there are only a few of those types of records. A new field, listing_type, was added to denote rental listings.
* The type codes (string, integer, number, etc.) nor the length have been included; this information will have to be added before the tables can be entered into a database.
* The tables are in 3NF with one exception. State is functionally dependent on Postal_code, i. e. a state can be determined by postal code. But due to common usage of always having state and postal-code included, they are maintained together. (Alternative is to have a separate postal_code to state translation table.)

---

#### Running Cases: The Spring Breaks 'R' Us Travel Service

As with other social networking sites and systems, users of the Spring Breaks 'R' Us social networking system face such risks as identity theft, phishing attacks, and viruses. Review the following information related to social networking risks and security published by the United States Computer Emergency Readiness Team, including:
* Socializing Securely: Using Social Networking Services (www.us-cert.gov/reading_room/safe_social_networking.pdf)
* Cyber Security Tip ST06-003: Staying Safe on Social Network Sites (www.us-cert.gov/cas/tips/ST06-003.html)
* Cyber Security Tip ST05-013: Guidelines for Publishing Information Online (www.us-cert.gov/cas/tips/ST05-013.html)

After reviewing this information, revisit the questions for this case in Chapter 6 for the Social Networking subsystem. Based on the contents of this chapter and the information contained in the readings, what specific controls and security measures should be incorporated into the Social Networking subsystem?

Answers will vary. There is always an issue about how easy to make it for friends to "find" and "interact" with each other, when contrasted with how secure (i.e. how difficult) the system to be. Students should address such things as:
* **Login Protection:**
    * Strong passwords
    * Remember MAC address
    * Personal questions
* **Connection Protection:**
    * What is allowed to be searched to find people
    * What is publicly viewable
    * Approval process for connected friends
* **Posting Protection:**
    * What can be posted on one's own account
    * What can be posted on friend's account
* **Viewing Protection:**
    * Different categories of friends
    * Privacy settings for posted materials
* **Log off protection:**
    * Automatic log off based on time or activity

---

#### Running Cases: On the Spot Courier Services

In Chapter 6, you discussed hardware requirements, and in Chapter 10, you developed component and deployment diagrams. Based on your work in those chapters, take these steps:
1. For each user and each type of device, discuss what security precautions and techniques should be used to protect access to the device itself.
2. For each user and each type of device, discuss what security precautions and techniques should be used to protect access to the application programs, connect to the home system, and protect the data being transmitted to the foreign devices.
3. Discuss any security precautions and techniques you would recommend for the home office and the network servers.

Answers will vary.

| User | Device | Protect Device | Protect data, connection, and software |
|---|---|---|---|
| Customer | Customer computer | Customer responsibility | Customer login required, Strong passwords required, Encrypt sent data (HTTPS), Validate all data entered to guard against XSS attacks, etc. |
| Delivery Person | Mobile device | Install tracking software (GPS), Have secure place in truck, Serial number on device | User login required, Encrypt all data transmitted, Limited inputs and outputs, Validate all inputs, Routes start/stop times to validate inputs |
| Warehouse person | Scanning device | Keep in warehouse, Have secure storage location, Serial number on device, Check out/check in device | Limited data transmittal, Keep software up to date, Validate device and expected inputs |
| Warehouse person | Warehouse computer | Keep in secure office, Automatic turn off | Login required, Automatic turn off |
| Bill | Home laptop | Bill keep in secure location | Keep software up to date, Login required, MAC address remembered, VPN Encrypted connections |
| Bill | Warehouse servers | Keep in secure office, Server security software | Validate all inputs, Encrypt all data transmissions, Keep software up to date |

---

#### Running Cases: Sandia Medical Devices

**Part 1.**
Review the original system description in Chapter 2, the additional project information in Chapters 3, 4, and 8, and the domain class diagram shown in Figure 12-26 to refamiliarize yourself with the proposed system. Assume that the type attribute of the AlertCondition class identifies one of three alert types:
1. Glucose levels that fall outside the specified range for 15 minutes (three consecutive readings)
2. Glucose levels that fall outside the specified range for 60 minutes (12 consecutive readings)
3. An average of glucose levels over a eight-hour period that falls outside a specified range

The specified range for an AlertCondition object is the set of values between and including lowerBound and upperBound. AlertCondition objects also include an effective time period specified by the attributes startHour and endHour, which enables physicians to set different alert parameters for sleeping and waking hours. When an alert is triggered, an object of type Alert is created and associated with an alertCondition object. The dateTime attribute records when the Alert object was created, and the value(s) attribute record(s) the glucose levels (alert types 1 and 2) or average level (alert type 3) that fell outside the specified range. Each Alert object is indirectly related to a Patient object via the association between Alert and AlertCondition and the association between AlertCondition and Patient. Develop a set of relational database tables based on the domain class diagram. Identify all primary and foreign keys, and ensure that the tables are in 3NF.

The following table:

| Table | Fields (Columns) |
|---|---|
| Patient | patientID, physicianID, deviceID, medical_rec_number, last_name, first_name, birthdate, gender, race, height, weight |
| Physician | physicianID, last_name, first_name |
| Monitor Device | deviceID, serial_number, manufacturer, manufacture_date, firmware_version |
| AlertCondition | alert_condID, patientID, type, start_hour, end_hour, upper_bound, lower_bound |
| Alert | alert_number, alert_condID, date_time, value |
| CellPhone | phoneID, patientID, phone_number, operating_system, os_version, application_version |
| Glucose Observation | observation_number, patientID, date_time, level |

Primary keys. Foreign Keys. All tables are in 3NF. (Correctly built class diagrams always result in tables in 3NF.)


# Data flow diagrams

A Data Flow Diagram (DFD) is a graphical technique used by systems analysts to show how data moves through an information system. I.e. from Input to the resulting output or useful information.

Take note: A set of DFDs provides a logical model that shows what the system does, not how it does it

DFD use four basic symbols representing:
* Processes
* data flows
* data stores and
* External entity.

(Refer to Gane and Sarson symbols in your prescribed text book)

Below is a brief of what each symbol in DFD represents;

**Process** - A process represents an activity or a function that is performed for some specific reason. It can be manual or computerized but ultimately each process should perform only one activity. 

Processes can vary from simple to complex. A process receives input data and produces output. The output has different content or/and form. The process contains business logic also called business rules that act on the inputs to convert them into output. 

The name of the process appears inside the tringle. The process name identifies a specific function and consist of a verb (and an adjective, if necessary) followed by a singular noun. Examples include: CALCULATE STUDENT DP, VERIFY ORDER, and VERIFY CUSTOMER DETAILS.

Processing details are never shown on a DFD. The document logic is documented in a process description NOT revealed in the process symbol.

The following terms are commonly applied to processes:
* **Black box** - it's a metaphor for a process or action that produces results in a non-transparent or non-observable manner. A process symbols is referred to as a black box. The inputs, outputs and general function of the process is known whereas the underlying details and logic of the processes are hidden.
* **Spontaneous generation** - refers to a process in a data flow diagram that has no inputs. (Note this is not desirable when you construct a DFD. A process must have inputs and outputs)
* **Black hole** - it's a process that has input but has no output. (Note this is not desirable when you construct a DFD. A process must have inputs and outputs)
* **Grey hole** - it's a process that has at least one input and one output, but the input is insufficient to generate the output shown. (Note this is not desirable when you construct a DFD. Inputs should provide sufficient data to yield outputs)

**Data Flow**
A data flow is a flow of a piece of data moving from one part of system to another. It may represent a single data item or a set of data items. 
The data flow does not show the detailed content. The details are included in the data dictionary. 
The data flow name consists of a singular noun and an adjective if needed. Example include: DEPOSIT, INVENTORY, STUDENT GRADE, CUSTOMERS. 
A dataflow name may appear below, above or a alongside the line that represent data flow item. A dataflow must at least have a process symbol on at least one end.

**Data Store** - a data store represents collection of data that the system stores and may be used later by one or more processes. 
The DFD does not show detailed contents of the data store, they are defined in the data dictionary. 
The name of the data store appears between the lines of the symbol. 
A data store name is always in Plural consisting of a noun with or without an adjective. Example: STUDENTS, PURCHASE REQUISITIONS, PRODUCTS. 
A data store must be connected to a process with a data flow. A data store must have at least one incoming and one outgoing data flow.

**External Entity** - an external entity may be a person, organization, or system that is external to the system but interacts with it and may provide data (input) to the system or may receive information (output) from the system. 
Entities are also called Terminators because they are either origin of data or final destination. 
An entity that supply data to the system may be called a source. An entity that receive data from the system may be referred to as a sink. 
An entity name should be singular. Each entity must be connected to a process by data flow.

**Context Diagram**
A context diagram represents the first step in constructing a set of DFD's for the system. It represents the highest-level overview of an information system that shows the system's boundaries and scope. It represents the system with a single process and then shows the external agents with Which the system interacts. 

Data flows are used to link the external entities with the process. Data stores are not part of the context diagram because they are contained within the system and remain hidden until more detailed diagrams are created. 

A context diagram is often assigned the name of the system and does not start with a verb as do other processes. By creating the context diagram first, the system analyst focuses on the outward communications and exchanges and later the inward communications and exchanges. 

After the context diagram is created the process is exploded to the next level to show the major processes in the system. Depending upon the complexity of the system, each of these processes can also be exploded into their own process model. The process of explosion continues until the goal of each process accomplishing a single function is reached. 

Because the context diagram is the highest level, the process in context diagram is designated Process 0 (zero).

**Diagram 0 (Zero)**
In order to show the details inside the context diagram (process zero), a DFD diagram 0 (zero) is created. Diagram 0 is the DFD one level below the context diagram. Diagram zero shows major processes, data flows, data stores hidden in the process zero of the context diagram. 

When the context diagram is expanded, it's important to retain all the connections that flow into and out of process 0. Depending on the system, diagram zero is expanded/exploded further to lower levels to reveal more processes, data stores and data flows. This expansion goes on until a state is reached whereby a process consists of a single function that may not be exploded further. 

A process that consists of a single function is called a Primitive process. When a DFD is exploded to a lower level, the higher-level diagram is referred to as the parent diagram and the lower level diagram is referred to as the child diagram. In order to accurately create lower level DFD, levelling and balancing techniques are used. 

(Refer to your prescribed book chapter 5 for detailed illustration on how to move from context diagram to diagram 0 and beyond)

**LEVELING**
It's the process of drawing a series of increasingly detailed DFD until all primitive processes are identified. Other terms used for levelling are: exploding, portioning, or decomposition. The process begins with constructing a context diagram, followed by diagram 0 (zero). This is followed by creating lower level DFDs. 
Also, note the numbering of processes in the lower DFD with reference to the parent process in the higher DFD.

(Refer to chap 5 in your prescribed book for detailed illustrations)

**BALANCING**
It's the process that aims at maintaining consistency among set of DFD by ensuring that the total inputs and outputs of the parent DFD are maintained on the child DFD (refer page 194-196 prescribed book for illustrations)

**Some basic guidelines for drawing DFD**
1. A process must have both data inflows and outflows. Name of the process appears inside the rectangle. Process name identifies a specific function and consist of a verb (and an adjective, if necessary) followed by singular noun. Examples. STUDENT
2. All data flows must be labeled with the precise data that is being exchanged.
3. Each Process must have a unique name and a reference number. Names should start with a verb and end with a descriptive noun with exceptional of a context diagram.
4. Data flows are named as descriptive nouns.
5. A data store must have at least one data inflow.
6. A data flow cannot go between an external entity and a data store, but a process must be in between.
7. Data flow lines must never cross


# Normalization

Normalization is a process in which we systematically examine relations between tables for anomalies and, when detected, remove those anomalies by splitting up the relation into two or more new, related tables.

To help us properly design tables we have a set of guidelines which, if followed properly, will help reduce the redundancy and chance of data corruption. We call this "Normalization".

The normalization process involves three stages, namely: first normal form (1NF), second normal form (2NF), and third normal form (3NF). The Three normal forms are constructed in progression, and the 3NF represents the best design.

Tables that have reached the 3NF are considered as "normalized".

Normalization is used for mainly two purposes:
* Eliminating redundant (repeated or useless) data.
* Ensuring data dependencies make sense i.e. data is logically stored.

### Problem without Normalization

Without Normalization, it becomes difficult to handle and update databases without facing loss of data. And hence anomalies would result.

**Example of Problem without Normalization:**
To understand these anomalies let us take an example of a Student table below with four fields. Assume Student_id is the primary key.

| Student_id | Student_Name | Student_Address | Subject |
| :--- | :--- | :--- | :--- |
| 401 | Adam | Silver Town | Bio |
| 402 | Boko | Mpekweni | Maths |
| 403 | Sipho | kimberly | Maths |
| 401 | Adam | SilverTown | Physics |

The table contains a repeated set of fields on student 401:

| | | | |
| :--- | :--- | :--- | :--- |
| 401 | Adam | Silver Town | Bio |
| 401 | Adam | Silver Town | Physics |

This will essentially result into the following practical anomalies:
* **Update Anomaly:** To update the address of a student e.g., Adam who occurs twice in a table, we will have to update the `S_Address` column in all the rows, else data will become inconsistent.
* **Insertion Anomaly:** Suppose for a new admission, we have a Student id, name and address of that student but if the student has not opted for any subjects yet then we have to insert NULL/BLANK there, leading to Insertion Anomaly.
* **Deletion Anomaly:** If (Student_id) 402 has only one subject and temporarily he drops it, when we delete that row, the entire student record will be deleted along with it.

So in order to avoid these problems we carry out the Normalization procedure.

---

### First Normal Form (1NF)

A table is in first normal form (1NF) if it does not contain repeating groups. This means each row of data must have a unique identifier. In order to achieve this, the normalized design is expanded to include a primary key.

For example consider a student table below which is in un-normalized form:

**Student Table:**

| Student_id | Student_Name | Subject_ID | Subject |
| :--- | :--- | :--- | :--- |
| 401 | Adam | 101 | Biology |
| 401 | Adam | 121 | Physics |
| 402 | Boko | 131 | Maths |
| 403 | Sipho | 131 | Maths |

You can clearly see here that student id and corresponding student name Adam are used twice in the table and subject maths with corresponding subject id 131 is repeated as well. These constitute repeating groups and hence violates the First Normal form. 

To reduce the above table to First Normal form, break the table into two different tables: Student table and Subject table.

**Student Table:**
| Student_id | S_Name |
| :--- | :--- |
| 401 | Adam |
| 402 | Boko |
| 403 | Sipho |

**Subject Table:**
| Subject_ID | Subject |
| :--- | :--- |
| 101 | Biology |
| 121 | Physics |
| 131 | Maths |

Now both the Student table and Subject table are normalized to first normal form because they do not have repeating groups of data.

---

### Second Normal Form (2NF)

A table to be in Second Normal Form (2NF) should meet all the requirements of First Normal Form (1NF). In addition, all other fields which are not part of the primary key must be functionally dependent on the entire key. Implying that there must not be any partial dependency of any field on the primary key. 

It means that for a table that has a combination of fields as the primary key, each of the other fields in the table that is not part of the primary key must depend upon the entire combined primary key for its existence. If there is at least one field that depends only on one part of the combined primary key, then the table fails 2NF.

For example, consider the Customer table below:

**Customer Table:**

| Cust_id | Cust_Name | Order_id | Order_Name | Sale_Detail |
| :--- | :--- | :--- | :--- | :--- |
| 101 | Adam | 10 | Order1 | Sale1 |
| 101 | Adam | 11 | Order2 | Sale2 |
| 102 | Boko | 12 | Order3 | Sale3 |
| 103 | Sipho | 13 | Order4 | Sale4 |

In the Customer table above, if a combination of `Cust_id` and `Order_id` is made the primary key, then there are no repeating groups and hence this table is in 1NF.
`CUSTOMER (Cust_id, Order_id, Cust_Name, Order_Name, sale_Detail)`

However, there are partial dependencies of fields on the primary key. `Customer_Name` is only dependent on `customer_id`, likewise `Order_name` is dependent on only `Order_id`. Only `sale_detail` depends on the primary key (both `Customer_Id` and `Order_Id`) of table CUSTOMER.

To reduce the Customer table to Second Normal form break the table into the following three different tables in order to remove the partial dependencies:

**Customer Table:**
| Customer_id | Customer_Name |
| :--- | :--- |
| 101 | Adam |
| 102 | Boko |
| 103 | Sipho |

Here `customer_id` is the primary key.
`CUSTOMER(Customer_id, Cust_Name)`

**Order Table:**
| Order_id | Order_name |
| :--- | :--- |
| 10 | Order1 |
| 11 | Order2 |
| 12 | Order3 |
| 13 | Order4 |

Here the `order_id` is the primary key.
`ORDER (Order_id, Order_Name)`

**Sale Detail Table:**
| Order_ID | Customer_ID | Sale_detail |
| :--- | :--- | :--- |
| 10 | 101 | Sale1 |
| 11 | 101 | Sale2 |
| 12 | 102 | Sale3 |
| 13 | 103 | Sale4 |

In the `sale_detail` table, the primary key is a combination of `Order_Id` and `Customer_ID`. Also note each component of the primary key is a foreign key as well in this table.
`SALE-DETAIL (Order_id, Customer_id, Sale_detail)`

Now all these three tables comply with Second Normal form.

---

### Third Normal Form (3NF)

Third Normal form stipulates that every non-key field of a table must be dependent on the primary key. The table must be in Second Normal form. Hence in First Normal Form as well. The 3NF design removes the redundancy and data integrity problems that may still exist in the 2NF.

Consider the Student_Detail table with following fields: Student id, student name, date of birth (DOB), street, city and postal code. I will present the field names in short form.

**Student_Detail Table:**

| ID | Name | DOB | Street | City | Province | Pcode |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| R145 | Jack | 30011998 | Ibhayi | PE | EC | 6001 |
| R155 | Amanda | 15081996 | Vincent | JHB | GP | 2019 |
| R4235 | Sipho | 12051999 | Phola | Hazy view | MP | 1240 |

`STUDENT (Stu_id, stu_name, DOB, Street, City, Province, Postal_code)`

In this table `Stu_id` is the Primary key. However, in a real sense, Street, city and Province depend upon `Postal_code` not necessarily on the `Stu_id` which is the primary key. This may cause data integrity problems. So the table is not in 3NF.

In order to apply 3NF, we need to move the street, city and province to a new table (ADDRESS), with Postal code as primary key.

**Address Table:**
`ADDRESS(Postal_code, Street, City, Province)`

**Student Table:**
`STUDENT(Stu_id, stu_name, DOB, Postal_code)`

The database design is now in 3NF. In this way the amount of data duplication is reduced and data integrity is achieved. 

*Note: `Postal_code` is a foreign key in table STUDENT. It links the student table data to the address table details.*


**Part 2.**
Based on what you learned in this chapter about databases, controls, and system security, review your answers to the questions for this case in Chapter 6. Assume that the patient's cell phone and the centralized servers are different nodes in a replicated database architecture and are regularly synchronized. What changes, if any, should be made to your answers now that you have a deeper understanding of databases, controls, security, and related design issues?

Answers will vary by student.

Use Case Diagram

Domain Model Class Diagram

Use Case Description

Storyboard

Relational Database Schema

First-cut design class diagram

Final design class diagram

First-cut sequence diagram

Multilayer design for sequence diagram




test
