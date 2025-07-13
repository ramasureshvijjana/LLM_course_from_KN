# 📘 What are LLMs and How Do They Work?

## 🔹 Foundation Models
- Foundation models are **large-scale neural networks** trained on **vast amounts of data**.
- These models serve as a base for various tasks like NLP, translation, and text generation.
- **Example**: GPT-3 is a foundation model.

## 🔹 Training Data
- LLMs are trained on a **large corpus of text** including:
  - Books
  - Articles
  - Conversations
  - And more
- Total training data size is in **petabytes**.

---

## 🧠 Training Phases of LLMs

### 1️⃣ First Stage: Unsupervised Learning
- Learns **patterns and relationships** in the data.
- No labeled data or alignment used.
- The model may output random or irrelevant responses.
- **Example**: "Hey, what’s up?" → might respond with “What’s up, with you?”

### 2️⃣ Second Stage: Supervised Learning
- Trained using **clear objectives** (e.g., sentiment classification, translation).
- Adjusts weights to align with **user intent** or specific goals.

### 3️⃣ Third Stage: Instruction Fine-tuning
- Uses **supervised instruction tuning** on labeled datasets.
- Further refined using **Reinforcement Learning from Human Feedback (RLHF)**:
  - Users rate the quality or usefulness of model outputs.
  - Model improves based on this feedback.
  - Works similarly to a **reward system**.
- Seen in tools like **ChatGPT**, **Gemini**, etc., where users rate or select best responses.

---
