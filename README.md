# AWS Lex Chatbot for Shortest Distance Calculation

Welcome to the **AWS Lex Chatbot Project**! This repository contains the code and instructions for building a serverless chatbot application that calculates the shortest distance between two cities or nodes in a directed graph.

---

## 🚀 **Project Overview**
This chatbot leverages **Amazon Lex**, **AWS Lambda**, **DynamoDB**, **API Gateway**, and **Cognito** to provide an interactive and intelligent experience for users. The chatbot computes the shortest distance between two nodes in a directed graph using **Breadth-First Search (BFS)** and responds in real time to user queries.

---

## 📂 **Repository Structure**

```
📁 Root Directory
├── api.py          # Lambda function for handling graph input and DynamoDB storage
├── dijkstra.py     # Implementation of BFS for shortest path calculation
├── sparksql.py     # Unused in this project (optional component)
├── test_web.html   # Frontend for testing the Lex chatbot
├── README.md       # This README file
```

---

## ✨ **Key Features**

### 1. **Interactive Chatbot**
- Built with **Amazon Lex**, allowing natural language interactions.
- Recognizes city names using Lex's predefined **AMAZON.US_CITY** slot type.
- Seamlessly linked to Lambda for real-time query fulfillment.

### 2. **Backend Processing**
- A REST API (using API Gateway and Lambda) parses graph input and stores data in **DynamoDB**.
- Shortest distances between nodes are precomputed using **BFS** for instant retrieval.

### 3. **Scalable Architecture**
- Secured with **AWS Cognito** for user authentication.
- Leveraged AWS serverless infrastructure for a highly scalable and efficient solution.

### 4. **Frontend Testing Interface**
- A user-friendly HTML interface (test_web.html) enables testing and visualization of chatbot interactions.

---

## 🛠 **Setup Instructions**

### Prerequisites
- AWS Account
- Familiarity with **Python**, **JavaScript**, or **Java**
- AWS CLI installed and configured

### Steps
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/cgw4455235/lex_city_dist_chat.git
   cd aws-lex-chatbot
   ```

2. **Set Up AWS Services:**
   - **Lambda:** Deploy `api.py` and `dijkstra.py` as Lambda functions.
   - **API Gateway:** Create a REST API for invoking the graph management Lambda.
   - **DynamoDB:** Set up a table for storing graph data (source, destination, distance).
   - **Amazon Lex:**
     - Create intents for querying distances.
     - Use **AMAZON.US_CITY** slot types for city names.
     - Link the Lex bot to the Lambda function for fulfillment.
   - **Cognito:** Configure an identity pool for secure access.

3. **Deploy Frontend:**
   - Use `test_web.html` as a frontend to interact with the chatbot.
   - Modify the Cognito Identity Pool ID in the script as needed.

4. **Test the Application:**
   - Send queries such as "What is the distance from Chicago to Urbana?"
   - Ensure responses match the precomputed values from DynamoDB.

---

## 🧪 **Testing**
- Verify end-to-end flows with a random graph using API Gateway and DynamoDB integration.

---

## 💻 **Usage Examples**
### Example Interaction
1. **User Input:** "What is the distance from Chicago to Springfield?"
2. **Chatbot Response:** "2"

3. **User Input:** "I need to find the distance between two cities."
   - **Chatbot Prompt:** "Source?"
   - **User Input:** "Chicago"
   - **Chatbot Prompt:** "Destination?"
   - **User Input:** "Urbana"
   - **Chatbot Response:** "1"

---

## 🛡 **Security**
- Secure data storage in AWS DynamoDB.

---

## 🎨 **Aesthetic Enhancements**
### Styling Improvements
- Improved frontend interface with CSS for user-friendly chatbot interactions.
- Color-coded user requests, chatbot responses, and error messages for clarity.

### Frontend Preview
![Chatbot Interface](https://via.placeholder.com/800x400.png?text=Frontend+Preview)

---

## 📝 **Contributing**
We welcome contributions! Please fork the repository and submit a pull request with a detailed explanation of your changes.

---

## 📜 **License**
This project is licensed under the MIT License. See the `LICENSE` file for details.

