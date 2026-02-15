**Serverless Task Management API**

AWS API Gateway + Lambda + DynamoDB


**Project Overview**

This project demonstrates a fully serverless REST API built using:
•	Amazon API Gateway – Exposes REST endpoints
•	AWS Lambda (Python) – Handles backend logic
•	Amazon DynamoDB – NoSQL database for storing tasks
The API supports full CRUD operations for managing tasks.


**Architecture**

<img width="1536" height="1024" alt="169a82b1-9b0f-420a-bd54-7f87001418d7" src="https://github.com/user-attachments/assets/e9a1e679-5bf2-460c-b14e-cde4bf1fb883" />




**DynamoDB Table Configuration**
### Attribute	Type
### taskId	String (Primary Key)

**Table Name: Tasks**
### Example Item:
```json
{
  "taskId": "b1f7c123-uuid",
  "title": "Learn Serverless",
  "description": "Deep dive",
  "status": "PENDING",
  "createdAt": "2026-02-15T10:00:00"
}
```

**API Endpoints**

**Base URL:**
https://<api-id>.execute-api.<region>.amazonaws.com/<stage>

**Example:**
https://abc123.execute-api.ap-south-1.amazonaws.com/dev

---

# 🔥 API Endpoints

---

## 1️⃣ Create Task

### POST `/tasks`

### 📌 Request Body

```json
{
  "title": "Learn Serverless",
  "description": "Deep dive"
}
```

### 📦 Response (201)

```json
{
  "taskId": "generated-uuid",
  "title": "Learn Serverless",
  "description": "Deep dive",
  "status": "PENDING",
  "createdAt": "timestamp"
}
```

---

## 2️⃣ Get All Tasks

### GET `/tasks`

### 📦 Response (200)

```json
[
  {
    "taskId": "uuid1",
    "title": "Task 1",
    "description": "Desc",
    "status": "PENDING"
  },
  {
    "taskId": "uuid2",
    "title": "Task 2",
    "description": "Another task",
    "status": "COMPLETED"
  }
]
```

---

## 3️⃣ Get Single Task

### GET `/tasks/{id}`

Example:

```
GET /tasks/1234-uuid
```

### 📦 Response (200)

```json
{
  "taskId": "1234-uuid",
  "title": "Learn Serverless",
  "description": "Deep dive",
  "status": "PENDING",
  "createdAt": "timestamp"
}
```

---

## 4️⃣ Update Task

### PUT `/tasks/{id}`

### 📌 Request Body

```json
{
  "title": "Learn Serverless",
  "description": "Deep dive",
  "status": "COMPLETED"
}
```

### 📦 Response (200)

```json
{
  "message": "Task updated"
}
```

---

## 5️⃣ Delete Task

### DELETE `/tasks/{id}`

### 📦 Response (200)

```json
{
  "message": "Deleted"
}
```

---

**Lambda Function Overview**

Main responsibilities:

-	Parse HTTP method from API Gateway event
-	Perform CRUD operations in DynamoDB
-	Return structured JSON response
-	Handle reserved keywords in UpdateExpression


**IAM Requirements**

Lambda Execution Role must have:

##### Minimum Required Permissions:

- dynamodb:PutItem
- dynamodb:GetItem
- dynamodb:UpdateItem
- dynamodb:DeleteItem
- dynamodb:Scan

Or attach:

- AmazonDynamoDBFullAccess


**API Gateway Stages**

Recommended environments:

- dev
- test
- prod

**Example URLs:**

- /dev/tasks
- /prod/tasks

---
##Testing:

You can test the API using **Postman**, curl, or any HTTP client.

POST:
 
<img width="975" height="754" alt="image" src="https://github.com/user-attachments/assets/3a2c72c7-4689-4d04-87c5-cfaba9a09a96" />


PUT:

<img width="975" height="689" alt="image" src="https://github.com/user-attachments/assets/83292270-1073-41f9-827f-7b36db96b080" />

 
GET:

 <img width="975" height="758" alt="image" src="https://github.com/user-attachments/assets/a6f9057f-e2a5-4370-abb4-0c2b69c1c5b5" />


DELETE:
 

<img width="975" height="633" alt="image" src="https://github.com/user-attachments/assets/62493d55-4a44-45a1-b7b3-c879e0166165" />



