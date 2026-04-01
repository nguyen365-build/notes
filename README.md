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

# Chapter 7 - Defining the System Architecture

# Chapter 8 - Designing the User Interface

# Chapter 9 - Designing the Database

# Chapter 10 - Approaches to System Development

# Chapter 11 - Project Planning and Project Management

# Chapter 11 - Project Management Techniques

# Chapter 12 - Object-Oriented Design: Fundamental

# Chapter 13 - Object-Oriented Design: Use Case Realization

# Chapter 14 - Deploying the New System

Use Case Diagram

Domain Model Class Diagram

Use Case Description

Storyboard

Relational Database Schema

First-cut design class diagram

Final design class diagram

First-cut sequence diagram

Multilayer design for sequence diagram


