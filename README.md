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
## Solutions to End-of-Chapter Problems 

### Review Questions 

### **1. List and briefly describe the five activites of systems analysis.** 
* Gather detailed information - meet with users to understand the business processes and needs 
* Define requirements document findings by building models such as use case diagram and class diagram 
* Prioritize requirements - Decide which requirements (such as use cases) should be done first 
* Develop user-interface dialogs work with the users to define exactly how they will use the system and what interactions with the system are required 
* Evaluate requirements with users  - ensure that the requirements are complete, accurate, and prioritized correctly 

**2. What are three types of models?** 
Textual models, graphical models, and mathematical models 

**3. What is the difference between functional requirements and nonfunctional requirements?** 
Functional requirements describe the business rules that must be supported by the new system, while non-functional requirements are the system characteristics such as speed, throughput, response time, and security.  Both are important. 

**4. Describe the steps in preparing for, conducting, and following up an interview session.** 
Prepare for an interview by establishing the objective, determining the users and project team members, write questions, review preliminary materials, set up the interview time and location and tell everybody.  Conduct the interview by asking questions, looking for exception conditions and probing for good details.  Also take good notes, and document all the follow-up items.  Follow-up the interview by reviewing everybody's notes, building the models as necessary, document open issues, then follow-up with them.  Be sure to thank contributors. 

**5. What are the benefits of doing vendor research during information-gathering activities?** 
It can inform the current team and users of new ideas and possibly more effective methods  The team can possibly find out about more current state-of-the-art solutions that vendors have created.  It may even be cheaper, faster, and more effective to purchase a solution instead of building. 

**6. What types of stakeholders should you include in fact finding?** 
Both internal and external stakeholders.  Internal stakeholders would include operational people who work with the system and executive stakeholders who may receive executive reports, or depend on the success of the system. [cite: 486, 489] External stakeholders may include customers or partner organizations, who also receive information directly from the system.  At the executive level, external stakeholders may be investors or regulators. 

**7. Describe the open-items list and then explain why it is important.** 
During fact finding activities, and in fact throughout all the project, some issues can be answered immediately, but others cannot be answered immediately.  Some questions may not be answered because more research may need to be done, or other items may need to be decided first, or the user procedure has not be finalized, etc.  Those items will need to be tracked so that they are not left out of the solution system.  The open-items list provides that tracking function by noting the item, assigning a responsible person, and tracking the completion of the open item. 

**8. List and briefly describe the six information gathering techniques.** 
Information gathering techniques include 
* Interview users and stakeholders - the most effective for information gathering, but the most expensive 
* Distribute questionnaires  - good for finding overview or summary information from many people [cite: 500, 501]
* Review current system documentation - good for understanding current processes 
* Observe current business processes  - also good for understanding the user's processes and requirements [cite: 504, 505]
* Research vendor solutions good for generating new ideas and learning what already has been done 
* Collect user comments good for finding out about problems with current processes 

**9. What is the purpose of an activity diagram?** 
One purpose of an activity diagram is to document current user workflows.  Activity diagrams are often called workflow diagrams.  They can be used to document a user procedure as he/she interacts with the computer system. 

**10. Draw and explain the symbols used on an activity diagram.** 
See Figure 2-14. 

---

### Problems and Exercises 

**1. Provide an example of each of the three types of models that might apply to designing a car, a house, and an office building.** 
* **Car:**  Mathematical model might be a set of calculatations having to do with horse-power, torque and acceleration.  Graphical model might be a set of 3 dimensional drawings of the body style.  Textual model might be some written specification of the materials to be used. 
* **House:**  Mathematical model might be some calculations to deteremine angle of roof and types of materials needed.  Graphical would be a set of blueprints.  Descriptive textual model might be a description of the materials to be used. 
* **Office building:**  An office building might have all types of mathematical models of the stresses and earthquake requirements.  Graphical would be blueprints or even a 3 dimensional physical model.  Descriptive textual model could be of materials or steps in the construction process. 

**2. One of the toughest problems in investigating system requirements is to make sure they are complete and comprehensive.**  **How would you ensure that you get all the right information during an interview session?** 
Answers should include the following points: 
* Ensure that all stakeholders are identified and included in the requirements definition activities. 
* Review every existing form and report to make sure that all information needs are understood. 
* Identify and understand every business activity.  Be sure that all business procedures have been discussed. 
* Ensure that all exception conditions have been identified and associated processing has been defined. 
* Maintain an open-items list and ensure that all items are resolved. 

**3. One of the problems you will encounter during your investigation is "scope creep" (i.e., user requests for additional features and functions).**  **Scope creep happens because users sometimes have many unsolved problems and the system investigation may be the first time anybody has listened to their needs.**  **How do you keep the system from growing and including new functions that should not be part of the system?** 
This problem is really a project management issue.  The project manager should establish guidelines to control this problem.  One preventative method is to be sure that the initial scope definition is adequate and comprehensive.  A partial definition during the scoping activities will exacerbate the problem of scope creep. [cite: 542, 545] Even for Agile projects, the users and the project team should attempt to do a thorough job of identifying all of the functional requirements. 
An effective way to control scope creep is to establish a committee that consists of both project team members and user (or client) members.  All new additions to the scope of the system need to be approved by the committee.  Prior to approval, an estimate should be done to determine the criticality of the request and the impact on the project schedule.  The client and the users should participate in the decision so that it is a combined decision and not dictated by the project manager.  An additional technique is to begin a list of enhancements for the next version of the system.  Some requests can easily be deferred to a later version. 

**4. What would you do if you got conflicting answers for the same procedure from two different people you interviewed?**  **What would you do if one was a clerical person and the other was the department manager?** 
The first thought would be to take the opinion of the department manager as the correct answer.  However, it is not uncommon for the department manager to be behind on some of the latest details of business procedures.  The best solution in this case is to get the two people together and let them discuss the differences until they both agree on the correct procedure.  The systems analyst should not make the decision as to which answer is correct, nor should he or she try to resolve the difference.  It is the users' responsibility to do so. 

**5. You have been assigned to resolve several issues on the open-items list, and you are having a hard time getting policy decisions from the user contact.**  **How can you encourage the user to finalize these policies?** 
Delayed policy decisions impact the project schedule.  Sometimes the user does not understand the impact of delayed decisions.  Thus, the first approach should be to explain the negative impact that a given decision is having on the project.  If that doesn't work, then stronger measures can be taken, such suggesting that the project steering committee review the outstanding-items list.  Also, if the outstanding-items list indicates the length of time that items have been open, the analyst can assign or adjust the priority of those items that have become critical. 

**6. In the running case of RMO, assume that you have set up an interview with the manager of the shipping department.**  **Your objective is to determine how shipping works and what the information requirements for the new system will be.**  **Make a list of questions-open ended and closed ended-that you would use.**  **Include any questions or techniques you would use to ensure you find out about the exceptions.** 
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

**7. Develop an activity diagram based on the following narrative.**  **Note any ambiguities or questions that you have as you develop the model.**  **If you need to make assumptions, also note them.** 
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

**8. Develop an activity diagram based on the following narrative.**  **Note any ambiguities or questions that you have as you develop the model.**  **If you need to make assumptions, also note them.** 
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

**9. Conduct a fact-finding interview with someone involved in a procedure that is used in a business or organization.**  **This person could be someone at the university, in a small business in your neighborhood, in the student volunteer office at the university, in a doctor's or dentist's office, or in a volunteer organization.**  **Identify a process that is done, such as keeping student records, customer records, or member records.**  **Make a list of questions and then conduct the interview.**  **Remember, your objective is to understand that procedure thoroughly (i.e., to become an expert on that single procedure).** 
Responses will vary.  Answers should include both closed-ended questions and open-ended questions.  Anwers might also include some questions to address exception conditions.  Answers to the questions can be written in text form or presented in an activity diagram. 

**10. Using RMO and the CSMS as your guide, develop a list of all the procedures that may need to be researched.**  **You may want to think about the exercise in the context of your experience with such retailers as L.L. Bean, Lands' End, or Amazon.com.**  **Check out the Internet marketing done on the retailers' Web sites and then think about the underlying business procedures that are required to support those sales activities.**  **List the procedures and then describe your understanding of each.** 
Answers will vary, but a good set of procedures might include all of the use cases identified in Figure 3-11 of the next chapter.  Figure 3-11 has five subsystems, each with several use cases. 

---

## Solutions to End-of-Chapter Cases 

### Case Study: Jacob and Jacob, Inc. On-Line Trading System 

**1. What is the best method for Edward to involve the brokers (users) in development of the new online trading system?**  **Should he use a questionnaire? Should he interview the brokers in each of the company's 30 offices, or would one or two brokers representing the entire group be better?**  **How can Edward ensure that the information about requirements is complete, yet not lose too much time doing so?** 
This situation is a viable candidate for a questionnaire.  The users are dispersed and probably diverse.  The questionnaire should focus on needs and preferences and can also help to establish which topics need further refinement.  It will probably cost too much to interview the brokers in all of the offices.  One way to select offices is to develop a set of characteristics that distinguish the various offices, and then to select a representative office from each set of similar offices.  If the answers to questions are very similar as interviews progress, it may be possible to abbreviate or shorten later visits to offices.  If there is a wide variation between needs and procedures, then additional interviews can be scheduled. 

**2. Concerning customer input for the new system, how can Edward involve customers in the process?**  **How can he interest them in participating? What are some ways that Edward can be sure that the customers he does involve are representative of Jacob and Jacob's entire customer group?** 
This may also be a viable candidate for a questionnaire.  Statistically, sampling can guarantee that a large enough group can be studied, at least for the questionnaire.  The questionnaire should focus on the types of services and reports (statements) that the customer receives from the system.  If interviews are needed, some distinguishing characteristics should first be identified.  Then, representative samples of customers could be interviewed.  The cost of interviewing can also be controlled through the use of telephone interviews. 

**3. As Edward considers what other stakeholders he should include, what are some criteria he should use?**  **Develop some guidelines to help him build a list of people to include.** 
Guidelines include: 
* Look at all the existing reports and destinations.  All of the destination persons will have an interest in the information provided by the system. 
* Look at all the different departments in the company to see if they currently receive or need to receive information from the new system. 
* Consider senior management to see if strategic information needs to be maintained and reported. 

---

### Running Cases: Community Board of Realtors 

**1. Who are the stakeholders for the issues related to real estate in your community, and what are their main interests?** 
Answers will vary.  Usually for each state/county there are such organizations as: 
* A Division of Real Estate for the state.  Often in a state's department of commerce 
* A state Association of Realtors 
* A state Multiple Listing Service 
* Local Realtor Boards and Associations 
* Real Estate Offices and Agents 

**2. What types of information does the board collect and make available to its members and to the community?** 
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

**3. Research the real estate industry in at least two countries other than the United States.**  **For each of these countries, what are some of the cultural and legal issues that differ from those in the United States?**  **If you were working on support for an international real estate cooperative system, in what ways would the information collection activity process be complicated?** 
Answers will vary. 

---

### Running Cases: The Spring Breaks 'R' Us Travel Service 

**1. Who are the stakeholders for SBRU? For each type of stakeholder, what aspects of the SBRU booking system are of particular interest?** 
* Students Student booking, Social Networking, Accounting and Finance 
* Resorts - Resort relations, Student Booking, Social Networking, Accounting and Finance 

**2. What are the main functional requirements for the major subsystem areas (i.e., resort relations, student booking, accounting and finance, and social networking)?** 
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

**3. Describe some usability requirements for students, booking interactions, and social networking interactions.** 
Students will be using all types of laptops, tablets (iPads), smartphones (iPhones) to make reservations, check status, and especially social networking.  Displays must be adaptable for all these types of computing devices.  Internet access will also be through ethernet, Wifi, and telephone access, with the varying speeds associated with each.  Hence images and text should be combined judiciously. 

**4. Assuming that social networking at the resorts will require wireless communication and connection to the Internet, what are some reliability requirements that resorts might be asked to maintain?**  **What are some performance requirements? Is this a bigger issue because resorts are in international locations?** 
Social networking capabilities can be provided two ways, either through SBRUs central servers or locally through the resort's server.  For smaller resorts using SBRU servers - provide high-bandwidth access to the Internet.  Service level should be close to 100% availability with very wide bandwidth.  For those resorts with high usage of SBRU clients, they may want to provide local connectivity services.  This would require the same support as the smaller resorts, but also allow local chatting and communication ability.  For international resorts sometimes there are problems of connectivity, bandwidth, and reliability.  Resorts that want to join SBRU will require a minimum service level guarantee. 

**5. What are some security requirements? Is there any reason why students in Europe, Asia, or other locations could not book rooms through SBRU?**  **What issues might be anticipated?** 
There are many security issues that must be addressed. 
1. Resorts have accounts with resort availability, reservations, accounts, and payments.  Different levels of security, data transmittal, and authorization is required.  Resort information only requires protection from hacking and defacing.  Reservations contain personal information and use HTTPS sites with TLS.  Consideration should be given to encryption.  Account and payment information most definitely requires TLS and encryption. 
2. Student information is also personal and private.  It will include payment and credit card information.  All financial information requires TLS and encryption. 
3. Social networking capabilities require protection of personal information and "friend" information. 
It SBRU should be able to support students from throughout the world. [cite: 774, 775] However, supporting international students may require web pages to be translated into other languages.  It will also require establishing relationships with international bank clearing houses to handle different currency systems. [cite: 777, 780]

**6. To collect information on functional requirements for the social networking subsystem, what are some techniques that might be used?**  **Be specific and include some sample questions you might ask by using various techniques.** 
Assuming SBRU has an existing system, with existing student customers and desires to add social networking (thus an existing customer base does exist).  The social networking system should be heavily driven by student desires and requests.  Some possible ways to determine the functional requirements are: 
1. Review other social networking sites to see how they work. 
2. Send out questionnaires to existing customers on the desirability and possible use of social networking. 
3. On selected customers conduct telephone interviews to elaborate student desires. 
4. After a social networking capability has been added, then use ongoing evaluation questionnaires to refine the usability and functional effectiveness of the system.  (For example after a vacation give an incentive to collect student feedback on the resort, the booking system, and the social networking system) 

---

### Running Cases: On the Spot Courier Services 

**1. Who are the stakeholders for On the Spot? How involved should On the Spot's customers be in system definition?**  **As the business grows, who else might be potential stakeholders and interested in system functions?** 
Stakeholders include: 
* Bill Wiley owner 
* Customers, usually businesses 
* Delivery persons 
* Warehouse staff 
Since Bill was the visionary for the business and the system, he will understand the needs of the system.  However, since he is letting business customers use the system to schedule packages, it would be a good idea to form a focus group of users who would be willing to help in requirements definition. [cite: 802, 803] Both the delivery persons and the warehouse staff will have suggestions on how to make their jobs easier.  They should be involved in requirements definition.  Bill's accountant should be involved to ensure that the system has sufficient financial information and controls. 

**2. If you were commissioned to build a system for Bill, how would you determine the requirements?**  **Be specific in your answer. Make a list of the questions you need answered.** 
Since this is a small start-up company, the work procedures are very probably not efficient and probably are not scaleable.  Therefore, care should be taken not to build the system to only support these small scale work procedures.  Either of two approaches can be taken.  If Bill has a good vision of how he wants his business to function as it expands and grows, then interviewing Bill is a good starting place.  However, if Bill is still focusing on the current procedures, it may be a good idea to start by research commercial solutions from vendors.  The courier business is well established with many players and several commercial systems available.  Researching commercial solutions can expand the vision and view of how On The Spot can provide expanded services.  After researching commercial solutions, Bill should be interviewed to discuss the exact requirements for On The Spot.  Other stakeholders, as identified in Answer 1, should also be interviewed. 
Kinds of questions that need answers. 
* Services offered by On The Spot: Same-day delivery, Overnight delivery, Package pickup, sizes and rates 
* Customers: Cash only customers, account customers, new customers, billing 
* Scheduling of pickup: What is allowed, phone, web page, fax 
* Payment: Cash only, on web page, monthly account 
* Routes: How to organize, pickup and delivery, standard routes, ad hoc routes, multiple per day 
* Warehouse: Windows of processing, equipment required, what information is tracked 
* Package delivery: routes, tracking of packages, 

**3. What technology and communication requirements do you see? What are the hardware requirements, and what kind of equipment will provide viable options to the system?**  **What would you recommend to Bill?** 
There appear to be four locations that will require interaction with the system. 
1. Customer Web pages where customers can list packages for pickup and also make payment. [cite: 829, 830] Regular customers may also print out their own labels. 
2. A work station where a clerk can handle phone requests for pickup. 
3. The warehouse where sorting occurs and tracking information is entered. 
4. The delivery trucks where pickups are noted, payments are accepted, labels are printed, deliveries are noted. [cite: 833, 834] These delivery trucks are mobile, and should have real time interaction with the home server. 

Equipment to support these functions might be: 
* A central server for the Web pages and for clerk entered pickup requests 
* Warehouse equipment, such as scanners, to note tracking information. 
* Mobile devices for the trucks.  Probably tablet computers Internet access and with scanning wand.  Also a mobile printer in the truck.  (If rates are by size, then they can be measured.  If rates are by weight, then set of scales is also needed.)  The mobile devices will need Internet access to communicate with the home office.  This can be provided either with cell phone technology and support, or with wide-area Wi-fi that is available in some cities.  Cell phone access to the Internet is more widespread. 

**4. What are the primary functional requirements for the system as described so far in the case?** 
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

**1. Who are RTGM's stakeholders? Should NMHS's patients be included in defining the system requirements? Why or why not?**  **Should RTGM interact with medical professionals other than physicians? Why or why not?** 
Stakeholders include: 
* Patients (users of the monitoring device and of the phone application) 
* Doctors (users of the information transmitted) 
* Other medical staff (those who enter patient medical information on phone app) 
* Medical equipment engineers (developers of the mobile monitoring equipment) 
* Technical staff (developers of the central server system, and the database) 
* Project team members (developers of the phone app) 

Patients should be included in defining system requirements for those areas that impact their use.  This would include the medical device (comfort, wearability, maintenance), and the phone app (installing, executing, user interface screen).  Other medical professionals other than physicians may need to be involved.  This would include medical staff that are involved in the design of the device (is it sensitive enough to read glucose levels, etc.).  Other medical professionals may want to research results for medical studies.  As such they will dictate what data should be captured. 

**2. If you were the lead analyst for RTGM, how would you determine the requirements? Be specific in your answer.**  **List several questions you need answered.** 
Assuming we are limiting the fact finding and requirements definition to the smartphone app.  Questions for the medical equipment engineers would include: What are the specifications for the device - range, transmit parameters, data formats, occurance of transmittal, ranges of values for normal, abnormal, and dangerous?  What "test" capabilities does it have and how is it enabled?  Questions for the patient would be about the user interface for the phone app how readable, how understandable, signalling for normal and abnormal conditions, message format?  How usable are the screens for entering data, reading information, "testing" the equipment?  Questions for the medical professionals include information about the data formats to be sent, how often data should be sent, how to notify the system about abnormal, emergency situations, what other patient information needs to be captured? 

**3. What are the primary functional requirements for the system as described so far in the case?** 
* Enter user (patient) information 
* Test monitoring device 
* Receive monitor-device data 
* Send monitoring data to server 
* Receive data from server 
* Alert patient (user) of abnormal situation 

**4. Are the parameters for alerting patients and medical personnel the same for every patient?**  **Can they vary over time for the same patient? What are the implications for the system's functional requirements?** 
The case does not describe medical parameter variation by patient, but it may be assumed that depending on severity of illness, or weight of the patient, or sex may impact the acceptable and dangerous levels.  Hence entering patient may need to be done by trained medical personnel, or it needs to be accessed from the central server.  The case does not address if alerts can change over time.  But assuming that severity of illness will cause the parameters to change, patient information should be updated as appropriate.  The functional requirements may need to change to maintain or access from the server, history information to automatically update alert levels. 

**5. Briefly describe some possible nonfunctional requirements for RTGM.** 
* **Usability** - Patients may be completely non-technical, may also be ill, may be disabled.  Usability needs to be assessed very carefully. 
* **Reliability** - Both the monitoring device and the phone app must be error free.  In addition, some type of fail safe capability should be built in.  For example if the monitoring device fails to communicate, the phone app should sound an alert.  The phone app should have a "normal operation" icon showing at all times (maybe a green light). 
* **Performance** - Probably not a problem for the phone app.  Performance, e.g. throughput will need to be evaluated for the central server and the telephone connectivity. [cite: 900, 901]
* **Security** - all medical information must conform to HIPAA requirements.  Transmittal of data over phone lines should be encrypted.  Care should taken so that multiple devices that are located near to each other do not interfere. 
The "+" requirements should also be address.  How easy is it to install the phone app?  How much memory does it require?  What kinds of devices is it compatible with?  How does it interface with the server application? 
# Chapter 3 - Identifying Use Stories and Use Case

**1. What are the six activities of systems analysis, and which activity is discussed beginning with this chapter?** 
The five activities of systems analysis are: 

1.  Gather detailed information - begun in Chapter 2 with discussion of fact finding, stakeholders, interviewing, etc. 
2.  Define requirements - begun in this chapter by creating use cases 
3.  Prioritize requirements 
4.  Develop user-interface dialogs 
5.  Evaluate requirements with users 

**2. What is a use case?** 
A use case is an activity that the system performs as a result of some event or action by a user. 

**3. What are the two techniques used to identify use cases?** 
User goal technique and the event decomposition technique 

**4. Describe the user goal technique for identifying use cases.** 
The user goal technique is done by interviewing a user (or user role) to see what their work "goals" or objectives are.  These are low level objectives to accomplish a piece of work or to complete a work procedure.  The system then must have use cases to support each user goal. 

**5. What are some examples of users with different functional roles and at different operational levels?** 
Functional roles may be like department organization such as shipping, or sales, or accounting.  Different operational level may be like clerks, or middle management like supervisors, and then executives. 

**6. What are some examples of use case names that correspond to your goals as a student going through the college registration process?** 
Be sure to use the verb-noun naming convention. 
Answers will vary: 

  * Find a course and section 
  * Register for a section of a course
  * Cancel a registration 

**7. What is the overarching objective of asking users about their specific goals?** 
To discover and document every use case that the system must support. 

**8. How many types of users can have the same user goals for using the system?** 
No real limit. Users from different departments can access the same use cases, e.g.  can have the same user goal for using the system. 

**9. Describe the event decomposition technique for identifying use cases.** 
Look at all of the business processes that result in some type of business event.  The business events are triggers that require system processing, e.g. that require use cases. 

**10. Why is the event decomposition technique considered more comprehensive than the user goal technique?** 
Event decomposition not only looks at user initiated events (the same as the user goal technique), but it also considers temporal events and state events.  Hence it is more comprehensive. 

**11. What is an elementary business process (EBP)?** 
An EBP is a fundamental business process that may input data and receive information, but upon completion of the EBP the system has finished processing and can enter a quiescent state ready for a new event. 

**12. Explain how the event decomposition technique helps identify use cases at the right level of analysis.** 
Since event decomposition depends on EBP, then it automatically arrives at the right level of analysis.  EBP, where the system has finished a complete transaction, is the same level that is required for a use case definition. 

**13. What is an event?** 
Something that occurs at a specific time and place. It can be identified, and for purposes of systems analysis, the system must recognize it and capture some information from it or about it. 

**14. What are the three types of events?** 

  * External event - usually from a user 
  * Temporal event - occurs at a point in time, or due to a time interval
  * State event a change of state or condition of some data within the system 

**15. Define an external event and then give an example that applies to a checking account system.** 
An external event is something that occurs external to the system, and is trigger by a user action.  An example might be that a user makes a direct deposit to his/her account. 

**16. Define a temporal event and then give an example that applies to a checking account system.** 
A temporal event is one that occurs at a point in time.  An example might be that at the end of the month interest (or monthly checking account fee) is calculated and credited to the account. 

**17. What are system controls, and why are they not considered part of the users' functional requirements?** 
System controls are safety procedures or mechanisms that protect the system and the data.  They are not part of the users' functional requirements because the users normally do not initiate nor activate these controls.  They must exist above and overriding the external events. These controls are not normally part of the users' work processes. 

**18. What is the perfect technology assumption?** 
It assumes that technology will work perfectly and that in the early stages of systems analysis we do not worry about such things as security, logging in, database backup, etc. Those issues are addressed after the initial functional requirements are determined. 

**19. What are three examples of events that are system controls in a typical information system that should not be included as a use case because of the perfect technology assumption?** 

  * Backing up a database 
  * User logging onto the system 
  * Restoring the database 

**20. What are the four operations that make up the CRUD acronym?** 

  * C= Create 
  * R= Read or Report (output) 
  * U= Update 
  * D= Delete 

**21. What is the main purpose of using the CRUD technique?** 
The CRUD technique is a good way to validate the use cases that have been identified using the user goal and event decomposition techniques.  It is a double check to make sure the list of use cases covers all of the processes against the database.  When it is used as the primary method to find use cases, the 
use cases often do not track the business procedures very well. 

**22. What is a brief use case description?** 
A one or two sentence description of the use case and what it accomplishes. 

**23. What is UML?** 
UML stands for Unified Modeling Language, and it is the graphical modeling technique used to model object-oriented models.  It is the industry standard for OO modeling. 

**24. What is the purpose of UML use case diagrams?** 
Use case diagrams provide a graphical view of use cases and the actors that invoke those use cases.  They provide a nice overview of use cases. They can organize use cases together in meaningful ways. 

**25. What is another name for "actor" in UML, and how is it represented on a use case diagram?** 
An actor is also an external agent. In a use case diagram it is represented as a stick figure. 

**26. What is the automation boundary on a use case diagram, and how is it represented?** 
The automation boundary is the boundary between the automated system, i.e. the application, and the external world, including the actors.  It is represented by a rectangular boundary box. 

**27. How many actors can be related to a use case on a use case diagram?** 
As many as necessary. All those that use that particular use case. 

**28. Why might a systems analyst draw many different use case diagrams when reviewing use cases with end users?** 
An analyst will draw different use case diagrams to organize the use cases in different ways to illustrate different subsystems, or departments, or work associations. 

**29. What is the «includes relationship between two use cases?** 
The \<\<includes\>\> relationship is where one use case effectively uses the services of another use case.  It is as though one use case were embedded within another use case. 


### Problems and Exercises 

**1. Review the external event checklist in Figure 3-3 and then think about a university course registration system.**  What is an example of an event of each type in the checklist?  Name each event by using the guidelines for naming an external event. 

  * External agent wants something - Student registers for a section of a course
  * External agent wants some information - Student searches for a course 
  * Data changed and needs to be updated - Instructor assigned to teach a course section
  * Management wants some information - Show enrollments for all courses in a department 

**2. Review the temporal event checklist in Figure 3-4. Would a student grade report be an internal or external output?**  Would a class list for the instructor be an internal or external output?  What are some other internal and external outputs for a course registration system?  Using the guidelines for naming temporal events, what would you name the events that trigger these outputs? 

  * Grade report: External 
  * Class list: Internal 
  * Other external: Financial aid confirmation, graduation notice, employment confirmation letter
  * Other internal: Enrollment report and paycheck 
    To name the temporal events, include Time to produce with the output name, as well as the recipient.  For example, Time to produce grade report for students. Others are similar. 

**3. Consider the following sequence of actions taken by a customer at a bank.**  Which action is the event the analyst should define for a bank account transaction-processing system?  (1) Kevin gets a check from Grandma for his birthday. (2) Kevin wants a car.  (3) Kevin decides to save his money. (4) Kevin goes to the bank. (5) Kevin waits in line.  (6) Kevin makes a deposit in his  savings account. (7) Kevin grabs the deposit receipt. (8) Kevin asks for a brochure on auto loans. 
The event for the bank is Customer makes a deposit.  Grabbing the receipt is just the way the response (receipt) is implemented.  Asking for a brochure on auto loans might be a separate event if the bank wants to remember that Kevin asked about it, or if they want to deduct one brochure in their brochure inventory system (if they have such a thing).  If the bank does not need to remember the event, then doing something by the system is not "required." 

**4. Consider the perfect technology assumption, which states that use cases should be included during analysis only if the system would be required to respond under perfect conditions.**  Could any of the use cases listed for the RMO CSMS be eliminated based on this assumption? Explain.  Why are such use cases as Log on to the system and Back up the database required only under imperfect conditions? 
All of the events listed must be included because the system must do something each time one 
of the events occurs even if there is perfect technology.  User logs on to system and Time to back up the data are only required because users are not perfectly honest, and disk drives are prone to crash or corrupt data. 

**5. Visit some Web sites of car manufacturers, such as Honda, BMW, Toyota, and Acura.**  Many of these sites have a use case that is typically named Build and price a car.  As a potential customer, you can select a car model, select features and options, and get the car's suggested price and list of specifications.  Write a brief use case description for this use case (see Figure 3-10). 

| Use case name: | Brief Description: |
|---|---|
| Build and price a car | Customer selects the model; the system displays the options; customer selects all the options; the system displays final result and suggested retail price. |



**6. Again looking at a Web site for one of the car manufacturers, consider yourself a potential buyer and then identify all the use cases included on the site that correspond to your goals.** 
Answers will vary: 

  * View available models 
  * View available options 
  * View detailed specifications 
  * Compare vehicles 
  * Build and price a car 
  * Find a dealer 
  * Get a quote on specific model 

**7. Set up a meeting with a librarian. During your meeting, ask the librarian to describe the situations that come up in the library to which the book checkout system needs to respond.**  List these external events. Now ask about points in time, or deadlines, that require the system to produce a statement, notice, report, or other output.  List these temporal events. Does it seem natural for the librarian to describe the system in this way?  List each event and then name the resulting use case. 
Answers will vary. 
External events might include 

  * Student checks out book 
  * Student returns book 
  * Student wants to check book availability 
    Temporal events might include 
  * End of month → Time to send overdue notice 
  * End of month → Time to produce monthly summary reports 
  * Book has not returned in a year → Time to declare book is lost 

**8. Again considering the library, ask some students what their goals are in using the library system.**  Also ask some library employees about their goals in using the system.  Name these goals as use cases (verb-noun) and discuss whether student users have different goals than employee users. 
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

**9. Visit a restaurant or the college food service to talk to a server (or talk with a friend who is a food server).**  Ask about the external events and temporal events, as you did in exercise 7. What are the events and resulting use cases for order processing at a restaurant? 
Answers will vary. External events might include Customer places order, Customer changes order, Kitchen returns completed order, Customer pays bill, and so on.  Temporal events might include Time to produce daily order totals report, Time to produce weekly sales analysis reports, and so on. 

**10. Review the procedures for course registration at your university and then talk with the staff in advising, in registration, and in your major department.**  Think about the sequence that goes on over an entire semester. What are the events that students trigger?  What are the events that your own department triggers? What are the temporal events that result in information going to students?  What are the temporal events that result in information going to instructors or departments?  List all the events and the resulting use cases that should be included in the system. 
Answers will vary. Events might include Department schedules a class, Student enrolls in a class, Student changes schedule, Student drops a class, Instructor submits final grades, Time to generate grade report for students, Time to produce enrollment totals report for administration, and Time to produce class lists for faculty.  Note that the event names should indicate information about the external agent or actor involved.  Temporal events make the most sense if Time to is used at the beginning of the event name. 

**11. Refer to the RMO CSMS Order Fulfillment subsystem shown in Figure 3-11.**  Draw a use case diagram that shows all actors and all use cases.  Use a drawing tool such as Microsoft Visio if it is available. 

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

**12. Again for the Order Fulfillment subsystem, draw a use case diagram showing just the use cases for the shipping department in preparation for a meeting with them about the system requirements.**  Use a drawing tool such as Microsoft Visio if it is available. 

  * Track shipment 
  * Ship items 
  * Shipping 
  * Manage shippers 
  * Create backorder 
  * Create item 
  * return 
  * Look up order 
  * status 

**13. Refer to the RMO CSMS Marketing subsystem shown in Figure 3-11.**  Draw a use case diagram that shows all actors and all use cases.  Use a drawing tool such as Microsoft Visio if it is available. 

  * Add/update product information 
  * Marketing 
  * Add/update promotion 
  * Add/update accessory package 
  * Merchandising 
  * Add/update business partner link 


**14. Refer to the RMO CSMS Reporting subsystem shown in Figure 3-11.**  These reports were identified by asking users about temporal events, meaning points in time that require the system to produce information of value.  In most actual systems today, an actor is assigned responsibility for producing the reports or other outputs when they are due.  Recall that the actor is part of the system-the manual, non-automated part.  Thus, this is one way the "system" can be responsible for producing an output at a point in time.  In the future, more outputs will be produced automatically. Draw a use case diagram that shows the use cases and actors, as shown in Figure 3-11.  Use a drawing tool such as Microsoft Visio if it is available. 

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

**1. To what events must the ticket-processing system respond? List each event, the type of event, and the resulting use case.** 

| Event | Type | Use case |
|---|---|---|
| Officer submits a ticket | External | Record new ticket |
| Driver sends in fine payment | External | Record fine payment |
| Driver requests trial | External | Process trial request |
| Court sends verdict | External | Record verdict |
| Time to produce warrant request | Temporal | Produce warrant request |



**2. Write a brief use case description for each use case.** 

| Use case | Description |
|---|---|
| Record new ticket | A clerk will enter the data recorded on a paper ticket which has been sent in from the officer. |
| Record fine payment | A clerk will enter the data from the payment sent in by the driver. |
| Process trial request | A clerk will enter the data from the trial request check-box and the envelop sent in by the driver. The system must generate a trial request and send it to the court system. It also produces a questionnaire for the driver. |
| Record verdict | The system records the verdict information sent by the court system. |
| Produce warrant request | After two weeks, the system produces a warrant request to be sent to the court. |


**3. The portion of the database used with the ticket-processing system involves driver data, ticket data, officer data, and court data.**  Driver data, officer data, and court data are read by the system, and the ticket-processing system creates and updates ticket data.  In an integrated system like the ticket-processing system, some domain classes are created by and updated by other systems, as described in this case.  Create a table with systems down the rows and the four types of data (domain classes) across the columns.  Indicate C, R, U, or D for each domain class and each system. 

| Use Case/Class | Driver | Ticket | Officer | Court |
|---|---|---|---|---|
| TICKET SYSTEM <br> Record new ticket <br> Record fine payment <br> Process trial request <br> Record verdict <br> Produce warrant request <br> ACCIDENT SYSTEM | R <br><br><br><br><br><br> U <br><br> U | C <br><br> U <br><br> U <br><br> U <br><br> U <br><br> R | R | R |
| DRIVING RECORDS SYSTEM | RU | R | | |
| DRIVER'S LICENSE SYSTEM | CRU | | | |


### Running Cases: Community Board of Realtors 

**1. To what events must the MLS system respond? List each event, the type of event, and the resulting use case.**  Be sure to consider all the use cases that would be needed to maintain the data in the MLS system, thinking in terms of the CRUD technique. 

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


**2. Draw a use case diagram based on the actors and use cases you identified in question 1.** 

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

**3. Given the information available in the system, consider yourself a potential customer looking for real estate.**  List as many specific use cases you would like to see based on your specific goals. 
Answers will vary. 

  * Find real estate agent 
  * Search for property (by various criteria) 
  * View property details 
  * View property images (video or pictures) 
  * Request a property visit 
  * Send a message to real estate agent 

**4. Draw a use case diagram for all the use cases for the potential customer you identified in question 3.** 

  * Buyer 
  * Find real estate agent 
  * Search for property 
  * View property details 
  * View property images 
  * Request property visit 
  * Send a message to agent 

### Running Cases: The Spring Breaks 'R' Us Travel Service 

**1. Using the event decomposition technique for each event you identify in the description here, name the event, state the type of event, and name the resulting use case.**  Draw a use case diagram for these use cases. 

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



**2. Consider the new Social Networking subsystem that SBRU is researching.**  Think in terms of the user goal technique to identify as many use cases as you can think of that you would like to have in the system.  SBRU is guessing you might want to join, send messages, and so forth, but there must be many interesting and useful things the system could do before, during, and after the trip.  Draw a use case diagram for these use cases. 
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

**1. From this description as well as the information from Chapter 2, identify all the actors that will be using the system.** 

  * Bill Wiley (owner and manager) 
  * Delivery person 
  * Warehouse person 
  * Customer 

**2. Using the actors that you identified in question 1, develop a list of use cases based on the user goal technique.**  Draw a use case diagram for these use cases. 
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

**1. Identify all the actors that will use RTGM.** 

  * Patient 
  * Health-care provider (Physician) 
  * Nurse (physician assistant) 

**2. Using the actors that you identified in question 1, develop a list of use cases based on the user goal technique.**  Draw a use case diagram for these use cases. 

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


**3. Using the event decomposition technique for each event you identified in the description, name the event, state the type of event, and name the resulting use case.**  Draw a use case diagram for these use cases. 

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

  
# Chapter 4 - Domain Modeling

# Chapter 5 - Use Case Modeling

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


