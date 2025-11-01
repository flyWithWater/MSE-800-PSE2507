"""
Develop an Object-Oriented (OO) Python project that reads either a string or a list, then performs two analyses:
Calculates the total length.
Determines the number of uppercase characters.
The project should be structured with appropriate classes and methods. After implementation, use Pylint to analyze
 and improve the code quality, ensuring adherence to Python’s best practices and style guidelines. 
 Share the result when you have done
"""


class TextAnalyzer:
    
    



    def calculate_length(self, text)-> int:
        """Calculate the length of the input text."""

        if isinstance(text, str):
            return len(text)
        elif isinstance(text, list):
            return -1
        return 0

    def count_uppercase(self, text) -> int:
        """Count the number of uppercase characters in the input text."""
        if isinstance(text, str):
            return sum(1 for char in text if char.isupper())
        elif isinstance(text, list):
            return sum(self.count_uppercase(item) for item in text if isinstance(item, str))
        return 0

def main():
    # Example usage
    



if __name__ == "__main__":
    main()