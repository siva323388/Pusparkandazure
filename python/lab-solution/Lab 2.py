"""
**Challenge: Analyze Word Frequency and Perform Queue Operations**

**Objective**

The goal of this challenge is to apply advanced Python data structures, including **Counter** from the `collections` module for word frequency analysis and **deque** for efficient queue operations. By completing this challenge, you will gain hands-on experience in:
- Analyzing and interpreting textual data.
- Using `Counter` for frequency analysis.
- Implementing queue operations with `deque`.

---

**Scenario**

You are tasked with analyzing customer reviews for a product and implementing a queuing system to manage real-time requests. The dataset includes:
1. A paragraph of customer reviews for word frequency analysis.
2. A sequence of customer service requests to be managed in a queue.

---

**Task Details**

1. **Word Frequency Analysis**
   - Use `Counter` to calculate the frequency of each word in the customer reviews.
   - Ignore case and remove punctuation for accurate word counts.
   - Identify and display:
     - The top 3 most frequent words.
     - Words that appear only once.

2. **Queue Operations with deque**
   - Simulate a real-time queue of customer service requests using `deque`.
   - Perform the following operations:
     1. Add 5 requests to the queue.
     2. Serve (remove) 2 requests from the queue.
     3. Add 3 more requests to the queue.
     4. Display the current state of the queue.

---

**Sample Data**

**Customer Reviews:**
```
"The product is great! Great value for money. I absolutely love the product, and the quality is outstanding."
```

**Customer Service Requests:**
```
requests = ["Request A", "Request B", "Request C", "Request D", "Request E"]
```

---

**Expected Output**

1. **Word Frequency Analysis**
   ```plaintext
   Top 3 Words: [('great', 2), ('the', 2), ('product', 2)]
   Words Appearing Once: ['is', 'value', 'for', 'money', 'i', 'absolutely', 'love', 'and', 'quality', 'outstanding']
   ```

2. **Queue Operations**
   ```plaintext
   Initial Queue: ['Request A', 'Request B', 'Request C', 'Request D', 'Request E']
   After Serving 2 Requests: ['Request C', 'Request D', 'Request E']
   After Adding 3 Requests: ['Request C', 'Request D', 'Request E', 'Request F', 'Request G', 'Request H']
   ```

---
"""

from collections import Counter, deque
import string

# Step 1: Word Frequency Analysis
def analyze_word_frequency(text):
    # Clean text: remove punctuation, convert to lowercase
    translator = str.maketrans("", "", string.punctuation)
    clean_text = text.translate(translator).lower()
    
    # Split into words
    words = clean_text.split()
    
    # Count word frequencies
    word_count = Counter(words)
    
    # Top 3 most frequent words
    top_words = word_count.most_common(3)
    
    # Words appearing only once
    single_occurrence_words = [word for word, count in word_count.items() if count == 1]
    
    return top_words, single_occurrence_words

# Step 2: Queue Operations
def perform_queue_operations(requests):
    # Initialize the deque
    queue = deque(requests)
    print("Initial Queue:", list(queue))
    
    # Serve (remove) 2 requests
    queue.popleft()
    queue.popleft()
    print("After Serving 2 Requests:", list(queue))
    
    # Add 3 more requests
    queue.extend(["Request F", "Request G", "Request H"])
    print("After Adding 3 Requests:", list(queue))

# Sample Data
reviews = "The product is great! Great value for money. I absolutely love the product, and the quality is outstanding."
requests = ["Request A", "Request B", "Request C", "Request D", "Request E"]

# Execute Word Frequency Analysis
top_words, single_occurrence_words = analyze_word_frequency(reviews)
print("Top 3 Words:", top_words)
print("Words Appearing Once:", single_occurrence_words)

# Execute Queue Operations
perform_queue_operations(requests)


# **Further Challenge Instructions**

# 1. **Run the provided code** with the sample data to understand the functionality.
# 2. Modify the sample text and requests to test different scenarios.
# 3. Extend the queue operations to:
#    - Check if the queue is empty before serving requests.
#    - Implement a priority queue (if time permits).
# 4. Document the results and observations.