"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [[]],
            "answer": []
        },
        {
            "input": [[5]],
            "answer": [5]
        }, 
        {
            "input": [[5, 1, 5, 0, 5]],
            "answer": [5, 5, 0, 5, 1]
        }, 
        {
            "input": [[5, 5, 1]],
            "answer": [5, 5, 1]
        }
    ],
    "Extra": [
        {
            "input": [[1, 3, 4, 5, 6, 4, 5, 5, 2, 3, 4]],
            "answer": [1, 3, 4, 5, 6, 2, 3, 4, 4, 5, 5]
        },
        {
            "input": [[5, 5, 1, 1, 1, 2, 4, 4]],
            "answer": [2, 4, 4, 5, 5, 1, 1, 1]
        }, 
        {
            "input": [[5, 1, 5]],
            "answer": [5, 5, 1]
        }, 
        {
            "input": [[1, 0, 1, 3, 1, 2, 2, 1]], 
            "answer": [1, 1, 0, 1, 2, 2, 1, 3]
        }
    ]
}
