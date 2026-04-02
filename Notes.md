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

?
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

?
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
?
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

?
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

?
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

?
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

?
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

?
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

?
# Section 2: Short-Answer Questions and Exercises