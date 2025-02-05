# Chess-Bot

 - **1.** [Introduction](#intro) 
 - **2.** [Context Diagram](#context) 
 - **3.** [User Stories](#stories) 
 - **4.** [Project Plan](#plan) 
 -  **5.** [System Class Diagram](#sys_diagram)
	 - 5.1 [Classes in the OMS](#oms_classes) 
	 - 5.2  [Conceptual Class Diagram of the OMS](#oms_conceptual)
	 - 5.3 	[Bottom-up approach to development](#oms_bottomup)
 -   **6.** [Object-Orientation in OMS](#oms_object)
 -  **7.** [Input Validation in the User Interface class](#input_val)
 -  **8.** [Formatted Output](#format_o)
 -  **9.** [Data Dictionary](#data_dict)
 -  **10.** [File Handling](#file_hand)
 -  **11.** [Pseudocode](#pseudo)
 -  **12.** [Sorting and Searching](#s_and_s)
 -  **13.** [Messaging (modelling dynamic behaviour) in an Object-Oriented system](#messaging)
 	-  13.1 [Polymorphism in the OSM](#polymorph)
 -  **14** [Code optimisation techniques for better collaboration and maintenance](#optimisation)
 	-  14.1 [Intrinsic and Extrinsic documentation](#docs)
  	-  14.2 [Organisation of source code files and modules](#src_org)
  	-  14.3 [Github commiting policy](#git_policy)
 -  **15** [Testing and Quality Assurance](#test_quality)
   	-  15.1 [Black box testing of OMS](#black_box)
 		-  15.1.1 [Test Cases](#test_cases)
		-  15.1.2 [Input-Output table for testing](#io_table)
	- 15.2 [White box testing of OMS](#white_box)

## 1. Introduction<a name="intro"></a>
## Introduction

This project aims to design and develop a chess bot for Lichess using Python, focusing on three key components: the game engine, chess AI (strategy and decision-making), and Lichess API integration (communication and user interface).

The division of the project into these components ensures maintainability, reflecting real-world scenarios where the user interface (Lichess platform interaction) can evolve, while the core AI logic and game strategies remain consistent. This project will utilize Python and the Lichess API for handling game interactions, allowing the bot to analyze positions, make moves, and communicate with the platform.

Project Overview:
Game Engine: This component will focus on handling the rules of chess, move validation, board state representation, and game status tracking. It ensures that the bot operates within the constraints of chess, such as legal moves, castling, en passant, and check/checkmate conditions.

Chess AI (Strategy and Decision-Making): The AI component will be designed to evaluate different board positions and determine optimal moves. This will involve a minimax algorithm, along with optimizations like alpha-beta pruning, to enhance decision-making. The AI will consider various factors such as material balance, piece activity, and tactical motifs when selecting moves.

Lichess Integration (User Interface and Communication): The bot will interact with Lichess using the official API, allowing it to join games, make moves, and analyze positions. The integration will also handle incoming game events (e.g., opponent moves) and send appropriate responses. The bot's interface will be capable of running asynchronously, ensuring that it can react to real-time game updates.

Testing and Refinement: After the initial implementation, the bot will be tested in various game scenarios, including different time controls and opponent strengths. Based on these tests, the AI’s performance will be refined, and the system will be optimized for faster response times and improved decision-making.

Documentation and Finalization: The  phase will include comprehensive documentation, covering how the bot works, how to set it up, and how to use it with Lichess. Additionally, the bot's performance and limitations will be analyzed and reported. This documentation process will be completed throughout the project's development.


## 2. Context Diagram<a name="context"></a>
The interactions between the end user and the chess bot can be depicted via a context diagram, as shown below in Figure 2. Further details of the context diagram are not shown to keep this document brief wherever possible.

![Coolest Context Diagram you've ever seen](https://github.com/user-attachments/assets/ad4dc476-5100-491d-8e93-eec1f79a9e08)

<i>Figure 2: Context Diagram (NEW)</i>

## 3. User Stories<a name="stories"></a>
User Stories are typically used in Agile frameworks to articulate how each software feature will add value to the user. Each user story is the smallest unit of work in an agile framework and has the following structure:
“As a [person], I [want to], [so that].”  

As a sales manager, I want to be able to view all the products that are ordered so I know which ones are the most popular.

As a Customer, I want to be able to search for my existing orders so that I can receive information about the order and/or update the order.

As a Postal Order customer, I want to track the status of my order so that I can be sure it is delivered at home.

As a Customer with a busy schedule, I want to be able to choose between a store and postal order and be provided information about delivery dates for the latter.
So that I can experience the utmost convenience and stay informed about the delivery status of my order.

As a customer without a mouse, I want to be able to utilise my keyboard while interfacing with a CLI to order my products. This is preffereble to a GUI because I have an unresponsive trackpad.

As an elderly customer, I want to be able to order postal orders to be as convenient as store orders so that I am not discriminated against for my age.

As a Manager, I want to be able to add/remove products from the product list, so that we can provide an up-to-date list of products for our customers

As a Manager, I want to be able to view all of the pending orders in the system, so that I can keep track of the orders and ensure that all orders are fulfilled

</ol>

## 4. Project Plan<a name="plan"></a>
The project is planned to be completed in 5 weeks. Observe that the project plan includes planning, analysis, design, implementation and testing tasks from the Software Development Life Cycle (SDLC). It also includes details such as how much of the work is accomplished and the roles of each team member.

![Online Gantt 20240604](https://github.com/sebastian-power/order-management-system/assets/140695410/3f684172-01b6-4b67-88d4-08af8c64114e)
Key:
Black - task grouping

Green - all

Orange - Olvier

Blue - James

Purple - Sebastian


<i>Figure 3: Project Management Plan</i>
## 5. System Class Diagram<a name="sys_diagram"></a>
### 5.1 Classes in the OMS<a name="oms_classes"></a>
Figure 5 shows the set of classes used in the OMS from a conceptual perspective. The classes are colour-coded to be consistent with the components used in the architecture diagram in Figure 1. In addition, in Figure 5, <<keyword>> notation is used to represent the classifier of the classes. {class} or {interface} could be used as a namespace for various classifiers. A classifier comprises Unified Modelling Language (UML) elements with standard features. In Figure 5, a <<boundary>> class is used to represent it deals with user interaction features but has no application logic for managing a business activity. On the other hand, the <<datatype>> classes only deal with file-handling operations and are used by the application logic components. Once the data from a file is read or written, the information is passed to the <<entity>> or <<actor>> classes, which represent the application logic of the business.
<img width="839" alt="Screenshot 2024-05-28 at 10 04 49" src="https://github.com/sebastian-power/order-management-system/assets/140695410/66770c0e-dc9c-489e-92f9-6820243d1695">
<i>Figure 5: Conceptual perspective of the Classes used in OMS</i>
Finer details of the features in each class are specified in Figure 6 (from a specification perspective). I have yet to include the classes for file handling here, but you need to include such classes in the report, too. Most details of each class are self-explanatory. However, special attention must be given to the Postal_Order class since it is inherited from the Order class. That is, all the attributes and methods of the Order are available in the Postal_Order class by default. Hence, these are shown in lighter-coloured text in Figure 6. In addition, it also has its own attributes, such as current_status, o_delivery_date and o_past_states. A Postal_Order differs from an Order by its state being able to be tracked, and the delivery date is one month from the order date. On the other hand, it is assumed that an Order will not be delivered. Hence, the above attributes should be included in the Postal_Order class. So, since a Postal_Order is a particular type of Order, it is designed as an inherited Order class.
![image](https://github.com/sebastian-power/order-management-system/assets/52031320/fbae7398-eeb3-4ac9-a50e-947310843ea0)
<i>Figure 6: Class details from a specification’s perspective</i>
### 5.2 Conceptual Class Diagram of the OMS<a name="oms_conceptual"></a>
A class diagram depicts a static nature of how the various classes are associated with one another in the system. In UML, an association is a relationship between classes. For example, it can be used to show that instances of classes could be linked to each other or combined logically or physically into some aggregation. Figure 7 depicts the class diagram of the OMS. 
<img width="1042" alt="Screenshot 2024-05-28 at 10 05 07" src="https://github.com/sebastian-power/order-management-system/assets/140695410/1c9886ee-6064-4cb4-9580-887c55ee859d">

<i>Figure 7: Class Diagram of the OMS</i>
An aggregation represents a whole-part association. The whole (aggregator) contains parts (aggregates). A diamond shape at the whole end denotes aggregation. For example, in OMS, the Order_Mgt_UI class has an aggregation of Order and Postal Order. A stronger form of aggregation is a composition. Here, the parts are tightly bound to the whole and are denoted by a black-filled diamond shape at the whole end. For example, An Order should have a customer and at least one Order_Item, and If an Order is deleted, the corresponding Customer and Order_Item details will also be deleted. Such an association is composition. Additional information such as arity and navigability are sometimes also specified in class diagrams. Arity refers to how many class instances can be associated with the other class. Navigability identifies the direction of the association. Let’s first consider arity in Figure 7. An Order_Mgt_UI class can exist with 0 or more Order(s) or with 0 or more Post_Order(s). This is represented by 0..n in the diagram, and the arrow of the association indicates the direction. For example, the direction of the association arrow is from the Order_Mgt_UI to the Postal_Oder to suggest that the Order_Mgt_UI class has the Postal_Order and not the other way around. An X mark is sometimes indicated on the association line to explicitly tell that a particular direction of association is not possible. For example, Figure 7 depicts a Postal_Order class object that is not navigable from a Postal_Order_DB class object.
### 5.3 Bottom-up approach to development<a name="oms_bottomup"></a>
This project uses several classes. The complexity of the design and development of projects with many classes in OOP can be reduced using either a bottom-up or a top-down approach. A bottom-up approach is considered for the OMS because bottom-up is more amenable to incremental development. In incremental development, independent classes are developed, tested, and debugged first, and then the dependent classes are developed, tested, and debugged before integrating them to build a concrete solution.  So, the bottom-up approach allows for early detection of errors, leading to smoother integration. Order_Mgt_UI is an example of a top-level class in the OMS project since it uses other classes. Another example of a top-level class is the Order class since it is dependent on Oder_DB, Order_Item and Customer classes. On the other hand, Order_DB is a bottom-level class. Top-down was also used for Customers because the functionallity depended on the database reading. It was easier to implement dummy values to test the class before creating the databases.

UML Class Diagram:


![Image](https://github.com/sebastian-power/order-management-system/blob/main/assets/images/UML%20Class%20Diagram.drawio.svg)

## 6. Object-Orientation in OMS<a name="oms_object"></a>
Object-oriented programming is popular because it enables the evaluation of existing classes without changing them. This reduces the maintenance cost. For example, a new inherited class can be created if a new attribute is required for a previously existing class. In Figure 7, inheritance is depicted. A triangular arrow is drawn from the Postal_Order class to the Order class for the inheritance reasons explained in section 5.1.
## 7. Input Validation in the User Interface<a name="input_val"></a>
Validating user input on the client side saves valuable maintenance time. This section explains how validation is incorporated when an Order_Item is ordered in an Order. A snippet of the code is provided in Figure 8, and the corresponding runtime interactive output statement is shown in Figure 9. Observe that a list of available products is first displayed, and then a choice is presented to the user to select an item number rather than asking the user to enter the item's name, which is more error-prone. In addition, the code checks for negative values and runtime errors if the user wrongly inputs non-numeric values for the item quantity. Similarly, input validation is performed for other inputs but is not illustrated here for space brevity. Please see the code in the appendix for complete details.
![image](https://github.com/sebastian-power/order-management-system/assets/52031320/b7638213-699d-4880-8032-6eee66245e91)

We have also used input validation when checking the email of the usesr. The email must be between 6 and 20 characters, and must not include whitesepace. It must also contain an @ symbol within the email (not at the start or end) just like real emails.
<img width="707" alt="Screenshot 2024-05-28 at 09 23 38" src="https://github.com/sebastian-power/order-management-system/assets/140695410/2af8f26d-187f-4609-81b1-6da2ff2f35a7">


<i>Figure 8: Code snippet for validation during input of an Order_Item</i>
![image](https://github.com/sebastian-power/order-management-system/assets/52031320/5c426f10-4452-43e8-8574-3883e09e1445)
<i>Figure 9: Runtime example of input validation for Order_Item</i>
## 8. Formatted Output<a name="format_o"></a>
A snip of the formatted output provided by the program is shown in Figure 10. 
![image](https://github.com/sebastian-power/order-management-system/assets/52031320/4c7b2ffa-4b9f-4d11-b62a-7dd5aa695718)
<i>Figure 10: Formatted Output</i>
The output clearly illustrates how the Postal Order details are grouped separately and how white space is used for readability.
## 9. Data Dictionary<a name="data_dict"></a>
A data dictionary comprehensively describes each attribute and class variable used in the system. Note that it is not all variables. Data dictionaries are valuable during the system's post-delivery maintenance. A data dictionary commonly includes variable name, data type, format, size in bytes, and the number of characters to display the item, including the number of decimal places (if applicable), the purpose of the variable, and a relevant example. Validation rules have been included where applicable. Details of records or arrays of records have been included in data dictionaries. These following figures show the data dictionaries for all 8 classes in the project. The main variables and all class attributes have been included, and variables used solely for logic control have been excluded.
![image](https://github.com/sebastian-power/order-management-system/assets/52031320/711265fd-2725-4e59-9d3b-29ff384da6e9)
![image](https://github.com/sebastian-power/order-management-system/assets/52031320/e70a1bf3-b3ac-4cff-b7e8-6aec779ac733)
![image](https://github.com/sebastian-power/order-management-system/assets/52031320/4cb4df36-34fe-4f18-b98f-ba400713fe68)
![image](https://github.com/sebastian-power/order-management-system/assets/52031320/6705f900-0cef-4542-b7ac-3a2e6f15d37e)
![image](https://github.com/sebastian-power/order-management-system/assets/52031320/28e3e345-9415-42ef-840d-75e6b9560243)
![image](https://github.com/sebastian-power/order-management-system/assets/52031320/9489f815-4654-4d06-bd3b-6bdc43a98415)
![image](https://github.com/sebastian-power/order-management-system/assets/52031320/4a1fac99-1911-43b7-8197-bb8a6719ca76)
![image](https://github.com/sebastian-power/order-management-system/assets/52031320/3b1b5d61-a1af-4dbe-9978-a25e77c6f182)

## 10. File Handling<a name="file_hand"></a>
File handling classes such as Customer_DB, Order_DB and Products_DB contain the logic for storing, retrieving, and updating the corresponding data in files. Navigation of these classes is always from the corresponding entity.
## 11. Pseudocode and flowchart<a name="pseudo"></a>
Pseudocode is usually used to illustrate the design of complex system parts. A complex part of a Postal_Order class is the algorithm to find whether a postal order has transitioned through all the states before it is delivered to the customer. This section contains the high-level pseudocode of the has_partial_valid_state_sequence method in the Postal Order class.  The algorithm assumes the valid states of  Postal Order are "Initiated", "Packed", "Shipped", and "Delivered". A postal order can transition from “Initiated” to “Packed” to “Shipped” and then to a “Delivered” state. Please assume that the algorithm needs to keep track of the current and past states as it transitions from one state to another. We can use a variable, states, to hold the list of past states of a Postal_Order. The has_partial_valid_state_sequence method can be used before updating the list of states. From this discussion, it is evident that the list of valid values in the list states can be one of the following: [ ] or  [“Initiated”] or [“Initiated”, “Packed”] or [“Initiated”, “Packed”, “Shipped] or [“Initiated”, “Packed”, “Shipped, “Delivered”]. The algorithm is as follows:
```
#states is the param containing the past states of a Postal Order. This can be any one of the lists mentioned above in blue text.
#valid_sequence is the param containing the list of valid states: [“Initiated”, “Packed”, “Shipped, “Delivered”]
function has_partial_valid_state_sequence(states, valid_sequence):
        IF the length of states > length of valid_sequence THEN
            RETURN “not valid”
        ENDIF
        FOR index = 0 to (length of states) -1
             IF states[index] is not equal to the first item in valid_sequence THEN
                  RETURN not valid
		    ELSE 
				Remove the first item in valid_sequence so that the following item now becomes the first
             ENDIF
        NEXT index
        RETURN “valid” 
END
```
Another example of psuedocode is:
```function get_cust_email():
    # Initialize a flag to control the loop
    done = False
    
    # Loop until a valid email is provided
    WHILE done is False:
        # Assume the email is valid unless proven otherwise
        done = True
        
        # Define a list of forbidden whitespace characters
        forbidden = [" ", "\n", "\r", "\t", "\b"]
        
        # Prompt the user to enter their email address
        email = INPUT("Enter your email. \n6-20 characters with an @. No white space chars allowed: ")
        
        # Check if the email length is less than 6 or greater than 20 characters
        IF length of email < 6 OR length of email > 20 THEN
            # Inform the user about the invalid length and set done to False
            PRINT "Email should be between 6-20 characters. Try again"
            done = False
        # Check if the email contains any forbidden whitespace characters
        ELSE IF any character in forbidden is in email THEN
            # Inform the user about the forbidden characters and set done to False
            PRINT "You have used white space characters. Try again"
            done = False
        # Check if the email starts or ends with '@', or if it doesn't contain exactly one '@'
        ELSE IF email[0] is "@" OR email contains not exactly one "@" OR email[-1] is "@" THEN
            # Inform the user about the incorrect '@' usage and set done to False
            PRINT "An in-between @ character expected in email. Try again"
            done = False
    # End the loop when a valid email is entered
    ENDWHILE
    
    # Return the valid email
    RETURN email
END FUNCTION

```
Purpose:
The get_cust_email function is designed to prompt the user to enter a valid email address. The function ensures that the email address meets specific criteria before accepting it. The email address must be between 6 and 20 characters long, contain exactly one "@" symbol, and not include any whitespace characters. If the input does not meet these criteria, the user is prompted to try again.

Parameters:
None: This function does not take any parameters.
Returns:
email (string): A valid email address entered by the user.
Procedure:
Initialization:

Set done to False to initiate the loop for user input.
Input Loop:

Use a WHILE loop that continues until done is True.
User Prompt:

Prompt the user to enter an email address with the message: "Enter your email. \n6-20 characters with an @. No white space chars allowed: ".

Validation:

Check if the length of the email is less than 6 or greater than 20 characters:

If true, print "Email should be between 6-20 characters. Try again" and set done to False.

Check if the email contains any forbidden characters (whitespace characters):

If true, print "You have used white space characters. Try again" and set done to False.

Check if the email starts with "@", does not contain exactly one "@", or ends with "@":

If any condition is true, print "An in-between @ character expected in email. Try again" and set done to False.

Loop Termination:

The loop continues until a valid email is entered, where all the conditions above are false, setting done to True.

Return:

Return the valid email address.

Similarly, you must identify all other complex algorithms in each class and write their pseudocode in this section.

![Image](https://github.com/sebastian-power/order-management-system/blob/main/assets/images/Software%20Flowchart%20Ordering%20Item-Page-1.drawio.svg)]
![Image](https://github.com/sebastian-power/order-management-system/blob/main/assets/images/Software%20Flowchart%20Ordering%20Item-Page-2.drawio.svg)]
## 12. Sorting and Searching<a name="s_and_s"></a>
<s>Sorting and searching are some of the ubiquitous operations in Information Systems. They are frequently used in order management systems to search for a product among thousands of products, sort the items in an order based on the price or the product's name, etc. Several types of searching and sorting algorithms are used in information systems, and each type's efficiency varies. The HSC exams typically contain questions on sorting and searching. However, this document does not contain any scoring algorithms. Please add a sorting algorithm in the Order class to sort all orders based on each item's product name or price. Alternatively, add a sorting algorithm in a new class that manages all orders. Since the sorting algorithms are standard, you must illustrate that you can adapt them for a specific purpose.</s>
Mr D'Souza said we should not do this.
## 13. Messaging (modelling dynamic behaviour) in an Object-Oriented system<a name="messaging"></a>
Class diagrams do not depict what methods and classes come into play from among the classes and methods in the system. for a specific purpose, such as a user story. For example, a software maintenance engineer may be interested in fixing a feature related to a user story. In such a case, a model such as a class diagram containing all the details of an OO system reduces the maintenance engineer's productivity. Hence, separate models for each user story are essential. In this section, the system's dynamic behaviour for user story 3.2 (As an aged customer, I want to create a Postal Order so that the order can be delivered to my address.) in section 3 is considered. A sequence diagram is usually used to model this, but the HSC syllabus needs to mention it. So, instead, a textual approach will be used to explain how messages are passed from one object to another when a user story needs to be satisfied. In OOP, message passing is a fundamental concept that enables objects to communicate with each other within a program.
The following invocations of methods from various classes are needed to get a Postal_Order object:
An end user starts interacting with the OMS through the Order_Mgt_UI object. Let order_mgt_ui be a reference to the Order_Mgt_UI object.
The definition of the constructor of this class is provided below:
```
    def __init__(self):
        self.cust_name=self.get_cust_name()
        self.cust_email=self.get_cust_email()
        #testing below: Creation of a regular Order and a Postal Order
        self.orders=[self.create_postal_order()]
```
Observe that the constructor of the object makes calls to get_cust_name(),  get_cust_email() and create_postal_order() methods to initialise its attributes cust_name, cust_email and orders, respectively. These attributes can be seen in the abstract definition of the Order_Mgt_UI class in Figure 6. The class diagram in Figure 6 is principally used to find the attributes and method signatures of all classes in the system. The method signatures of get_cust_name() and get_cust_email()  in Figure 6 indicate they return a string each, representing a customer name and email from the keyboard. 
The get_create_postal_order(): Postal_Order method signature in the Order_Mgt_UI class can create a Postal_Order. 
The sequence of messages so far is as follows:
```
     order_mgt_ui
     |
         |->get_cust_name()
         |->get_cust_email()
         |->create_postal_order()
```
The definition of create_postal_order() provides more information about the sequence of messaging:
```
    def create_postal_order(self):
        a_customer = Customer(self.cust_name,self.cust_email)
        a_postal_order = Postal_Order(a_customer)
        done=False
        while not done:
            done=True
            a_postal_order.add_item(self.create_order_item())
            correct_more=False
            while not correct_more:
                correct_more=True
                more = input("Do you want to order another item Y/N: ")
                more = more.strip()
                if more not in ['Y', 'y','N','n']:
                     print("You did not enter Y or N. Please try again")
                     correct_more=False
            if more in ['Y','y']:
                 done=False
        return a_postal_order
```
It first calls the constructor of the Customer class by passing cust_name and cust_email as arguments, which in turn calls the setter methods in the Customer class by default.
![image](https://github.com/sebastian-power/order-management-system/assets/52031320/0e5dfa3c-effb-4b5b-8a44-4a8d30b1de61)
It then invokes the constructor of Postal_Order. The constructor of the Postal_Order class is shown below.
```
    def __init__(self, customer:Customer):
        super().__init__(customer)
        one_month_from_now=(datetime.now()+timedelta(days=30))#one month from now
        self.o_delivery_date=one_month_from_now       
        self.past_states=[] 
        self.current_state=0#current state is, "initiated", among past states
```
Since Postal_Order inherits from Order, it first calls the constructor of the Order class, where the setter methods of the Order class attributes are called by default.
```
    def __init__(self, customer:Customer):
        Order.order_num +=1
        self.order_id=str(Order.order_num)
        self.customer = customer
        self.order_date= datetime.now()
        self.items = []  # Initialize an empty list to store order items
```
<br></br>
![image](https://github.com/sebastian-power/order-management-system/assets/52031320/5dd51e34-ec4c-48e2-ae02-8987cc2d904b)

At this stage, the user interface class has a Postal_Order object but no order items in the Postal_Object. That is why the Postal Order’s add_item() method is invoked in the outer while loop of the create_postal_order() method in the Order_mgt_UI class to add one or more Order_Item objects. The inherited add_item() method of the Postal_Order class requires an Order_Item object as an argument. Hence, it invokes the create_order_item() method of the user interface class to get the details of an Order_Item from the keyboard before invoking the add_item() method. The create_order_item() also uses the Product class to get the name and price of each item, but this has not been shown in the following messaging structure due to lack of space.
![image](https://github.com/sebastian-power/order-management-system/assets/52031320/de2bc2ca-4213-45b7-a412-7eb0ec08d390)
In summary, each object in an OOP project is a self-contained unit with its data and behaviour (methods), and an object is not the same as a class. A class is a template (like a cookie cutter) that consists of data members or variables and functions and defines the attributes and methods for potential objects to be created in the future. An object is an instance of a class(like a cookie created using the cookie cutter), and each object has its values for the different attributes present in its class. This feature allows multiple developers to work on other parts of the program simultaneously, as they can create their classes and objects. When an object (the sender) needs to communicate with another object (the receiver), it sends a message. The receiver processes the message, performs the requested action, or provides the requested data. This communication is essential for building modular, reusable, and maintainable software systems. 

Sequence Diagram of the System: (Customers can Access their Orders through the AdminUI Method, But can't Add / Remove Products)
![Image](https://github.com/sebastian-power/order-management-system/blob/main/assets/images/Software%20Engineering%20Project%20Sequence%20Final%20Diagram.svg)
### 13.1 Polymorphism in the OSM<a name="polymorph"></a>
Polymorphism in OOP refers to exhibiting different behaviours by inherited methods with the same signature depending on the associated object. In the OSM, the Postal_Order class inherits from the Order class. The Order class is the parent class, and the Postal_Order class is the child class. Additionally, only the str() method has the same signature. When the str() method is called on an Order object, it returns the string representation instance attributes of the Order object. In contrast, when the same str() method is called on a Postal_Order object, it returns the string representation of the Postal_Order attributes. This is shown below.
![image](https://github.com/sebastian-power/order-management-system/assets/52031320/38bfbbcd-2083-4e26-90a3-aa2151adc8d8)
The above table shows the difference between the two methods regarding additional information, such as the delivery date and the states in the postal order’s str() method. 
## 14. Code optimisation techniques for better collaboration and maintenance<a name="optimisation"></a>
Most Information System projects are created in groups. An essential component of collaboration within object-oriented programming is the ability for developers to understand how each other operates. This can be done in several ways. One approach is providing Intrinsic and extrinsic documentation during the SDLC phases. Another way is by providing a consistent directory structure for each team member’s source code. These two approaches are considered below.
### 14.1 Intrinsic and extrinsic documentation<a name="docs"></a>
Intrinsic documentation exists within the code and directly relates to its readability and understanding. It facilitates collaboration among team members by providing context and guidance. Examples of intrinsic documentation include (i) Using meaningful names for variables, classes, functions and code directories. (ii) Adding comments in the code to provide explanations, clarify intent, or guide other programmers. (iii) Consistent naming conventions for variable, function, and class names enhance code readability. (iv) Inline documentation in the form of brief explanations within the code for method signatures and parameter descriptions. A cursory glance at the source code in the appendix indicates these conventions have been followed. An example is given below:
```
    #Returns true if the 'states' parameter has a set of valid states. Returns False otherwise
    #Parameter ‘valid_sequence’ has values ["Initiated", "Packed", "Shipped", "Delivered"]
    #A Postal order's valid partial state sequence can only have the following form:
    #[]
    #["initiated"],
    #["Initiated", "Packed"]
    #["Initiated", "Packed", "Shipped"],
    #["Initiated", "Packed", "Shipped", "Delivered"]
    def has_partial_valid_state_sequence(self,states:type[list[int]], valid_sequence:list[type[str]])->type[bool]:
```

Sure, here is a more concise version of the documentation with placeholders where you can insert your own file names and specific details.

---

# Project Documentation

## Table of Contents
1. Introduction
2. File Handling Logic
3. Source Code Organization
4. Software Development Life Cycle Phases
5. Installation Guide
6. Source Code (Appendix)
7. Intrinsic Documentation

---

## 1. Introduction


**Description:** This project is developed using Python and SQL for the database. It employs Object-Oriented Programming (OOP) principles for the overall structure.

---

## 2. File Handling Logic

**Description:** The project includes logic to store, retrieve, and update data in a file. The file format used is JSON.

### File Handling Operations:

1. **Storing Data:**
   - Function: `store_data(data, file_path)`
   - Description: Stores the given data into the specified file.
   - Parameters:
     - `data` (dict): The data to be stored.
     - `file_path` (str): The path to the file where data will be stored.
   - Return: None

2. **Retrieving Data:**
   - Function: `retrieve_data(file_path)`
   - Description: Retrieves data from the specified file.
   - Parameters:
     - `file_path` (str): The path to the file from which data will be retrieved.
   - Return: `data` (dict): The retrieved data.

3. **Updating Data:**
   - Function: `update_data(new_data, file_path)`
   - Description: Updates the existing data in the specified file with new data.
   - Parameters:
     - `new_data` (dict): The new data to be added/updated.
     - `file_path` (str): The path to the file where data will be updated.
   - Return: None

### File Format:

The data is stored in JSON format. Example:

```json
{
    "key1": "value1",
    "key2": "value2"
}
```

---

## 3. Source Code Organization

The project is organized into the following modules:

1. **`main.py`:** The entry point of the application.
2. **`admin.py`:** Inherits from Customer, for admin operations
3. **`Order_DB.py`:** Manages file operations (store, retrieve, update).
4. **`Customer.py`:** Manages the customer class
5. **`Order.py`:** For ordering products
6. **`Postal_Order.py`:** For ordering productsas store orders
7. **`Products.py`:** Logic for ordering products
8. **`Order_mgt_UI.py`:** CLI setup for the user to interact with

---

## 4. Software Development Life Cycle Phases

### Requirement Analysis

- Gathered requirements for file handling, database interactions, and OOP structure.

### Design

- Designed the overall architecture with clear module separation.

### Implementation

- Developed main application logic in `main.py`.
- Implemented UI logic in `Order_mgt_UI.py`.
- Implemented database operations in `Order_DB.py`.

### Testing

- Performed unit testing for each module.
- Conducted integration testing to ensure all components work together.

### Deployment

- Created installation guide for deploying the application from GitHub.

### Maintenance

- Documented the process for updating and maintaining the code.

---

## 5. Installation Guide

To install the program from GitHub, follow these steps:

1. Install git-lfs if not already installed. (<a href="https://github.com/git-lfs/git-lfs?utm_source=gitlfs_site&utm_medium=installation_link&utm_campaign=gitlfs#installing">Instructions Here</a>)
2. Clone the repository:
   ```sh
   git clone https://github.com/sebastian-power/order-management-system.git
   ```
3. Navigate to the project directory:
   ```sh
   cd order-management-system
   ```
4. Run the application:
   ```sh
   python src/main.py
   ```

---

The full source code is available at this link: https://github.com/sebastian-power/order-management-system.git

### 14.2 Organization of source code files and modules<a name="src_org"></a>
Organising the project files and assets into appropriate directories is crucial for maintaining a clean and efficient codebase. The directory structure of the OMS project is as follows:

![image](https://github.com/sebastian-power/order-management-system/assets/52031320/da7948c9-fea8-49ba-8569-c1c61138795d)

This shows the entire file structure.  

### 14.3 Github policies<a name="git_policy"></a>
It was strong policy that nobody commit to main, ever, under any circumstances, even for small changes, no matter what, come hell or high water, come rain or shine, for love or money, till the cows come home, until pigs fly, under pain of death, do or die, in sickness and in health, through thick and thin, over my dead body, when hell freezes over, till kingdom come, come what may, against all odds, in a New York minute, until the end of time, by hook or by crook, in a pig's eye, by the skin of your teeth, for all the tea in China, when the stars align, till the last dog dies, and especially not Oliver or James. <s>Seb can push to main whenever he feels like, for some reason.</s> This was to ensure that there would be less merge errors.

Programmers also always pulled from main immediately before pushing to ensure no merge conflicts.
## 15. Testing and Quality Assurance<a name="test_quality"></a>
In software engineering, there are different testing levels to ensure a software product's quality. These levels include unit testing, subsystem testing, and system testing. Unit testing focuses on verifying the functionality of each component or module of the software application. Developers typically perform it by testing the components in isolation. Subsystem testing is a type of integration testing that verifies the behaviour and interaction between multiple components or modules within a subsystem. It ensures that the subsystem functions are as expected and meet the specified requirements. System testing checks whether the software, hardware, or product meets the specified requirements. It focuses on validating the entire system's functionality and is usually done by developers and testers.
The tests mentioned above are usually conducted using a black-box testing approach. Black box testing is performed when the inputs and expected outputs are known. These tests assert whether the expected output for a series of instructions or test data matches the actual output. Despite conducting these tests correctly, if the assertion fails, then white-box testing is performed. White box testing is a technique requiring explicit knowledge of the internal workings of the code being tested. Though programmers can conduct it while testing for syntax, logic, or runtime errors, it is only used to check for logic or runtime errors after performing the black box testing. An example could be a developer testing whether the attributes of an object were changed correctly or whether a function modified the value in a variable correctly.
### 15.1 Black box testing of OMS<a name="black_box"></a>
Black box unit tests of some of the classes in OMS were performed using the Visual Studio Code (VSC) IDE’s pytest framework. Details of how to configure VSC for unit tests are available at Testing Python in Visual Studio Code. This section illustrates how the Postal_Order’s has_partial_valid_state_sequence(self,states:type[list[int]], valid_sequence:list[type[str]])->type[bool] method can be unit tested. This is our test case.
### 15.1.1 Test Cases<a name="test_cases"></a>
A test case is a sequence of actions to verify a specific functionality. It outlines the necessary steps, prerequisites, inputs and expected outcomes for testing a particular functionality. The pre-requisite for testing the case is that a Postal_Order  and a Customer object must be available.
### 15.1.2 Input-Output table for testing<a name="io_table"></a>
From the earlier discussion on its intrinsic documentation in section 14.1, we know the list of valid states of a Postal_Order object. An Input-Output (IO) table is provided to document a list of valid and invalid inputs for the states of a Postal_Order.
![image](https://github.com/sebastian-power/order-management-system/assets/52031320/7f7448cf-e1cd-456c-9298-d2effd0ecf8e)
The test data in the IO table can be used to create a test suite for has_partial_valid_state_sequence. A test suite was developed based on the IO table entries. This is shown in the figure below.
![image](https://github.com/sebastian-power/order-management-system/assets/52031320/a512ceca-ffb5-4ac2-829c-d47c53bd2a7f)
Observe that all the test cases in the IO tables are tested. 

User Stories IPO Table: 
![Image](https://github.com/sebastian-power/order-management-system/blob/main/assets/images/User%20Stories%20IPO%20Table%201.png)
![Image](https://github.com/sebastian-power/order-management-system/blob/main/assets/images/User%20Stories%20IPO%20Table%202.png)


### 15.2 White box testing of OMS<a name="white_box"></a>
The code passed all the test cases except test case number 10. White box testing and debugging using breakpoints and line-by-line tracing was used to identify a logical error in Postal_Order.  Consequently, statement numbers 61 to 63 were added to fix the error.
![image](https://github.com/sebastian-power/order-management-system/assets/52031320/f3f84bc1-6b0f-41fc-8529-c4ef7d4075cc)
The output of VSC following the bug fix is shown below:
![image](https://github.com/sebastian-power/order-management-system/assets/52031320/0e9e237d-008e-4635-b88d-9841bf82eb49)
