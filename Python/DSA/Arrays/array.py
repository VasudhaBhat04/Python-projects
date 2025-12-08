
# An array is a collection of elements (usually of the same data type) stored in contiguous memory locations.
"""
| Property              | Description                                                                             |
| --------------------- | --------------------------------------------------------------------------------------- |
| **Fixed size**        | The size of an array is defined when it’s created (in low-level languages like C, C++). |
| **Same data type**    | All elements must be of the same type (e.g., all integers, all floats).                 |
| **Indexing**          | Elements are accessed by their **index**, starting from `0`.                            |
| **Contiguous memory** | Stored one after another in memory → enables fast random access.                        |

list = [] python in array
Python doesn’t have a true static array like C or Java — instead, it uses lists, which are dynamic arrays (they grow/shrink automatically).

| Operation     | Description           | Time Complexity                    |
| ------------- | --------------------- | ---------------------------------- |
| **Access**    | `arr[i]`              | **O(1)** (direct access via index) |
| **Search**    | Find element in array | **O(n)** (linear search)           |
| **Insertion** | Add element in middle | **O(n)** (elements need shifting)  |
| **Deletion**  | Remove element        | **O(n)** (shift elements)          |
| **Traversal** | Visit all elements    | **O(n)**                           |

"""

