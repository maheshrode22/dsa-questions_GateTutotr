# Problem Creation & Verification Workflow Guide

This guide outlines the standard process for creating, structuring, and verifying coding problems.

## 1. Problem File Structure (JSON)
Each problem must be a JSON file (e.g., `1.json`) with the following structure:

```json
{
    "problems": [
        {
            "id": null,
            "title": "Problem Title",
            "description": "Clear problem statement.\n\nInput format.\nOutput format.",
            "examples": "Sample Input\n...\n\nSample Output\n...\n\nExplanation:\n...",
            "constraints": "Constraints on input size, values, etc.",
            "hints": 2,
            "timeLimit": 1,
            "memoryLimit": 256,
            "subdomainId": 2032,
            "difficulty": 1, 
            "testCases": [ ... ],
            "starterCodes": [ ... ],
            "hintsList": [ "Hint 1", "Hint 2" ]
        }
    ]
}
```

*   **Difficulty**: 1 (Easy), 2 (Medium), 3 (Hard).
*   **SubdomainId**: Specific ID for the topic.

## 2. Test Cases
*   **Quantity**: At least 5 test cases.
*   **Variety**:
    *   **Basic**: Simple, standard cases.
    *   **Edge Cases**: Empty strings, single characters, maximum constraints.
    *   **Negative Cases**: Cases where the answer is "False", "-1", or empty.
*   **Format**: `input` string must match exactly what the starter code reads. `expectedOutput` must match exactly what the solution prints (trimmed).

## 3. Starter Code Structure
Starter codes must be provided for 5 languages. They must handle Input/Output (I/O) so the student only implements the logic.

### Python (Language ID: 1)
```python
class Solution:
    def solve(self, args):
        # TODO: Implement logic
        pass

if __name__ == '__main__':
    # Read input
    # Call Solution
    # Print output
```

### Java (Language ID: 2)
```java
import java.io.*;
import java.util.*;

class Solution {
    public ReturnType solve(Args args) {
        // TODO: Implement logic
        return defaultVal;
    }
    
    public static void main(String[] args) throws Exception {
        // Use BufferedReader for fast I/O
        // Parse input
        // Print output
    }
}
```

### JavaScript (Language ID: 3)
```javascript
class Solution {
    solve(args) {
        // TODO: Implement logic
        return defaultVal;
    }
}

function solve(input) {
    // Parse input from string
    // Print output
}

const fs = require('fs');
solve(fs.readFileSync(0, 'utf-8'));
```

### C++ (Language ID: 4)
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    ReturnType solve(Args args) {
        // TODO: Implement logic
        return defaultVal;
    }
};

int main() {
    // Fast I/O if needed
    // cin >> input
    // cout << output
    return 0;
}
```

### C (Language ID: 5)
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void solve(Args args) {
    // TODO: Print output
}

int main() {
    // scanf input
    // solve(args)
    return 0;
}
```

## 4. Verification Process (Step-by-Step)

1.  **Drafting**: Create the JSON file with the problem details and starter code.
2.  **Manual Review**: Check if the description is clear and constraints are reasonable.
3.  **Automated Verification**:
    *   Create a script (e.g., `verify_problems.py`).
    *   Implement a **Reference Solution** for the problem within the script.
    *   The script should:
        1.  Inject the reference solution into the starter code structure.
        2.  Run the code against the defined `testCases`.
        3.  Compare the actual output with `expectedOutput`.
4.  **Fixing Issues**:
    *   If a test fails, check if the Reference Solution is wrong OR if the Expected Output in the JSON is wrong.
    *   Fix the JSON file accordingly.
5.  **Final Polish**: Ensure formatting (newlines, spaces) is consistent.

## 5. Common Pitfalls
*   **Ambiguous Outputs**: Ensure there is only one valid answer (e.g., if multiple substrings have the same length, specify "return the first one" or ensure test cases don't have ties).
*   **Formatting**: Trailing spaces or newlines in `expectedOutput` can cause test failures.
*   **Input Parsing**: Ensure the starter code correctly parses the input format described in the problem.
